from random import randint

some_list = [randint(0, 10) for i in range(randint(10, 50))]
count = 0

for i, _ in enumerate(some_list):
    if 0 < i < len(some_list) - 1:
        if some_list[i - 1] < some_list[i] > some_list[i + 1]:
            count += 1

print(f'Cписок: {some_list}')
print(f'Кількість елементів які більше сусідніх: {count}')
