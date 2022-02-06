import re

class Wordlist:

    def __init__(self, list):
        self.list = list

    def remove_matching_words(self, pattern):
        new_list = self.list
        for word in self.list:
            if re.search(pattern, word) == None:
                print(word)
                new_list.remove(word)

        self.list = new_list

    def get_list(self):
        return self.list