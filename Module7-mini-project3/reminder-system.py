## importing build in modules
import time
from datetime import datetime

def countdown (seconds):
    while seconds > 5:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1 
        print("Time's up! Reminder: Take a break and stretch!")

        countdown(20)