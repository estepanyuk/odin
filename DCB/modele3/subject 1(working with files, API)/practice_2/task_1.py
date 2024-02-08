import json
import random
from pprint import pprint

str_json = """
{
    "response": {
        "count": 32363,
        "items": [
            {
                "id": 287350527,
                "first_name": "Sonya",
                "last_name": "Kargina",
                "photo_50": "https://pp.vk.me/...2c1/J2EL--qCZa8.jpg"
            },
            {
                "id": 341523166,
                "first_name": "Slava",
                "last_name": "Kholod",
                "photo_50": "https://pp.vk.me/...321/eTxKNQSJMuk.jpg"
            }
        ]
    }
}
"""
print(type(str_json))

data = json.loads(str_json)
print(type(data))
#вариант 1
#print(json.dumps(data["response"]["count"], indent=4))
#print(json.dumps(data["response"]["items"], indent=4))
#вариант 2
'''
for item in data["response"]["items"]:
    pprint(item)
'''

#print(data["response"]["items"][0]["first_name"], data["response"]["items"][0]["last_name"])

'''
for item in data["response"]["items"]:
    print(item["first_name"], item["last_name"])
'''

for item in data["response"]["items"]:
    del item["id"]
    item["likes"] = random.randint(100, 200)

pprint(data["response"]["items"])









