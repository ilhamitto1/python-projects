print("CHARACTER TYPE CHECKER")
char = input("Enter a single character")
if char.isalpha():
  print("The character is a letter")
elif char.isdigit():
  print("The character is a digit")
else:
  print("The character is a special character")