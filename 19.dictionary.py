# dictionary = a chageable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

print(capitals['Russia'])
print(capitals.get('Germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

print("-"*40)
for key, value in capitals.items():
    print(key,value)

print("-"*40)
capitals.update({'Germany':'Berlin'})
for key, value in capitals.items():
    print(key,value)

print("-"*40)
capitals.update({'USA':'Las Vegas'})
for key, value in capitals.items():
    print(key,value)

print("-"*40)
capitals.pop('China')
for key, value in capitals.items():
    print(key,value)

print("-"*40)
capitals.clear()
for key, value in capitals.items():
    print(key,value)