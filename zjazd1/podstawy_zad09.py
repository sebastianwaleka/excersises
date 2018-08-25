#Napisz program, który sprawdzi pełnoletność osoby na podstawie roku jej urodzenia
from datetime import datetime

birth_date = int(input('Podaj rok urodzenia: '))

# ŹLE TO WYGLĄDA
#if 2018 - birth_date >= 18:
#   print('Jesteś pełnoletni!')
#else:
#    print("Jesteś osobą niepełnoletnią!")
# ###########################################################################
# TU TEŻ ŹLE
#if birt_date <= 2000:
#   print("Jesteś pełnoletni!")
#else:
#    print("Jesteś niepełnoletni!")
# ##########################################################################
# TU LEPIEJ
#rok_biezacy = 2018
#wiek = rok_biezacy - birth_date
#if wiek >= 18:
#    print("Jesteś pełnoletni!")
#else:
#    print("Jesteś niepełnoletni!")
# ######################################################################3
# TAK POWINNO BYĆ
rok_biezacy = datetime.today().year #z modułu datetime pobieram klasę datetime, wywołuję metodę statyczną today(), która odczytuje rok (year)
wiek = rok_biezacy - birth_date

if wiek >= 18:
    print("Jesteś pełnoletni!")
else:
    print("Jesteś niepełnoletni!")