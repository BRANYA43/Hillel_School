"""Пароль, що вводиться користувачем, повинен відповідати вимогам,
  1. Як мінімум 1 символ від a-z
  2. Як мінімум 1 символ від A-Z
  3. Щонайменше 1 символ від 0-9
  4. Як мінімум 1 символ із $#@-+=
  5. Мінімальна довжина пароля 8 символів.
  Програма приймає на введення рядок, якщо пароль неправильний - пише якій вимогі не відповідає і запитує знову, якщо правильний - пише 'Password is correct'."""
import re


class ValidityPassword:
    """
    Клас Валідності паролю

    Робить перевірки наданого паролю, якщо не виконані вимоги, то повідомляє які саме вимоги не були виконані.

    АТРИБУТИ:
        __PATTERN_PASSWORD: str
            Шаблон пошуку паролю.

        __PATTERN_NUMBER: str
            Шаблон пошуку цифри.

        __PATTERN_UPPER_LETTER: str
            Шаблон пошуку літери верхнього регістру.

        __PATTERN_LOWER_LETTER: str
            Шаблон пошуку літери нижнього регістру.

        __PATTERN_SYMBOL: str
            Шаблон пошуку символу: @, #, $, -, +, =.

        __PATTERN_CORRECT_LENGTH: str
            Шаблон пошуку мінімум 8 символів.


    МЕТОДИ:
        def check_requirements(password: str) -> str:
            Використовує усі перевірки які вимагає шаблон паролю, та повертає повідомлення що до вимог пароля.

    """
    __PATTERN_PASSWORD = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$-+=])[a-zA-Z\d@#$-+=]{8,}$'
    __PATTERN_NUMBER = r'\d'
    __PATTERN_UPPER_LETTER = r'[A-Z]'
    __PATTERN_LOWER_LETTER = r'[a-z]'
    __PATTERN_SYMBOL = r'[@#$-+=]'
    __PATTERN_CORRECT_LENGTH = r'.{8,}'

    def check_requirements(self, password: str) -> str:
        """Використовує усі перевірки які вимагає шаблон паролю, та повертає повідомлення що до вимог пароля."""
        error = {
            self.__PATTERN_NUMBER: 'Повинна бути мінімум одна цифра.\n',
            self.__PATTERN_UPPER_LETTER: 'Повинна бути мінімум 1 літера у верхньому регістрі.\n',
            self.__PATTERN_LOWER_LETTER: 'Повинна бути мінімум 1 літера у нижньому регістрі.\n',
            self.__PATTERN_SYMBOL: 'Повинен бути мінімум 1 один символів: @, #, $, -, +, =.\n',
            self.__PATTERN_CORRECT_LENGTH: 'Довжина пароля повинна бути мінімум 8 символів.\n'
        }
        ret_msg = ''
        if re.search(self.__PATTERN_PASSWORD, password) is None:
            for pattern, msg in error.items():
                if re.search(pattern, password) is None:
                    ret_msg += msg
            return ret_msg

        return 'Пароль є коректним'


def client_code():
    msg = ''
    count = 0
    validity = ValidityPassword()
    while msg != 'Пароль є коректним' and count != 3:
        password = input('Введіть пароль: ')
        msg = validity.check_requirements(password)
        if count == 3:
            print('Кіл-ть спроб закінчилась.')
        count += 1
        print(msg)


if __name__ == '__main__':
    client_code()
