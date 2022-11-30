from sys import getrecursionlimit

working = True


def get_integral(number: int):
    if number == 1:
        return 1
    else:
        return number * get_integral(number - 1)


def get_input_number(message: str):
    ret = ''
    while not ret.isdigit():
        ret = input(message)
    return int(ret)


while working:
    try:
        number = get_input_number('Введіть ціле число: ')
        print(get_integral(number))
        working = False

    except RecursionError:
        print('Дуже велике число, кампуктер не справляеться.\n'
              f'Введіть число менше {getrecursionlimit() - 1}.')