 # API Reference

## Summary


## Endpoints

### api/recipes
Endpoint to recieve all recipes or add a new recipe.
#### Method: GET

##### Summary
Returns a list of all recipes in paginated form. Defaults to 10 results per page.

##### Request Data
| Request Variable | Type|  Required? | Usage | Default Value |
| :--- | :--- | :---: | :--- | :--- |
| page | INT | No | fetches the specific page of the paginated results | 1 |
| per_page | INT | No | Sets the number of results per page | 10 |
```bash
GET http://localhost:5000/api/recipes?page=2&per_page=5
```
This request would return the second page with five results per page.

##### Response Data
Returns a JSON object with Navigation Data (Links for Previous, Current, and Next pages). Meta Data (current page, total items and total pages). and "Items" which is an array of Recipe Summaries and their ID. See Example for Format of response.


##### Example:
Request:
 ```BASH
GET http://localhost:5000/api/recipe
 ```
Response:
```JSON
{
  "_links": {
    "next": null, 
    "prev": null, 
    "self": "/api/recipes?page=1&per_page=10"
  }, 
  "_meta": {
    "page": 1, 
    "total_items": 1, 
    "total_pages": 1
  }, 
  "items": [
    {
      "id": 1, 
      "recipe_name": "Test Recipe 1", 
      "time": 6240
    },
    ...
  ]
}
```
This request would return the first page with a default of 10 results per page.

#### Method: POST
##### Summary
Used to add a new recipe to the database. 
 
