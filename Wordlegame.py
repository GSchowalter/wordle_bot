import Tile
import wordlist

class Wordlegame:

    def __init__(self, list):
        self.tiles = [Tile.Tile(), Tile.Tile(), Tile.Tile(), Tile.Tile(), Tile.Tile(),]
        self.wordlist = wordlist.Wordlist(list)
        self.known_letters_unplaced = ""
        
    def guess(self):
        self.update_wordlist()
    
        # Generate a word
        return self.wordlist.get_list()[0]
         
    def update_wordlist(self):
        pattern = str.format("[{}][{}][{}][{}][{}]", self.tiles[0].get_candidates(), self.tiles[1].get_candidates(), self.tiles[2].get_candidates(), self.tiles[3].get_candidates(), self.tiles[4].get_candidates())
        self.wordlist.remove_matching_words(pattern)
        # Remove words that don't contain all of the the uplaced letters
        self.wordlist.remove_words_without_letters(self.known_letters_unplaced)


    def remove_letters(self, letters):
        for tile in self.tiles:
            tile.remove_letters(letters)
            
    # input a letter with known position
    def place_letter(self, letter, tile):
        # Retieve correct tile
        t = self.tiles[tile]
        # Remove all letters but the chosen one
        t.place_letter(letter)

    # inform of a known letter with the place found 
    def letter_found(self, letter, tile):
        # Add to known letters
        self.known_letters_unplaced = self.known_letters_unplaced + letter
        # Remove letter from candidates in tile
        self.remove_letter(letter, tile)
        
    def remove_letter(self, letter, tile):
        self.tiles[tile].remove_letter(letter)
        
    def get_wordlist(self):
        return self.wordlist.get_list()

    def reset(self, new_wordlist):
        self.wordlist = wordlist.Wordlist(new_wordlist)
        self.tiles = [Tile.Tile(), Tile.Tile(), Tile.Tile(), Tile.Tile(), Tile.Tile(),]
