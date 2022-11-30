number = ''

while not number.isdigit():
    number = input('Введіть кількість зірок: ')

print('*' * int(number))
