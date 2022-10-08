import click

@click.command()
def hello():
    click.echo("Hellow World!")
#def hello():
#    print("Hello World!")

if __name__ == "__main__":
    hello()