"""Написати функцію яка поверне найдовше слово у рядку:
longest_word("What makes a good man") -> makes"""


def longest_word(text: str) -> str:
    return max(text.split(), key=len)


print(longest_word("What makes a good man"))
