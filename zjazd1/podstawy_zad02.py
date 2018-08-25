#print('Program liczący pole trapezu o wymiarach podstaw 3, 9 i wysokości 6.5')
#a = 3
#b = 9
#h = 6.5
#p = (a + b) /2 *h
#print('Pole trapezu o długości podstaw 3 i 9 oraz wysokości 6.5, to: ', p)

def pole_trapezu(a, b, h):
    p = (a + b) / 2 * h
    return p
	
print('Pole trapezu o wymiarach:\n a = 3\n b = 9\n h = 6.5\nwynosi: ', pole_trapezu(3, 9, 6.5))

# od pythona 3.6 można użyć składni fstring: -> obecnie najbardziej zalecane
print(f'Pole trapezu o wymiarach:\n a = 3\n b = 9\n h = 6.5\nwynosi: {pole_trapezu(3, 9, 6.5):.2f}') 

# sposób popularny w python 2, ale wciąż dostępny
print(f'Pole trapezu o wymiarach:\n a = 3\n b = 9\n h = 6.5\nwynosi: %d' % pole_trapezu(3, 9, 6.5)) 

