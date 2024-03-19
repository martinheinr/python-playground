import json
import yaml
import os

people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]


current_dir = os.getcwd()
print(current_dir)

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2)

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)

#load deserializes json from a file to basic python objects
#The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file.  
with open('people.json', 'r') as people_json:
    people = json.load(people_json)
    
print(people)