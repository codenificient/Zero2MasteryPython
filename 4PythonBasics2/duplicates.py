some_list = ['a', 'b', 'c', 'b', 'b', 'd', 'm', 'n', 'n']
singles = []
dups = []
for letter in some_list:
    if letter  in singles and letter not in dups:
        dups.append(letter)
    else:
        singles.append(letter)

print(dups)

name = "christian"
print(name.title())

