import click

class Config(object):

    def __init__(self):
        self.verbose=False

pass_config = click.make_pass_decorator(Config, ensure = True)

@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type=click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory

    #if verbose:
    #    click.echo('We are in verbose mode')

@cli.command()
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