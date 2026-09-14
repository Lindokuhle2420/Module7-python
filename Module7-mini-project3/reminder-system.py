# Workout Reminder System
import time
from datetime import datetime
def countdown(seconds):
    print("Workout started at :", datetime.now())
    while seconds > 0:
        print("Time left:", seconds)
        time.sleep(1)
        seconds -= 1 

    print("Take a breather and drink some water!")
countdown(10)