from operator import truediv
from Assets.player import Player
import Routines.Scoring.black_jack as scoring

class Dealer(Player):
    def __init__(self):
        Player.__init__(self,-1)
        self.create_init_hand(0)


