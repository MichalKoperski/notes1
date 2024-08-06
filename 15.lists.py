food = ["pizza", "hamburger", "hotdog", "spaghetti"]

print(food)
print(food[2])

food[0] = "sushi"

print(food)

for x in food:
    print(x)

print("-"*40)
food.append("ice cream")
for x in food:
    print(x)

print("-"*40)
food.remove("hotdog")
for x in food:
    print(x)

print("-"*40)
food.pop()
for x in food:
    print(x)

print("-"*40)
food.insert(0,"cake")
for x in food:
    print(x)

print("-"*40)
food.sort()
for x in food:
    print(x)

print("-"*40)
food.clear()
for x in food:
    print(x)