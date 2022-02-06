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
assert len(test_game.get_wordlist()) == 5
assert len(game.get_wordlist()) == 10657

# Test remove letters
test_game.remove_letters("x")
test_game.update_wordlist()
print(len(test_game.get_wordlist()))
assert len(test_game.get_wordlist()) == 4

# Teset reset
test_game.reset(wordlist_constants.TESTWORDS)
assert 5 == len(test_game.get_wordlist())

# Test place letter
test_game.reset(wordlist_constants.TESTWORDS)
test_game.place_letter("t", 0)
test_game.update_wordlist()
print(test_game.wordlist.get_list())
assert len(test_game.wordlist.get_list()) == 2

test_game.reset(wordlist_constants.TESTWORDS)

test_game.update_wordlist()
print(test_game.wordlist.get_list())
assert len(test_game.wordlist.get_list()) == 5

# test letters removed from tile found
test_game.reset(wordlist_constants.TESTWORDS)
test_game.letter_found('z', 1)
assert len(test_game.tiles[1].candidate_letters) == 25
assert len(test_game.tiles[0].candidate_letters) == 26

# test that update wordlist removes words without the known letters
test_game.update_wordlist()
print(test_game.get_wordlist())
assert len(test_game.get_wordlist()) == 1