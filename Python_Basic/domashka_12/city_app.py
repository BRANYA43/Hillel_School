"""Написати програму Місто.

   У міста є вулиці та будинки та можливості їх додавати та видаляти.
   Вулиці можуть умістити випадкову кількість будинків від 5 до 20.
   Будинки можуть мати випадкову кількість населення від 1 до 100 осіб.
   Має бути можливість заповнити місто одним методом.
   У міста має бути атрибут, який поверне кількість населення.
   А також метод для друкування таблиці:

   Вулиця Будинок Населення
   1 1 5
   1 2 10
   1 3 25
   2 1 22
   ..."""
from random import randint

from tabulate import tabulate


class House:
    """Class House"""
    def __init__(self, number: int):
        """Initializes house number and count residents."""
        self.__number = number
        self.count_residents = randint(1, 100)

    @property
    def number(self):
        return self.__number


class Street:
    """Class Street"""

    def __init__(self, name: str):
        """Initializes street name, count houses, and dictionary of houses objects."""
        self.name = name
        self.__count_house = randint(5, 21)
        self.__houses = {i + 1: House(i + 1) for i in range(self.__count_house)}

    @property
    def population(self) -> int:
        """Amount residents of the street."""
        return sum(house.count_residents for _, house in self.__houses.items())

    @property
    def houses(self) -> list:
        """List of homes."""
        return [house for house in self.__houses]

    @property
    def count_residents_houses(self) -> dict:
        """Dictionary of houses, and the count residents of houses."""
        return {number: house.count_residents for number, house in self.__houses.items()}

    def add_house(self):
        """Add house by last number."""
        self.__houses[max(self.__houses) + 1] = House(max(self.__houses) + 1)
        self.__count_house += 1

    def delete_house(self, number: int):
        """Delete house by number. If there is no house in the dictionary, it gives an error."""
        if 0 < number <= len(self.__houses):
            del self.__houses[number]
            self.__count_house -= 1
        else:
            print(f'Home {number} is not on street {self.name.capitalize()}.')


class City:
    """Class of the city"""
    street_names = [
        'гавнокод',
        'чистокод',
        'тижпрограміст',
    ]

    def __init__(self, name):
        """Initializes name city and the dictionary of street objects."""
        self.name = name
        self.__streets = {}

    @property
    def population(self) -> int:
        """City population."""
        return sum(street.population for _, street in self.__streets.items())

    @property
    def streets(self) -> list:
        """List of streets."""
        return [street for street in self.__streets.keys()]

    @property
    def houses_on_street(self) -> dict:
        """Dictionary of streets and list of houses on the street."""
        return {name_street: street.houses for name_street, street in self.__streets.items()}

    def create_tab(self) -> list:
        """Creates a table of streets, houses and residents."""
        tab = []
        for name_street, street in self.__streets.items():
            for house, count_people in street.count_residents_houses.items():
                tab.append({'street': name_street.capitalize(), 'house': house, 'resident': count_people})
        return tab

    def tab(self):
        """Outputs table of streets, houses, and the count residents in console."""
        print(tabulate(self.create_tab(), headers='keys'))

    def add_house(self, name: str, number_houses: int):
        """Adds house/houses to the street."""
        for i in range(number_houses):
            self.__streets[name].add_house()

    def delete_house(self, name: str, *args_number: int):
        """Deletes house/houses from the street. If there is no house in the dictionary, it gives an error."""
        for number in args_number:
            self.__streets[name].delete_house(number)

    def add_street(self, *args_name: str):
        """Deletes the house/houses from the street."""
        for name in args_name:
            self.__streets[name] = Street(name)

    def delete_street(self, *args_name: str):
        """Deletes street/streets from a city. If there is no street in the dictionary, it gives an error."""
        for name in args_name:
            if name in self.__streets:
                del self.__streets[name]
            else:
                print(f'Streets {name.capitalize()} not in city {self.name.capitalize()}.')

    def fill_city(self):
        """Fills the city with streets whose names takes from list."""
        for name in self.street_names:
            self.add_street(name)


def main():
    kharkiv = City('харків')
    kharkiv.fill_city()
    print(kharkiv.streets)
    kharkiv.delete_street('гавнокод', 'тижпрограміст')
    kharkiv.add_street('антонівка', 'пітонівська')
    print(kharkiv.streets)
    print(kharkiv.houses_on_street)
    kharkiv.delete_house('пітонівська', 1, 2, 5)
    kharkiv.add_house('пітонівська', 10)
    print(kharkiv.houses_on_street)
    kharkiv.tab()
    print(kharkiv.population)


if __name__ == '__main__':
    main()
