import random

rockGraph = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paperGraph = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissorsGraph = ''' 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

GameGraphs = (rockGraph,paperGraph,scissorsGraph)
PcChoice = random.randint(0,2)
print(PcChoice)

UserChoice = int(input("What do you choose?\n0 for Rock \n1 for Paper \n2 for Scissors\n").lower())

if UserChoice >= 3 or UserChoice < 0:
    print("You typed invalid number, you loose!")
else:
    print(GameGraphs[UserChoice])
    if UserChoice == 0 and PcChoice == 2:
        print(GameGraphs[PcChoice],'\nyou won!')
    elif UserChoice == 1 and PcChoice == 0:
        print(GameGraphs[PcChoice], '\nyou won!')
    elif UserChoice == 2 and PcChoice == 1:
        print(GameGraphs[PcChoice], '\nyou won!')
    elif UserChoice == PcChoice:
        print(GameGraphs[PcChoice], '\nyou won!')
    else:
        print(f'{GameGraphs[PcChoice]}\nyou loose')



