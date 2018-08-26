# Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
# Sprawdź jak dużo liczb jest liczbami parzystymi w zakresie 0-100 - w celu skorzystaj z operatora iloczynu.

numbers = set()
while True:
    number = input('Enter number or "q": ')
    if number.lower() == 'q':
        break
    else:
        numbers.add(int(number))

# zero_hundred = set(range(101))
#
# common_part = numbers & zero_hundred
# common_part_divided_by_two = set()
# for num in common_part:
#     if num % 2 == 0:
#         common_part_divided_by_two.add(num)
# print(f'In total you gave {len(numbers)} unique numbers. List of given numbers: {numbers}')
# print(f'In range 0-100 you gave {len(common_part_divided_by_two)} numbers divided by 2.')

# Drugie podejście beż użycia pętli for do szukania parzystych liczb
zero_hundred_divided_by_two = set(range(2,101,2))

common_part = numbers & zero_hundred_divided_by_two

print(f'In total you gave {len(numbers)} unique numbers. List of given numbers: {numbers}')
print(f'In range 0-100 you gave {len(common_part)} numbers divided by 2.')
