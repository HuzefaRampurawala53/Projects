import random

# Mapping choices to proper emojis
emojis = {'r': '🪨', 'p': '📜', 's': '✂'}
choices = ('r', 'p', 's')


while True:
    user_choice = input("Select (r=rock, p=paper, s=scissors or q=quit): ").lower()

    if user_choice == 'q':
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice! Please select from 'r', 'p', or 's'.")
        continue

   
    computer_choice = random.choice(choices)

    
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("Yayyy! You won! 🎉")
    else:
        print("OHH :( You lost! Try again.")

    # Show choices
    print(f"You chose {emojis[user_choice]} {user_choice}")
    print(f"Computer chose {emojis[computer_choice]} {computer_choice}")
    
