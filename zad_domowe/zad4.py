'''
Zaimplementuj funkcję zliczającą liczbę wystąpień poszczególnych słów w zadanym napisie.
Podpowiedź: do podzielenia napisu na słowa użyj metody split().
Przykład użycia:
>>	policz_slowa('ala ma kota i kota ma ala')
{'ala': 2, 'i': 1, 'kota': 2, 'ma': 2}
'''
def policz_slowa(text):
    text = text.split()
    slowa = {}
    for slowo in text:
        slowa[slowo] = slowa.get(slowo, 0) + 1
    return slowa


def test_policz_slowa_poprawny():
    assert policz_slowa('ala ma kota i kota ma ala') == {'ala': 2, 'i': 1, 'kota': 2, 'ma': 2}
    assert policz_slowa('jak tam') == {'jak': 1, 'tam': 1}


def test_policz_slowa_niepoprawny():
    assert not policz_slowa('kurła kiedyś to było') == {'kiedyś': 1, 'to': 2, 'było': 1}
    assert not policz_slowa('janusz') == {}
