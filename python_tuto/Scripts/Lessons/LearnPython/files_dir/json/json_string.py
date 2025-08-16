import json


json_str = '''
{
    "students": [
        {
            "id": 1,
            "name": "Anjie",
            "age": 21,
            "married": false
        },
        {
            "id": 2,
            "name": "Njad",
            "age": 23,
            "married": true
        }
    ]
}
'''

data = json.loads(json_str)
print(type(data))
print(data)

# adding new data= dumping
data['test'] = True
new_json = json.dumps(data, indent=4)
print(new_json)
