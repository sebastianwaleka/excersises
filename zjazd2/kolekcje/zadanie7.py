# Napisz program zliczający liczbę samogłosek (a, e, i, o, u, y) w podanym przez użytkownika napisie.

word = input('Enter text: ')
count = 0
VOWEL = 'aeiouy'  # po ang. samogłoski
for w in word:
    if w.lower() in VOWEL: # or w in VOWEL.upper(): po dodaniu .lower() nie trzeba szukać wielkich liter
        count += 1
print(f'Number of vowels in text "{word}" is: {count}.')
