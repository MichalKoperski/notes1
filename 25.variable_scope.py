# scope = the region that a variable is recognized
#         a variable is only available from inside the region it is created
#         a global and locally scoped versions of a variable can be created

name = "Bro"

def display_name():
    name = "Code"
    print(name)

display_name()
print(name)