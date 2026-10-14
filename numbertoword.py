phone_number = (input('Phone: '))

words = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'
}
output = ''
for number in phone_number:
    output += words.get(number, '!') + ' '

print(output)



