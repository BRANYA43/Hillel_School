LIMIT_RANGE = 150

list_of_six = list(range(100, 200, 6))
list_divisible_five = []

for elem in list_of_six:
    if elem % 5 == 0 and elem < LIMIT_RANGE:
        list_divisible_five.append(elem)

print(list_divisible_five)