import lottery.lottery
import sys
import click


class Config(object):
    def __init__(self):
        self.verbose = False


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type=click.Path())
@pass_config
def main(config, verbose, home_directory):
    """The main routine."""
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory

    print("This is the main routine.")
    print("It should do something interesting.")


@main.command()
@click.option('--string', default='World', help='This is the the thing that is greeted.')
@click.option('--repeat', default=1, help='How many times you should be greeted.')
@click.argument('out', type=click.File('w'), default=None, required=False)
@pass_config
def say(config, string, repeat, out):
    """Greetings in say"""
    if config.verbose:
        click.echo('We are in verbose mode')
    click.echo('Home directory is %s' % config.home_directory)
    for x in range(repeat):
        click.echo('Hello %s!' % string, file=out)
    lottery.lottery_menu()


def greetings(config, string, repeat, out):
    """This scripts greets you."""
    if config.verbose:
        click.echo('We are in verbose mode')
    click.echo('Home directory is %s' % config.home_directory)
    click.echo(out)
    for x in range(repeat):
        click.echo('Hello %s!' % string, file=out)


@main.command()
@click.argument("input", type=click.File("rb"), nargs=-1)
@click.argument("output", type=click.File("wb"))
# @pass_config
def inout(config, input, output):
    for f in input:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            output.write(chunk)
            output.flush()


@main.command()
@click.argument("json_obj", type=click.Path("rb"))
@click.argument("items", type=int, default=2)
# @pass_config
def losulosujson(config, json_obj, items):
    all_weights = []
    print(json_obj)

    with open(json_obj) as json_file_opened:
        json_loader = json.load(json_file_opened)
    for person in range(len(json_loader)):
        try:
            current_weight = json_loader[person]["weight"]
            current_weight = ast.literal_eval(current_weight)
            all_weights.append(current_weight)
        except:
            all_weights.append(1)
    # print(all_weights)
    randomList = random.choices(json_loader, weights=all_weights, k=items)
    print(randomList)
    return randomList


@main.command()
@click.argument("csv_obj", type=click.Path("rb"))
@click.argument("items", type=int, default=2)
# @pass_config
def losulosucsv(config, csv_obj, items):
    with open(csv_obj) as csv_file_opened:
        csv_reader = csv.reader(csv_file_opened, delimiter=',')
        line_count = 0
        all_weights = []
        all_ids = []
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
                current_id = ast.literal_eval(row[0])
                all_ids.append(current_id)
                try:
                    current_weight = ast.literal_eval(row[3])
                    all_weights.append(current_weight)
                except:
                    all_weights.append(1)
        # print(all_ids)
        # print(all_weights)
        randomList = random.choices(all_ids, weights=all_weights, k=items)
        print(randomList)
        return randomList


# lottery.lottery_menu()

# lottery.cli()


if __name__ == "__main__":
    main()
    #  print("File one executed when ran directly")

