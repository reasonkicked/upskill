import json, random, pathlib, csv
from urllib.request import urlopen
import ast
import click


number_of_winners = 3#int(input("Enter a number of winners: "))

def read_input_File(file_path):
    if file_path.endswith(".json"): 
        loaded_file = json.load(open(file_path,"r"))   
        return loaded_file
    elif file_path.endswith(".csv"): 
        loaded_file = json.dumps(list(csv.DictReader(open(file_path))), indent = 4)
        print(loaded_file)
        return loaded_file
    else: raise ValueError("The file is not json nor csv")


read_input_File("data/participants1.")

def losulosu_json(json_obj, items):
    all_weights = []
    with open(json_obj) as json_file_opened:
        json_loader = json.load(json_file_opened)
    for person in range(len(json_loader)):
        try:
            current_weight = json_loader[person]["weight"]
            current_weight = ast.literal_eval(current_weight)
            all_weights.append(current_weight)
        except:
            all_weights.append(1)
    #print(all_weights)
    randomList = random.choices(json_loader, weights = all_weights, k=items)
    print(randomList)
    return randomList

def losulosu_csv(csv_obj, items):
    with open(csv_obj) as csv_file_opened:
        csv_reader = csv.reader(csv_file_opened, delimiter=',')
        line_count = 0
        all_weights = []
        all_ids = []
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
                current_id = ast.literal_eval(row[0])
                all_ids.append(current_id)
                try:
                    current_weight = ast.literal_eval(row[3])
                    all_weights.append(current_weight)
                except:
                    all_weights.append(1)
        #print(all_ids)
        #print(all_weights)
        randomList = random.choices(all_ids, weights = all_weights, k=items)
        print(randomList)
        return randomList
        
#losulosu_csv("data/participants2.csv", number_of_winners)

#losulosu_json("data/participants1.json", number_of_winners)

def printwinners(csv_obj):
    winners=losulosu_csv(csv_obj, number_of_winners)
    data_from_csv = {}
    with open(csv_obj) as csv_file_opened:
        csv_reader = csv.DictReader(csv_file_opened)
        for rows in csv_reader:
            id = rows['id']
            data_from_csv[id] = rows
    print(winners)
    with open("jsonfile.json", 'w') as jsonFile:
        jsonFile.write(json.dumps(data_from_csv, indent=4))

    with open("data/participants1.json") as json_file_opened:
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

printwinners("data/participants1.csv")





