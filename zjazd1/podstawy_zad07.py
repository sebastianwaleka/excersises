#ZAD 7
#Napisz progfram sprawdzający, czy podana przez użytkownika liczba jest podzielna przez 2, podzielna przez 3 i większa od 10 lub jest to liczba 7
num = int(input('Podaj liczbę: '))
wynik = (num % 2 == 0 and num % 3 == 0 and num > 10) or num == 7 # and wiąże silnie niż or - dlatego nawiasy nie są wymagane
print(f'Liczba jest podzielna przez 2 i 3 oraz większa od 10 lub jest równa 7: {wynik}')

# & == and, | == or -> raczej nie używać tych znaków. Preferowane są słowa and i or.
