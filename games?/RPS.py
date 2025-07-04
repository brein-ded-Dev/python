from random import *
import sys
print("Let's play ROCK, PAPER, SCISSORS\n Controls for this game are:\n 'S' or 's' for SCISSORS\n 'R' or 'r' for ROCK\n 'P' or 'p' for PAPER\n 'Q' or 'q' for QUIT")

win=0
loss=0
tie=0
possible_moves = {'s','r','p','q'}
print("To play Endless rounds Please enter '-1'")
print("Enter the number of Rounds you would like to play")

rounds = input('>')
if not rounds.strip('-').isdigit():
    print("Please Enter a valid number next time.")
    sys.exit()

if int(rounds) == -1:
    while True:
        print("Rock, Paper, Scissors")
        move = input("Shoot >")
        move =move.strip().lower()
        if move in possible_moves:
            if  move == 's':
                print("Scissors vs. . . . . ",end='')
            elif  move == 'r':
                print("Rock vs. . . . . ",end='')
            elif  move == 'p':
                print("Paper vs. . . . . ",end='')
            elif  move == 'q':
                print("Leaving so soon?")
                break
                
            computer= randint(1,3)
            
            if computer == 1:
                computer = 's'
                print("Scissors")
            elif computer ==2:
                computer = 'r'
                print("Rock")
            elif computer == 3:
                computer = 'p'
                print("Paper")
                
            if move==computer:
                print("Tie")
                tie += 1
                
            if move =='r' and computer =='s':
                print("Win")
                win+=1
            if move =='s' and computer =='p':
                print("Win")
                win+=1
            if move =='p' and computer =='r':
                print("Win")
                win+=1
                
            if move =='r' and computer =='p':
                print("Lose")
                loss += 1
            if move =='s' and computer =='r':
                print("Lose")
                loss += 1
            if move =='p' and computer =='s':
                print("Lose")
                loss += 1
                
        else:
            print("Please provide a valid input")
            continue
        
else:
    for i in range(int(rounds)):
        print("Rock, Paper, Scissors")
        move = input("Shoot >")
        move =move.strip().lower()
        if move in possible_moves:
            if  move == 's':
                print("Scissors vs. . . . . ",end='')
            elif  move == 'r':
                print("Rock vs. . . . . ",end='')
            elif  move == 'p':
                print("Paper vs. . . . . ",end='')
            elif  move == 'q':
                print("Leaving so soon?")
                break
                
            computer= randint(1,3)
            
            if computer == 1:
                computer = 's'
                print("Scissors")
            elif computer ==2:
                computer = 'r'
                print("Rock")
            elif computer == 3:
                computer = 'p'
                print("Paper")
                
            if move==computer:
                print("Tie")
                tie += 1
                
            if move =='r' and computer =='s':
                print("Win")
                win+=1
            if move =='s' and computer =='p':
                print("Win")
                win+=1
            if move =='p' and computer =='r':
                print("Win")
                win+=1
                
            if move =='r' and computer =='p':
                print("Lose")
                loss += 1
            if move =='s' and computer =='r':
                print("Lose")
                loss += 1
            if move =='p' and computer =='s':
                print("Lose")
                loss += 1
                
        else:
            print("Please provide a valid input")
            continue
        
print("Your final score is: \n%d Wins\n%d Losses\n%d Ties"%(win,loss,tie))
print("We hope you had fun.")