def fix_endings(name: str) -> str:
    """Додає правильне закінчення назві"""
    if name[-1] == 'о':
        ret = name + 'м'
    elif name[-1] in 'ауеиі':
        ret = name[:-1] + 'ом'
    else:
        ret = name + 'ом'
    return ret


class Product:
    """
    АТРИБУТИ:
        __type: str
            тип продукту
        __name_type_ua: str
            назва типу продукта українською мовою
        type: str
            тип продукту
        type_ua: str
            назва типу продукта українською мовою
        name: str
            назва продукту
        price: int
            вартість продукту. Не може бути від'ємним.
        count: int
            кількість продукту (за замовчуванням 5). Не може бути від'ємними
    """

    def __init__(self, _type: str, name_type_ua: str, name: str, price: int, count: int):
        self.__type = _type
        self.__name_type_ua = name_type_ua
        self.name = name
        self.price = price
        self.count = count

    def __str__(self):
        return '{}: {} Ціна: {} грн Кіл-ть: {} шт.'.format(self.__name_type_ua.capitalize(), self.name.capitalize(),
                                                           self.price, self.count)

    def __repr__(self):
        return f'{self.name}'

    @property
    def type(self):
        return self.__type

    @property
    def type_ua(self):
        return self.__name_type_ua


class Coffee(Product):
    """Клас Кави"""
    def __init__(self, name: str, price: int, count: int):
        super().__init__('coffee', 'кава', name, price, count)

    def __add__(self, other):
        """Створює новий об'єкт ґрунтуючись на двох інших об'єкта що додаються."""
        if type(other) is Additional:
            name = fix_endings(f'{self.name} з {other.name}')
            price = self.price + other.price
            self.count -= 1
            other.count -= 1
            return Coffee(name, price, 1)


class Tea(Product):
    """Клас Чаю"""
    def __init__(self, name: str, price: int, count: int):
        super().__init__('tea', 'чай', name, price, count)

    def __add__(self, other):
        """Створює новий об'єкт ґрунтуючись на двох інших об'єкта що додаються."""
        if type(other) is Additional:
            name = fix_endings(f'{self.name} з {other.name}')
            price = self.price + other.price
            self.count -= 1
            other.count -= 1
            return Tea(name, price, 1)


class Additional(Product):
    """Клас Додатку"""
    def __init__(self, name: str, price: int, count: int):
        super().__init__('additional', 'додаток', name, price, count)

    def __add__(self, other):
        return other.__add__(self)
