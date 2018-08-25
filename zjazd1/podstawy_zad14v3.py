#Napisz program wyświetlający minimalną oraz maksymalną liczbę ze wszystkich liczb wprowadzonych przez użytkownika. Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią komendą. Zadbaj o obsłużenie przypadku, gdy użytkownik nie wprowadzi żadnej liczby.

min = max = None

while True:
    number = input('Enter number or end: ')
    if number == 'end':
        break
    else:
        try:
            number = int(number)
            if max is None or number > max:
                max = number
            if min is None or number < min:
                min = number
        except Exception:
            print('Wrong value.')

if max is not None:
    print(f'\nMax: {max}. Min: {min}')
print('END')