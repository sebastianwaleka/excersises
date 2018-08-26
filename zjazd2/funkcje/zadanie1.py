# Napisz funkcję sprawdzającą, czy dana liczba jest liczbą pierwszą.

def test_czy_jest_pierwsza_dla_liczby_pierwszej():
    assert liczba_pierwsza(3)  # tu powinno być zwrócone True
    assert liczba_pierwsza(7)
    assert liczba_pierwsza(11)


def test_czy_jest_pierwsza_dla_liczby_niepierwszej():
    assert not liczba_pierwsza(4)  # tu powinno być zwrócone False, ale dopisek not daje True
    assert not liczba_pierwsza(6)
    assert not liczba_pierwsza(100)
    assert not liczba_pierwsza(22)

def liczba_pierwsza(number):
    for num in range(2, number):
        if number % num == 0:
            return False
    return True

#
# number = int(input('Enter number: '))
#
# print(liczba_pierwsza(number))
