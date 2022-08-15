import json

with open("common/yob2021.txt", encoding="utf-8") as file:
    lines = [line.rstrip() for line in file]

names = []

for counter in range(0, len(lines)):
    columns = lines[counter].split(",")
    names.append(columns)

json_dump = json.dumps(names)

print(json_dump)