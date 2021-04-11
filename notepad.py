"""
data = {"sensors":
        {"-KqYN_VeXCh8CZQFRusI":
            {"bathroom_temp": 16,
             "date": "02/08/2017",
             "fridge_level": 8,
             "kitchen_temp": 18,
             "living_temp": 17,
             "power_bathroom": 0,
             "power_bathroom_value": 0,
             "power_kit_0": 0
        },
        "-KqYPPffaTpft7B72Ow9":
            {"bathroom_temp": 20,
             "date": "02/08/2017",
             "fridge_level": 19,
             "kitchen_temp": 14,
             "living_temp": 20,
             "power_bathroom": 0,
             "power_bathroom_value": 0
        },
        "-KqYPUld3AOve8hnpnOy":
            {"bathroom_temp": 23,
             "date": "02/08/2017",
             "fridge_level": 40,
             "kitchen_temp": 11,
             "living_temp": 10,
             "power_bathroom": 1,
             "power_bathroom_value": 81,
        }
    }
}
kitchen_temp = data["sensors"]["-KqYN_VeXCh8CZQFRusI"]["kitchen_temp"]
print(kitchen_temp)
"""
#with urlopen("https://gist.githubusercontent.com/kinlane/c5e71db5769a6d6b7f221ba89686e3e0/raw/29e9c19907ff36899d4f2b9b6acbc42c1c491dcb/apis-json-example.json") as response:
 #   source = response.read()

#data = json.loads(source)

#usd_rates = dict
#print(data)


#for item in data['apis']:
 #   print(item)
 #   type_of_resource = item['properties']
  #  print(type_of_resource)
	#price = item['resource']['fields']['price']
	#usd_rates[name] = price
	#print(name, price)

#print(50 * float(usd_rates['USD/EUR']))

#for person in participants1:
#    print(person['id'], person['first_name'], person['last_name'])

#for person in participants2:
#    print(person['id'], person['first_name'], person['last_name'], person['weight'])
#with open('winners.json', 'w') as f:
 #   json.dump(data, f, indent=2)

"""
people_string = '''
{
    "people": [
        {
            "firstName": "Mietek",
            "lastName": "Gosztyła",
            "hobbies": ["running", "sky diving", "singing"],
            "age": 35,
            "weight": 2, 
            "Phone": "123123212"
        },
        {
            "firstName": "Kazek",
            "lastName": "Laskow",
            "hobbies": ["running", "sky diving", "singing"],
            "Phone": "123123212",
            "age": 35,
            "weight": 2 
        }
    ]
}
'''
#with open("data_file.json", "w") as write_file:
#    json.dump(data, write_file)
#with open("participants1.json", "r") as read_file:
#    data = json.load(read_file)
#print(data)
#data = json.loads(people_string)
#print(type(data['people']))
"""
"""
for person in data['people']:
    print(person['firstName'])

for person in data['people']:
    print(person)

for person in data['people']:
    del person['Phone']

for person in data['people']:
    print(person)

new_string = json.dumps(data, indent=2, sort_keys=True) #each level

print(new_string)
"""