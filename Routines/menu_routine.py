from Assets.application import Application
import click
import Utils.input_util as iU, Utils.messaging_util as mU


def menu_routine(routine: Application):
        click.clear()
        menu_options = "Quick Game: Play solo against the dealer [q]\n"
        menu_options += "Custom Game: Multiple players and decks [c]\n"
        menu_options += "Exit game [e]"

        click.echo(menu_options)

        while (True):
            uinput = click.getchar()
            click.echo()
            c = iU.sanitize_input_case_sensitivity(uinput)
            if c == 'q' or c == 'c':
                # initiate quick game
                return menu_sub_routine(c)
            elif c == 'e':
                routine.close_game()
            else:
                click.echo(mU.build_not_a_valid_arument_message(c))


def menu_sub_routine(selected_option):
    if selected_option == 'q':
        return (1,1)
    else:
        return get_custom_game_params()

def get_custom_game_params():
    players = get_number_of_players()
    decks = get_number_of_decks()
    return (players,decks)

    
def get_number_of_players():
    return iU.get_integer_input_within_range("Number of players:",0,16)

def get_number_of_decks():
    return iU.get_integer_input_within_range("Number of decks of cards:",0,11)