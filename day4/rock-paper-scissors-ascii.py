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

#Write your code below this line 👇
images = [rock, paper, scissors]
user_choice = input("Welcome to the game. Select 0 for Rock, 1 for Paper, 2 for Scissors\n")

if user_choice.isnumeric() is True:
    user_choice_int = int(user_choice)
    if user_choice_int > 2 or user_choice_int < 0:
        print("Invalid number: You lose!")
    else:
        print(f"You chose: {user_choice_int}\n")
        print(f"{images[user_choice_int]}")
        computer_choice = random.randint(0, 2)
        print(f"Computer chose: {computer_choice}\n")
        print(f"{images[computer_choice]}")
        if user_choice_int == computer_choice:
            print("It's a draw")
        elif user_choice_int == 1 and computer_choice == 0:
            print("You win!")
        elif user_choice_int == 0 and computer_choice == 2:
            print("You win!")
        elif user_choice_int == 2 and computer_choice == 1:
            print("You win!")
        else:
            print("You lose!")
else:
    print("Invalid data type. Get outta here")