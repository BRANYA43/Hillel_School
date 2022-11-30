from task_1 import get_input_number


def get_sequence_numbers(sequence: list, a: int, b: int):
    if a <= b:
        while a <= b:
            sequence.append(a)
            a += 1
    else:
        while a >= b:
            sequence.append(a)
            a -= 1


def main():
    sequence_numbers = []
    a = get_input_number(f'Введіть число a: ')
    b = get_input_number(f'Введіть число b: ')
    get_sequence_numbers(sequence_numbers, a, b)
    print(sequence_numbers)


if __name__ == '__main__':
    main()
