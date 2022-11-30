list_ten = list(range(10, 51, 10))
list_reversible = []

for i in range(len(list_ten)):
    list_reversible.append(list_ten[-1-i])

print(list_reversible)
