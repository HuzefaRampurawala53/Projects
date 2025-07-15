import random
letter='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*'
length=int(input("Enter Length of your password : "))
password=""
for a in range(length):
    password+=random.choice(letter)
print(password)
while True:
    save = input("Do you want to save this password?(y/n): ")
    if save.lower() == "y":
        with open("passwords.txt","a") as file:
            file.write(password)

        break
    elif save.lower() == "n":
        break
    else:
        print("Invalid Input")
        continue