"""
Написати функцію `is_date`, що приймає 3 аргументи - день, місяць і рік.
Повернути `True`, якщо дата коректна (треба враховувати число місяця.
Наприклад 30.02 - дата не коректна, так само 31.06 або 32.07 тощо), та `False` інакше.
"""
from datetime import date


def get_format_date(day: int, month: int) -> str:
    ret = ''
    if day < 10:
        ret += f'0{day}'
    else:
        ret += f'{day}'

    if month < 10:
        ret += f'.0{month}'
    else:
        ret += f'.{month}'
    return ret


def get_input_number(message: str) -> int:
    ret = ''
    while not ret.isdigit():
        ret = input(message)
    return int(ret)


def is_date(day: int, month: int, year: int) -> bool:
    now_date = date.today()
    if day == now_date.day and month == now_date.month and year.isdigit():
        return True
    else:
        return False


def main():
    some_day = get_input_number('Введіть день: ')
    some_month = get_input_number('Введіть місяць: ')
    some_year = get_input_number('Введіть рік: ')

    print(f'Дата сьогодні {date.today()}')

    if is_date(some_day, some_month, some_year):
        print(f'Дата {get_format_date(some_day, some_month)} є коректною. ')
    else:
        print(f'Дата {get_format_date(some_day, some_month)} не є коректною. ')


if __name__ == '__main__':
    main()
