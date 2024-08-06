import random

age = 21
age += 1
#-----------------------------------------
print("-"*40)
print("do konkatenacji potrzebne stringi")
#-----------------------------------------
print("Your age is: "+str(age))

height = 250.5
print("Your height is "+str(height))

#-----------------------------------------
print("-"*40)
print("multiple assignment")
#-----------------------------------------
name, age, attractive = "Mike", 21, True

#-----------------------------------------
print("-"*40)
print("string methods")
#-----------------------------------------
name = "mike"

print(len(name))
print(name.find("k"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("k"))
print(name.replace("k","r"))
print(name*3)

#-----------------------------------------
print("-"*40)
print("type casting")
#-----------------------------------------
x = 1
y = 2.0
z = "3"

print(float(x))
print(int(y))
print(int(z))

#-----------------------------------------
print("-"*40)
print("user input")
#-----------------------------------------
#name = input("What is your name?: ")
#age = int(input("How old are you?: "))
#age += 1
#height = float(input("How tall are you?: "))

#print("You are "+str(age)+" years old, and are "+str(height)+"cm tall")

#-----------------------------------------
print("-"*40)
print("math functions")
#-----------------------------------------
import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(pi))
print(max(x,y,z))
print(min(x,y,z))

#-----------------------------------------
print("-"*40)
print("string slicing")
#-----------------------------------------
name = "Bro Code"

first_name = name[0:3]
first_name = name[:3]

last_name = name[4:8]
last_name = name[4:]

funky_name = name[0:8:2]
funky_name = name[::2]

reversed_name = name[::-1]
print(first_name+" oraz "+last_name+" oraz "+funky_name+" oraz "+reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])

#-----------------------------------------
print("-"*40)
print("if statement")
#-----------------------------------------
age = random.randrange(200)
print(age)
if age == 18:
    print("You are an adult!")
elif age >= 100:
    print("You are old")
elif age < 0:
    print("You have not been born yet")
else:
    print("You are a child")

#-----------------------------------------
print("-"*40)
print("logical operators")
#-----------------------------------------
temp = random.randrange(50)
print(temp)

if temp >= 0 and temp <= 30:
    print("good")
elif temp < 0 or temp > 30:
    print("bad")

if not(temp >= 0 and temp <= 30):
    print("bad")
elif not(temp < 0 or temp > 30):
    print("good")