# Napisz grę polegającą na poszukiwaniu skarby na dwuwymiarowej planszy 10x10. Użytkownik może wprowadzać komendy zmieniające położenie postaci. Po każdym ruchu użytkownik powinien otrzymać informację o tym, czy zmierza w dobrym kierunku. Wyjście poza planszę oznacza koniec gry. Po znalezieniu skarbu wypisz liczbę ruchów wykorzystanych do dojścia do celu.
# Dodatkowe:
# - po wykonaniu większej liczby kroków niż minimalna wartość x2. umieść skarb w nowym miejscu
# - z prawdopodobieństwem 1/5 nie podawaj graczowi wskazówek po wykonaniu kroku

from random import randint

treasurex = randint(1, 10)
treasurey = randint(1, 10)
pozx_player = randint(1, 10)
pozy_player = randint(1, 10)

min_moves = abs(pozx_player - treasurex) + abs(pozy_player - treasurey)
moves = 0
distance = min_moves

while True:
    distx = abs(pozx_player - treasurex)
    disty = abs(pozy_player - treasurey)
    print(f'\nYour position is: {pozx_player}x{pozy_player}.')
    
    if (pozx_player, pozy_player) == (treasurex, treasurey):
        print(f'Aye, aye Captain. We found it at {treasurex}x{treasurey}! It took you {moves} moves.')
        break
    
    move = input('Which way? [wsad] or [q] to quit ')
    if move == 'w':
        pozy_player += 1
    elif move == 's':
        pozy_player -= 1
    elif move == 'a':
        pozx_player -= 1
    elif move == 'd':
        pozx_player += 1
    elif move == 'q':
        print('End of game')
        break
    else:
        print('Wrong input.')
        continue
    moves += 1 #liczę liczbę kroków
    distx1 = abs(pozx_player - treasurex) # nowa odległość na osi X do skarbu 
    disty1 = abs(pozy_player - treasurey) # nowa odległość na osi Y do skarbu
    prob = randint(1, 5)
    if prob == 1:
        pass
    else:
        if distx1 < distx or disty1 < disty:
            print('Good way. Keep going.')
        else:
            print('Wrong way')    
    
    if pozx_player not in range(1, 11) or pozy_player not in range(1, 11):
        print('Out of bounds. GAME OVER!')
        break
    if moves == (min_moves * 2):
        treasurex = randint(1, 10)
        treasurey = randint(1, 10)
        print('Captain, someone stole our treasure. It\'s in different location now')
        min_moves = abs(pozx_player - treasurex) + abs(pozy_player - treasurey)