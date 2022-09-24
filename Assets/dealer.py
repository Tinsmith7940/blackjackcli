from Assets.player import Player

class Dealer(Player):
    def __init__(self):
        Player.__init__(self,-1)
        self.create_init_hand(0)


