import random

num = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Guess the number: "))
        attempts += 1

        if guess < num:
            print("It's low.")
        elif guess > num:
            print("It's high.")
        elif(guess=="show").lower():
            print(num)
        else:
            print(f"It's a match! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid number. Please enter an integer.")
