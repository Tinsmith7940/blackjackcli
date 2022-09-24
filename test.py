from Assets.player import Player
from Assets.dealer import Dealer
import Data.test_data as tD, Utils.black_jack as rules

def test_player_blackjack():
    player = Player(0)
    player.create_init_hand(5)
    player.get_hand().add_cards(tD.BLACKJACK_HAND)

    result = rules.evaluate_score_with_aces(player)

    assert result == 0, f"did not get a result of '0' as expected. Returned value: {result}"
    assert player.get_blackjack() == True

def test_player_bust():
    player = Player(0)
    player.create_init_hand(5)
    player.get_hand().add_cards(tD.BUST_HAND)

    result = rules.evaluate_score_with_aces(player)

    assert result == -1, f"did not get a result of '-1' as expected. Returned value: {result}"
    assert player.get_bust() == True

def test_player_scoring():

    # Non-Blackjack 21 score
    player = Player(0)
    player.create_init_hand(5)
    player.get_hand().add_cards(tD.TWENTYONE_NO_BLACKJACK_HAND)

    result = rules.evaluate_score_with_aces(player)

    assert result == 21, f"got score different than 21: {result}"
    assert player.get_blackjack() == False

    # score 18
    player = Player(0)
    player.create_init_hand(5)
    player.get_hand().add_cards(tD.EIGHTEEN_HAND)

    result = rules.evaluate_score_with_aces(player)

    assert result == 18, f"got score different than 18: {result}"

def test_continue_dealer_turn_on_blackjack():
    dealer = Dealer()
    dealer.get_hand().add_cards(tD.BLACKJACK_HAND)

    result = rules.continue_dealer_turn(dealer)

    score = dealer.get_score()
    assert result == False, f"did not get a result of 'False' for continuing the dealer's turn after blackjack. Result: {result}"
    assert score == 21, f"Blackjack dealer score was not 21 as expected: {score}"
    assert dealer.get_blackjack() == True
 
def test_continue_dealer_turn_on_sixteen():
    dealer = Dealer()
    dealer.get_hand().add_cards(tD.SIXTEEN_HAND)

    result = rules.continue_dealer_turn(dealer)
    score = dealer.get_score()
    assert result == True, f"did not get a result of 'True' for continuing the dealer's turn after 16 hand. Result: {result}"
    assert score == 16, f"Blackjack dealer score was not 16 as expected: {score}"

def test_continue_dealer_turn_on_seventeen():
    dealer = Dealer()
    dealer.get_hand().add_cards(tD.SEVENTEEN_HAND)

    result = rules.continue_dealer_turn(dealer)
    score = dealer.get_score()
    assert result == False, f"did not get a result of 'False' for continuing the dealer's turn after 16 hand. Result: {result}"
    assert score == 17, f"Blackjack dealer score was not 17 as expected: {score}"

def test_continue_dealer_turn_on_eighteen_with_ace():
    dealer = Dealer()
    dealer.get_hand().add_cards(tD.DEALER_EIGHTEEN_HAND)

    result = rules.continue_dealer_turn(dealer)
    score = dealer.get_score()
    assert result == False, f"did not get a result of 'False' for continuing the dealer's turn after 16 hand. Result: {result}"
    assert score == 18, f"Blackjack dealer score was not 18 with ACE as expected: {score}"

def test_dealer_turn_on_bust():
    dealer = Dealer()
    dealer.get_hand().add_cards(tD.BUST_HAND)

    result = rules.continue_dealer_turn(dealer)
    score = dealer.get_score()
    assert result == False, f"did not get a result of 'False' for continuing the dealer's turn after bust. Result: {result}"
    assert score > 21, f"Blackjack dealer score was > 21 as expected: {score}"
    assert dealer.get_bust() == True

def test_playerblackjack_dealerblackjack_tie():
    player = Player(0)
    dealer = Dealer()

    player.create_init_hand(50)
    player.set_blackjack()

    dealer.set_blackjack()

    rules.get_winnings(player,dealer)

    # Since both player and dealer have blackjack, we have a 'Push' and player keeps money
    winnings = player.get_hand().get_bet()
    assert winnings == 50, f"player did not have a remaining winnings of 50 as expected: {winnings}"

def test_playerblackjack_dealer():
    player = Player(0)
    dealer = Dealer()

    player.create_init_hand(50)
    player.set_blackjack()

    rules.get_winnings(player,dealer)

    # Since player blackjack, we have a 'Blackjack' and player gest 1.5x winnings
    winnings = player.get_hand().get_bet()
    assert winnings == 125, f"player did not have a remaining winnings of 125 as expected: {winnings}"

def test_player_dealerblackjack():
    player = Player(0)
    dealer = Dealer()

    player.create_init_hand(50)
    
    dealer.set_blackjack()

    rules.get_winnings(player,dealer)

    # Since dealer has blackjack, player loses bet
    winnings = player.get_hand().get_bet()
    assert winnings == 0, f"player did not have a remaining winnings of 0 as expected: {winnings}"

def test_player_dealer_twentyone_tie():
    player = Player(0)
    dealer = Dealer()

    player.create_init_hand(50)
    player.set_score(21)

    dealer.set_score(21)
    rules.get_winnings(player,dealer)

    winnings = player.get_hand().get_bet()
    assert winnings == 50, f"player did not have a remaining winnings of 50 as expected: {winnings}"

def test_player_beats_dealer():
    player = Player(0)
    dealer = Dealer()

    player.create_init_hand(50)
    player.set_score(20)

    dealer.set_score(19)
    rules.get_winnings(player,dealer)

    winnings = player.get_hand().get_bet()
    assert winnings == 100, f"player did not have a remaining winnings of 100 as expected: {winnings}"

def test_dealer_beats_player():
    player = Player(0)
    dealer = Dealer()

    player.create_init_hand(50)
    player.set_score(18)

    dealer.set_score(19)
    rules.get_winnings(player,dealer)

    winnings = player.get_hand().get_bet()
    assert winnings == 0, f"player did not have a remaining winnings of 0 as expected: {winnings}"


########################################
# Validate player/dealer blackjack logic
########################################

test_player_blackjack()

test_player_bust()

test_player_scoring()

# To verify dealer has blackjack=True and STOPS drawing cards
test_continue_dealer_turn_on_blackjack()

# To verify dealer scored correctly and KEEPS drawing cards
test_continue_dealer_turn_on_sixteen()

# To verify dealer scored correctly and STOPS drawing cards
test_continue_dealer_turn_on_seventeen()

# To make sure dealer auto-scores ACE appropriately and STOPS drawing cards
test_continue_dealer_turn_on_eighteen_with_ace()

# To test dealer goes bust and STOPS drawing cards
test_dealer_turn_on_bust()

# Blackjack tie should result in a 'Push'
test_playerblackjack_dealerblackjack_tie()

# Player blackjack should result in 1.5 winnings
test_playerblackjack_dealer()

# Dealer blackjack should result in losing winnings
test_player_dealerblackjack()

# No blackjack, but 21 tie should result in a 'Push' with keeping bet
test_player_dealer_twentyone_tie()

# No blackjack, player beats dealer in points. Winnings are 1x
test_player_beats_dealer()

# No blackjack, player loses to dealer in points. Winnings are 0
test_dealer_beats_player()