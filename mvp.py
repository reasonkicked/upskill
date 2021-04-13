import json, random, pathlib, csv, sys
from urllib.request import urlopen
import ast
import click


number_of_winners = 5#int(input("Enter a number of winners: "))


# function loads .csv or .json file and returns JSON list
def read_input_file(file_path):
    if file_path.endswith(".json"): 
        loaded_file = json.load(open(file_path,"r"))         
        loaded_file = json.dumps(loaded_file, indent=4)
        #print(loaded_file) 
        return loaded_file
    elif file_path.endswith(".csv"): 
        loaded_file = json.dumps(list(csv.DictReader(open(file_path))), indent = 4)        
        return loaded_file
    else: raise ValueError("The file is not json nor csv.")


# select json or csv file and convert it to json
json_obj = read_input_file("data/participants1.json")
#print(type(json_obj))
#print(json_obj)
original_stdout = sys.stdout # Save a reference to the original standard output
with open('participants_converted.json', 'w') as f:
    sys.stdout = f 
    print(json_obj)
    sys.stdout = original_stdout 


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
    all_indexes_set = set(all_indexes) #converting list to set to avoid repetitions
    print(all_indexes_set)
    randomList = random.choices(list(all_indexes_set), weights = all_weights, k=items)
    print(randomList, "in losulosu_json")
    return randomList


#losulosu_json(number_of_winners)

def item_giveaway_lottery():
    with open("data/lottery_templates/item_giveaway.json") as json_file_opened:
            json_loader = json.load(json_file_opened)
    lottery_template = json_loader
    #print(lottery_template)
    winners = losulosu_json(5)
    data_from_csv = {}
    #print(winners)
    list_of_winners = json.dumps(winners)
    print(list_of_winners, " winners returned by losulosu_json in printwinners_json")
    with open("jsonfile.json", 'w') as jsonFile:
        jsonFile.write(json.dumps(data_from_csv, indent=4))

    with open("participants_converted.json") as json_file_opened:
        json_loader = json.load(json_file_opened)

    data=[]
    for x in winners:
        my_item = next((item for item in json_loader if item['id'] == str(x)), None)
        data.append(my_item)
        
    print(data,  " converted json list of winners in printwinners_json")
    with open("winners.json", 'w') as winners_file:
        winners_file.write(json.dumps(data, indent=4))






    with open("winners.json") as winners_file:
        winners_loader = json.load(winners_file)
        #winners_loader[1]["prize"] = 3
        #print(winners_loader)
        print("The list of winners:")        
        for x in range(len(winners_loader)):
            winners_loader[x]['prize'] = lottery_template['prizes'][0]
            current_winner_first_name = winners_loader[x]['first_name']
            current_winner_last_name = winners_loader[x]['last_name']
            print(current_winner_first_name, current_winner_last_name + " has won", winners_loader[x]['prize']['name'])
        print(winners_loader)   
    return(winners)


def separate_prizes_lottery():
    with open("data/lottery_templates/separate_prizes.json") as json_file_opened:
            json_loader = json.load(json_file_opened)
    lottery_template = json_loader
    #print(lottery_template)
    winners = losulosu_json(3)
    data_from_csv = {}
    #print(winners)
    list_of_winners = json.dumps(winners)
    print(list_of_winners, " winners returned by losulosu_json in printwinners_json")
    with open("jsonfile.json", 'w') as jsonFile:
        jsonFile.write(json.dumps(data_from_csv, indent=4))

    with open("participants_converted.json") as json_file_opened:
        json_loader = json.load(json_file_opened)

    data=[]
    for x in winners:
        my_item = next((item for item in json_loader if item['id'] == str(x)), None)
        data.append(my_item)
        
    print(data,  " converted json list of winners in printwinners_json")
    with open("winners.json", 'w') as winners_file:
        winners_file.write(json.dumps(data, indent=4))

    with open("winners.json") as winners_file:
        winners_loader = json.load(winners_file)
        #winners_loader[1]["prize"] = 3
        #print(winners_loader)
        print("The list of winners:")        
        for x in range(len(winners_loader)):
            winners_loader[x]['prize'] = lottery_template['prizes'][x]
            current_winner_first_name = winners_loader[x]['first_name']
            current_winner_last_name = winners_loader[x]['last_name']
            print(current_winner_first_name, current_winner_last_name + " has won", winners_loader[x]['prize']['name'])
        print(winners_loader)   
    return(winners)


def lottery_menu():
    lottery_template_version = 2
    if lottery_template_version == 1:
        

        item_giveaway_lottery()

        
    elif lottery_template_version == 2:
        

        separate_prizes_lottery()
        

        
    else: raise ValueError("Entered value is incorrect.")



lottery_menu()


