import random
easy_words=["apple","box","photo"]
medium_words=["cupboard","mirror","laptop"]
hard_words=["huzefa","chatgpt","eifiel tower"]

difficulty_level=input("enter the level of difficulty (easy or medium or hard): ")
if(difficulty_level=="easy"):
    secret=random.choice(easy_words)
elif(difficulty_level=="medium"):
    secret=random.choice(medium_words)
elif(difficulty_level=="hard"):
    secret=random.choice(hard_words)
else:
    print("Invalid choice,Default choosing easy words")
    secret=random.choice(easy_words)
print(secret)
