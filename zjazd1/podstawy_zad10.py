# KALKULATOR

num1 = int(input('Podaj pierwszą liczbę: '))
num2 = int(input('Podaj drugą liczbę: '))
znak = input('Podaj znak działania: +, -, /, *: ')

def suma(a,b):
   return a+b
 
def roznica(a,b):
    return a-b

def iloczyn(a,b):
    return a*b

def iloraz(a,b):
    return a/b

if znak == '+':
	wynik = suma(num1, num2)
elif znak == '-':
    wynik = roznica(num1, num2)
elif znak == '/':
    if num2 == 0:
        print('Nie można dzielić przez 0!')
    else:
        wynik = iloraz(num1, num2)
elif znak == '*':
    wynik = iloczyn(num1, num2)
else:
    wynik = None

if wynik is not None:
    print(f'Wynik: {wynik}')	
else:
    print('Nieznana operacja')
