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
def solvePartI(numbers): 
    result = 0
    for number in numbers:
        result += int(number)
    return result

def filter_json(obj):
    if isinstance(obj, list):
        #print("----LOS Gehts Array-----")
        filtered_list = []
        for item in obj:
            if isinstance (item, (dict, list)):
                #print(item, "ist Verschachtelt")
                filtered_list.append(filter_json(item))
            else:
                filtered_list.append(item)
        return filtered_list
    elif isinstance(obj, dict):
        #print("----LOS Gehts Objekt-----")
        filtered_dict = {}
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                #print(value, "ist verschachtelt")
                filtered_dict[key] = filter_json(value)
            elif "red" in str(value):
                filtered_dict = {}
                return filtered_dict
            else:
                #print(value,"ist normal")
                filtered_dict[key] = value
        return filtered_dict


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
    return filtered_json_string
    
def solvePartII(): 
    processd = process_json_txt_file(file.name)
    with open("processed_input.txt", 'w') as outfile:
        outfile.write(processd)
    numbers = re.findall('-?\d+',processd)
    result = 0
    for number in numbers:
        result += int(number)
    print("Ergebnis II",result)
    print("done")

print("Ergebnis I",solvePartI(numbers))
solvePartII()

