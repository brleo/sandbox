import json
import secrets
  
json_file = open("common/yob2021.json")
json_data = json.load(json_file)

print(len(json_data))

json_elements = []

for counter in range(0, 10):
    json_element = secrets.choice(range(1, len(json_data) + 1))
    json_elements.append(json_element)
    
print(json_elements)

for json_element in json_elements:
    print(json_data[json_element])
  
json_file.close()