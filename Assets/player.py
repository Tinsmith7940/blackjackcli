from Assets.hand import Hand
class Player:
    def __init__(self,seat):
        self.seat = seat
        self.hands = []
        self.score = 0
        self.blackjack = False
        self.bust = False
    
    def create_init_hand(self, bet):
        self.hands.append(Hand(bet))

    def get_hand(self, index=0):
        return self.hands[index]

    def print_player_cards(self):
        for hand in self.hands:
            hand.print_cards()

    def set_score(self, score):
        self.score = score
    
    def get_score(self):
        return self.score

    def get_seat(self):
        return self.seat

    def set_blackjack(self,status=True):
        self.blackjack = status

    def get_blackjack(self):
        return self.blackjack
    
    def set_bust(self, status=True):
        self.bust = status

    def get_bust(self):
        return self.bust

    def get_seat(self):
        return self.seat

    def reset(self):
        self.hands = []
        self.score = 0
        self.blackjack = False
        self.bust = False
