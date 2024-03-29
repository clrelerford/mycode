#!/usr/bin/env python3

"""Final Project:Recipe Search | CRelerford"""
## Converting JSON from an API to python data types using the Python standard library
## The API we will be reading from is: https:api.edamam.com/api/recipes/v2?

import os
import urllib.request
import json
from pyinputplus import inputMenu


# define base URL

# user search options
diet=["balanced", "high-fiber", "high-protein", "low-carb", "low-fat", "low-sodium"]
health=["dairy-free", "egg-free", "gluten-free", "paleo", "peanut-free", "shellfish-free", "soy-free", "vegan", "vegetarian"]
mealType=["breakfast", "brunch", "lunch", "dinner", "snack"]

diet= inputMenu(diet, numbered=True)
health= inputMenu(health, numbered=True)
mealType= inputMenu(mealType, numbered=True)


API = f"https://api.edamam.com/api/recipes/v2?type=public&app_id=008acd60&app_key=a1ed70789362dcf0ee8c4977a77efb2e&diet={diet}&health={health}&mealType={mealType}"

print(API)

def main():
    """run time code"""
    
    # from now on all commands will run from this directory
    os.chdir("/home/student/mycode")

    #perform an http get request
    response = urllib.request.urlopen(API)

    #strip JSON off of response
    data = response.read()
    json_data = json.loads(data)

    #loop through the recipes and print their names
    for recipe in json_data["hits"]:
        print(recipe["recipe"]["label"])
        print(recipe["recipe"]["url"])
        print(recipe["recipe"]["ingredientLines"], sep = "\n")
        print("")

if __name__ == '__main__':
    main()
