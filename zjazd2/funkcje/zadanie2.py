# Napisz funkcję zwracającą zbiór wszystkich znaków występujących w napisie więcej niż zadana liczba razy.
# Przykład:
# wiecej_niz('ala ma kota, a kot ma ale', 3)

def wiecej_niz(tekst, liczba):
    # slownik = {}
    # zbior = set()
    # for znak in tekst:
    #     slownik[znak] = slownik.get(znak, 0) + 1
    # for key in slownik:
    #     if slownik[key] > liczba:
    #         zbior.add(key)
    # return zbior
    # Druga wersja
    zbior = set()
    for znak in tekst:
        if tekst.count(znak) > liczba:
            zbior.add(znak)
    return zbior


def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('', 1) == set()
    assert wiecej_niz('', 0) == set()
    assert wiecej_niz('', 5) == set()


def test_wiecej_niz_dla_napisu_poprawny():
    assert wiecej_niz('ala ma kota, a kot ma ale', 3) == {'a', ' '}
    assert wiecej_niz('kozakiewicz', 0) == {'k', 'o', 'z', 'a', 'i', 'e', 'w', 'c'}
    assert wiecej_niz('jakis napis', 3) == set()


def test_wiecej_niz_dla_napisu_bledny():
    assert not wiecej_niz('ala', 3) == {'a'}
    assert not wiecej_niz('ala', 2) == {'a'}
    assert not wiecej_niz('ala', 1) == {'a', 'l'}
