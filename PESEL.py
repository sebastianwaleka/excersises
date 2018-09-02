'''
This program will check person's sex basing on PESEL number.
It won't check whether number is correct or not. (FOR NOW)
'''

def pesel(number):
    if len(number) < 11:
        return 'Number too short.'
    elif len(number) > 11:
        return 'Number too long.'
    else:
        if number[-2] in ('0','2','4','6','8'):
            return 'Woman'
        else:
            return 'Man'


def test_pesel_correct():
    assert pesel('90012016888') == 'Woman'
    assert pesel('89102575777') == 'Man'
    assert pesel('9090909') == 'Number too short.'


def test_pesel_false():
    assert not pesel('66121315787') == 'Man'
    assert not pesel('665588') == 'Woman'
    assert not pesel('8') == 'Number too long.'


number = input('Enter PESEL number: ')
print(pesel(number))