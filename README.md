 # Recipe Book

 Recipe Book is a API for storing and retrieving recipes from a database. This project is being created specifically for integration into a Home Assistant Integration. 

 This project is purely an API service, all front-end and UI integrations for this project is managed by other applications. 

 Implementation of this project is being covered in the Home automation tutorial on my website (http://www.kranous.com/projects/home_automation/homeAutomation_00.html)

**IMPORTANT**
This is not a production ready application. If you run it, it should not be exposed to internet. There is MINIMAL security built into this API in it's current form


## To Do
- [] Write Function to return paginated Recipe list
- [] Write function to add new recipe to database
- [x] Write function to modify recipe
    - [x] Modify Recipe Summary
    - [x] Modify Recipe Ingredients
    - [x] Modify Recipe Directions
- [] Write Function to Delete Recipe
    - [] Delete Recipe Summary
        If Recipe summary is deleted, then All Ingredients and Directions should be deleted also
    - [] Delete Recipe Ingredient
    - [] Delete Recipe Direction Step
        If a step is removed, other steps need to be updated with new step number
- [] More documentation
