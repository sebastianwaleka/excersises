#Napisz program wyświetlający minimalną oraz maksymalną liczbę ze wszystkich liczb wprowadzonych przez użytkownika. Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią komendą. Zadbaj o obsłużenie przypadku, gdy użytkownik nie wprowadzi żadnej liczby.


max = float('-Inf')
min = float('Inf')

while True:
    number = input('Enter number or end: ')
    if number == 'end':
        break
    else:
        try:
            number = int(number)
        except Exception:
            print('Wrong value.')
            continue
        if number > max:
            max = number
        if number < min:
            min = number
    
if max != float('-Inf'):
    print(f'\nMax: {max}. Min: {min}')
print('END')