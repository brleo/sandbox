from pathlib import Path
import csv
import json

def convert_csv_to_json(csv_file_path, json_file_path):
    path = Path(csv_file_path)
    if path.is_file():
        rows = []
        with open(csv_file_path, encoding="utf-8") as csv_text_wrapper: 
            csv_text_reader = csv.DictReader(csv_text_wrapper) 

            for row in csv_text_reader: 
                rows.append(row)
    
        with open(json_file_path, "w", encoding="utf-8") as json_text_wrapper: 
            json_element = json.dumps(rows, indent=4)
            json_text_wrapper.write(json_element)
    else:
        print("{} is not a valid file.".format(csv_file_path))

convert_csv_to_json("common/yob2021.txt", "common/yob2021.json")