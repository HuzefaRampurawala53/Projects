import random

count = 0  # Initialize count outside the loop

while True:
    choice = input("Roll the dice (yes/no): ").lower()

    if choice == 'yes':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        count += 1
        print(f"{die1}, {die2}")
    elif choice == 'no':
        print("Thank you for playing the game....")
        break
    else:
        print("Invalid choice. Please type 'yes' or 'no'.")

print(f"You rolled the dice {count} time(s).")
