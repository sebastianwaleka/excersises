# Napisz program wypisujący liczby od 0 do 100, podzielne przez 3 lub 5.
# Wypisz także jak dużo takich liczb wystąpiło w tym przedziale.

list = list(range(101))
count = 0
print('Numbers divided by 3 or 5:')
for i in list:
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        count += 1
print(f'In range 0-100 there is {count} numbers divided by 3 or 5.')
