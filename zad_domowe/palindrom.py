'''
Zaimplementuj funkcję, która sprawdzi czy podany napis jest palindromem (napis czytany tak samo od lewej,
jak i od prawej).
Podpowiedź: do odwrócenia napisu możemy wykorzystać mechanizm wycinania (ang. slicing).
Przykład użycia:
>>	czy_palindrom('kajak')
True
>>	czy_palindrom('python')
False
'''
def czy_palindrom(text):
    if text != '':
        text = text.strip().lower().replace(' ','')
        if text == text[::-1]:
            return True
        else:
            return False
    else:
        return 'Nie podano tekstu.'

def test_czy_palindrom_poprawny():
    assert czy_palindrom('kajak') == True
    assert czy_palindrom('python') == False
    assert czy_palindrom('Kobyła ma mały bok') == True


def test_czy_palindrom_niepoprawny():
    assert not czy_palindrom('zając') == True
    assert not czy_palindrom('toyota') == True
    assert not czy_palindrom('aibofobia') == False


def test_czy_palindrom_pusty():
    assert czy_palindrom('') == 'Nie podano tekstu.'


