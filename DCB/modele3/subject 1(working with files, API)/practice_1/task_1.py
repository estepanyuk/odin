import requests
import json

response = requests.get('https://randomuser.me/api/').json()
print(type(response))

"""
#сереализация
to_python = json.dumps(response, indent=4)
print(type(to_python))
print(to_python)


#2 вариант
#десерилизация
y = json.loads(to_python)
print(type(y))

print(y["results"][0]["location"]["street"])
"""

#3 вариант запись в файл
with open('data.json', 'w') as file:
    json.dump(response, file)

with open('data.json', 'r') as j:
    json_data = json.load(j)
    print(type(json_data))
    to_python = json.dumps(json_data, indent=4)
    print(type(to_python))
    print(to_python)

y = json.loads(to_python)
print(y["results"][0]["login"])














