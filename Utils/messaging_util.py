from pyfiglet import Figlet
import click, time

def get_card_details(card):
    return card.get_face_value() + " of " + card.get_suit()

def build_post_mortem_message(players, dealer):

        allparticipants = [*players,dealer]
        msg = ""
        for player in allparticipants:
            score = player.get_score()
            msg += build_post_mortem_player_title(player)
            msg += "\nFinal Score: " + str(score)

            if player.get_blackjack() or player.get_bust():
                msg += "\nStatus: "
                if(player.get_bust()):
                    msg += "Bust"
                else:
                    msg += "Blackjack"

            msg += "\nWager/Winnings: " + str(player.get_hand().get_bet())
            msg += "\nFinal Cards:"

            for card in player.get_hand().get_cards():
                msg += "\n" + card.get_face_value() + " of " + card.get_suit()

            msg += "\n\n"

        
        return msg

def build_post_mortem_player_title(player):
    if(player.get_seat() != -1):
        return "Player " + str(player.get_seat()) + " results:"
    else:
        return "Dealer results:"

def build_win_lose_blackjack_messages(player_seat,player_bj, dealer_bj):

    msg = "'Player " + str(player_seat) + "'" 
    
    if dealer_bj and not player_bj:
        msg += " cannot beat the dealer's blackjack. You lose everything."
    elif player_bj and not dealer_bj:
        msg += " has blackjack and the dealer does not. You win."
    else:
        msg += " and the dealer both have blackjack. You keep your bet."
    return msg

def build_dealer_bust_players_win_message(seat):
    msg = "'Player " + str(seat) + "', the dealer went bust so you win your bet!"
    return msg

def build_player_bust_lost_message(seat):
    msg = "'Player " + str(seat) + "' went bust."
    return msg

def build_player_dealer_points_message(player_seat, player_pt, dealer_pt):
    msg = "'Player " + str(player_seat) + "'"

    if( player_pt > dealer_pt):
        msg += " has " + str(player_pt) + " and dealer only has " + str(dealer_pt) + ". Player wins!"
    elif(player_pt == dealer_pt):
        msg += " has " + str(player_pt) + " and dealer also has " + str(dealer_pt) + ". Push"
    else:
        msg += " has " + str(player_pt) + " but dealer has " + str(dealer_pt) + ". You lose."
    
    return msg

def build_not_a_valid_arument_message(c):
    msg = "'" + c + "' is not a valid argument. Please try again."
    return msg

def build_player_title(seat):
    playername = "Player " + str(seat)

    length = len(playername) + 6;

    msg = ""

    count = 0
    frame = ""
    while count < length:
        frame += "="
        count += 1
    msg += frame
    msg += "\n|| " + playername + " ||\n"
    msg += frame
    return msg

def pause(t=0.5):
    time.sleep(t)

def pause_loading(t=1, sequence=[1,2]):
    with click.progressbar(sequence) as bar:
        for x in bar:
            time.sleep(t)

def print_title(game_title):
    click.clear()
    title = Figlet(font='slant')
        
    print(title.renderText(game_title))


def print_player_dealt_card(seat,card):
    face = card.get_face_value()
    suit = card.get_suit()

    msg = ""
    if seat > -1:
        msg = f"Player {seat} was dealt a {face} of {suit}"
    else:
        msg = "Dealer drew "
        if card.get_orientation() == True:
            msg += f"a {face} of {suit}"
        else:
            msg += "a facedown card"
    click.echo(msg)
    pause()

def print_placing_bets_title():
    border = "================"
    tagline = "|| Place Bets ||"

    title = border + '\n' + tagline + '\n' + border

    click.echo(title)
    pause()

def print_dealing_cards_title(players):
    border = "================"
    tagline = "|| Deal Cards ||"

    title = border + '\n' + tagline + '\n' + border

    click.echo(title)
    pause()
    click.echo()
    click.echo("Player order starting at dealer's left and going clockwise is:")

    for player in players:
        click.echo(f"Player {player.get_seat()}")

    click.pause()

def print_winnings_title():
    click.clear()
    border = "========================"
    tagline = "|| Calculate Winnings ||"

    title = border + '\n' + tagline + '\n' + border

    click.echo(title)
    pause_loading(2)

def print_resolve_player_actions_title():
    click.clear()
    border = "===================================="
    tagline = "|| Time to Resolve Player Actions ||"

    title = border + '\n' + tagline + '\n' + border

    click.echo(title)
    pause_loading(1)   

def print_resolving_dealer_blackjack():
    click.clear()
    border = "================================="
    tagline = "||     Dealer has BlackJack    ||"
    tagline += "\n|| Auto-resolving and skipping ||"

    title = border + '\n' + tagline + '\n' + border

    click.echo(title)
    pause_loading(1)  
