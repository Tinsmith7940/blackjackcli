import json, click
import Utils.data_util as dUtil, Utils.messaging_util as mU
from Data.data_files import DataFiles as dF

class Application():

    def __init__(self):
        self.game_data = json.loads(dUtil.get_file_data(dF.GAMEDATA))

    def close_game(self):
        click.clear()
        mU.print_title("Thanks for playing!!")
        exit()
        


