import json
import random
import csv
import sys
import ast

import lottery
from debugly import debug, debugmethods


# function read_input_file loads .csv or .json file and returns JSON list
# @debug(prefix='***')
def read_input_file(file_path):
    if file_path.endswith(".json"):
        loaded_file = json.load(open(file_path, "r"))
        loaded_file = json.dumps(loaded_file, indent=4)
        # print(loaded_file)
        print("JSON file loaded successfully.")
        return loaded_file
    elif file_path.endswith(".csv"):
        loaded_file = json.dumps(list(csv.DictReader(open(file_path))), indent=4)
        print("CSV file loaded successfully.")
        # print(loaded_file)
        return loaded_file
    else:
        raise ValueError("The file is not json nor csv.")

# function conversion_to_json creates file containing participants from loaded file in common format


def conversion_to_json(json_obj):
    original_stdout = sys.stdout  # Save a reference to the original standard output
    with open('participants_converted.json', 'w') as f:
        sys.stdout = f
        print(json_obj)
        sys.stdout = original_stdout


"""
Function load_participants creates a list of Participant class objects and returns list of weights (if they exists).
"""


def load_participants():
    with open("participants_converted.json") as json_file_opened:
        json_loader = json.load(json_file_opened)

        list_of_participants = []
        list_of_weights = []
        for person in range(len(json_loader)):
            participant_id = json_loader[person]['id']
            participant_id = ast.literal_eval(participant_id)
            participant_first_name = json_loader[person]['first_name']
            participant_last_name = json_loader[person]['last_name']

            try:
                current_weight = json_loader[person]["weight"]
                current_weight = ast.literal_eval(current_weight)
                list_of_weights.append(current_weight)
            except KeyError:
                current_weight = 1
                list_of_weights.append(1)

            participant = lottery.Participant(participant_id, participant_first_name, participant_last_name,
                                              current_weight)
            list_of_participants.append(participant)

        return list_of_participants, list_of_weights
        # return ('[%s]' % ', '.join(map(str, list))) # to return list without the quotation marks


"""
Function load_prizes creates a list of Prize class objects and returns list of prizes
"""


def load_prizes(lottery_template):
    with open(lottery_template) as json_file_opened:
        json_loader = json.load(json_file_opened)

        list_of_prizes = []
        for prize in range(len(json_loader['prizes'])):
            prize_id = json_loader['prizes'][prize]['id']
            prize_name = json_loader['prizes'][prize]['name']
            prize_amount = json_loader['prizes'][prize]['amount']

            prize = lottery.Prize(prize_id, prize_name, prize_amount)

            list_of_prizes.append(prize)
        # print(list_of_prizes)
        return list_of_prizes


def get_int(prompt):
    while True:
        try:
            choice = int(input(prompt))
            break
        except ValueError:
            print('Please enter an integer value.')
    return choice


def lottery_menu(participants_template_file, lottery_template_file):
    participants_path = participants_template_file

    lottery_template = lottery_template_file

    # conversion participants file to common format
    json_obj = read_input_file(participants_path)
    conversion_to_json(json_obj)

    # creating list of prizes
    list_of_prizes = load_prizes(lottery_template)
    list_of_participants, list_of_weights = load_participants()

    awesome_lottery = lottery.Lottery(list_of_participants, list_of_weights, list_of_prizes)

    awesome_lottery.random_winners_choice()


if __name__ == "__main__":
    print("File two executed when ran directly")
else:
    pass
    #  print("File two executed when imported")
