imiona = ['Robert', 'Kamil', 'Piotrek', 'Karolina']

print(type(imiona))
print(imiona)
print(len(imiona))

print('Robert' in imiona)
print('Rafał' in imiona)

for imie in imiona:
    print(imie)

print(imiona[2])

print(imiona)
imiona.append('Rafał')
print(imiona)
print(imiona.pop())
print(imiona)
imiona.append('Kamil')
print(imiona)
imiona.remove('Kamil')
print(imiona)
