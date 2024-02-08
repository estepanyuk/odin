import json

with open('people.json') as file:
    people = json.load(file)

    people_sorted = sorted(people, key=lambda x: (x["age"], x["name"]))

    for person in people_sorted:
        print(f"{person["name"]}, {person["country"]}, {person["age"]}")

