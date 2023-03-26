#Rock Paper Scissors

import random

def PrintChoose(choosen):
    if choosen == 0:
        print(rock)
    elif choosen == 1:
        print(paper)
    elif choosen == 2:
        print(scissors)
    else:
        print('You Enter Wrong Number ')
        choose = int(input('What do you choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS. '))
        PrintChoose(choose)
def Rules(you_chos,comp_chos):
    if you_chos == comp_chos:
        print('Match is Draw')
    elif you_chos ==0 & comp_chos == 2 :
        print('You WON')
    elif  you_chos == 2 & comp_chos == 1:
        print('You WON')
    elif you_chos == 1 & comp_chos == 0 :
        print('You WON')
    else:
        print('You Lose')

    

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
play = 0
while (play == 0):
    choose = int(input('What do you choose? Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS. '))
    PrintChoose(choose)
    computer_choose = random.randint(0,2)
    print(f'Computer Choose')
    PrintChoose(computer_choose)
    Rules(choose, computer_choose)
    play = int(input('\nTo PLay Again Type 0 = '))