"""Формат українських номерів: ВН1010НС чи АА1010АА
  На введення програма отримує рядок, у відповідь має повернути чи є рядок автомобільним номером чи ні.
  * Дод. Повинна повернути регіон (має знати регіони 2004 та 2013 рр.)
      Повинна однаково сприймати AI – англійський та АІ – український варіанти.
      (Для BI, AI, IA і т.д.)"""
import re
import csv


class ValidityCarNumber:
    """
    Клас Валідності номеру авто

    АТРИБУТИ:
        self.__bd_code_region: dict
            База даних регіонів та їх кодів.

        self.__PATTERN_CAR_NUMBER: str
            Шаблон пошуку номера.
        self.__LATIN_TO_CYRILLIC: dict
            Словник для переводу латиниці у кирилицю.

    МЕТОДИ:
        def get_info(car_number: str) -> str:
            Повертає інформацію о номері авто.

        def is_car_number(car_number: str) -> bool:
            Перевіряє чи є номер авто у потрібному форматі.

    КЛАСОВІ МЕТОДИ:

        def translated_code_in_ua(self, car_number: str) -> str:
            Перевіряє чи є у номері авто латиниця, якщо так, то переводить її у кирилицю та звмінює їх у номері авто.
            Після повертає номер авто.

        def get_name_region(self, car_number: str) -> str:
            Шукає у базі даних, за кодом номера авто, регіону реєстрації та повертає його.

        def import_bd_code_region(self):
            Імпортує з ua_auto.cvs базу даних регіонів та їх кодів.
    """
    __PATTERN_CAR_NUMBER = r'^[ABCEHIKMOPTX|АВСЕНІКМОРТХ]{2}\d{4}[ABCEHIKMOPTX|АВСЕНІКМОРТХ]{2}$'
    __LATIN_TO_CYRILLIC = {'A': 'А', 'B': 'В', 'C': 'С', 'E': 'Е', 'H': 'Н', 'I': 'І', 'K': 'К', 'M': 'М', 'O': 'О',
                           'P': 'Р', 'T': 'Т', 'X': 'Х'}

    def __init__(self):
        __bd_code_region = {}
        self.__import_bd_code_region()

    def get_info(self, car_number: str) -> str:
        """Повертає інформацію о номері авто."""
        return f'Номер авто: {car_number}\n' \
               f'Регіон реєстрації: {self._get_name_region(car_number)}'

    def is_car_number(self, car_number: str) -> bool:
        """Перевіряє чи є номер авто у потрібному форматі."""
        if re.search(self.__PATTERN_CAR_NUMBER, car_number) is None:
            return False
        return True

    def _translated_code_in_ua(self, car_number: str) -> str:
        """Перевіряє чи є у номері авто латиниця, якщо так, то переводить її у кирилицю та звмінює їх у номері авто.
        Після повертає номер авто.
        """
        code_ua = ''
        code_en = car_number[:2]
        number = car_number[2:7]
        for letter in code_en:
            if ord('A') <= ord(letter) <= ord('X'):
                code_ua += self.__LATIN_TO_CYRILLIC[letter]
            else:
                code_ua += letter
        return code_ua[:2] + number + car_number[-2:]

    def _get_name_region(self, car_number: str) -> str:
        """Шукає у базі даних, за кодом номера авто, регіону реєстрації та повертає його."""
        car_number = self._translated_code_in_ua(car_number)
        for region, code in self.__bd_code_region.items():
            if car_number[:2] in code:
                return region
        return 'None'

    def __import_bd_code_region(self):
        """Імпортує з ua_auto.cvs базу даних регіонів та їх кодів."""
        with open('ua_auto.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                self.__bd_code_region[r['Регіон']] = [r['Код 2004'], r['Код 2013']]


def client_code():
    car_number = input('Введіть номер авто: ')
    validity = ValidityCarNumber()
    if validity.is_car_number(car_number):
        print(validity.get_info(car_number))
    else:
        print('Невірний номер.')


if __name__ == '__main__':
    client_code()
