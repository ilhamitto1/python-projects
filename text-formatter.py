print("🗣️ TEXT CAPITALIZER 🗣️")
text = input("🤷‍♂️️ What is your text?🤷‍♀️ ")
print("1 - UPPERCASE")
print("2 - LOWERCASE")
print("3 - title case")
print("4 - sentence case")

choice = int(input("Enter your choice: 1-4"))

if choice == 1:
  print(text.upper())
elif choice == 2:
  print(text.lower())
elif choice == 3:
  print(text.title())
elif choice == 4:
  print(text.capitalize())
else:
  print("Invalid choice")