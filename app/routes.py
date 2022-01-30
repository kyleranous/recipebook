from flask import render_template, jsonify
from app import app
from app.models import Recipe, Ingredient


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api/all_recipes', methods=['GET'])
def get_all_recipes():
    pass


@app.route('/api/recipe/<int:id>', methods=['GET'])
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
    print(r["ingredients"])
    # If the Recipe and Ingredients have been found query the steps

    return jsonify(r)