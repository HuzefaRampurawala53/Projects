import random
import pyttsx3
engine=pyttsx3.init()
subjects = [
    "Salman Khan",
    "A Bamboo Tree",
    "Mukesh Ambani",
    "Husband",
    "Huzefa",

]
actions=[
    "Farts",
    "Laughs",
    "Got Slapped",
    "Dancing on bed",
    "Eating fast",
]
places=[
    "at Ipl match",
    "in Hospital",
    "on Rooftop",
]
while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place=random.choice(places)
    headline=f"BREAKING NEWS!!!: {subject} {action} {place}"
    engine.say(headline)

    engine.runAndWait()  # Speak it now

    
    print(headline)
    engine.say(headline)
    user_input=input("Do you want to see another news (yes/no)?: ")
    if(user_input == 'yes'):
        print(headline)
        engine.say(headline)
        engine.runAndWait()
    else:
        print("Thank you have a good day...")
        break

