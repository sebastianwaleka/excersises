#Stwórz tuplę zawierającą 10 różnych liczb całkowitych. Korzystając z operatora dostępu oraz wycinania pobierz:
# - drugi element
# - przedostatni element
# - elementy od trzeciego do siódmego włącznie
# - co trzeci element
# - co drugi element licząc od końca

numbers = (1,2,3,4,5,6,7,8,9,10)

print('Drugi element tupli: ', numbers[1])
print('Przedostatni element tupli: ', numbers[-2])
print('Elementy tupli od 3 do 7 włącznie: ', numbers[2:7])
print('Co trzeci element tupli: ', numbers[::3])
print('Co drugi element tupli licząc od końca: ', numbers[::-2]) # działa tak samo jak numbers[-1::-2]
