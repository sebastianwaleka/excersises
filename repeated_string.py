'''
User gives a string 's' which is repeted infinitely. Than, user gives number that determines the length of the string.
In that string we must find how many times letter 'a' occurred. Program must return that number.

Example:
'abc'
10
4
'''


def repeated_string(s, lenght):
    while len(s) < lenght:
        s += s
    s = s[:lenght]
    a_counter = 0
    for letter in s:
        if letter == 'a':
            a_counter += 1
    return a_counter

def test_repeated_string():
    assert repeated_string('abc', 10) == 4
    assert repeated_string('a', 100000) == 100000
    assert repeated_string('bde', 50) == 0
