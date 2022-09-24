import Utils.deck_util as deckbuilder,click, Utils.input_util as iUtil
import Utils.player_util as playerUtil, Routines.Scoring.black_jack as scoring, Utils.messaging_util as mU
from Data.deck_type import DeckType
from Assets.dealer import Dealer

class Game:
    # Define the number of players and their seat order
    # Define the type and number of decks in play
    # Always shuffle the deck at the beginning of the game

    def __init__(self, player_number=1, deck_number=1, deck_type=DeckType.STANDARD):
        self.player_number = player_number
        self.deck_number = deck_number
        self.deck_type = deck_type

        self.dealer = Dealer()

        self.game_decks = deckbuilder.build_multiple_standard_card_decks(
            self.deck_number)
        self.game_decks = deckbuilder.shuffle(self.game_decks)

        self.players = playerUtil.create_players(self.player_number)


    def get_number_of_players(self):
        return len(self.players)

    def get_number_of_cards(self):
        return len(self.gameDecks)

    def get_players(self):
        return self.players

    def place_bets(self):
        for player in self.players:
            click.clear();
            seat_num = player.seat
            msg = "Player " + str(seat_num) + " please place your bet:"
            bet = iUtil.get_integer_input_within_range(msg,2,500,5)

            player.create_init_hand(bet)

    def deal_cards(self):
        self.issue_cards_to_players()
        self.issue_card_dealer_faceup()
        self.issue_cards_to_players()
        self.issue_card_dealer_facedown()



    ######################################
    # Issuing cards, getting cards, etc...
    ######################################
    def issue_cards_to_players(self):
        for player in self.players:
            self.give_player_card(player, 0)


    def give_player_card(self,player, messaging = False, hand_index=0, faceup=True):
        # Note: need to account for if we have run out of cards in the deck
        card = self.game_decks[0] # Got top card in the deck
        card.set_orientation(faceup)
        hand = player.get_hand(hand_index)
        hand.add_card(card)
        
        self.game_decks.pop(0) # remove the card from the deck

        if messaging:
            click.clear()
            click.echo("Dealer hands you a " + card.get_face_value() + " of " + card.get_suit())
            click.pause()

    def print_all_player_cards(self):
        for player in self.players:
            print("Player " + str(player.seat) + " has the following cards:")
            player.print_player_cards()

    def print_dealer_cards(self):
        print("The dealer has the following cards:")
        self.dealer.print_player_cards()

    def issue_card_dealer_faceup(self):
        self.give_player_card(self.dealer,0,0,True)
    
    def issue_card_dealer_facedown(self):
        self.give_player_card(self.dealer,0,0,False)      

    def expose_face_down_cards(self):
        for card in self.dealer.get_hand().get_cards():
            if card.get_orientation() == False:
                card.set_orientation(True)
                click.echo("Dealer reveals facedown card: " + mU.get_card_details(card))
                click.pause()

    ########################
    # Execute Players turn
    ########################
    def execute_player_turns(self):
        for player in self.players:
            self.execute_player_turn(player)

    def execute_player_turn(self, player):
        # Evaluate if player has a natural
        continue_turn = True

        msg = "Player " + str(player.seat) + ", what would you like to do?"
        msg += "\n<- Hit [h]"
        msg += "\n<- Stand [st]"
        msg += "\n<- Review cards on table [r]"
        msg += "\n\n Enter action"

        while(continue_turn):
            click.clear()
            title = mU.build_player_title(player.get_seat())
            click.echo(title)
            continue_turn = scoring.continue_player_turn(player)
            if continue_turn:
                player.print_player_cards()
                c = click.prompt(msg, type=str)

                if c == "h":
                    self.give_player_card(player,True)
                elif c == "r":
                    click.clear()
                    self.print_all_player_cards()
                    self.print_dealer_cards()
                    click.pause()
                elif c == "st":
                    return
                else:
                    click.clear()
                    click.echo(mU.build_not_a_valid_arument_message(c))
                    click.pause()
            else:
                return # Players turn cannot continue because they failed the continue_player_turn check


    #######################
    # Executing Dealer turn
    #######################
    def execute_dealer_turn(self):
        click.clear()
        click.echo("Beginning the dealers turn....\n")

        self.expose_face_down_cards()
        self.print_dealer_cards()
        click.pause()
        self.process_dealer_action()

    def process_dealer_action(self):
        continue_dealer_action = True
        
        while(continue_dealer_action):
            continue_dealer_action = scoring.continue_dealer_turn(self.dealer)
            if continue_dealer_action:
                self.issue_card_dealer_faceup()
                self.print_dealer_cards()
                click.pause()


    #####################
    # Round Winnings Calc
    #####################
    def execute_winnings_routine(self):
        
        for player in self.players:
            scoring.get_winnings(player,self.dealer)

    ########################
    # Round Results Printout
    ########################
    def post_mortem(self):
        click.clear()
        click.echo("[[ Final Game Results ]]\n\n\n")
        msg = mU.build_post_mortem_message(self.players,self.dealer)
        click.echo(msg)
        click.pause()

        keepgoing = self.should_game_continue()
        return keepgoing

    def should_game_continue(self):
        while True:
            c = click.prompt("Continue to another round? [y/n]", type=str)
            if c == "y":
                return True
            elif c == "n":
                return False
            else:
                click.echo(mU.build_not_a_valid_arument_message(c))        

    ###################################
    # Reset hands/wagers
    # Conditionally reshuffle all cards
    ###################################
    def clean(self):

        # If deck has been used, reshuffle all cards
        if(len(self.game_decks) != (52 * self.deck_number)):
            self.game_decks = deckbuilder.build_multiple_standard_card_decks(self.deck_number)
            self.game_decks = deckbuilder.shuffle(self.game_decks)

        # Reset player hands/wagers/scoring
        for player in self.players:
            player.reset()

        # Reset dealer scoring/hand/etc
        self.dealer = Dealer()
