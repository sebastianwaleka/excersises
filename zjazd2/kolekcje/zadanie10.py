# Napisz program zliczający liczbę wystąpień każdego znaku w podanym przez użytkownika napisie.

words = dict()

text = input('Enter text: ')

for char in text.lower():
    # if char in words:
    #     words[char] += 1
    # else:
    #     words[char] = 1
    words[char] = words.get(char, 0) + 1

for item in words.items():
    if item[0] == ' ':
        print(f'Space appeared {item[1]} times.')
    else:
        print(f'Char > {item[0]} < appeared {item[1]} times.')
