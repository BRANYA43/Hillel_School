"""
Написати програму яка поверне кількість введених користувачем слів та загальну кількість символів.
"""


def get_count_word(text: str) -> int:
    return len(text.split())


def get_count_symbols(text: str) -> int:
    return len(text) - text.count(' ')


def main():
    text_input = input('Введіть речення: ')
    print(f'Кількість символів у реченні: {get_count_symbols(text_input)}')
    print(f'Кількість слів у реченні: {get_count_word(text_input)}')


if __name__ == '__main__':
    main()
