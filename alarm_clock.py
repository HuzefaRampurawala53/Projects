from playsound import playsound
import time

# Use proper escape characters for terminal control
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1
        time_remaining = seconds - time_elapsed
        minutes_left = time_remaining // 60
        seconds_left = time_remaining % 60
        print(f"{CLEAR_AND_RETURN}{minutes_left:02d}:{seconds_left:02d}")
    playsound("alarm.mp3")

# Get input from user
minutes = int(input("How many minutes? "))
seconds = int(input("How many seconds? "))
total_seconds = minutes * 60 + seconds

# Start alarm
alarm(total_seconds)

