'''
PESEL number generator and validator.
Formula: 1×a + 3×b + 7×c + 9×d + 1×e + 3×f + 7×g + 9×h + 1×i + 3×j + 1×k
'''
from random import randint, randrange


def pesel_generator(birth_date, sex):  # YYYY-MM-DD
    year = birth_date[0:4]
    year = int(year)
    month = birth_date[5:7]
    month = int(month)
    if 1800 <= year < 1900:
        month += 80
    elif 2000 <= year < 2100:
        month += 20
    elif 2100 <= year < 2200:
        month += 40
    elif 2200 <= year < 2300:
        month += 60
    # Extracting every single number from birth date in format YYYY-MM-DD
    pesel_1 = birth_date[2]
    pesel_1 = int(pesel_1)
    pesel_2 = birth_date[3]
    pesel_2 = int(pesel_2)
    if len(str(month)) == 2:
        pesel_3 = str(month)
        pesel_3 = pesel_3[0]
        pesel_3 = int(pesel_3)
        pesel_4 = str(month)
        pesel_4 = pesel_4[1]
        pesel_4 = int(pesel_4)
    else:
        pesel_3 = 0
        pesel_4 = str(month)
        pesel_4 = pesel_4[0]
        pesel_4 = int(pesel_4)
    pesel_5 = birth_date[8]
    pesel_5 = int(pesel_5)
    pesel_6 = birth_date[9]
    pesel_6 = int(pesel_6)
    # Calculating other numbers
    while True:
        pesel_7 = randint(0, 9)
        pesel_8 = randint(0, 9)
        pesel_9 = randint(0, 9)
        if sex.lower() == 'm':
            pesel_10 = randrange(1, 9, 2)
        elif sex.lower() == 'k' or 'w':
            pesel_10 = randrange(0, 9, 2)
        pesel_11 = randint(0, 9)
        # Validation rule
        _check = 1 * pesel_1 + 3 * pesel_2 + 7 * pesel_3 + 9 * pesel_4 + 1 * pesel_5 + 3 * pesel_6 + 7 * pesel_7 + 9 * pesel_8 + 1 * pesel_9 + 3 * pesel_10 + 1 * pesel_11
        if _check % 10 == 0:
            return f'{pesel_1}{pesel_2}{pesel_3}{pesel_4}{pesel_5}{pesel_6}{pesel_7}{pesel_8}{pesel_9}{pesel_10}{pesel_11}'
            break


# Validator of actual or generated PESEL
def pesel_validator(pesel):
    pesel_numbers = []
    for number in pesel:
        number = int(number)
        pesel_numbers.append(number)
    _check = 1 * pesel_numbers[0] + 3 * pesel_numbers[1] + 7 * pesel_numbers[2] + 9 * pesel_numbers[3] + 1 * \
             pesel_numbers[4] + 3 * pesel_numbers[5] + 7 * pesel_numbers[6] + 9 * pesel_numbers[7] + 1 * pesel_numbers[
                 8] + 3 * pesel_numbers[9] + 1 * pesel_numbers[10]
    if _check % 10 == 0:
        return 'Valid'
    else:
        return 'Invalid'


birth_date = input('Enter birth date in format YYYY-MM-DD: ')
sex = input('Enters sex man [m] woman [w]: ')
PESEL = pesel_generator(birth_date, sex)
print(PESEL)
print(pesel_validator(PESEL))
