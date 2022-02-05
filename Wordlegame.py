import Tile
import Wordlist
import wordlist_constants

class Wordlegame:

    def __init__(self):
        self.tiles = [Tile.Tile(), Tile.Tile(), Tile.Tile(), Tile.Tile(), Tile.Tile(),]
        self.wordlist = Wordlist.Wordlist(wordlist_constants.VALIDGUESSES)
        self.known_letters_unplaced = ""
        
    def guess(self):
        # Build regex to eliminate words from wordlist
        # [abcdefghi][xyas][fds][asdf][o]
        print(len(self.wordlist.get_list()))
        pattern = str.format("[{}][{}][{}][{}][{}]", self.tiles[0].get_candidates(), self.tiles[1].get_candidates(), self.tiles[2].get_candidates(), self.tiles[3].get_candidates(), self.tiles[4].get_candidates() )
        self.update_wordlist(pattern)
        print(len(self.wordlist.get_list()))


        # Remove words from wordlist that don't match regex

        # Remove words that don't contain all of the the letters unplaced

        # Generate a word
            # Select words with no repettions if possible
            # Select words with most commonly used letters
        return pattern
         
    def update_wordlist(self, pattern):
        self.wordlist.remove_matching_words(pattern)

    def remove_letters(self, letters):
        for tile in self.tiles:
            tile.remove_letters(letters)
