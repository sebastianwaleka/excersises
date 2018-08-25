# Program ma pytać użytkownika o kolejne liczby całkowite.
# Może być ich dowolnie wiele, a żeby zakończyć podawanie liczby, użytkownik podaje tekst 'koniec'.
# Na końcu program podaje sumę wpisanych liczb.

sum = 0
i = 0

while True:
    num = input('Enter number: ')
    if num == 'end':
        break
    else:
        try:
            sum += int(num)
            i += 1
        except:
            print('Enter number or "end"')
            continue
if i > 0:   
    print(f'Sum of given numbers: {sum}. Number of numbers: {i}, average: {sum/i}.')