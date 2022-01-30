from app import db
import datetime as dt


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(128), index=True, unique=True)
    servings = db.Column(db.Integer)
    prep_time = db.Column(db.Integer)
    cook_time = db.Column(db.Integer)
    description = db.Column(db.Text)
    ingredients = db.relationship('Ingredient', backref='recipe', lazy='dynamic')
    directions = db.relationship('Steps', backref = 'recipe', lazy='dynamic')

    def __repr__(self):
        return f'{self.id}. {self.recipe_name} - Prep Time: {self.prep_time} Cook Time: {self.cook_time}'

    def to_dict(self):
        data = {
            'id': self.id,
            'recipe_name': self.recipe_name,
            'servings': self.servings,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'description': self.description,
        }
        return data

    def summary(self):
        
        summary = {
            'id': self.id,
            'recipe_name': self.recipe_name,
            'time': self.prep_time + self.cook_time,
        }

        return summary
    
    def from_dict(self, data):
        for field in ['recipe_name', 'servings', 'prep_time', 'cook_time', 'description']:
            if field in data:
                setattr(self, field, data[field])


class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    ingredient = db.Column(db.String(128))
    qty = db.Column(db.Numeric)
    unit = db.Column(db.String(16))

    def __repr__(self):
        return f'{self.qty} {self.unit} - {self.ingredient}'

    def to_dict(self):
        data = {
            'ingredient': self.ingredient,
            'qty': self.qty,
            'unit': self.unit
        }

        return data


class Steps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    step_number = db.Column(db.Integer)
    step_text = db.Column(db.Text)

    def __repr__(self):
        return f'{self.step_number}. {self.step_text}'
    
    def to_dict(self):
        data = {
            "step_number": self.step_number,
            "step_text": self.step_text
        }

        return data