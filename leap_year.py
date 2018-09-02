'''
Program will check if given year is leap year or not.
If correct it will return 'Year YYYY is leap year.'
Else 'Year YYYY is NOT leap year.'.
Leap year is when year is divisible by 4 or 400 but not divisible by 100.
'''


def leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return f'Year {year} is leap year.'
    else:
        return f'Year {year} is NOT leap year.'

def test_leap_year_correct():
    assert leap_year(2000) == 'Year 2000 is leap year.'
    assert leap_year(1984) == 'Year 1984 is leap year.'
    assert leap_year(1900) == 'Year 1900 is NOT leap year.'


def test_leap_year_false():
    assert not leap_year(2013) == 'Year 2013 is leap year.'
    assert not leap_year(1928) == 'Year 1928 is NOT leap year.'

try:
    year = int(input('Enter year you want to check: '))
    print(leap_year(year))
except Exception as e:
    print(f'Something goes wrong - {e}')