import Tile
import wordlist

class Wordlegame:

    def __init__(self, list):
        self.tiles = [Tile.Tile(), Tile.Tile(), Tile.Tile(), Tile.Tile(), Tile.Tile(),]
        self.wordlist = wordlist.Wordlist(list)
        self.known_letters_unplaced = ""
        
    def guess(self):
        # Build regex to eliminate words from wordlist
        # [abcdefghi][xyas][fds][asdf][o]
        # Remove words from wordlist that don't match regex
        self.update_wordlist()
        
        # Remove words that don't contain all of the the uplaced letters

        # Generate a word
            # Select words with no repettions if possible
            # Select words with most commonly used letters
        return ""
         
    def update_wordlist(self):
        pattern = str.format("[{}][{}][{}][{}][{}]", self.tiles[0].get_candidates(), self.tiles[1].get_candidates(), self.tiles[2].get_candidates(), self.tiles[3].get_candidates(), self.tiles[4].get_candidates())
        self.wordlist.remove_matching_words(pattern)

    def remove_letters(self, letters):
        for tile in self.tiles:
            tile.remove_letters(letters)
            
    def get_wordlist(self):
        return self.wordlist
