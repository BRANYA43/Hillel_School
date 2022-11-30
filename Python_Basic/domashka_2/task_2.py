number = ''

while not number.isdigit():
    number = input('Введіть ціле число: ')

number = int(number)
print(f'Наступне число пілся {number} є {number + 1}\n'
      f'Попереднє число перед {number} є {number - 1}')
