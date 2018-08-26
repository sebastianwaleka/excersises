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
    if znak1 == znak2:
        raise ValueError('znaki początku i końca muszą być różne')
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

tekst = input('Podaj tekst: ')
print(policz_znaki(tekst))