x = ''
y = ''

while not x.isdigit() or not y.isdigit():
    if not x.isdigit():
        x = input('Введите число для x: ')
    if not y.isdigit():
        y = input('Введите число для y: ')

x = int(x)
y = int(y)

print(f'x = {x}, y = {y}')
print(f'{x} + {y} = {x + y}')
print(f'{x} // {y} = {x // y}')
print(f'{x} % {y} = {x % y}')
print(f'{x}^{y} = {x ** y}')

