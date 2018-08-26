# Napisz funkcję obliczającą liczbę znaków w zadanym napisie pomiędzy zadanymi znakami.
# Znaki, pomiędzy którymi ma odbywać się zliczanie, powinny być argumentami z wartościami domyślnymi odpowiednio < i >.
# Nawiasy mogą być zagnieżdzone i mogą wystąpić wiele razy.
# Znaki pomiędzy zagnieżdżonymi nawiasami liczone są zgodnie z poziomem zagnieżdżenia.
# Przykład użycia:
# >>> policz_znaki('ala ma <kota> a kot ma ale')
# 4
# >>> policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']')
# 18
# >>> policz_znaki('a <a<a<a>>>')
# 6

def policz_znaki(tekst, znak1='<', znak2='>'):
    licznik = 0
    poziom = 0
    for znak in tekst:
        if znak == znak1:
            poziom += 1
            continue
        elif znak == znak2:
            poziom -= 1
            continue
        # elif poziom > 0:
        licznik += poziom
    return licznik

def test_policz_znaki_pusty_tekst():
    assert policz_znaki('') == 0


def test_policz_znaki_dla_niepustego_tekstu_poprawny():
    assert policz_znaki('ala ma <kota> a kot ma ale') == 4
    assert policz_znaki('ala [kota [a kot]] ma [ale]', '[', ']') == 18
    assert policz_znaki('a <a<a<a>>>') == 6
    assert policz_znaki('<ala <ma <kota <a> kot> ma> ale>') == 51
    assert policz_znaki('<ala ma kota a ]kot ma ale','<',']') == 14
    assert policz_znaki('ala ma kota a kot ma ale') == 0
    assert policz_znaki('ala .ma- kota a kot ma ale', '.', '-') == 2


def test_policz_znaki_pusty_tekst_bledny():
    assert not policz_znaki('') == 1


def test_policz_znaki_dla_niepustego_tekstu_bledny():
    assert not policz_znaki('ala ma <<kota>> a kot ma ale') == 4
    assert not policz_znaki('ala kota <a kot> ma <ale>', '[', ']') == 18
    assert not policz_znaki('a <a<a<a>>>') == 3
    assert not policz_znaki('ala ma kota a kot ma ale') == 1
