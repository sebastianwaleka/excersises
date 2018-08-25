# Napisz program obliczający koszt przejazdu z miasta A do B na podstawie podanej przez użytkownika liczby kilometrów, ceny paliwa oraz spalania. Zapytaj użytkownika także o nazwy miejscowości.
# Przykładowy komunikat:
# Miasto A: Warszawa
# Miasto B: Gdańsk
# Dystans Warszawa - Gdańsk: 420
# Cena paliwa: 4.55
# Spalanie na 100 km: 5.5
#
# Koszt przejazdu Warszawa - Gdańsk to 105 PLN.

def travel_cost(distance, fuel_cost, combustion):
    cost = distance * combustion * fuel_cost / 100
    return cost
    
city_a = input('Miasto A: ')
city_b = input('Miasto B: ')
distance = int(input(f'Dystans {city_a} - {city_b}: '))
fuel_cost = float(input('Cena paliwa: '))
combustion = float(input('Spalanie na 100 km: '))

koszt = travel_cost(distance, fuel_cost, combustion)

print(f'\nKoszt przejazdu {city_a} - {city_b} to {koszt:.0f} PLN')
