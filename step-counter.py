print("🏃‍♂️ STEP COUNTER 🏃‍♂️")
step = int(input("what is your daily step goal? "))
rest_step = int(input("what is your rest step goal? "))

remaining = step - rest_step

if remaining > 0:
     print(f"You have {remaining} steps remaining")
else:
     print(f"Congratulations! You have reached your daily step goal.")
