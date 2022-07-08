user_choice = int(input("Welcome to the game. Select 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer_choice = random.randint(0, 2)
options_list = ["rocks", "paper", "scissors"]

print(f"You chose: {user_choice}")
print(f"Computer chose: {computer_choice}")

if user_choice > 2:
    print("Invalid number: You lose!")
elif user_choice == computer_choice:
    print("It's a draw")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")