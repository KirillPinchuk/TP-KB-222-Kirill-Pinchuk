from random import choice
choise = ["rock", "scissor", "paper"]
my_choice = input("Select: rock, scissors, paper:")
comp_choice = choice(choise)
print(f"You: {my_choice}")
print(f"Computer: {comp_choice}")
if my_choice == comp_choice:
    print("It's a draw")
elif my_choice == "rock" and comp_choice == "scissors":
    print("You Win")
elif my_choice == "scissors" and comp_choice == "paper":
    print("You Win")
elif my_choice =="paper" and comp_choice == "rock":
    print("You Win")
else:
    print("Lose")