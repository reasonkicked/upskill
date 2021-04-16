import json, random, pathlib, csv, sys
from urllib.request import urlopen
import ast
#import click


class Participant:
    def __init__(self, id, first_name, last_name, weight = 1):
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._weight = weight

    @property
    def get_first_name(self):        
        return self._first_name
    @property
    def get_last_name(self):        
        return self._last_name
    @property
    def get_id(self):        
        return self._id
    def get_weight(self):
        return self._weight
    #@last_name.getter
    #def last_name(self):
     #   return self._last_name

class Prize:
    def __init__(self, id, prize_name, prize_amount):
        self._id = id
        self._prize_name = prize_name
        self._prize_amount = prize_amount
    @property
    def print_prize_name(self):
        print(self._prize_name)
        return self._prize_name
    @property
    def get_prize_name(self):
        return self._prize_name
    pass

class Lottery:
    def __init__(self, list_of_participants, list_of_weights, list_of_prizes):
        self._list_of_participants = list_of_participants
        self._list_of_prizes = list_of_prizes
        self._list_of_weights = list_of_weights
        
    @property
    def print_list_of_participants(self):
        print(self._list_of_participants)
        return self._list_of_participants

    def losulosu(self):
        #for x in (range(len(lis)))
        winners = []
        winners = random.choices(list(set(self._list_of_participants)), weights=self._list_of_weights, k=len(self._list_of_prizes))
        #print(winners)
        for person in range(len(winners)):
            print(winners[person].get_id, winners[person].get_first_name, winners[person].get_last_name, " has won ", self._list_of_prizes[person].get_prize_name)

    
# function loads .csv or .json file and returns JSON list
def read_input_file(file_path):
    if file_path.endswith(".json"): 
        loaded_file = json.load(open(file_path,"r"))         
        loaded_file = json.dumps(loaded_file, indent=4)
        print("JSON file loaded successfully.") 
        return loaded_file
    elif file_path.endswith(".csv"): 
        loaded_file = json.dumps(list(csv.DictReader(open(file_path))), indent = 4)  
        print("CSV file loaded successfully.")       
        return loaded_file
    else: raise ValueError("The file is not json nor csv.")


"""
function load_participants creates a list of Participant class objects and returns list of weights
"""
def load_participants():
    with open("participants_converted.json") as json_file_opened:
        json_loader = json.load(json_file_opened)
        
        list_of_participants = []
        list_of_weights = []
        for person in range(len(json_loader)):
            participant_id  = json_loader[person]['id']
            participant_id = ast.literal_eval(participant_id)
            participant_first_name = json_loader[person]['first_name']
            participant_last_name = json_loader[person]['last_name']
            
            try:
                current_weight = json_loader[person]["weight"]            
                current_weight = ast.literal_eval(current_weight)
                list_of_weights.append(current_weight)            
            except:
                current_weight = 1
                list_of_weights.append(1)      
            participant = Participant(participant_id, participant_first_name, participant_last_name, current_weight)
            list_of_participants.append(participant)            
        
        return list_of_participants, list_of_weights
        #return ('[%s]' % ', '.join(map(str, list))) # to return list without the quotation marks
        
def load_prizes(lottery_template):

    with open(lottery_template) as json_file_opened:
        json_loader = json.load(json_file_opened)

        list_of_prizes = []
        for prize in range(len(json_loader['prizes'])):
            prize_id = json_loader['prizes'][prize]['id']
            prize_name = json_loader['prizes'][prize]['name']
            prize_amount = json_loader['prizes'][prize]['amount']
            
            prize = Prize(prize_id, prize_name, prize_amount)
            
            list_of_prizes.append(prize)
        print(list_of_prizes)
        return list_of_prizes
        
def conversion_to_json(json_obj):
    original_stdout = sys.stdout # Save a reference to the original standard output
    with open('participants_converted.json', 'w') as f:
        sys.stdout = f 
        print(json_obj)
        sys.stdout = original_stdout 


def lottery_menu():
    print("Welcome to Losowanko!!! Please select the list of participants and the list of prizes: ")
    
    #todo - prevent input from being anything but 4 numbers
    file_path_select = input("""Please select the participants file path: \n
                            1 - data/participants1.csv \n 
                            2 - data/participants1.json \n 
                            3 - data/participants2.csv \n 
                            4 - data/participants2.json \n
                            """) 
    participants_path = "data/participants1.csv"

    def select_participants_file(x):
        return {
            '1': "data/participants1.csv",
            '2': "data/participants1.json",
            '3': "data/participants2.csv",
            '4': "data/participants2.json",
        }.get(x, 1)
    participants_path = select_participants_file(file_path_select)

    #todo - prevent input from being anything but 4 numbers
    file_path_select = input("""Please select the lottery template path: \n
                            1 - data/lottery_templates/item_giveaway.json \n 
                            2 - data/lottery_templates/separate_prizes.json \n                             
                            """) 
    def select_lottery_template_file(x):
        return {
            '1': "data/lottery_templates/item_giveaway.json",
            '2': "data/lottery_templates/separate_prizes.json",
        }.get(x, 1)
    lottery_template = select_lottery_template_file(file_path_select)

    #conversion participants file to common format
    json_obj = read_input_file(participants_path)
    conversion_to_json(json_obj)
    
    
    list_of_prizes = load_prizes(lottery_template)
    list_of_participants, list_of_weights = load_participants()
    


    multilotek = Lottery(list_of_participants, list_of_weights, list_of_prizes)


    multilotek.losulosu()


lottery_menu()


"""
not-objected

#lottery_menu()
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

"""