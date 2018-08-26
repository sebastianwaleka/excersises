# Zaimplementuj funkcję formatującą podane napisy.
# Przykład użycia:
# >>> formatuj(
#               'koszt $cena PLN',
#               'kwota $cena brutto',
#                cena = 10,
#        )
# 'koszt 10 PLN\nkwota 10 brutto'
#
def formatuj(*napisy, **znaczniki):
    napisy = '\n'.join(napisy)
    for znacznik in znaczniki:
        napisy = napisy.replace(f'${znacznik}', str(znaczniki[znacznik]))
    return napisy


def test_formatuj_napisy_bez_znacznikow():
    assert formatuj('Hello World') == 'Hello World'


def test_formatuj_napisy_bez_znacznikow():
    assert formatuj('Hello World', 'I am Sebastian') == 'Hello World\nI am Sebastian'


def test_formatuj_napis_ze_znacznikem():
    assert formatuj('koszt $cena PLN', cena=10) == 'koszt 10 PLN'


def test_formatuj_napisy_ze_znacznikem():
    assert formatuj('koszt $cena PLN', 'kwota $cena brutto', cena=10) == 'koszt 10 PLN\nkwota 10 brutto'
    assert formatuj('koszt $cena PLN', 'kwota $kwota brutto', cena=10, kwota=15) == 'koszt 10 PLN\nkwota 15 brutto'
    assert formatuj('koszt $kwota PLN', 'kwota $kwota brutto', kwota=10) == 'koszt 10 PLN\nkwota 10 brutto'
