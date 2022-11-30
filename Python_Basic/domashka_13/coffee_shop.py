"""Написати програму кавовий магазин.
Об'єкти:
  Product
  - тип може бути тільки coffee, tea, або additional (не можна створити об'єкт з іншим типом)
  - властивості: найменування, тип, ціна
  - print об'єкта продукту повинен повертати "Кава: Еспресо, ціна: 27грн."

  Store
  - може імпортувати продукти із файлу invertory.csv
  (за замовчуванням по 5 шт. кожного найменування, або вказану кількість)
  - може повернути список продуктів потрібного типу (tea, coffee чи всі продукти)
  - може повернути загальну вартість продуктів
  - може продати продукт

* Зробити можливість поєднання типів Espresso та Молоко, у підсумку повинно повернути об'єкт Latte """
import csv

from tabulate import tabulate

from products import Coffee, Tea, Additional


class Store:
    """
    АТРИБУТИ:
        __inventory: dict
            інвентар товарів магазину
        __cash: int
            заробіток за продаж продуктів
        __sold: int
            продано продуктів
        name: str
            назва магазину

    МЕТОДИ:
        def add(type: str, name: str, price: int, count: int):
            Додає товар у словник за назвою або додає кількість до вже існуючого у словнику товару.

        def sell(name: str, count: int):
            Продає товар за назвою.

        def set(name: str, count: int):
            Змінює назву або вартість продукту.

        def show(name: str):
            Показує таблицю товарів, відсортовану таблицю товарів за типом, вартість всіх товарів, кількість всіх товарів,
            кількість зароблених грошей, кількість проданого товару.

        def mix(product1: str, product2: str)
            Створює новий товар об'єднанням двох інших товарів.

        def export_inventory()
            Збереження таблиці товарів у файл

        def __import_inventory():
            Завантажує товари з файл формату csv у інвентар у магазин.

        def create_tab_for_save():
            Створює таблицю для збереження у файл

        def _name_validity(name: str) -> bool:
            Перевіряє чи є товар у інвентарі.
            Якщо немає, то повертає False та друкує - Товара з назвою name не має.

        def _type_validity(_type: str) -> bool:
            Перевіряє чи є тип товару.
            Якщо немає, то повертає False та друкує - Товара з типом _type не має.

        def _count_validity(count: int) -> bool:
            Перевіряє чи є count цілим та не від'ємним числом.
            Якщо ні, то повертає False та друкує - Кіл-ть повинна бути цілим не від'ємним числом.

        def _is_count_in_product(name: str, count: int) -> bool:
            Перевіряє чи дорівнює різниця count та кіл-ть товару нулю.
            Якщо так то повертає False та друкує - Товару з назвою name не вистачає.

        def _price_validity(price: int) -> bool:
            Перевіряє чи є price цілим або дробним не від'ємним та не нульовим числом.
            Якщо ні ,то повертає False та друкує - Ціна повинна бути цілим або дробовим не від\'ємним та
            не нульовим числом.

        def _is_additional(name: str) -> bool:
            Перевіряє чи є товар у інвентарі.
            Якщо ні, то повертає False.

        def _operation_validity(operation: str, operations: dict) -> bool:
            Перевіряє чи є operation у словнику operations.
            Якщо ні, то повертає False та друкує - Операція operation не існує.

        def _get_tab() -> str:
            Повертає таблицю товарів.

        def _get_tab_sort(_type: str) -> str:
            Повертає  відсортовану таблицю товарів.

        def _get_full_price() -> str:
            Повертає вартість усіх товарів.

        def _get_full_item() -> str:
            Повертає кількість усіх товарів.

        def _get_cash() -> str:
            Повертає заробіток магазину за весь час.

        def _get_sold() -> str:
            Повертає кількість проданих товарів за весь час.

        def _set_name(name: str new_name: str):
            Перейменовує назву товару.

        def _set_price(name: str new_price: int):
            Змінює вартість товару

    ПОМИЛКИ:
        def add()
            Товара з назвою name не має.
            Товара з типом _type не має.
            Кіл-ть повинна бути цілим не від\'ємним числом.
            Ціна повинна бути цілим або дробовим не від\'ємним та не нульовим числом.

        def sell()
            Товара з ім'ям name не має
            Кіл-ть повинна бути цілим не від\'ємним числом.

        def mix()
            Товара з ім'ям name не має
            Кіл-ть повинна бути цілим не від\'ємним числом.
            Товару з назвою name не вистачає.
            Один з товарів повинен бути з типом Additional(Додаток)

        def set()
            Товара з ім'ям name не має
            Нова назва повинна бути строкою.
            Ціна повинна бути цілим або дробовим не від\'ємним та не нульовим числом.
            Операція operation не існує.

        def show()
            Операція operation не існує.
            Товара з типом _type не має
    """
    products = {
        'coffee': Coffee,
        'tea': Tea,
        'additional': Additional
    }

    def __init__(self, name: str):
        self.name = name
        self.__inventory = {}
        self.__cash = 0
        self.__sold = 0
        self.__import_inventory()

    def add(self, name: str, count: int, price=1, _type='default'):
        """Створює та додає товар в інвентар магазину. Якщо товар вже є в інвентарі додає тільки кількість."""
        type_validity = self._type_validity(_type)
        count_validity = self._count_validity(count)
        price_validity = self._price_validity(price)

        if name not in self.__inventory and type_validity and count_validity and price_validity:
            self.__inventory[name] = self.products[_type](name, price, count)
        elif self._name_validity(name) and count_validity:
            self.__inventory[name].count += count

    def sell(self, name: str, count: int):
        """Продає товар з інвентаря. Також додає у __cash гроші за товар, а у __sold кіл-ть проданого товару."""
        if self._is_count_in_product(name, count):
            self.__inventory[name].count -= count
            self.__cash += self.__inventory[name].price * count
            self.__sold += count

    def mix(self, name1: str, name2: str, count=1):
        """Створює новий товар об'єднанням товару з типом Additional та іншим товаром."""
        if self._is_additional(name1) or self._is_additional(name2):
            if self._is_count_in_product(name1, count) and self._is_count_in_product(name2, count):
                product = self.__inventory[name1] + self.__inventory[name2]
                self.__inventory[name1].count -= count - 1
                self.__inventory[name2].count -= count - 1
                self.add(product.name, count, product.price, product.type)
        else:
            print('Один з товарів повинен бути з типом Додаток')

    def set(self, name: str, operation: str, value: str | int):
        """Змінює назву або вартість товару.

        Операції: reprice, rename
        """
        operations = {
            'reprice': self._set_price,
            'rename': self._set_name
        }
        if self._operation_validity(operation, operations):
            operations[operation](name, value)

    def show(self, operation, _type='default'):
        """Показує таблицю товарів, відсортовану таблицю товарів за типом, вартість всіх товарів, кількість всіх товарів,
        кількість зароблених грошей, кількість проданого товару.

        Операції: tab, tab_sort, full price, full item, cash, sold
        """
        operations = {
            'tab': self._get_tab,
            'tab sort': self._get_tab_sort,
            'full price': self._get_full_price,
            'full item': self._get_full_item,
            'cash': self._get_cash,
            'sold': self._get_sold,
        }
        is_operation = self._operation_validity(operation, operations)
        type_is_product = self._type_validity(_type)
        if is_operation and type_is_product:
            if _type == 'default':
                print(operations[operation]())
            else:
                print(operations[operation](_type))

    def _name_validity(self, name: str) -> bool:
        """Перевіряє чи є товар у інвентарі.
        Якщо немає, то повертає False та друкує - Товара з назвою name не має.
        """
        if name not in self.__inventory:
            print(f'Товару з назвою {name.upper()} не має.')
            return False
        return True

    def _type_validity(self, _type: str) -> bool:
        """Перевіряє чи є тип товару.
        Якщо немає, то повертає False та друкує - Товара з типом _type не має.
        """
        if _type not in self.products and _type != 'default':
            print(f'Товару з типом {_type.upper()} не має.')
            return False
        return True

    @staticmethod
    def _count_validity(count: int) -> bool:
        """Перевіряє чи є count цілим та не від'ємним числом.
        Якщо ні, то повертає False та друкує - Кіл-ть повинна бути цілим не від'ємним числом.
        """
        if count < 0 or type(count) is not int:
            print(f'Кіл-ть повинна бути цілим не від\'ємним числом.')
            return False
        return True

    def _is_count_in_product(self, name: str, count: int) -> bool:
        """Перевіряє чи дорівнює різниця count та кіл-ть товару нулю.
        Якщо так, то повертає False та друкує - Товару з назвою name не вистачає.
        """
        name_is_inventory = self._name_validity(name)
        is_count = self._count_validity(count)
        if self.__inventory[name].count - count < 0 and name_is_inventory and is_count:
            print(f'Товару з назвою {name.upper()} не вистачає.')
            return False
        return True

    @staticmethod
    def _price_validity(price: int) -> bool:
        """Перевіряє чи є price цілим або дробним не від'ємним та не нульовим числом.
        Якщо ні, то повертає False та друкує - Ціна повинна бути цілим або дробовим не від\'ємним та не нульовим числом.
        """
        if price <= 0 or type(price) is not int and type(price) is not float:
            print(f'Ціна повинна бути цілим або дробовим не від\'ємним та не нульовим числом.')
            return False
        return True

    def _is_additional(self, name: str) -> bool:
        """Перевіряє чи є товар у інвентарі.
        Якщо ні, то повертає False.
        """
        if type(self.__inventory[name]) is not Additional and self._name_validity(name):
            return False
        return True

    @staticmethod
    def _operation_validity(operation: str, operations: dict) -> bool:
        """Перевіряє чи є operation у словнику operations.
        Якщо ні, то повертає False та друкує - Операція operation не існує."""
        if operation not in operations:
            print(f'Операція {operation} не існує.')
            return False
        return True

    def create_tab_for_save(self):
        """Створює таблицю для запису у файл"""
        tab = []
        for _, product in self.__inventory.items():
            tab.append({'Назва': product.name, 'Тип': product.type,  'Ціна': product.price,
                        'Кількість': product.count})
        return tab

    def _get_tab(self) -> str:
        """Повертає таблицю товарів."""
        tab = []
        for _, product in self.__inventory.items():
            tab.append({'Тип': product.type_ua, 'Назва': product.name.capitalize(), 'Ціна': product.price, '': 'грн.',
                        'Кіл-ть': product.count, ' ': 'шт.'})
        return tabulate(tab, headers='keys', tablefmt="psql")

    def _get_tab_sort(self, _type: str) -> str:
        """Повертає  відсортовану таблицю товарів."""
        tab = []
        for _, product in self.__inventory.items():
            if product.type == _type:
                tab.append({'Тип': product.type_ua, 'Назва': product.name.capitalize(), 'Ціна': product.price,
                            '': 'грн.', 'Кіл-ть': product.count, ' ': 'шт.'})
        return tabulate(tab, headers='keys', tablefmt="psql")

    def _get_full_price(self) -> str:
        """Повертає вартість усіх товарів."""
        return 'Вартість всіх товарів: {} грн'.format(sum(product.price for _, product in self.__inventory.items()))

    def _get_full_item(self) -> str:
        """Повертає кількість усіх товарів."""
        return 'Кількість всіх товарів: {} шт.'.format(sum(product.count for _, product in self.__inventory.items()))

    def _get_cash(self) -> str:
        """Повертає заробіток магазину за весь час."""
        return f'Зароблено грошей: {self.__cash} грн'

    def _get_sold(self) -> str:
        """Повертає кількість проданих товарів за весь час."""
        return f'Продано товару: {self.__sold} шт.'

    def _set_price(self, name: str, new_price: int):
        """Перейменовує назву товару."""
        if self._price_validity(new_price):
            self.__inventory[name].price = new_price

    def _set_name(self, name: str, new_name: str):
        """Змінює вартість товару"""
        if self._name_validity(name) or type(new_name) is not str and not new_name.isdigit():
            self.__inventory[name].name, self.__inventory[new_name] = new_name, self.__inventory[name]
            del self.__inventory[name]
        else:
            print('Нова назва повинна бути строкою.')

    def __import_inventory(self):
        """Завантажує товари з inventory.csv у інвентар магазину"""
        try:
            with open('inventory.csv', 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for r in reader:
                    if not r['Кількість'].isdigit():
                        r['Кількість'] = 5
                    if r['Назва'] is not None and r['Тип'] is not None and r['Ціна'].isdigit():
                        self.add(r['Назва'], int(r['Кількість']), int(r['Ціна']), r['Тип'])
        except FileNotFoundError:
            print('Файлу не знайдено.')

    def export_inventory(self):
        with open('inventory.csv', 'w', encoding='utf-8', newline='') as f:
            tab = self.create_tab_for_save()
            writer = csv.DictWriter(f, fieldnames=tab[0].keys())
            writer.writeheader()
            for row in tab:
                writer.writerow(row)


if __name__ == '__main__':
    shop = Store('каварня')
    shop.show('tab')
    shop.add('Молоко', 20)
    shop.add('Лате', 20)
    shop.sell('Імбирний чай', 5)
    shop.sell('Імбирний чай', 10)
    shop.set('Зелений чай', 'rename', 'Салатовий чай')
    shop.set('Салатовий чай', 'reprice', 65)
    shop.mix('Лате', 'Молоко')
    shop.mix('Лате', 'Молоко', 5)
    shop.mix('Коньяк', 'Лате')
    shop.show('tab')
    shop.show('tab sort', 'coffee')
    shop.show('full price')
    shop.show('full item')
    shop.show('cash')
    shop.show('sold')
    shop.export_inventory()
