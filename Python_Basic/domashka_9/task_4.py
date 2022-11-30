"""Написати функцію яка замінить у тексті слово інше.
 Функція приймає 4 аргументи, початковий рядок, слово, що замінюється, нове слово, кількість замін, приклад:
 fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1) -> 'Marvel makes good movies, DC makes good comics'
 fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2) -> 'Marvel makes good movies, Marvel makes good comics'"""


def fake_string(text: str, old_word: str, new_word: str, n: int) -> str:
    return text.replace(old_word, new_word, n)


print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 2))
