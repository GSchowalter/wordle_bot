import  Wordlegame
import wordlist
import wordlist_constants

# list = Wordlist.Wordlist(wordlist_constants.VALIDGUESSES)
# print(len(list.get_list()))
# list.remove_matching_words("[abcdefghijklmnopqrstuvwxyz][abcdefghijklmnopqrstuvwxyz][mg][io][cn]")
# length = len(list.get_list())
# print(length)
# print(list.get_list()[length-1])

test_game = Wordlegame.Wordlegame(wordlist_constants.TESTWORDS)
game = Wordlegame.Wordlegame(wordlist_constants.VALIDGUESSES)

# Test constructor
assert len(test_game.get_wordlist().get_list()) == 5
assert len(game.wordlist.get_list()) == 10657

# Test remove letters
test_game.remove_letters("x")
test_game.update_wordlist()
print(len(test_game.get_wordlist().get_list()))
assert len(test_game.get_wordlist().get_list()) == 4


