# a lot of inputs :3
import random
import time
import os

choiceslist = ["""
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)
(ROCK)
""","""
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)
(PAPER)
""","""
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)
(SCISSORS)"""]
#ascii art for RPS (Found online)
rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)
(ROCK)
'''
paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)
(PAPER)
'''
scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)
(SCISSORS)
'''  

Playername = "Player"
Playerscore = 0
Computerscore = 0
ComputerChoice = [""]
PlayerChoice = ""


# the actual game
def game():
    global Playerscore
    global Computerscore
    global ComputerChoice
    os.system('cls')
    print("----- Rock Paper Scissors! -----")
    if str(Playerscore) == "3":
        print(f"""
Congratulations {Playername}, you have beaten the computer!
You won by {Playerscore - Computerscore} points!
[{Playerscore} : {Computerscore}] 
Would you wish to replay?""")
        replaych = input("Y/N > ")
        if replaych.upper() == "Y":
            Playerscore = 0
            Computerscore = 0
            game()
    elif str(Computerscore) == "3":
        print(f"""
Uh oh! The computer has won!
The Computer won by {Computerscore - Playerscore} points!
[{Computerscore} : {Playerscore}] 
Would you wish to try again?""")
        replaych = input("Y/N > ")
        if replaych.upper() == "Y":
            Playerscore = 0
            Computerscore = 0
            game()
    else:
            print(f"""
    Current score :
    Computer : {str(Computerscore)}
    Player : {str(Playerscore)}

    ---- OPTIONS ----
    1 ) Choose R,P OR S [DEFAULT]
    2 ) Restart
    3 ) Exit to main menu
    """)
            choice = input("Choice > ")
            choice1 = random.choice(choiceslist)
            Computerchoice = choice1
            
        
            if choice == "1" or choice == "":
                RPS = input("R,P OR S > ")
                if RPS.upper() == "R":
                    Playerchoice = "Rock"
                    print(f"""
{Playername} :
{rock}

Computer :
{Computerchoice}
""")

                elif RPS.upper() == "P":
                        Playerchoice = "Paper"
                        print(f"""
{Playername} :
{paper}

Computer :
{Computerchoice}
""")
                elif RPS.upper() == "S":
                        Playerchoice = "Scissors"
                        print(f"""
{Playername} :
{scissors}

Computer :
{Computerchoice}
""")
                else:
                    print("Non valid option, please pick [R P or S]!")
                    game()
                    
                if "paper" in Computerchoice.lower() and "rock" in Playerchoice.lower():
                    Computerscore = Computerscore + 1
                    print("Computer gained 1 point! \n ")
                elif "paper" in Playerchoice.lower() and "rock" in Computerchoice.lower():
                    Playerscore = Playerscore + 1
                    print("Player gained 1 point! \n ")
                elif "scissors" in Computerchoice.lower() and "paper" in Playerchoice.lower():
                    Computerscore = Computerscore + 1
                    print("Computer gained 1 point! \n ")
                    
                elif "scissors" in Playerchoice.lower() and "paper" in Computerchoice.lower():
                    Playerscore = Playerscore + 1
                    print("Player gained 1 point! \n ")
                elif "rock" in Computerchoice.lower() and "scissors" in Playerchoice.lower():
                    Computerscore = Computerscore + 1
                    print("Computer gained 1 point! \n ")
                    
                elif "rock" in Playerchoice.lower() and "scissors" in Computerchoice.lower():
                    Playerscore = Playerscore + 1
                    print("Player gained 1 point! \n ")
                else:
                    print("")
                input("Press enter to continue > ")
                game()

                if RPS.upper() == "R":
                    print("")
            elif choice == "2":
                Playerscore = 0
                Computerscore = 0
                game()
            else:
                print("Not a valid option. please pick [1 , 2 or 3]")
                game()
                


def mainmenu():
    os.system('cls')
    print("----- Welcome to Rock Paper Scissors! -----")
    print("""
    - You (the player) will be up against the opponent (the computer)
    - To win you have to score 3 times AGAINST the computer.
    - IF the computer scores 3 times you lose!
    - Rock is represented as 'R'
    - Paper is represented as 'P'
    - Scissors are represented as 'S'


    1 ) Play
    2 ) Credits
    3 ) Exit to desktop
    """)
    startch = input("Choice > ")
    if startch == "1":
        game()
    elif startch == "2":
        os.system('cls')
        print("""
----- Rock Paper Scissors Credits! -----
- Creator - > Thomas G (github.com/sgtflixy)
- Resources - > https://devdojo.com (RPS ASCII)
- Python Team
""")
        crch = input("Press enter to go back > ")
        mainmenu()
    else:
        mainmenu()
mainmenu()
