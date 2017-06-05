# How it works:
# 	1. Player moves
# 	2. Computer moves
# 	3. Compare moves
# 		 - is it a tie?
# 		 - is it a win?
# 		 - is it a lose?


import random
import sys
import unittest

moves = ['r', 'p', 's']
player_wins = ['pr', 'sp', 'rs']


player1_move = sys.argv[1]
player2_move = random.choice(moves)
# # if player1_move == "q":
# # 	break
# print "You: ", player1_move
# print "Me: ", player2_move

# if player1_move == player2_move:
# 	print "Sorry, seems like a tie!"
# elif player1_move + player2_move in player_wins:
# 	print "So, seems you win!...yaaaaaaaaiy!"
# else:
# 	print "Better Luck next time chap!"


def player1_choice_rock():
    if player1_move == 'r':
        return "You tie Bitch"
    elif player2_move == 'p':
        return "You win Sensei"
    else:
        return "Go home!"


def player1_choice_paper():
    if player1_move == 'r':
        return "Go home!"
    elif player2_move == 'p':
        return "You tie Bitch"
    else:
        return "You win Sensei"


def player1_choice_scissors():
    if player1_move == 'r':
        return "You win Sensei"
    elif player2_move == 'p':
        return "Go home!"
    else:
        return "You tie Bitch"


if player2_move == 'r':
    print player1_choice_rock()
elif player2_move == 'p':
    print player1_choice_paper()
else:
    print player1_choice_scissors()



# class RPSTestCase
#   def test_simple_win_lose
#     # :rock loses :paper
#     turn_person = rps_game([[:rock], [:paper]])
#     assert_equal(turn_person, [0, 1])
    
#     # :rock wins :scissors
#     turn_person = rps_game([[:rock], [:scissors]])
#     assert_equal(turn_person, [0, 0])
    
#     # :sissors wins :paper
#     turn_person = rps_game([[:paper], [:scissors]])
#     assert_equal(turn_person, [0, 1])
# end