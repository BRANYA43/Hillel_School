table = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
         [98762, 'Programming Python, Mark Lutz', 5, 56.80],
         [77226, 'Head First Python, Paul Barry', 3, 32.95],
         [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

print(list(map(lambda row: tuple(round(item + 10, 2) if type(item) is float and item < 100 else item for item in row), table)))
