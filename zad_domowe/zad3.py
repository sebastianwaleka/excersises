'''
Zaimplementuj funkcję zwracającą listę lat przestępnych na podstawie zadanego zakresu.
Podpowiedź: rok przestępny to taki który dzieli się przez 4, ale nie dzieli się przez 100 lub dzieli się przez 400.
Przykład użycia:
>>	lata_przestepne(1990, 2020)
[1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]
'''
def lata_przestepne(rok_poczatek, rok_koniec):
    przestepne = []
    for rok in range(rok_poczatek, rok_koniec+1):
        if rok % 4 == 0 and rok % 100 != 0 or rok % 400 == 0:
            przestepne.append(rok)
    return przestepne


def test_lata_przestepne_poprawne():
    assert lata_przestepne(1990, 2020) == [1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020]


def test_lata_przestepne_niepoprawne():
    assert not lata_przestepne(1990,1995) == [1990, 1991, 1992]
