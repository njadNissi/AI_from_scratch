import json

with open("json\data.json", "r") as f:
    data = json.load(f)

print(data)
print(data.items())

with open("json\data2.json", "w") as f:
    json.dump(data, f, indent=4)
    # json.dump(data, f)
