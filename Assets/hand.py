class Hand:
    def __init__(self,wager=0,order=0):
        self.wager = wager
        self.cards = []
        self.order = order

    def add_card(self, card):
        self.cards.append(card)

    def place_bet(self, bet):
        self.wager = bet

    def get_bet(self):
        return self.wager

    def add_winnings(self, winnings):
        self.wager += winnings

    def lose_bet(self):
        self.wager = 0
    
    def print_cards(self):
        for card in self.cards:
            if card.get_orientation() == True:
                print(card.get_face_value() + " of " + card.get_suit())
            else:
                print("Facedown")

    def get_cards(self):
        return self.cards