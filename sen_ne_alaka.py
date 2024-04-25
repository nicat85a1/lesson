{
"name": "john",
"age": 30,
"city": "New York",
"is_student": False,
"grades": [85, 90, 88],
"address": {
    "street": "123 Main St",
    "zip_code": "10001",
},
"is_employed": True,
"spouses": None
}

json_str = '{"name": "john", "age": 30, "city": "New York", "is_student": false}'
print(type(json_str))

import json

my_json = json.loads(json_str)
print(type(my_json))
print(my_json["name"])

"""users = [
    {
        "name": "john",
        "age": 30,
    },
    {
        "name": "jane",
        "age": 25,
    }
]

print(type(users))

for user in users:
    print(user)"""