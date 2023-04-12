import random

player_choice = int(input(
    "Make your move, 0 for rock, 1 for paper, 2 for scissiors: "))
computer_choice = random.randint(0, 2)
rpc_array = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)________
           __________)
          ___________)
         ___________)
---.______________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
try:
    print(f"You choose {rpc_array[player_choice]}")
    print(f"Computer choose {rpc_array[computer_choice]}")

    if player_choice == computer_choice:
        print("Its a draw")
    elif (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1) or (player_choice == 0 and computer_choice == 2):
        print("You win")
    elif (player_choice == 0 and computer_choice == 1) or (player_choice == 1 and computer_choice == 2) or (player_choice == 2 and computer_choice == 0):
        print("You lose")
except:
    print("You typed an invalid number, you lose!")

