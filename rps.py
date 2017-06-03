# How it works:
# 	1. Player moves
# 	2. Computer moves
# 	3. Compare moves
# 		 - is it a tie?
# 		 - is it a win?
# 		 - is it a lose?



import random

moves = ['r', 'p', 's']
player_wins = ['pr', 'sp', 'rs']

player1_move = raw_input("Hey, play now: ")
player2_move = random.choice(moves)

print "You: ", player1_move
print "Me: ", player2_move

if player1_move == player2_move:
	print "Sorry, seems like a tie!"
elif player1_move + player2_move in player_wins:
	print "So, seems you win!...yaaaaaaaaiy!"
else:
	print "Better Luck next time chap!"