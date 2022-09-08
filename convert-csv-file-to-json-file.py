from dataclasses import field, fields
from collections import defaultdict
from pathlib import Path
from datetime import datetime

import csv
import json
import os

def convert_csv_to_json(csv_file_path, json_file_path, field_names, no_empty_values):
    
    path = Path(csv_file_path)
    
    if path.is_file():        
        
        with open(csv_file_path, encoding="utf-8") as csv_text_wrapper:
            
            csv_text_reader = csv.DictReader(csv_text_wrapper, field_names)
            rows = []
            
            if no_empty_values:
                for row in csv_text_reader:
                    for column in field_names:
                        if row[column]:
                            rows.append(row)
            else:
                for row in csv_text_reader:
                    rows.append(row)
    
        with open(json_file_path, "w", encoding="utf-8") as json_text_wrapper:
            json_element = json.dumps(rows, indent=4, ensure_ascii=False)
            json_text_wrapper.write(json_element)
    else:
        print("{} is not a valid file.".format(csv_file_path))
        

def convert_csv_to_jsons(csv_file_path, json_files_path, field_names, split_field_names, main_field_name):
    
    path = Path(csv_file_path)
    
    if path.is_file():
        
        rows = []
        
        with open(csv_file_path, encoding="utf-8") as csv_text_wrapper:
            
            csv_text_reader = csv.DictReader(csv_text_wrapper, field_names)
            
            columns_name = defaultdict(list)
            
            for row in csv_text_reader:
                rows.append(row)
                for (k,v) in row.items():
                    columns_name[k].append(v)

        if not os.path.exists(json_files_path):
            os.makedirs(json_files_path)
                        
        for column in split_field_names:
            
            filter_rows = []
            json_file = (json_files_path + "/" + main_field_name + "_" + column + ".json")
            
            if "+" in column:

                columns = column.split("+")
                    
                for counter in range(0, len(rows)):
                    
                    column_values = {}                    
                    save = True
                    
                    for col in columns:
                        if columns_name[col][counter]:
                            column_values[col] = columns_name[col][counter]
                        else:
                            save = False
                            break
                    
                    if save:
                        filter_rows.append(column_values)
                    
                with open(json_file, "w", encoding="utf-8") as json_text_wrapper:
                    json_element = json.dumps(filter_rows, indent=4, ensure_ascii=False)
                    json_text_wrapper.write(json_element)
                    
            else:
                filter_rows = []
                json_file = (json_files_path + "/" + main_field_name + "_" + column + ".json")
                
                for counter in range(0, len(rows)):
                    
                    column_values = {}
                    column_values[column] = columns_name[column][counter]
                
                    filter_rows.append(column_values)
                    
                with open(json_file, "w", encoding="utf-8") as json_text_wrapper:
                    json_element = json.dumps(filter_rows, indent=4, ensure_ascii=False)
                    json_text_wrapper.write(json_element)
                
    else:
        print("{} is not a valid file.".format(csv_file_path))




## call convert_csv_to_json()
## print("Starting at {}".format(datetime.now()))
## field_names = ("firstName","lastName","gender","country")
## convert_csv_to_json("common/csv/DJ.csv", "common/json/DJ.json", field_names, False)
## print("Finished at {}".format(datetime.now()))

## call convert_csv_to_jsons()
print("Starting at {}".format(datetime.now()))
field_names = ("firstName","lastName","gender","country")
split_field_names = ("firstName+gender","lastName")
main_field_name = ("country")
convert_csv_to_jsons("common/csv/BR.csv", "common/json/BR", field_names, split_field_names, main_field_name)
print("Finished at {}".format(datetime.now()))