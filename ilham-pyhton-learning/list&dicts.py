numbers = [1,2,3,4,5]
print(numbers[0])
numbers[1] = 100
numbers.append(3)
numbers.remove(4)

print(numbers)
print(len(numbers))


numbers = [1,2,3,4,5]
print(numbers[1:3])
print(numbers[::3])
print(numbers[::-1])
print(numbers +[6,7,9])
print(numbers*2)

student = {
  "name": "John",
  "age": 30,
  "is_student": True
}

print(student["name"])
print(student.get("age"))
print(student.get("phone"))
student["grade"] = "A"
student["age"] = "40"
print(student)
print(student.keys())
print(student.values())
print(student.items())

for key,value in student.items():
  print(f"{key}:{value}")
  
unique_colors = {"red","blue","green"}
print("unique_colors:", unique_colors)