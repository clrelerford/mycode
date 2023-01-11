#!/usr/bin/env python3

"""Looping with for challenge"""


farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


def main():

    farm_name = input("Which farm would you like to choose? (NE Farm, W Farm, or SE Farm)")

    for farm in farms:
        if farm["name"] == farm_name:
        animals = [animal for animal in farm["agriculture"] if animal not in ["carrots", "celery"]]
        print("The animals raised on " + farm_name + " is " + ", ".join(animals))

main()
