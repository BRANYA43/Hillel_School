working = True

integer_part = ''
fractional_part = ''
number = ''


while working:
    number = input('Введіть дрібне число: ')
    try:
        if float(number) and not number.isdigit():
            if number[-1] == '.':
                number += '0'
            working = False
    except ValueError:
        print(f'Ви ввели помилкові данні.')

_, fractional_part = number.split('.')
print(f'Дрібна частина числа: {fractional_part}\n'
      f'Перша цифра дрібної частини: {fractional_part[0]}')
