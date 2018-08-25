# Program ma w pętli pytać o liczbę całkowitą, a zakończyć się na podaniu liczby podzielnej przez 7.
print('START...')
while True:
    try:
        num = int(input('Enter number: '))
    except:
        print('Value Error. Input number please.')
        continue
    if num % 7 == 0:
        print('Division by 7 occur.\nEND')
        break