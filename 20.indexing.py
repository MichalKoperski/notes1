name = "bro Code!"

if(name[0].islower()):
    name = name.capitalize()
print(name)

first_name = name[0:3].upper()
first_name = name[:3].upper()
print(first_name)

last_name = name[4:].lower()
print(last_name)

last_character = name[-1]
print(last_character)

