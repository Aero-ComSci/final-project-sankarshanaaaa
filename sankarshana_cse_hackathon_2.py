# cse hackathon - sankarshana

# summertime random activity generator!
# type in things you like to do and when youre done it will print a random activity out of those for you to do

import random
import time

def validLength(activities):
    if len(activities) >= 1:
        return True
    else:
        return False

activityList = []

print("Welcome to your cure to boredom this summer... The random activity wheel!")
time.sleep(2)
print("Enter activities that you like to do into the wheel.")
time.sleep(2)
print("Once you're done, the wheel will give you a random activity to do!")
time.sleep(2)
print("You can come back whenever you want :)")
time.sleep(2)
print("")

while True:
    activity = input("Enter an activity to add to the random activity picker! Type 'end' to finish: ")
    if not activity:
        print("You can't do nothing for an activity silly! Enter something you like to do: ")
    else:
        if activity == "end":
            break
        else:
            activityList.append(activity)

print("Great! Now your activities have been added to the list.")
while True:
    select = input("Enter anything to select your next activity, leave it blank and press enter to stop: ")
    if not select:
        time.sleep(1)
        print("Hope this helped cure your boredom! Come back whenever you want!")
        break
    else:
        if validLength(activityList) == True:
            print("Your next activity is...")
            time.sleep(3)
            print(random.choice(activityList) + "!")
            time.sleep(1)
        else:
            print("There's nothing in the activity wheel.")
            time.sleep(1)
            print("Try running the program again and adding activities to the list.")
            break
