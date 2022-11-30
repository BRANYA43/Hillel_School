year = ''

while not year.isdigit():
    year = input('Введіть рік: ')

year = int(year)

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'{year} рік є високосним.')
else:
    print(f'{year} рік не є високосним.')
