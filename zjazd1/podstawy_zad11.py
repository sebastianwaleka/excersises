#Napisz program, który na podstawie pozycji gracza (x, y) na planszy w przedziale od 0 do 100 wyświetli jego przybliżone położenie (centrum, prawy górny róg, górna krawędź, ...) lub informację o pozycji poza planszą. Przyjmij wartość 10 jako margines krawędzi.
#
# Przykładowy komunikat programu:
# Podaj pozycję gracza X: 95
# Podaj pozycję gracza Y: 95
#
# Gracz znajduje się w prawym górnym rogu.

#W PORÓWNANIU DO INNYCH ROZWIĄZAŃ, TO NIE JEST ZBYT OPTYMLNE. JEST ZA DŁUGIE!

def pozycja(X, Y):
    if Y in range(0,10):
        if X in range(0,10):
            return 'lewy dolny róg'
        elif X in range(10, 91):
            return 'dolny margines'
        else:
            if X > 101 or X < 0:
                return 'poza planszą'
            else:
                return 'prawy dolny róg'
    elif Y in range(10, 91):
        if X in range(0, 10):
            return 'lewy margines'
        elif X in range(10, 91):
            return 'centrum'
        else:
            if X > 100 or X < 0:
                return 'poza planszą'
            else:
                return 'prawy margines'
    elif Y in range(91, 101):
        if X in range(0, 10):
            return 'lewy górny róg'
        if X in range(10, 91):
            return 'górny margines'
        else:
            if X > 100 or X < 0:
                return 'poza planszą'
            else:
                return 'prawy górny róg'
    else:
        return 'poza planszą'

# EXCEPTION MYŚLĘ ŻE JEST OK       
try:        
    X = int(input('Podaj pozycję gracza X: '))
    Y = int(input('Podaj pozycję gracza Y: '))

    print(f'Pozycja gracza to: {pozycja(X,Y)}')
except Exception as e:
    print(f'Wystąpił błąd: {e}')