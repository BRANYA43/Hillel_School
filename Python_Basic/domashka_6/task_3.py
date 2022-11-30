"""Дано перелік значень. Повернути словник, де кожен ключ - це індекс листа,
  а значення листа – це значення ключа:
  Input:
    ['a', 'b', 'c', 'd', 'e']
  Output
  {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}"""

letters = ['a', 'b', 'c', 'd', 'e']
letters_dict = {key: item for key, item in enumerate(letters)}
print(letters_dict)
