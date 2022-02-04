from ast import Pass
from tempfile import TemporaryFile
from flask import render_template, jsonify, request
from flask import redirect, url_for
from app import app, db
from app.models import Recipe, Ingredient, Steps


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api-reference')
def api_reference():
    return render_template('api_reference.html', title='API Reference')


# API ROUTES
@app.route('/api/recipes', methods=['GET'])
def get_all_recipes():
    
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = Recipe.to_collection(Recipe.query, page, per_page, 'get_all_recipes')

    return jsonify(data)


@app.route('/api/recipes', methods=['POST'])
def add_recipe():

    # Add a new recipe to the Database
    data = request.get_json() or {}
    
    #Check Required `recipe` keys exist
    for field in ['recipe_name', 'servings']:
        if field not in data:
            print(f'missing field: {field}')
            return jsonify({'error': f'missing required field - {field}'})
    
    # Set New Recipe Values or defaults if not present
    name = data['recipe_name']
    servings = data['servings']
    prep_time = data.get('prep_time', 0)
    cook_time = data.get('cook_time', 0)
    description = data.get('description', 'No description provided.')
    r = Recipe(recipe_name=name, servings=servings, prep_time=prep_time,
               cook_time=cook_time, description=description)
    db.session.add(r)
    db.session.commit()

    # If ingredients are included add them
    if 'ingredients' in data:
        
        ingredients = data['ingredients']
        
        for item in ingredients:
            for field in ['ingredient', 'qty', 'unit']:
                if field not in item:
                    return jsonify({'error': f'missing required field - {field}'})
            
            i = Ingredient(recipe_id=r.id, ingredient=item['ingredient'],
                           qty=item['qty'], unit=item['unit'])
            
            db.session.add(i)

    if 'directions' in data:

        steps = data['directions']

        for step in steps:
            for field in ['step_number', 'step_text']:
                if field not in step:
                    return jsonify({'error': f'missing required field - {field}'})

            s = Steps(recipe_id=r.id, step_number=step['step_number'],
                      step_text=step['step_text'])
            db.session.add(s)

    db.session.commit()

    return get_recipe(r.id) # Update Return to return a success method 


@app.route('/api/recipes/<int:id>', methods=['GET'])
def get_recipe(id):

    # Find the Recipe with matching ID
    try:
        r = Recipe.query.get(id).to_dict()
    
    except: # If Recipe can't be found, return the error message
        return jsonify({"error": f"No Recipe with id:{id}"})

    # If the Recipe has been found query the ingredients
    try:    
        i = Ingredient.query.filter_by(recipe_id=id).all()

    except: # If no ingredients found - return error message
        return jsonify({"error": f"No Ingredients for Recipe {id}"})

    # Add Ingredients to recipe dict
    ingredients = []    
    for item in i:
        ingredients.append(item.to_dict())
    r["ingredients"] = ingredients
    
    # If the Recipe and Ingredients have been found query the steps
    try:
        d = Steps.query.filter_by(recipe_id=id).all()

    except: # If No Steps Found - return error message
        return jsonify({"error": f"No Directions for Recipe {id}"})

    # Add Directions to recipe dict
    steps = []
    for step in d:
        steps.append(step.to_dict())
    r["directions"] = steps

    return jsonify(r)


@app.route('/api/recipes/<int:id>', methods=['PUT'])
def update_recipe(id):

    data = request.get_json() or {}
    r = Recipe.query.get_or_404(id)
    if 'ingredients' in data:
        
        ingredients = data['ingredients']

        for i in ingredients:
            ing = Ingredient.query.get_or_404(i['id'])
            ing.from_dict(i)
    
    if 'directions' in data:

        directions = data['directions']
        for d in directions:
            stp = Steps.query.get_or_404(d['id'])
            stp.from_dict(d)

    r.from_dict(data)
    db.session.commit()


    # Return Success Message once done with Debugging
    return get_recipe(id)


@app.route('/api/recipes/<int:id>', methods=['DELETE'])
def delete_recipe(id):

    # Delete Recipe Entry and All Ingredients and Directions child to Recipe
    r = Recipe.query.get_or_404(id)
    db.session.delete(r)
    db.session.commit()
    
    return 'SUCCESS'


@app.route('/api/recipes/<int:id>/ingredients', methods=['GET'])
def get_ingredients(id):

    ingredients = Ingredient.query.filter_by(recipe_id=id).all()
    ingredient_list = []
    for i in ingredients:
        ingredient_list.append(i.to_dict())
    
    return jsonify(ingredient_list)
    

@app.route('/api/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>', methods=['PUT'])
def update_ingredients(recipe_id, ingredient_id):
    
    data = request.get_json() or {}
    id = ingredient_id
    i = Ingredient.query.filter_by(id=ingredient_id).first()
    i.from_dict(data)
    db.session.commit()

    # Return Success Message once done with Debugging
    return get_recipe(recipe_id)


@app.route('/api/recipes/<int:recipe_id>/ingredients/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(recipe_id, ingredient_id):

    i = Ingredient.query.filter_by(id=ingredient_id, recipe_id=recipe_id).first()
    db.session.delete(i)
    db.session.commit()

    return "Success"


@app.route('/api/recipes/<int:recipe_id>/directions', methods=['GET'])
def get_directions(recipe_id):

    directions = Steps.query.filter_by(recipe_id=recipe_id).all()
    direction_list =[]
    for step in directions:
        direction_list.append(step.to_dict())

    return jsonify(direction_list)


@app.route('/api/recipes/<int:recipe_id>/directions/<int:direction_id>', methods=['PUT'])
def update_directions(recipe_id, direction_id):

    data = request.get_json() or {}
    direction = Steps.query.get_or_404(direction_id)

    direction.from_dict(data)
    db.session.commit()

    # Return success message once done with debugging
    return get_recipe(recipe_id)


@app.route('/api/recipes/<int:recipe_id>/directions/<int:direction_id>', methods=['DELETE'])
def delete_step(recipe_id, direction_id):

    s = Steps.query.filter_by(id=direction_id, recipe_id=recipe_id).first()
    db.session.delete(s)
    db.session.commit()

    return "Success"