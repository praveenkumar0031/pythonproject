import random

if __name__=="__main__":
    option=["rock","paper","scissors"]
    comscr=0
    userscr=0
    drawscr=0
    rnd=1
    print("Welcom to rock papper scissor game :)")
    print("-------------------------------------")
    while True:
        print(f"Round : {rnd}")
        print("---------------------")
        user=input("Enter your choice (rock/paper/scissors):")
        com = random.choice(option)
        if user==option[0] or user==option[1] or user==option[2]:
            if com==user:
                print(f"Round is tie you both choosed : {com}")
                drawscr+=1
            elif com==option[0]:
                if user=="paper":
                    userscr+=1
                    print(f"You choose #{user} and opponent choose #{com} ")
                    print("You Wins !")
                else:
                    comscr+=1
                    print(f"You choose #{user} and opponent choose #{com} ")
                    print("You Lose !")
            elif com==option[1]:
                if user=="scissors":
                    userscr+=1
                    print(f"You choose {user} and opponent choose {com} ")
                    print("You Wins !")
                else:
                    comscr+=1
                    print(f"You choose {user} and opponent choose {com} ")
                    print("You Lose !")
            elif com==option[2]:
                if user=="rock":
                    userscr+=1
                    print(f"You choose {user} and opponent choose {com} ")
                    print("You Wins !")
                else:
                    comscr+=1
                    print(f"You choose {user} and opponent choose {com} ")
                    print("You Lose !")
            ch=input("do you want to try another round :")
            rnd+=1
            print("---------------------")
            if ch=="no":
                print("score board ")
                print("-------------------------")
                print(" You | opponent | Ties ")
                print("-------------------------")
                print(f"  {userscr}  |    {comscr}     |  {drawscr}  ")
                if userscr==comscr:
                    print("Match is Tie !")
                elif userscr>comscr:
                    print("You won the match !")
                else:
                    print("You lose the match !")
                break
        else:
            print("Inalid choice try again ")