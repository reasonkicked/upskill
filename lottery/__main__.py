import lottery.lottery
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
    """
    Welcome to Grand Lottery menu. To see available options run
    lottery default --help

    example:
    lottery default --participants data/participants1.csv --lottery_template data/lottery_templates/separate_prizes.json
    """
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory

    # print("This is the main routine.")
    # print("It should do something interesting.")


@main.command()
@click.option('--participants', type=click.Choice(['data/participants1.csv', 'data/participants2.csv',
                                                   'data/participants1.json', 'data/participants2.json']))
@click.option('--lottery_template', type=click.Choice(['data/lottery_templates/item_giveaway.json',
                                                       'data/lottery_templates/separate_prizes.json']))
@click.option('--string', default='World', help='This is the the thing that is greeted.')
@click.option('--repeat', default=1, help='How many times you should be greeted.')
@click.argument('out', type=click.File('w'), default=None, required=False)
@pass_config
def default(config, string, repeat, out, participants, lottery_template):
    """
    Default lottery
    """
    if config.verbose:
        click.echo('We are in verbose mode')
    # click.echo('Home directory is %s' % config.home_directory)
    for x in range(repeat):
        click.echo('Hello %s!' % string, file=out)
    lottery.lottery_menu(participants, lottery_template)


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
    # lottery.lottery_menu()


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
@pass_config
def inout(config, input, output):
    for f in input:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            output.write(chunk)
            output.flush()


# lottery.lottery_menu()

# lottery.cli()


if __name__ == "__main__":
    main()
    #  print("File one executed when ran directly")
