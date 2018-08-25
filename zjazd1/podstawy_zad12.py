#Napisz program obliczający kwadrat 100 pierwszych liczb całkowitych i wypisujący wyniki na konsole
print('########## Wersja pierwsza ##########')
i = 1
while i <= 100:
    print(f'{i} do kwadratu to: {i*i}')
    i += 1
    
print('\n########## Druga wersja ##########')
i = 1
while True:
    print(f'{i} do kwadratu to: {i*i}')
    i += 1
    if i > 100:
        break