##### Request Data
| Request Variable | Type |  Required? | Usage | Default Value |
| :--- | :--- | :---: | :--- | :--- |
| recipe_name | String | Yes | Name Recipe will be store under | None |
| servings | INT | Yes | Servings the base recipe will serve | None |
| prep_time | INT | No | Prep Time for recipe in seconds | None |
| cook_time | INT | No | Time to cook the recipe in seconds | None |
| description | String | No | Short Description of the Recipe | "No description provided" |
| ingredients | Array | No | An Array of Ingredients - See  [ingredients](!#) for formatting and fields | None |
| directions | Array | No | An Array of Directions - See [directions](!#) for formatting and fields | None |
*Note: Any non-required information that is not included in this request will have to be added using other endpoints*

Request Format:
```JSON
{
    "recipe_name": "Name of Recipe",
    "servings": [INT Number of Servings],
    "prep_time": [INT Prep Time in Seconds],
    "cook_time": [INT Cook Time in Seconds],
    "description": "Brief description of recipe",
    "ingredients": [
        {
            ingredient 1
        },
        {
            ingredient 2
        },
        ...
    ],
    "directions": [
        {
            direction 1
        },
        {
            direction 2
        },
        ...
    ]
}
```

##### Response Data
Returns a redirect to the recipe page you just added. This will be changed in an upcomming release to a success message containing the new recipe ID and a link to the recipe.

##### Example:
Minimum Required Information
Request Message:<br>
JSON Object
 ```JSON
    {
        "recipe_name": "Smores",
        "servings": 1,
    }
 ```
 Response:
 ```JSON
{
    "cook_time": Null,
    "description": "No description provided.",
    "directions": [],
    "id": [Database ID Number],
    "ingredients": [],
    "prep_time": Null,
    "recipe_name": "Smores",
    "servings": 1
}
 ```

Full Recipe Added:
Request Message:
```JSON
{
    "recipe_name": "Smores",
    "servings": 1,
    "prep_time": 300,
    "cook_time": 120,
    "description": "Tastey Campfire Smores",
    "ingredients": [
        {
            "ingredient": "Large Marshmellow",
            "qty": 1,
            "unit": "ea"
        },
        {
            "ingredient": "Grahm Cracker",
            "qty": 1,
            "unit": "ea"
        },
        {
            "ingredient": "Chocolate Bar",
            "qty": 0.5,
            "unit": "ea"
        }
    ],
    "directions": [
        {
            "step_number": 1,
            "step_text": "Start a campfire"
        },
        {
            "step_number": 2,
            "step_text": "Toast Marshmellow to perfection"
        },
        {
            "step_number": 3,
            "step_text": "Split Grahm Cracker in half"
        },
        {
            "step_number": 4,
            "step_text": "Place 1/2 Chocolate Bar on one of the Grahm Cracker Halfs"
        },
        {
            "step_number": 5,
            "step_text": "Place toasted marshmellow ontop of Chocolate Bar"
        },
        {
            "step_number": 6,
            "step_text": "Place other half of cracker ontop of the marshmellow"
        }
    ]
}
```
Response:
```JSON
{
    "cook_time": 120,
    "description": "Tastey Campfire Smores",
    "directions": [
        {
            "id": 4,
            "step_number": 1,
            "step_text": "Start a campfire"
        },
        {
            "id": 5,
            "step_number": 2,
            "step_text": "Toast Marshmellow to perfection"
        },
        {
            "id": 6,
            "step_number": 3,
            "step_text": "Split Grahm Cracker in half"
        },
        {
            "id": 7,
            "step_number": 4,
            "step_text": "Place 1/2 Chocolate Bar on one of the Grahm Cracker Halfs"
        },
        {
            "id": 8,
            "step_number": 5,
            "step_text": "Place toasted marshmellow ontop of Chocolate Bar"
        },
        {
            "id": 9,
            "step_number": 6,
            "step_text": "Place other half of cracker ontop of the marshmellow"
        }
    ],
    "id": 3,
    "ingredients": [
        {
            "id": 9,
            "ingredient": "Large Marshmellow",
            "qty": 1,
            "unit": "ea"
        },
        {
            "id": 10,
            "ingredient": "Grahm Cracker",
            "qty": 1,
            "unit": "ea"
        },
        {
            "id": 11,
            "ingredient": "Chocolate Bar",
            "qty": 0.5,
            "unit": "ea"
        }
    ],
    "prep_time": 300,
    "recipe_name": "Smores",
    "servings": 1
}
```

### api/recipes/[recipe_id_number]
Endpoint to access a specific recipe.
#### Method: GET
##### Summary
 Returns the Recipe, Ingredients and Directions for the recipe reference by [recipe_id_number]
##### Request Data
None

##### Response Data
JSON object
```
{
    "cook_time": [INT Time to cook in seconds],
    "description": "Breif description",
    "directions": [
        ...
    ],
    "id": [Database ID Number],
    "ingredients": [
        ...
    ],
    "prep_time": [INT Time to prep in seconds],
    "recipe_name": "Name of the Recipe",
    "servings": [INT Number of Servings]
}
```
##### Example:
 Request:
 ```bash
GET http://localhost:5000/api/recipes/3
 ```
 Response:
 ```JSON
{
    "cook_time": 120,
    "description": "Tastey Campfire Smores",
    "directions": [
        {
            "id": 4,
            "step_number": 1,
            "step_text": "Start a campfire"
        },
        {
            "id": 5,
            "step_number": 2,
            "step_text": "Toast Marshmellow to perfection"
        },
        {
            "id": 6,
            "step_number": 3,
            "step_text": "Split Grahm Cracker in half"
        },
        {
            "id": 7,
            "step_number": 4,
            "step_text": "Place 1/2 Chocolate Bar on one of the Grahm Cracker Halfs"
        },
        {
            "id": 8,
            "step_number": 5,
            "step_text": "Place toasted marshmellow ontop of Chocolate Bar"
        },
        {
            "id": 9,
            "step_number": 6,
            "step_text": "Place other half of cracker ontop of the marshmellow"
        }
    ],
    "id": 3,
    "ingredients": [
        {
            "id": 9,
            "ingredient": "Large Marshmellow",
            "qty": 1,
            "unit": "ea"
        },
        {
            "id": 10,
            "ingredient": "Grahm Cracker",
            "qty": 1,
            "unit": "ea"
        },
        {
            "id": 11,
            "ingredient": "Chocolate Bar",
            "qty": 0.5,
            "unit": "ea"
        }
    ],
    "prep_time": 300,
    "recipe_name": "Smores",
    "servings": 1
}
 ```

#### Method: PUT
##### Summary
 Updates the recipe referenced by [recipe_id_number]
##### Request Data

##### Response Data

##### Example:
 Request:
 ```BASH

 ```
Response:
 ```JSON

 ```

#### Method: DELETE
##### Summary
 Deletes a Recipe and all child ingredients and directions.
##### Request Data
None
##### Response Data

##### Example:
 Request:
 ```bash

 ```
 Response:
 ```JSON

 ```