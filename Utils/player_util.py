from Assets.player import Player

def create_players(number_of_players=1):
    players = []
    count = 0

    while(count < number_of_players):
        players.append(Player(count))
        count += 1

    return players
