from app import db
from app.models import Recipe, Ingredient
import datetime

#Check if Test Recipe 1 Exists and pull it if it does
if db.session.query(Recipe).filter_by(recipe_name='Test Recipe 1').first() is not None:
    print("Found Recipe 1")
    r = db.session.query(Recipe).filter_by(recipe_name='Test Recipe 1').first()

else:
    # Create Time Objects for Prep and Cook Time
    print("Creating Recipe 1")
    # Table stores time values as integer seconds
    preptime = 30 * 60 #30 Minutes converted to seconds
    cooktime = (1*3600) + (14*60) #1 Hour and 14 Minutes Converted to seconds

    #Create Recipe Object for Test Recipe 1
    r = Recipe(recipe_name='Test Recipe 1', servings=6, prep_time=preptime,
               cook_time=cooktime, description='This is a test Recipe')

    #Add Test Recipe 1 to db and commit
    db.session.add(r)
    db.session.commit()

if len(r.ingredients.all()) == 0:
    #Create Ingredients for Test Recipe 1
    print('Creating Ingredients for Recipe 1')
    i1 = Ingredient(recipe_id=r.id, ingredient='Test Ingredient 1', qty=0.25,
                    unit='cups')

    db.session.add(i1)

    i2 = Ingredient(recipe_id=r.id, ingredient='Test Ingredient 2', qty=1,
                    unit='tbsp')

    db.session.add(i2)

    #Commit Ingredients
    db.session.commit()
else:
    print('Ingredients for Recipe 1 exist')