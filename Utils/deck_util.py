# Build a deck of cards
import Assets.card, random, json, Utils.data_util as dUtil
from Data.data_files import DataFiles
from Data.deck_type import DeckType

def build_standard_card_deck():
    data = dUtil.get_file_data(DataFiles.DECK)

    json_obj = json.loads(data)

    suits = json_obj[DeckType.STANDARD]['suits']
    ranks = json_obj[DeckType.STANDARD]['ranks']

    deck = []
    for suit in suits:
        for rank in ranks:
            card = Assets.card.Card(suit,rank)
            deck.append(card)
    
    return deck


def build_multiple_standard_card_decks(number):
    count = 0
    combined = []
    while(count < number):
        combined += build_standard_card_deck()
        count += 1
    
    return combined

def shuffle(deck):
    random.shuffle(deck)
    return deck