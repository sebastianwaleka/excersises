#Napisz program sprawdzający, czy podana przez użytkownika liczba jest:
# - większa od 10
# - mniejsza równa 15
# - podzielna przez 2

number = int(input('Podaj liczbę: '))
print(f'\nWiększa od 10: {number > 10}')
print(f'Mniejsza równa 15: {number <= 15}') #WAŻNE <= itp piszemy BEZ SPACJI
print(f'Podzielna przez 2: {number % 2 == 0}')