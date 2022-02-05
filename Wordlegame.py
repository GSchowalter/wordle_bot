import Tile
import wordlist

class Wordlegame:

    def __init__(self):
        self.tiles = [Tile(), Tile(), Tile(), Tile(), Tile()]
        self.wordlist = wordlist.VALIDGUESSES
        
    def guess(self):
        return ""
         
    def update_wordlist(self):
        for tile in self.tiels:
            tile.