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

#Write your code below this line 👇

import random
comp_choice = random.randint(1,3)
print('Enter "R" for Rock, "P" for Paper, "S" for Scissors')
user_choice = input("Enter your choice: ")
user_choice = user_choice.lower()
if user_choice == "r":
    print(rock)
    if comp_choice == 1:
        print(rock)
        print("Draw")
    elif comp_choice == 2:
        print(paper)
        print("You loose")
    else:
        print(scissors)
        print('You Win')
elif user_choice == "p":
    print(paper)
    if comp_choice == 1:
        print(rock)
        print("You Win")
    elif comp_choice == 2:
        print(paper)
        print("It's a Draw")
    else:
        print(scissors)
        print('You Loose')
elif user_choice == "s":
    print(scissors)
    if comp_choice == 1:
        print(rock)
        print("You Loose")
    elif comp_choice == 2:
        print(paper)
        print("You Win")
    else:
        print(scissors)
        print("It's a Draw")
else:
    print("Invalid choice. Please enter 'R', 'P', or 'S'.")
