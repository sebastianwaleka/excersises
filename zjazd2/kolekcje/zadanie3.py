# Napisz program zliczający wystąpienia liczb dodatnich i ujemnych w zadanej liście liczb załkowitych.

numbers = [1, 2, -1, -4, 0, -2, 5, -9, -200, 1000, 345]
count_plus = 0
count_minus = 0
numbers_plus = list()
numbers_minus = list()

for number in numbers:
    if number > 0:
        count_plus += 1
        numbers_plus.append(number)
    elif number < 0:
        count_minus += 1
        numbers_minus.append(number)
#    else:
#        continue

print(f'Number of positive numbers: {count_plus}. List of this numbers: {numbers_plus}')
print(f'Number of negative numbers: {count_minus}. List of this numbers: {numbers_minus}')
