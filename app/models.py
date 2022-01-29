from app import db


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(128), index=True, unique=True)
    servings = db.Column(db.Integer)
    prep_time = db.Column(db.Time)
    cook_time = db.Column(db.Time)
    description = db.Column(db.Text)
    ingredients = db.relationship('Ingredient', backref='recipe', lazy='dynamic')
    directions = db.relationship('Steps', backref = 'recipe', lazy='dynamic')

    def __repr__(self):
        return f'{self.id}. {self.recipe_name} - Prep Time: {self.prep_time} Cook Time: {self.cook_time}'


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    ingredient = db.Column(db.String(128))
    qty = db.Column(db.Numeric)
    unit = db.Column(db.String(16))

    def __repr__(self):
        return f'{self.qty} {self.unit} {self.ingredient}'

class Steps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    step_number = db.Column(db.Integer)
    step_text = db.Column(db.Text)

    def __repr__(self):
        return f'{self.step_number}. {self.step_text}'