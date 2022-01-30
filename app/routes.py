from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/api/all_recipes', methods=['GET'])
def get_all_recipes():
    pass


@app.route('/api/recipe/<int:id>', methods=['GET'])
def get_recipe(id):
    pass