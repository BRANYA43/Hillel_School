"""Написати функцію, яка визначить, чи є введений текст паліндромом
(той який читається однаково з будь-якого боку), приклад:
Шалаш, зараз, Дід, Піп, 13231
Паліндром — і ні морд, ні лап"""
from string import punctuation


def delete_punctuation(text: str) -> str:
    """Видаляє пунктуацію з заданого тексту"""
    for symbol in text:
        if symbol in punctuation:
            text = text.replace(symbol, '')
    return text


def is_palindrome(text: str) -> bool:
    """Перевіряє чи є заданний текст паліндромо. Не враховуе пунктуацію, прогалини та регістр літер."""
    text = delete_punctuation(text.lower().replace(' ', ''))
    if text == text[::-1]:
        return True
    else:
        return False


def main():
    print(is_palindrome('ШаЛаШ'))
    print(is_palindrome('Паліндром - і ні морд, ні лап'))


if __name__ == '__main__':
    main()
