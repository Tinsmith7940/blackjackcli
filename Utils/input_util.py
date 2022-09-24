import click
def get_integer_input_within_range(msg, lower=0, upper=500, default=1):
        while(True):
            c = click.prompt(msg,default,False, type=int)

            if c > lower and c < upper:
                return c
            else:
                click.echo('\nPlease enter a value greater than ' + str(lower) + ' and less than ' + str(upper))

def get_specific_integer_inputs(msg, integers=[1,11]):
    while(True):
        c = click.prompt(msg,1,confirmation_prompt=True,type=int)

        if(integers.count(c) > 0):
            return c
        else:
            click.echo("\n Please enter a valid integer value " + str(integers) + "...")
