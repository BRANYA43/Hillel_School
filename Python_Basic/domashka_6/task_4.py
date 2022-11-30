"""Написати функцію, яка повертає поточний час. І обернути її у декоратор який відрахує 3 секунди.
  Приклад:
  what_time_is_it_now()
  3
  2
  1
  '16:21'
  Повернути час допоможе метод time.strftime з аргументом '%H:%M' """

from datetime import datetime
from time import sleep


def countdown_from_three(func):
    def wrapper(*args, **kwargs):
        for i in range(3, 0, -1):
            print(i)
            sleep(1)
        func(*args, **kwargs)
    return wrapper


@countdown_from_three
def what_time_is_it_now():
    dt = datetime.now()
    print(dt.strftime('%H:%M'))


def main():
    what_time_is_it_now()


if __name__ == '__main__':
    main()



