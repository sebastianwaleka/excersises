# Napisz program wyliczający kwotę należną za zakupiony towar na podstawie podanej przez użytkownika wagi
# i nazwy produktu. Do przechowywania informacji o cenie za kilogram danego produktu użyj słownika.
# Wypisz wszystkie dostępne produkty w sklepie

items = {
    'bananas': 4.00,
    'potatos': 1.50,
    'water': 1.00,
    'tomatos': 5.50
}
stock = {
    'bananas': 5.50,
    'potatos': 20,
    'water': 50,
    'tomatos': 15
}
shopping_list = list()

print('We have:')
for item in items:
    print(f'{item} - {items[item]:.2f} PLN/kg - {stock[item]} kilos in stock')
while True:
    deliver_or_buy = input('Are you customer (c) or provider (p)? [q] to quit')
    if deliver_or_buy == 'c':
        while True:
            product_name = input('What do you want to buy? [q] to quit: ')
            if product_name == 'q':
                print(f'\nFor your goods you have to pay {sum(shopping_list)} PLN')
                break
            if product_name not in items:
                print('There is no such product.')
                continue
            if stock[product_name] <= 0:
                print('We are waiting for delivery. Pick something else.')
                continue
            weight = float(input('How much? '))
            if stock[product_name] < weight:
                print('You want too much.')
                continue
            if product_name in stock:
                stock[product_name] -= weight
            bill = items[product_name] * weight
            shopping_list.append(bill)
    elif deliver_or_buy == 'p':
        while True:
            product_name = input('What do you want to provide? [q] to quit')
            if product_name == 'q':
                break
            product_quantity = float(input('How much? '))
            if product_name in stock:
                stock[product_name] += product_quantity
            else:
                stock[product_name] = product_quantity
    else:
        break
