class Tile:
    
    def __init__(self):
        self.candidate_letters = "abcdefghijklmnopqrstuvwxyz"
        
    def remove_letter(self, letter):
        if(letter in  self.candidate_letters):
            self.candidate_letters = self.candidate_letters.replace(letter, "")
            
    def remove_letters(self, letters):
        for letter in letters:
            self.remove_letter(letter)

    def place_letter(self, letter):
        new_list = ''.join(filter(lambda x: x==letter, self.candidate_letters))
        self.candidate_letters = new_list

    def get_candidates(self):
        return self.candidate_letters