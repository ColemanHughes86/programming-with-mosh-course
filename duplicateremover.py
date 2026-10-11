list = [1, 3, 5, 7, 9, 9, 6, 3, 5, 2, 1]
uniques = []
for number in list:
    if number not in uniques:
        uniques.append(number)

uniques.sort()
print(uniques)