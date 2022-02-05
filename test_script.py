import  Wordlegame
import Wordlist
import wordlist_constants

# list = Wordlist.Wordlist(wordlist_constants.VALIDGUESSES)
# print(len(list.get_list()))
# list.remove_matching_words("[abcdefghijklmnopqrstuvwxyz][abcdefghijklmnopqrstuvwxyz][mg][io][cn]")
# length = len(list.get_list())
# print(length)
# print(list.get_list()[length-1])

game = Wordlegame.Wordlegame()
game.remove_letters("qx")
print(game.guess())
