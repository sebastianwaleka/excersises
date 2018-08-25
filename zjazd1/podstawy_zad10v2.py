# KALKULATOR - NAPISANY PO PYTHONOWEMU
def dzialanie(operacja, arg1, arg2):
    if operacja == '+':
	    return arg1 + arg2
    elif operacja == '-':
        return arg1 - arg2
    elif operacja == '/':
        return arg1/arg2
    elif operacja == '*':
        return arg1 * arg2
    else:
        raise ValueError(f'Nieznana operacja {operacja}')

try:
    num1 = int(input('Podaj pierwszą liczbę: '))
    num2 = int(input('Podaj drugą liczbę: '))
    znak = input('Podaj znak działania: +, -, /, *: ')
	
    wynik = dzialanie(znak, num1, num2)
    print(f'Wynik: {wynik}')	
except Exception as e:
    print(f'Nastąpił błąd: {e}')
	
print('Koniec')

