import json, random, pathlib
from urllib.request import urlopen
import ast


number_of_winners = 3#int(input("Enter a number of winners: "))

with open("data/participants1.json") as f:
    participants1 = json.load(f)

with open("data/participants2.json") as g:
    participants2 = json.load(g)

#print(type(participants1))

merged =  {"participant": participants1 + participants2}
#merged = participants2

to_json = json.dumps(merged, indent = 2)
#print(merged)
print(type(to_json))
print(type(merged))
print(type(participants2))
#print(participants2)
#rint(merged['participants'])
#randomList = random.choices(merged['participants'], k=number_of_winners)
#print(randomList)
#print(merged)
all_weights = []

for person in range(len(participants2)):
    current_weight = participants2[person]["weight"]
    current_weight = ast.literal_eval(current_weight)
    #print(current_weight)
    all_weights.append(current_weight)
print(all_weights)

number_of_participants = len(participants2)
#all_weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#print(all_weights)
print(number_of_participants)
def losulosu(json_obj, all_weights, items):
    randomList = random.choices(json_obj, weights = all_weights, k=items)
    print(randomList)
    return randomList

losulosu(participants2, all_weights, number_of_winners)

#print(randomList)
#for person in merged:
#   print(person['id'], person['first_name'], person['last_name'])