from random import randint

plays = ["Rock", "Paper", "Scissors"]

computer = plays[randint(0,2)]
score = [0,0]
evil_computer = randint(1,10)

while True:

    player = input("Rock, Paper, Scissors?")
    player = player.capitalize()

    for play in plays:
        if player == play:
            player_int = plays.index(play)
        if computer == play:
            computer_int = plays.index(play)

    if evil_computer == 1:
        computer_int = (player_int+1)%3
        computer = plays[computer_int]

    print("You played", player, "and the computer played", computer)

    for play in plays:
        if player == play:
            player_int = plays.index(play)
        if computer == play:
            computer_int = plays.index(play)

    if player_int == computer_int:
        print('Draw!')
    elif player_int == (computer_int+1)%3:
        print('Player wins!')
        score[0] += 1
    else:
        print('Computer wins!')
        score[1] += 1

    print('Score: \n''Player:',score[0],'Computer:',score[1])
    
    if score[0] == 3:
        print('Player is the winner')
        break
    elif score[1] == 3:
        print('Computer is the winner')
        break

    computer = plays[randint(0,2)]
    evil_computer = randint(1,10)