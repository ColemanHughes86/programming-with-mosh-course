numbers = [12, 4, 66, 32, 23, 8, 12, 16, 48, 22, 45]
max = numbers[0]

for count in numbers:
    if max < count:
        max = count

print(max)