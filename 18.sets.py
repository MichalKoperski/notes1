# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

for x in utensils:
    print(x)

print("-"*40)
utensils.add("napkin")
for x in utensils:
    print(x)

print("-"*40)
utensils.remove("fork")
for x in utensils:
    print(x)

print("-"*40)
utensils.clear()
for x in utensils:
    print(x)

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

print("-"*40)
utensils.update(dishes)
for x in utensils:
    print(x)

print("-"*40)
dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)

print("-"*40)
print(utensils.difference(dishes))
print(dishes.difference(utensils))
print(utensils.intersection(dishes))