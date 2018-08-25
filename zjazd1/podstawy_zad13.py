#temp = list()
print()
NUMBER_OF_DAYS = 7
i = 0
temp = 0
while i < 7:
    i += 1
    day = float(input(f'Please insert temperature of {i}. day: '))
    temp += day
 
print(f'\nAverage temperature of {NUMBER_OF_DAYS} days is {temp/NUMBER_OF_DAYS:.1f}')