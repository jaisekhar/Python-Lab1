#Initializing Dictionaries
d1 = {'B': 2, 'A': 1, 'C': 3}
d2 = {'F': 6, 'D': 4, 'E': 5}

#Concatenated Dictionaries and printing them
d2.update(d1)
print(d2)

#Sorting Dictionaries based on the keys
for value,key in sorted(d2.items(), key=lambda t: t[1]):
    print (value,':',key)