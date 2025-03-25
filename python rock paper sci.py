#Rock Paper Sciscor 
import random
def roundrps(gamecount, userwins, comwins, username, tiecount):
    options = ["rock", "paper", "scissors"]
    comchoice = random.choice(options)
    userchoice = input("Choice: rock, paper, or scissors:")

    print (f"Player's choice: {userchoice}")
    print (f"Opponent's choice: {comchoice}")

    if userchoice == comchoice:
        gamecount = gamecount + 1 
        tiecount = tiecount + 1
        print("It's a tie")
    elif userchoice == "rock" and comchoice == "scissors":
        print(f"Rock beats Scissors, {username} Wins")
        gamecount = gamecount + 1 
        userwins = userwins + 1
    elif userchoice == "scissors" and comchoice == "paper":
        print(f"Scissors beats Paper, {username} Wins")
        gamecount = gamecount + 1
        userwins = userwins + 1
    elif userchoice == "paper" and comchoice == "rock":
        print(f'Paper Beats Rock, {username} wins')
    else:
        print('Computer wins')
        gamecount = gamecount + 1
        comwins = comwins + 1 
    print(f"Game count:{gamecount}, {username}'s wins: {userwins}, Com wins:{comwins}, Tie count: {tiecount}")
    
    return gamecount, userwins, comwins, tiecount

def gamerps(gamecount, userwins, comwins, username, tiecount):
    print(f'Game stats after {gamecount} games')
    print(f"{username}'s wins: {userwins}")
    print(f"Com's total wins: {comwins}")
    print(f"Total ties: {tiecount}")


    




    



username = input("Enter Username:")
print('welcome',username)
print('To Rock Paper Scissors')

comwins=0
userwins=0
gamecount=0
tiecount = 0

for _ in range(5):
    gamecount, userwins, comwins, tiecount = roundrps(gamecount, userwins, comwins, username, tiecount)
    
    if gamecount > 4:
        gamerps(gamecount, userwins, comwins, username, tiecount)