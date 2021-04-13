import click

def printwinners_json(number_of_winners):
    #lottery_template = select_lottery_template()
    #print(lottery_template)
    winners = losulosu_json(number_of_winners)
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
            #winners_loader[x]['prize'] = lottery_template['prizes'][0]
            current_winner_first_name = winners_loader[x]['first_name']
            current_winner_last_name = winners_loader[x]['last_name']
            print(current_winner_first_name, current_winner_last_name)# + " has won", winners_loader[x]['prize']['name'])
        print(winners_loader)   
    return(winners)
def printwinners(csv_obj):
    winners = losulosu_csv(csv_obj, number_of_winners)
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

def losulosu_csv(csv_obj, items):
    with open(csv_obj) as csv_file_opened:
        csv_reader = csv.reader(csv_file_opened, delimiter=',')
        line_count = 0
        all_weights = []
        all_ids = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:                
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
        
class Config(object):

    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config, ensure = True)

#@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type=click.Path())



@click.command()
@click.argument("input", type=click.File("rb"), nargs=-1)
@click.argument("output", type=click.File("wb"))
@pass_config
def inout(input, output, config, verbose, home_directory):
    for f in input:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            output.write(chunk)
            output.flush()
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory
    
    if verbose:
        click.echo('We are in verbose mode')



@click.option('--string', default='World',
                help='This is the the thing that is greeted.')
@click.option('--repeat', default=1,
                help='How many times you should be greeted.')

@click.argument('out', type=click.File('w'), default=None, required=False)

@pass_config
def say(config, string, repeat, out):
    #print('Hello %s!' % string)
    """This scripts greets you."""
    if config.verbose:
        click.echo('We are in verbose mode')
    click.echo('Home directory is %s' % config.home_directory)
    click.echo(out)
    for x in range(repeat):
        click.echo('Hello %s!' % string, file=out)

if __name__ == '__main__':
    cli()


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