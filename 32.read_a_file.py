try:
    with open('32.test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found")