"""
 Написати функцію square, що приймає 1 аргумент - сторону квадрата, і повертає 3 значення (за допомогою кортежу):
 периметр квадрата, площа квадрата та діагональ квадрата.
"""


def get_format_number(number: int | float) -> int | float:
    if type(number) is float:
        return number * 10 // 1 / 10
    else:
        return number


def is_float(value) -> bool:
    try:
        if float(value):
            return True
    except ValueError:
        return False


def get_input_number(message: str) -> int | float:
    working = True
    while working:
        ret = input(message)
        if ret.isdigit():
            return int(ret)
        elif is_float(ret):
            return float(ret)


def square(a: int | float) -> tuple[int | float, int | float, float]:
    perimeter = a * 4
    area = a ** 2
    diagonal = (a * 2 ** 0.5)
    return perimeter, area, diagonal


def main():
    number = get_input_number('Введіть розмір сторони квадрата: ')
    info_square = square(number)
    print(f'Периметр: {get_format_number(info_square[0])}\n'
          f'Площа: {get_format_number(info_square[1])}\n'
          f'Диагональ: {get_format_number(info_square[2])}')


if __name__ == '__main__':
    main()
