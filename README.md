 # Recipe Book

 Recipe Book is a API for storing and retrieving recipes from a database. This project is being created specifically for integration into a Home Assistant Integration. 

 This project is purely an API service, all front-end and UI integrations for this project is managed by other applications. 

 Implementation of this project is being covered in the Home automation tutorial on my website (http://www.kranous.com/projects/home_automation/homeAutomation_00.html)

**IMPORTANT**
This is not a production ready application. If you run it, it should not be exposed to internet. There is MINIMAL security built into this API in it's current form


## Road Map
 - Search Integration - Search by Recipe Name or Ingredients. Ingredient Search should allow for AND OR and EXCLUDE. IE Search For Recipes that have Chicken but no Mushrooms
 ```Python

# Search for sub string
Model.query.filter(Model.columnName.contains('sub string'))

# Search for recipes that contain or items
Model.query.filter(or_(Model.columnName == v for v in ['item1', 'item2', 'item3']))

# Exclude an item from a search
Model.query.filter(not_(Model.columnName.contains('sub string')))

 ```

 - Share Recipe - Send formatted recipe through an e-mail

## To Do
- [x] Write Function to return paginated Recipe list
- [x] Write function to add new recipe to database
- [x] Write function to modify recipe
    - [x] Modify Recipe Summary
    - [x] Modify Recipe Ingredients
    - [x] Modify Recipe Directions
- [x] Write Function to Delete Recipe
    - [x] Delete Recipe Summary
        If Recipe summary is deleted, then All Ingredients and Directions should be deleted also
    - [x] Delete Recipe Ingredient
    - [x] Delete Recipe Direction Step
- [ ] Conduct Code Review
    - [ ] Change All references to directions to steps...or change steps to directions
- [ ] More documentation
