my_dict = dict()

my_dict = {
    'javascript': 'language...',
    'ruby': 'little wors python'
}
my_dict['python'] = 'The best language ever'
my_dict['assembler'] = 'The hardest language ever'

print(my_dict)

print('python' in my_dict)
print(my_dict.get('c++', 'Jeszcze tego nie ma'))

lista_jezykow = ['python', 'c++', 'c#', 'assembler']

for lang in lista_jezykow:
    print(my_dict.get(lang, 'Jeszcze tego nie mam'))