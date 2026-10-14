text = input('>')

list = text.split(' ')

emoji_converter = {
    ':(': '😟',
    ':)': '😃'
}

output = ''

for word in list:
    output += emoji_converter.get(word, word) + ' '

print(output)
