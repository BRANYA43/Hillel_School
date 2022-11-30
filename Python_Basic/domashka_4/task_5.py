def get_alphabet() -> str:
    ret = ''
    for elem in range(ord('A'), ord('Z') + 1):
        ret += chr(elem)
    return ret


def main():
    alphabet = get_alphabet()
    print(alphabet)
    print(f'Третій символ: {alphabet[2]}')
    print(f'Предостаній символ: {alphabet[-2]}')
    print(f"Перші п'ять символів: {alphabet[0:5]}")
    print(f'Весь рядок крім двох останіх символів: {alphabet[0:-2]}')
    print(f'Символи з парними індексами: {alphabet[0::2]}')
    print(f'Символи з не парними індексами: {alphabet[1::2]}')
    print(f'Перевернутий рядок: {alphabet[::-1]}')
    print(f'Перевернутий рядок з кожним другим симоволом: {alphabet[-1::-2]}')
    print(f'Довжина рядка: {len(alphabet)}')


if __name__ == '__main__':
    main()