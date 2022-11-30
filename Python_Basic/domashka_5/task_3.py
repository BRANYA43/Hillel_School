"""
Написати функцію яка поверне площу фігури: за замовчуванням трикутника, опціонально.
На вході 2 величини та параметр типу фігури.
"""
from random import randint

from task_5 import get_input_number


def get_area_figures(figure: int) -> int | float:
    ret = 0
    if figure == 0:
        ret = get_formulas_area_figures(
            get_input_number('a = '),
            get_input_number('h = ')
        )
    elif figure == 1:
        ret = get_formulas_area_figures(
            get_input_number('d1 = '),
            get_input_number('d2 = ')
        )
    elif figure == 2:
        ret = get_formulas_area_figures(
            get_input_number('a = '),
            get_input_number('b = '), figure=1
        )
    elif figure == 3:
        ret = get_formulas_area_figures(
            get_input_number('a = '),
            get_input_number('h = '), figure=1
        )
    elif figure == 4:
        ret = get_formulas_area_figures(
            get_input_number('a = '), figure=2
        )
    elif figure == 5:
        ret = get_formulas_area_figures(
            get_input_number('a = '),
            get_input_number('b = '),
            get_input_number('h = '), figure=3
        )
    elif figure == 6:
        ret = get_formulas_area_figures(
            get_input_number('r = '), figure=4
        )
    elif figure == 7:
        ret = get_formulas_area_figures(
            get_input_number('n = '),
            get_input_number('a = '),
            get_input_number('r = '), figure=5
        )
    return ret


def get_formulas_area_figures(n1: int, n2=0, n3=0, figure=0) -> int | float:
    formulas = {
        0: n1 * n2 / 2,
        1: n1 * n2,
        2: n1 ** 2,
        3: (n1 + n2) * n3 / 2,
        4: n1 ** 2 * 3.14,
        5: n1 * n2 * n3 / 2
    }
    return formulas[figure]


def main():
    figures = ['Трикутник',
               'Ромб',
               'Прямокутник',
               'Параллелограмм',
               'Квадрат',
               'Трапеція',
               'Коло',
               'n-кутник'
               ]
    for i, elem in enumerate(figures):
        print(f'{i}. {elem}')

    choose_figure = -1
    while choose_figure > 7 or choose_figure < 0:
        choose_figure = get_input_number('Оберіть фігур (від 0-7): ')
    print(figures[choose_figure])
    print(get_area_figures(choose_figure))


if __name__ == '__main__':
    main()
