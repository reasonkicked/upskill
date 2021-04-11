import json, random, pathlib, csv
from urllib.request import urlopen
import ast


number_of_winners = 3#int(input("Enter a number of winners: "))





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
        
losulosu_csv("data/participants2.csv", number_of_winners)

losulosu_json("data/participants1.json", number_of_winners)

