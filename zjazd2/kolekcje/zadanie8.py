# Napisz program zliczający liczbę znaków w podanym przez użytkownika napisnie pomiędzy nawiasami <>.
# Nawiasy mogą wystąpić tylko raz.
#
# Ala ma <kota>, a kot ma Alę.
# 4

text = 'Ala ma <kota>, a kot ma Alę'
# print(text)
# start = text.find('<')
# end = text.find('>')
#
# print(len(text[start+1:end]))

# używając pętli
print(text)
count = 0
between_brackets = False
for char in text:
    if char == '<':
         between_brackets = True
    elif char == '>':
        break
    elif between_brackets:
        count += 1

print(count)