#  temp = int(input("What is the temperature outside?"))
#  if temp > 30:
#  print("It's a hot day")
# print("Drink plenty of water")
# elif temp > 20:
# print("It's a nice day")
# else:
# print("It's a cold day")
# print("Wear warm clothes")

# checking multiple conditions
  
age = 28
has_license = False
if age >= 18 and has_license:
  print("You can drive")
elif age >= 18 and not has_license:
    print("You can get a license")
else:
    print("You can not drive")