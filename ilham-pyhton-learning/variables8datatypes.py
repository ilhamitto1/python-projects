print("Hello World")
name = "john"

age = 25
 
height = 5.9

is_student = True

print("My name is" + name + "and I am" + str(age) + "years old")

print(name[0])

message = "Hello World"
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.replace("H","l"))
print("World" in message)
print(len(message))

greeting1 = "Hello"
greeting2 = "World"
if(greeting1 == greeting2):
    print("The strings are equal")
else:
    print("The strings are not equal")
    
age_str = "25"
age_num = int(age_str)

print(type(age_str))
print(type(age_num))
