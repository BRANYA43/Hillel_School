SOME_TUPLE = tuple(range(10, 101, 10))
working = True

x = ''
save_x = ''

while working:
    x = input('Введіть число: ')
    try:
        save_x = x
        x = float(x)
        working = False
    except ValueError:
        print('Ви ввели не число')


if x % 1 == 0:
    x = int(x)

if abs(x) in SOME_TUPLE:
    print(f'Значення x = {save_x} є у послідовності {SOME_TUPLE}.')
else:
    print(f'Значення x = {save_x} немає у послідовності {SOME_TUPLE}.')