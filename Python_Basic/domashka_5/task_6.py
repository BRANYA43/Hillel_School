"""
Написати функцію яка прибере з dict елементи із значеннями None:
{'first_color': 'Red', 'second_color': 'Green', 'third_color': None}
Повинно повернути {'first_color': 'Red', 'second_color': 'Green'} # * dict може бути довільним
"""


def get_keys_is_none(some_dict: dict) -> list:
    keys_in_none = []
    for key, item in some_dict.items():
        if item is None:
            keys_in_none.append(key)
    return keys_in_none


def delete_keys_is_none(some_dict: dict):
    for key in get_keys_is_none(some_dict):
        some_dict.pop(key)


def main():
    colors = {'first_color': 'Red', 'second_color': 'Green', 'third_color': None, 'fourth': 'Blue', 'fifth': None,
              'sixth': None, 'seventh': 'Black', 'eighth': 'White', 'ninth': 'Pink', 'tenth': None}
    print(f'Словник до змін: {colors}')
    delete_keys_is_none(colors)
    print(f'Словник після змін: {colors}')


if __name__ == '__main__':
    main()
