'''
Zaimplementuj funkcję, która na podstawie podanej listy stworzy nową listę zawierającą tylko elementyoryginalnej
kolekcji z podanego zakresu.
Funkcja powinna przyjmować trzy parametry:listę początek zakresu koniec zakresu
Przykład użycia:
>>	filtruj([-2, 10, 0, 5, 1, 16, 9], 5, 15)
[10, 5, 9]
'''

def filtruj(lista, poczatek, koniec):
    if len(lista) > 0:
        z_zakresu = []
        for element in lista:
            if poczatek <= element <= koniec:
                z_zakresu.append(element)
    else:
        return 'Lista jest pusta.'
    return z_zakresu


def test_filtruj_poprawnie():
    assert filtruj([-2, 10, 0, 5, 1, 16, 9], 5, 15) == [10, 5, 9]
    assert filtruj([1, 2, 3, 4, 5, 6], 3, 5) == [3, 4, 5]
    assert filtruj([0, -2, -3, -4, 5, 10, 100], 1, 2) == []


def test_filtruj_niepoprawne():
    assert not filtruj([1, 2, 3, 4, 5], 2, 4) == [1, 2, 3, 4]
    assert not filtruj([-1, -2, 3, 4, 5, 10], 3, 10) == [-1, -2]


def test_filtruj_pusta_lista():
    assert filtruj([], 1, 2) == 'Lista jest pusta.'
