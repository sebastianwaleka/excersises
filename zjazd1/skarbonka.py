skarbonka = 20

while True:
    print(f'Aktualna ktowa w skarbonce: {skarbonka} PLN')
    if skarbonka >= 100:
        print('Brawo! Masz już 100 PLN')
        break
    try:
        i = float(input('Podaj wysokość wpłaty: '))
        skarbonka += i
    except:
        print('Proszę podaj liczbę!')
        