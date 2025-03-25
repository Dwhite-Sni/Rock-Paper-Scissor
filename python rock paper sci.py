#Rock Paper Sciscor 
import random
def roundrps(gamecount, userwins, comwins, username, tiecount, comloss, userloss):
    options = ["rock", "paper", "scissors"]
    comchoice = random.choice(options)
    userchoice = input("Choice: rock, paper, or scissors:")

    print (f"Player's choice: {userchoice}")
    print (f"Opponent's choice: {comchoice}")

    if userchoice == comchoice:
        gamecount = gamecount + 1 
        tiecount = tiecount + 1
        print("It be a draw")
    elif userchoice == "rock" and comchoice == "scissors":
        print(f"Rock doth smite Scissors, {username} triumpheth")
        gamecount = gamecount + 1 
        userwins = userwins + 1
        comloss = comloss + 1
    elif userchoice == "scissors" and comchoice == "paper":
        print(f"Scissors doth strike Paper, {username} triumpheth")
        gamecount = gamecount + 1
        userwins = userwins + 1
        comloss = comloss + 1
    elif userchoice == "paper" and comchoice == "rock":
        print(f'Paper doth cover Rock, {username} triumpheth')
        gamecount = gamecount + 1
        userwins = userwins + 1
        comloss = comloss + 1
    else:
        print('Computer wins')
        gamecount = gamecount + 1
        comwins = comwins + 1
        userloss = userloss + 1 
    print(f"Game count:{gamecount}, {username}'s wins: {userwins}, Com wins:{comwins}, Tie count: {tiecount}\n")
    
    return gamecount, userwins, comwins, tiecount, userloss, comloss

def gamerps(userwins, comwins, username, tiecount, comloss, userloss):
    print(f"{username}:{userwins} wins, {userloss} loss, {tiecount} draw")
    print(f"Com: {comwins} wins, {comloss} loss, {tiecount} draw")

    if userwins > comwins:
        print(f"Huzzah, {username}, thou hast triumphed!")
    elif userwins < comwins:
        print(f"Ha, I Sir Compute be the victor, thou art the vanquished. \nMayhap fortune smiles upon thee next time, {username}!")
    else:
        print(f"A draw it be, let us play once more! \nI doth challenge thee, {username}, once again!")

    




    



username = input("Enter Username:")
print(f'Hail,{username}! I be Sir Compute, let us play a game')

comwins=0
userwins=0
comloss=0
userloss=0
gamecount=0
tiecount = 0

for _ in range(5):
    gamecount, userwins, comwins, tiecount, comloss, userloss = roundrps(gamecount, userwins, comwins, username, tiecount, comloss, userloss)
    
gamerps(userwins, comwins, username, tiecount, userloss, comloss)