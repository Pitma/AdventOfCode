import re
import numpy as np
import json

isTest = False

if isTest:
    file = open("sample.txt","r")
else:
    file = open("input.txt","r")

file_data = file.read()

numbers = re.findall('-?\d+',file_data)
#fiel_pattern = re.compile(r'\[[^\[]*red.*?\][^\]]|\{[^\{]*red.\}[^\}]')
#print(fiel_pattern.sub('',file_data))
def solvePartI(numbers): 
    result = 0
    for number in numbers:
        result += int(number)
    return result

def filter_json(obj):
    #print(obj)
    if isinstance(obj, list):
        filtered_list = []
        for item in (filter_json(item) for item in obj):
            print("ITEM",item)
            if "red" not in str(item):
                filtered_list.append(item)
        return filtered_list
    elif isinstance(obj, dict):
        filtered_dict = {}
        for key, value in obj.items():
            print("VALUE",value)
            if "red" not in str(value):
                filtered_dict[key] = filter_json(value)
        return filtered_dict
    else:
        return obj

def process_json_txt_file(input_file):
    with open(input_file, 'r') as infile:
        try:
            # Versuche, den Inhalt der Textdatei als JSON zu laden
            data = json.load(infile)
        except json.JSONDecodeError:
            print("Die Textdatei enthält kein gültiges JSON.")
            return
        
    with open("out.txt", 'w') as outfile:
        outfile.write(json.dumps(data,indent=2))

    filtered_data = filter_json(data)
    filtered_json_string = json.dumps(filtered_data, indent=2)
    print(filtered_json_string)
    return filtered_json_string
    
def solvePartII(numbers): 
    #filter all parts with "red"
    print(process_json_txt_file("input.txt"))
    #redo part1
    print("done")

print("Ergebnis I",solvePartI(numbers))
print("Ergebnis II",solvePartII(numbers))





