table = [[34587, 'Learning Python, Mark Lutz', 4, 40.95],
         [98762, 'Programming Python, Mark Lutz', 5, 56.80],
         [77226, 'Head First Python, Paul Barry', 3, 32.95],
         [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]]

print(list(map(lambda row: (row[0], round(row[2] * row[3], 2) + (10 if row[2] * row[3] < 100 else 0)), table)))
