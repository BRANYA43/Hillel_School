"""Написати функцію, яка рахуватиме кількість очок футбольної команди.
Перемога дає 3 очки, нічия 1 очко, поразка -1 очко.
Функція приймає три аргументи – win, draw, loss.
Приклад : count_points(3, 2, 2) -> 9"""


def count_points(win: int, draw: int, loss: int) -> int:
    return win * 3 + draw - loss


print(count_points(3, 2, 2))
