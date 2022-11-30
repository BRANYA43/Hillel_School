"""
Даний перелік випадкових цілих чисел. Замініть усі непарні числа списку нулями. І виведете їхню кількість.
"""
from random import randint

numbers = [randint(0, 100) for i in range(50)]

for i, n in enumerate(numbers):
    if n % 2 != 0:
        numbers[i] = 0

print(f'Список: {numbers}')
print(f'Кількість нулів у списку: {numbers.count(0)}')
