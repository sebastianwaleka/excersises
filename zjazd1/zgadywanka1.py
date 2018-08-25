# 'Program sprawdzający znajomość tabliczki mnożenia'
# Program losuje 2 liczby i pyta użytkownika 'Ile wynosi iloczyn tych liczb'.
# Użytkownik wprowadza odpowiedź, a program sprawdza jej poprawność.
# Odpowiadamy tak długo, aż trafimy. Na koniec program wypisuje gratulacje oraz informację, w której próbie udało się trafić.

from random import randint

RANGE = 10

x = randint(1, RANGE)
y = randint(1, RANGE)
i = 1

print('\n' + '#'*10 + ' Program starts! ' + '#'*10)

while True:
    try:
        result = int(input(f'\nHow much is the multiplication of {x} and {y}? '))
    except:
        print('Enter number please.')
        continue
    if result == x * y:
        print('\nGood job! You get the right result!')
        break
    else:
        print('\nTry again.')
        i += 1       

print(f'It took you {i} times to get the right answer.\n')

print('#'*10 + ' Program ends! ' + '#'*10)