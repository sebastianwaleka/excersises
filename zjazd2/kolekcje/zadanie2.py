# Użytkownik ma podać 10 liczb. Potem program oblicza średnią. Do przechowywania liczb użyj liczby.
# Pozwól na wprowadzenie max 10 liczb. Skorzystaj z funkcji sum().

numbers = list()
while len(numbers) < 10:
    number = input('Enter number or quit [q]: ')
    if number == 'q' or number == 'Q':
        break
    else:
        number = int(number)
        numbers.append(number)

print('Your numbers: ', numbers)
print('Średnia = ', sum(numbers) / len(numbers))

# #Druga wersja
# numbers1 = list()
# while len(numbers1) < 10:
#     nums = input('Enter 10 numbers, separated by coma: ')
#     if ',' in nums:
#         nums = nums.split(',')
#     elif ' ' in nums:
# jest błąd przy wpisaniu liczby dwucyfrowej i większej - rozdziela na pojedyncze cyfry.
#         nums = nums.split(' ')
#     for num in nums:
#         num = int(num)
#         numbers1.append(num)
# if len(numbers1) > 10:
#     numbers1 = numbers1[:10]
#
# print('Your numbers: ', numbers1)
# print('Average = ', sum(numbers1)/len(numbers1))
