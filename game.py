import random


def game():
    print("You are playing Rock Paper Scisscors. Let the")

    # creating  list of possible play options
    comp_possible = 1, 2, 3

    # holds the score of played games
    score = [0, 0]
    flag = 0
    while True:
        print("Enter your choice:")
        while True:
            choice = raw_input('->')
            if choice == 'r' or choice == 'R' or choice == 'Rock' or choice == 'rock' or choice == '1':
                choice_identifier = 1
                break
            elif choice == 'S' or choice == 's' or choice == 'Scissors' or choice == 'sciccors' or choice == '2':
                choice_identifier = 2
                break
            elif choice == 'P' or choice == 'p' or choice == 'Paper' or choice == 'paper' or choice == '3':
                choice_identifier = 3
                break
            else:
                print('That\'s not an option in this game :)')
                print('Try again:')
                continue

        comp_choice = random.choice(comp_possible)
        if choice_identifier == comp_choice:
            print('It\'s a draw!')
            score[0] = score[0] + 1
            score[1] = score[1] + 1
        elif (choice_identifier == 1 and comp_choice == 2) or (choice_identifier == 2 and comp_choice == 3) or (choice_identifier == 3 and comp_choice == 1):
            print('You win!')
            score[0] = score[0] + 1
        else:
            print('You lose...')
            score[1] = score[1] + 1

        while True:
            answer = raw_input('Play another round?')
            if answer == 'y' or answer == 'Y' or answer == 'yes' or answer == 'Yes' or answer == 'ye' or answer == 'Ye' or answer == 'sure' or answer == 'Sure':
                print(' Current score: You - ',
                      score[0], ' Computer - ', score[1])
                flag = 0
                break
            elif answer == 'n' or answer == 'N' or answer == 'no' or answer == 'No' or answer == 'nah' or answer == 'Nah':
                print('Thanks for playing! Final score: You - ',
                      score[0], ' Computer - ', score[1])
                flag = 1
                break
            else:
                print('Yay or nay...')
                continue
        if flag == 0:
            continue
        else:
            break

game()


# assign a random play to the computer
computer = t[randint(0, 2)]

# set player to False
player = False

while player == False:
    # set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")
    # player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0, 2)]


def ball_collide(ball_1, ball_2):
    x1, y1, r1 = ball_1
    x2, y2, r2 = ball_2
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    radiisum = r1 + r2
    if (distance <= radiisum):
        print "True"
    else:
        print "False"


ball_collide((0, 0, 1), (3, 3, 1))




