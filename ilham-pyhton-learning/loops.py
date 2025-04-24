print("counting from 1 to 10")
for i in range(1,11):
  print(i)
  
print("\nReverse counting from 10 to 1")
for i in range(10,0,-1):
  print(i)
  
  
count = 5
print("\nReverse counting from 1 to 5 ")
while count >=1:
  print(count)
  count -= 1
  
fruits = ["apple","banana","cherry"] 
print("\nMy Fruits")
for fruit in fruits:
  print(fruit)
  
print("\nMy Fruits")
for fruit in reversed(fruits):
  print(fruit)
  
print("\n Fruits with index")
for index,fruit in enumerate(fruits):
  print(index,fruit)
  
print("\n Reversed fruites with index")
for index,fruit in enumerate(reversed(fruits)):
  print(index,fruit)
  