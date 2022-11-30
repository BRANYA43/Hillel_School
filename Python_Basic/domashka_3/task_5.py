from random import randint

count = 3
number = 0
guess_number = randint(1, 10)


def get_input_number(message: str):
    ret = ''
    while not ret.isdigit():
        ret = input(message)
    return int(ret)


while count > 0:
    number = get_input_number('Введіть число від 1 до 10: ')
    if 0 < number < 11:

        if guess_number == number and count != 0:
            print(f'Вітаємо, Ви вгадали!')
            count = 0
        else:
            print('Ви не вгадали.')
            count -= 1
    else:
        print('Ви ввели число вне діпазону.')
