from Assets.game import Game
import Routines.intro_routine as iR, Routines.menu_routine as mR
from Routines.game_routine import GameRoutines

routine = GameRoutines()

# Intro messaging
iR.intro_routine(routine)

while True:
    # Setup the game!
    black_jack = Game(*mR.menu_routine(routine))

    keepplaying = True
    count = 0
    # Overall Game Cycle routine
    while keepplaying:

        if count > 0:
            black_jack.clean()

        # Betting routine
        black_jack.place_bets()

        # Dealing routine
        black_jack.deal_cards()

        # Resolve each player turn routine
        black_jack.execute_player_turns()
        black_jack.execute_dealer_turn()

        # Resolve Scoring routine
        black_jack.execute_winnings_routine()

        # Final Screen
        keepplaying = black_jack.post_mortem()
        count += 1