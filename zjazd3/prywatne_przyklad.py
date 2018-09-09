class Produkt:

    def __init__(self, id, name, price):
        self.price = price

        self._id = id
        self._name = name
        self._discount = 0  # jeśli ustawiam wartość domyślną, nie muszę wpisywać go jako atrybut init.

    @property
    def full_name(self):
        return 'Product: ' + self._name

    @property
    def discount_price(self):
        '''price after discount'''
        return self.price - (self.price * self._discount)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if type(value) == float or type(value) == int:
            if 0 < value <= 0.3:
                self._discount = value

    @discount.deleter
    def discount(self):
        # wersja brutalna
        # del self._discount

        # wersja łagodniejsza
        self._discount = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 3:
            self._name = value


# pr1 = Produkt(1, 'bułka', 10)
#
# print(f'Cena produktu: {pr1.price}')
# print(f'Id produktu (prywatne): {pr1._id}')
# print(pr1.full_name)
# print(f'Cena ze zniżką ({pr1.discount*100}%): {pr1.discount_price}')
#
# # atrybut jest chroniony za pomocą property
# print(pr1.name)
# pr1.name = 'ale ma kota'
# print(pr1.name)
#
# # zmiana na wartość niezgodną z polityką jest niemożliwa
# pr1.name = 'ale'
# print(pr1.name)
#
# pr1.discount = 0.2
# print(pr1.discount)
# print(f'Cena ze zniżką ({pr1.discount*100}%): {pr1.discount_price}')
# pr1.discount = 0.1
# print(pr1.discount)
# print(f'Cena ze zniżką ({pr1.discount*100}%): {pr1.discount_price}')
# pr1.discount = 'kot'
# print(pr1.discount)
# print(f'Cena ze zniżką ({pr1.discount*100}%): {pr1.discount_price}')
# help(Produkt.discount_price) # printuje docstringa z property discount_price

def test_discount_with_setter():
    pr1 = Produkt(1, 'bułka', 10)
    pr1.discount = 0.2
    assert pr1.discount_price == 8.0

def test_discount_deleter():
    pr1 = Produkt(1, 'bułka', 10)
    pr1.discount = 0.2
    del pr1.discount
    assert pr1.discount == 0