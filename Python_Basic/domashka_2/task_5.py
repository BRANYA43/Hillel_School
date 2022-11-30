x = ''
while not x.isdigit():
    x = input('Введіть число: ')
    try:
        if int(x) < 0:
            break
    except ValueError:
        pass

x = int(x)

if x > 0:
    print(f'sign({x}) = 1')

elif x < 0:
    print(f'sign({x}) = -1')

else:
    print(f'sign({x}) = 0')
