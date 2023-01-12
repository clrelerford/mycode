#!/usr/bin/env python3

"""Final Project:Recipe Search | CRelerford"""
## Converting JSON from an API to python data types using the Python standard library
## The API we will be reading from is: https:api.edamam.com/api/recipes/v2?

import os
import urllib.request
import json



# build a URL
API = "https://api.edamam.com/api/recipes/v2?

type=public
&
app_id=008acd60
&
app_key=a1ed70789362dcf0ee8c4977a77efb2e 
&
diet=[]

def main():
    ""run time code""
    
    # from now on all commands will run from this directory
    os.chdir("/home/student/mycode")

    #perform an http get request
    response = urllib.request.urlopen(API)

    #strip JSON off of response
    data = response.read()
    

