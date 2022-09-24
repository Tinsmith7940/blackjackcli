from pyfiglet import Figlet
import click

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

def print_title(game_title):
    click.clear()
    title = Figlet(font='slant')
        
    print(title.renderText(game_title))

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