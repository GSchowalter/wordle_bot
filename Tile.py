class Tile:
    
    def __init__(self) -> None:
        self.candidate_letters = "abcdefghijklmnopqrstuvwxyz"
        
    def remove_letter(self, letter):
        if(letter in  self.candidate_letters):
            self.candidate_letters.replace(letter, "")