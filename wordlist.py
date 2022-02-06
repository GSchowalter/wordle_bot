import re

class Wordlist:

    def __init__(self, list):
        self.list = list

    def remove_matching_words(self, pattern):
        new_list = self.list.copy()
        for word in self.list:
            if re.search(pattern, word) == None:
                print(word)
                new_list.remove(word)

        self.list = new_list

    def remove_words_without_letters(self, letters):
        new_list = self.list.copy()
        for letter in letters:
            for word in self.list:
                if letter not in word:
                    new_list.remove(word)
        self.list = new_list

    def get_list(self):
        return self.list.copy()