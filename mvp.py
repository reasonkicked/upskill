import json, random, pathlib, csv, sys
from urllib.request import urlopen
import ast
import click


number_of_winners = 3#int(input("Enter a number of winners: "))


# function loads .csv or .json file and returns JSON list
def read_input_file(file_path):
    if file_path.endswith(".json"): 
        loaded_file = json.load(open(file_path,"r"))         
        loaded_file = json.dumps(loaded_file, indent=4)
        print(loaded_file) 
        return loaded_file
    elif file_path.endswith(".csv"): 
        loaded_file = json.dumps(list(csv.DictReader(open(file_path))), indent = 4)        
        return loaded_file
    else: raise ValueError("The file is not json nor csv")


json_obj = read_input_file("data/participants1.csv")
print(type(json_obj))
print(json_obj)
original_stdout = sys.stdout # Save a reference to the original standard output

with open('participants_converted.json', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created.
    print(json_obj)
    sys.stdout = original_stdout # Reset the standard output to its original value


# function losulosu_json returns array of winners
def losulosu_json(items):
    all_weights = []
    all_indexes = []
    with open("participants_converted.json") as json_file_opened:
        json_loader = json.load(json_file_opened)
    for person in range(len(json_loader)):
        current_index  = json_loader[person]['id']
        current_index = ast.literal_eval(current_index)
        all_indexes.append(current_index)
        try:
            current_weight = json_loader[person]["weight"]            
            current_weight = ast.literal_eval(current_weight)            
            all_weights.append(current_weight)            
        except:
            all_weights.append(1)
    #print(all_weights)
    randomList = random.choices(all_indexes, weights = all_weights, k=items)
    print(randomList, "in losulosu_json")
    return randomList



losulosu_json(number_of_winners)


def printwinners_json():
    
    winners = losulosu_json(number_of_winners)
    data_from_csv = {}
    #print(winners)
    list_of_winners = json.dumps(winners)
    print(list_of_winners)
    with open("jsonfile.json", 'w') as jsonFile:
        jsonFile.write(json.dumps(data_from_csv, indent=4))

    with open("participants_converted.json") as json_file_opened:
        json_loader = json.load(json_file_opened)

    data=[]
    for x in winners:
        my_item = next((item for item in json_loader if item['id'] == str(x)), None)
        print(my_item)
        data.append(my_item)

    
    print(data)
    with open("winners.json", 'w') as winners_file:
        winners_file.write(json.dumps(data, indent=4))

    with open("winners.json") as winners_file:
        winners_loader = json.load(winners_file)  
        print("The list of winners:") 
        for x in range(len(winners_loader)):
            current_winner_first_name = winners_loader[x]['first_name']
            current_winner_last_name = winners_loader[x]['last_name']
            print(current_winner_first_name, current_winner_last_name + " has won.")
            
    return(winners)

#printwinners("data/participants1.csv")
#printwinners_json("data/participants1.json")
printwinners_json()





