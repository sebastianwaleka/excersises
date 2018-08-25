#Napisz program wyświetlający minimalną oraz maksymalną liczbę ze wszystkich liczb wprowadzonych przez użytkownika. Daj użytkownikowi możliwość zakończenia wprowadzania liczb odpowiednią komendą. Zadbaj o obsłużenie przypadku, gdy użytkownik nie wprowadzi żadnej liczby.

#numbers = list()
#maxi = 0
#mini = 0
i = 0
while True:
    try:
        number = int(input('\nEnter number: '))
    except Exception:
        print('Enter number please.')
        continue
    #numbers.append(number)
    if i == 0:
        maxi = number
        mini = number
        i += 1
    else:
        if number > maxi:
            maxi = number
        if number < mini:
            mini = number
    choice = input('Continue? [Y/N] ')
    if choice == 'N' or choice == 'n':
        break
    elif choice != 'Y' and choice != 'y':
        print('Please, enter Y or N')
        #continue

print(f'\nMaksymalna z podanych liczb to: {maxi}. Minimalna: {mini}')
print('Koniec')