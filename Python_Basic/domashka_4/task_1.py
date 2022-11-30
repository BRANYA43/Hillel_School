def get_input_number(message: str) -> int:
    ret = ''
    while not ret.isdigit():
        ret = input(message)
    return int(ret)


def get_count_day(some_distance: int, some_search_distance: int, some_increase: float) -> int:
    count = 0
    while some_distance < some_search_distance:
        some_distance *= some_increase
        count += 1
    return count


def main():
    INCREASE = 1.1
    distance = get_input_number('Введіть число скільки пробіг в перший день спортсмен (км): ')
    search_distance = get_input_number('Введіть число скільки повинен пробігти спортсмен (км): ')
    count_day = get_count_day(distance, search_distance, INCREASE)

    print(f'Спортсмен досяг відмітки {search_distance}(км) у {count_day + 1} день.')


if __name__ == '__main__':
    main()
