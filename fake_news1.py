import random
import pyttsx3

engine = pyttsx3.init()


subjects = [
    "Salman Khan",
    "A Bamboo Tree",
    "Mukesh Ambani",
    "Husband",
    "Huzefa",
    "A Flying Monkey",
    "Ranveer Singh in pajamas",
    "A Confused Magician",
    "ChatGPT's evil twin",
    "A Sleepwalking Grandma",
    "A Jealous Parrot",
    "Elon Musk's Clone",
    "A Ghost with WiFi issues",
    "Batman on vacation",
    "A Motivational Speaker Goat"
]

actions = [
    "Farts",
    "Laughs",
    "Got Slapped",
    "Dancing on bed",
    "Eating fast",
    "Slips on a banana peel",
    "Sings opera in reverse",
    "Winks aggressively",
    "Does push-ups in slow motion",
    "Argues with a mirror",
    "Orders pizza telepathically",
    "Forgets how to blink",
    "Cries over spilled ketchup",
    "Wears socks on hands",
    "Starts a podcast about silence"
]

places = [
    "at IPL match",
    "in Hospital",
    "on Rooftop",
    "Inside a washing machine",
    "On a unicorn-shaped boat",
    "At the top of Mount Confusion",
    "Inside a giant samosa",
    "Under the neighbor’s WiFi router",
    "During a Zoom call with aliens",
    "In a haunted ATM booth",
    "On a treadmill in space",
    "Inside a Tupperware box",
    "Behind the fridge of destiny"
]



while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places)

    headline = f"BREAKING NEWS!!! {subject} {action} {place}"

    print(headline)
    engine.say(headline)
    engine.runAndWait()  # Speak it now

    user_input = input("Do you want to see another news (yes/no)?: ").strip().lower()
    if user_input != 'yes':
        goodbye = "Thank you, have a good day!"
        print(goodbye)
        engine.say(goodbye)
        engine.runAndWait()
        break
