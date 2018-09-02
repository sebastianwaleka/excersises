'''
Program will check if given string is palindrome or not.
If it is, it will return str "It's palindrome" else "Not palindrome".
'''


def palindrome(text):
    if len(text) > 1:
        if text == text[::-1]:
            return 'It\'s palindrome.'
        else:
            return 'Not palindrome.'
    elif text == '':
        return 'No text found!'
    else:
        return 'Text too short.'


def test_palindrome_empty():
    assert palindrome('') == 'No text found!'


def test_palindrome_correct():
    assert palindrome('kajak') == 'It\'s palindrome.'
    assert palindrome('lol') == 'It\'s palindrome.'
    assert palindrome('zaraz') == 'It\'s palindrome.'


def test_palindrome_false():
    assert not palindrome('bardzo') == 'Palindrome'
    assert not palindrome('interesting') == 'Palindrome'
    assert not palindrome('zając') == 'Palindrome'


def test_palindrome_one_letter():
    assert not palindrome('x') == 'Not palindrome.'


text = input('Enter text: ')
print(palindrome(text))
