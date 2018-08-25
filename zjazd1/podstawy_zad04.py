# Napisz program wyliczający kwotę należną za zakupiony towar na podstawie ceny za kg oraz liczbt zakupiuonych kg. Do przechowywania informacji o cenie oraz liczbie kg użyj zmiennych. Wypisz wszystkie informacje na konsolę. Przykładowy komunikat to:
# Cena za kg: 10.0
# Waga: 2.5
# Należność: 25.0

def naleznosc(cena, waga):
    wynik = cena * waga
    return wynik

cena = float(input('Podaj cenę za kg: '))
waga = float(input('Podaj wagę: '))
print(f'Cena za kg: {cena} PLN')
print(f'Waga: {waga} kg')
print(f'Należność: {naleznosc(cena,waga)} PLN')