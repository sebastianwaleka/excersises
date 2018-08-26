from zadanei3 import policz_znaki

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
