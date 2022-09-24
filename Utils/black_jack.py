from Assets.player import Player
from Assets.hand import Hand
from Assets.card import Card
import Utils.input_util as iU, click, Utils.messaging_util as mU

def continue_player_turn(player: Player):
    playerturn = evaluate_hand_condition(player)
    
    return playerturn

def evaluate_hand_condition(player: Player):
    handeval = evaluate_score_with_aces(player)

    if handeval == -1:
        click.echo("You went bust!")
        click.pause()
        return False
    elif handeval == 0:
        click.echo("You have BlackJack!")
        click.pause()
        return False
    else:
        click.echo("Your current card score is: " + str(handeval))
        return True

def auto_resolve_all_turns_blackjack(players, dealer):
    dbj = does_player_have_blackjack(dealer.get_hand().get_cards())

def evaluate_score_with_aces(player: Player):
    hand = player.get_hand()
    cards = hand.get_cards()

    bJ = does_player_have_blackjack(cards)
    if bJ == True:
        player.set_blackjack()
        player.set_score(21)
        return 0
    
    playerscore = get_score_of_non_ace_cards(cards)
    acescore = get_score_of_ace_cards(cards, playerscore)

    total_playerscore = acescore + playerscore
    player.set_score(total_playerscore)

    if total_playerscore > 21:
        score = -1 # Bust
        player.set_bust()
        return score
    else:
        return total_playerscore
            
            
def get_score_of_non_ace_cards(cards):
    playerscore = 0
    for card in cards:
        playerscore += get_card_value(card)

    return playerscore

def get_score_of_ace_cards(cards, score):
    acescore = 0
        
    aces = []
    for card in cards:
        if is_ace(card):
            aces.append(card)
        
    if len(aces) == 0:
        return acescore
    else:
        click.echo("You have " + str(len(aces)) + " ACES in your hand with a score of " + str(score) + " with non-ace cards")
        for ace in aces:
            acescore += get_ace_value_from_player()

        return acescore


# evaluate whether player has blackjack or not
# Blackjack is an initial hand of one ACE and one 10 card (face or pip)
def does_player_have_blackjack(cards):
    if len(cards) > 2:
        return False
    elif num_of_aces_in_hand(cards) == 1:
        nonacescore = get_score_of_non_ace_cards(cards)
        if nonacescore == 10:
            return True
        else:
            return False
    else:
        return False

def update_players_have_blackjack(players):
    result = False
    for player in players:
        cards = player.get_hand().get_cards()
        if does_player_have_blackjack(cards) == True:
            player.set_blackjack(True)
            player.set_score(21)
            result = True

    return result
    
# return blackjack specific card point values
def get_card_value(card: Card):
    cardrank = card.get_face_value()

    try: 
        return int(cardrank) # If face value is pip, then return pip as int
    except:
        if cardrank != "ACE":
            return 10 # For face cards, score is 10
        else:
            return 0 # Need player to determine whether to score ACE as 1 or 11

def get_ace_value_from_player():
    return iU.get_specific_integer_inputs("Please set a value for your ACE card [1/11]")

def continue_dealer_turn(dealer):
        hand = dealer.get_hand()
        cards = hand.get_cards()
        dealerscore = get_score_of_non_ace_cards(cards)
        acescore = get_score_of_dealer_ace_cards(cards, dealerscore)

        totalscore = dealerscore + acescore
        dealer.set_score(totalscore)
        if totalscore > 21:
            dealer.set_bust()

        if totalscore >= 17:
            if totalscore == 21 and len(cards) == 2:
                dealer.set_blackjack()
            return False
        else:
            return True

def get_score_of_dealer_ace_cards(cards, dealerscore):
    acescore = 0
    score = dealerscore
    num_aces = num_of_aces_in_hand(cards)

    if num_aces >= 1:
        total_with_eleven = score + 11 + (num_aces-1)
        if total_with_eleven <= 21 and total_with_eleven >= 17:
            acescore = 11 + (num_aces-1)
        else:
            acescore = num_aces

    return acescore


def is_ace(card):
    if card.get_face_value() == "ACE":
        return True
    else:
        return False

def num_of_aces_in_hand(cards):
    count = 0
    for card in cards:
        if is_ace(card):
            count += 1
    return count


def get_winnings(player, dealer):
    dealer_bj = dealer.get_blackjack()
    player_bj = player.get_blackjack()
    dealerbust = dealer.get_bust()
    playerbust = player.get_bust()
    seat = player.get_seat()
    msg = ""
    if(dealer_bj or player_bj):
        msg = mU.build_win_lose_blackjack_messages(seat,player_bj,dealer_bj)
        if player_bj and not dealer_bj:
            win_bet(player,1.5)
        elif dealer_bj and not player_bj:
            lose_bet(player)

        # Push player bet - player keeps money if above don't match
    elif dealerbust == True and playerbust == False:
        msg = mU.build_dealer_bust_players_win_message(seat)
        win_bet(player,1);
    elif playerbust == True:
        msg = mU.build_player_bust_lost_message(seat)
        lose_bet(player)
    else:
        pscore = player.get_score()
        dscore = dealer.get_score()
        msg = mU.build_player_dealer_points_message(seat,pscore,dscore)
        if pscore > dscore:
            win_bet(player,1)
        elif pscore < dscore:
            lose_bet(player)
        
        # Push player bet - player keeps money if above don't match
    click.echo(msg)
    click.pause()



def win_bet(player, multiplier):
    orig_bet = player.get_hand().get_bet()
    winnings = orig_bet * multiplier
    player.get_hand().add_winnings(winnings)

def lose_bet(player):
    player.get_hand().lose_bet()
