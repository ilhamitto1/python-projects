import random

random_number = random.randint(1,10)
print(f"Random number is {random_number}")


fruits = ["apple","banana","cherry"]
random_fruits = random.choice(["apple","banana","cherry"])
print(f"random fruits is {random_fruits}")

random.shuffle(fruits)
print(f"shuffle the list {fruits}")

# datetime module
import datetime
current_time = datetime.datetime.now()
print(f"current time is {current_time}")
print(f"current year is {current_time.year}")
print(f"current month is {current_time.month}")
print(f"current day is {current_time.day}")

import os

current_directory = os.getcwd()
print(f"current directory is {current_directory}")
print(f"List of files: {os.listdir(current_directory)}")


import time
print("waiting for 5 seconds...")
time.sleep(5)
print("done")