from random import randint

X_AXIS = tuple(str(elem) for elem in range(1, 9))
Y_AXIS = tuple(chr(elem) for elem in range(ord('A'), ord('A') + 8))

knight = {'x': 4,
          'y': 4}

list_coordinates = []

for i in range(2):
    list_coordinates.append({'x': randint(0, len(X_AXIS) - 1),
                             'y': randint(0, len(Y_AXIS) - 1)})

for elem in list_coordinates:
    x = abs(elem['x'] - knight['x'])
    y = abs(elem['y'] - knight['y'])

    if x == 2 and y == 1 or x == 1 and y == 2:
        print(f'Кінь с ({X_AXIS[knight["x"]]} {Y_AXIS[knight["y"]]}) може походить на'
              f' ({X_AXIS[elem["x"]]} {Y_AXIS[elem["y"]]}).')
    else:
        print(f'Кінь с ({X_AXIS[knight["x"]]} {Y_AXIS[knight["y"]]}) не може походить на'
              f' ({X_AXIS[elem["x"]]} {Y_AXIS[elem["y"]]}).')

