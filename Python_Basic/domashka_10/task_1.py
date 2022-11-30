"""Програма яка при запуску повинна:
Створити текстовий файл, записати в нього дані, які вводить користувач.
Закінченням введення нехай служить порожній текст. Кожен введений текст у файлі повинен починатися з нового рядка."""


def save_file(name_file: str, text_list: list):
    """Зберігає/дописує текс зі списку рядків. Кожен елемент списку дописуеться з нового рядка."""
    with open(name_file, 'a') as f:
        for text in text_list:
            f.write(f'{text}\n')


def get_messengers_list() -> list:
    """Повертає список рядків які ввів користувач. Запит продовжується поки користувач не введе пусту строку(enter)."""
    text_list = []
    text = ' '
    while text != '':
        text = input('Введіть текс (Щоб закінчити натисніть Enter): ')
        text_list.append(text)
    return text_list


def main():
    save_file('messengers_user.txt', get_messengers_list())


if __name__ == '__main__':
    main()
