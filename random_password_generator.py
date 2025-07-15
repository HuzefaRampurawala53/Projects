import random
letter='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*'
length=int(input("Enter Length of your password : "))
password=""
for a in range(length):
    password+=random.choice(letter)
print(password)