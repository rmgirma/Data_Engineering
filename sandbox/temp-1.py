import json
import re
from pprint import pp
import requests

# Set the global variable "results"
global results
results = []

def fetch_data(page_number):
    response = requests.get(f'https://swapi.dev/api/people/?page={page_number}')
    data = response.json()
    return data

# Fetch data from all 9 pages of the Star Wars API
for i in range(1, 10):
    page_data = fetch_data(i)
    results.extend(page_data['results'])

def get_character_names():
    global results
    names = [character['name'] for character in results]
    return names

# Test the function
character_names = get_character_names()
pp(character_names)

