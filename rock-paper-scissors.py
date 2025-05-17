import random

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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
if choice == 0:
    print (rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("You type an invalid number!Please choice[0,1,2]")
comp_choice = random.randint(0,2)
if comp_choice == 0:
    print(rock)
elif comp_choice == 1:
    print(paper)
elif comp_choice == 2:
    print(scissors)

# you win
if choice == 0 and comp_choice == 2:
    print("You Win!")
elif choice == 1 and comp_choice == 0:
    print("You Win!")
elif choice == 2 and comp_choice == 1:
    print("You Win!")

#Computer win
if choice == 0 and comp_choice == 1:
    print("Computer Win!")
elif choice == 1 and comp_choice == 2:
    print("Computer Win!")
elif choice == 2 and comp_choice == 0:
    print("Computer Win!")

#Draw
if choice == 0 and comp_choice == 0:
    print("Draw!")
elif choice == 1 and comp_choice == 1:
    print("Draw!")
elif choice == 2 and comp_choice == 2:
    print("Draw!")