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
    
    r = Recipe.query.all()
    
    # Return Pagified List of Recipes in Database
    return jsonify({'message': 'This would be a list of all the recipes'})


@app.route('/api/recipies', methods=['POST'])
def add_recipe():

    # Add a new recipe to the Database
    data = request.get_json() or {}
    pass


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
    print(data)
    r = Recipe.query.get_or_404(id)
    if 'ingredients' in data:
        print("HELLO")
        ingredients = data['ingredients']
        print(type(ingredients))
        return jsonify(ingredients)

    r.from_dict(data)
    db.session.commit()

    print(data)

    # Return Success Message once done with Debugging
    return get_recipe(id)


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
    i = Ingredient.query.get_or_404(ingredient_id)
    i.from_dict(data)
    db.session.commit()

    # Return Success Message once done with Debugging
    return get_recipe(recipe_id)


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

