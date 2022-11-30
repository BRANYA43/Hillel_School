"""Написати функцію яка частково приховуватиме e-mail, приклад:
 hide_email(somebody_email@gmail.com) -> em***@**il.com"""


def hide_email(email: str) -> str:
    first, second = email.split('@')
    return f'{first[-5:-3]}***@**{second[3:]}'


print(hide_email("somebody_email@gmail.com"))
