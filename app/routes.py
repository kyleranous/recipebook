from tempfile import TemporaryFile
from flask import render_template, jsonify, request
from app import app
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
    pass