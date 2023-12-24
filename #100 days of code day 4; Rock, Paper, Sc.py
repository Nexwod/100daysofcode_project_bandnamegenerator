#100 days of code day 4; Rock, Paper, Scissors
import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

random = random.randint(0,2)
if random == 0:
    computer = rock
elif random == 1: 
    computer = paper
else:
    computer = scissors

user = input("What do you choose ? Type 'R' for Rock, 'P' for Paper or 'S' for scissors\n")
user=user.lower()

if user == 'r' and computer == rock:
    print(rock)
    print('Computer choose:')
    print(computer)
    print("Draw")
elif user == 'r' and computer == paper:
    print(rock)
    print('Computer choose:')
    print(computer)
    print("Paper Covers Rock; You Lose!")
elif user == 'r' and computer == Scissors:
    print(rock)
    print('Computer choose:')
    print(computer)
    print("Rock breaks Scissors; You win!!")
elif user == 'p' and computer == rock:
    print(paper)
    print('Computer choose:')
    print(computer)
    print("Paper Covers Rock; You Lose!")
elif user == 'p' and computer == scissors:
    print(paper)
    print('Computer choose:')
    print(computer)
    print("Scissors cuts Paper; You lose!")
elif user == 'p' and computer == paper:
    print(paper)
    print('Computer choose:')
    print(computer)
    print("Draw")
elif user == 's' and computer == rock:
    print(scissors)
    print('Computer choose:')
    print(computer)
    print("Rock breaks Scissors; You Lose!")
elif user == 's' and computer == paper:
    print(scissors)
    print('Computer choose:')
    print(computer)
    print("Scissors cuts Paper; You win!")
elif user == 's' and computer == scissors:
    print(scissors)
    print('Computer choose:')
    print(computer)
    print("Draw")
