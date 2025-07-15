history = "history.txt"
import math
def show_history():
    try:
        with open(history, 'r') as f:
            lines = f.readlines()
            if len(lines) == 0:
                print("No history found...")
            else:
                print("\n--- Calculation History ---")
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history file found.")

def clear_history():
    with open(history, 'w') as f:
        pass  
    print("History cleared...")

def save_history(equation,result  ):
    with open(history, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    try:
        result = eval(user_input)
        rounded_result=round(result,2)
        print(f"Result: {rounded_result}")
        save_history(user_input, rounded_result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"Invalid expression. Error: {e}")

while True:
    print("\nOptions:")
    print("1. Calculate")
    print("2. Show History")
    print("3. Clear History")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        expression = input("Enter an expression:  ")
        calculate(expression)
    elif choice == '2':
        show_history()
    elif choice == '3':
        clear_history()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose between 1 and 4.")
