"""Написати програму яка форматуватиме номер телефону до єдиного вигляду.
  На введення програма приймає рядок введеного телефонного номера, наприклад:
  063-999-99-99 повертає (+38) 063 999-99-99
  063 999-99-99 повертає (+38) 063 999-99-99
  063-99999-99 повертає (+38) 063 999-99-99
  +3806399-999-99 повертає (+38) 063 999-99-99
  380639999999 повертає (+38) 063 999-99-99
  Якщо щось не так із номером - пише 'Failed to recognize number'."""
import re


class FormatTelNum:
    """
    Клас Форматування номера телефону

    АТРИБУТИ:
        self.__PATTERN_TEL_NUM
            Шаблон пошуку номера телефона.

        self.__PATTERN_SUB
            Шаблон пошуку рисок та прогалин у номері.

        self.__PATTERN_FORMAT_TEL_NUM
            Шаблон пошуку групп у номері телефону.

    МЕТОДИ:
        def is_tel_num(self, num: str) -> bool:
            Перевіряє чи є валідним наданий номер телефону у різних видах його запису.

        def format_tel_num(self, num: str) -> str:
            Форматує номер телефону у вид (+38) 000 000-00-00.
    """
    __PATTERN_TEL_NUM = r'^(\+?38)?(\d{3})(\s?\-?\d\d\d?\s?\-?\d\s?\-?\d\s?\-?\d\s?\-?\d\d)$'
    __PATTERN_SUB = r'-|\s'
    __PATTERN_FORMAT_TEL_NUM = r'^(\+?38)?(\d{3})(\d{3})(\d\d)(\d\d)$'

    def is_tel_num(self, num: str) -> bool:
        """Перевіряє чи є валідним наданий номер телефону у різних видах його запису."""
        if re.search(self.__PATTERN_TEL_NUM, num) is None:
            return False
        return True

    def format_tel_num(self, num: str) -> str:
        """Форматує номер телефону у вид (+38) 000 000-00-00."""
        num = re.sub(self.__PATTERN_SUB, '', num)
        result = re.search(self.__PATTERN_FORMAT_TEL_NUM, num)
        return f'(+38) {result.group(2)} {result.group(3)}-{result.group(4)}-{result.group(5)}'


def client_code():
    tel_nums = ['063-999-99-99', '063 999-99-99', '063-99999-99', '+3806399-999-99', '380639999999', '23']
    format_tel = FormatTelNum()
    for num in tel_nums:
        if format_tel.is_tel_num(num):
            print(format_tel.format_tel_num(num))
        else:
            print('Не вдалося розпізнати номер')


if __name__ == '__main__':
    client_code()
