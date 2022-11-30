def print_stairs(start: int, end: int):
    some_str = ''
    for i in range(start, end + 1):
        some_str += str(i)
        print(some_str)


def main():
    print_stairs(1, 9)


if __name__ == '__main__':
    main()
