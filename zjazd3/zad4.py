'''
Zaimplementuj klasę Basket umożliwiającą dodawanie produktów w określonej liczbie do koszyka. Zaimplementuj metodę
obliczającą całkowitą wartość koszyka oraz wypisującą informację o zawartości koszyka. Dodanie dwa razy tego samego
produktu do koszyka powinno stworzyć tylko jedną pozycję.
Przykład użycia:
>> basket = Basket()
>> product = Product(1, 'Woda', 10.00)
>> basket.add_product(product, 5)
>> basket.count_total_price()
50.0
>> basket.generate_report()
'Produkty w koszyku:\n
- Woda (1), cena: 10.00 x 5\n
W sumie: 50.00'
'''


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f'"{self.name}", id: {self.id}, cena: {self.price} PLN')

    def __str__(self):
        return f"{self.id} | {self.name} | {self.price}"


class BasketEntry:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_entry_price(self):
        return self.product.price * self.quantity


class Basket:
    def __init__(self):
        self.entries = []

    def add_product(self, product, quantity):
        products_in_basket = [x.product for x in self.entries]
        if product in products_in_basket:
            pass
        else:
            entry = BasketEntry(product, quantity)
            self.entries.append(entry)

    def count_total_price(self):
        suma = 0
        for entry in self.entries:
            suma += entry.count_entry_price()
        return suma

    def generate_report(self):
        pass


def test_product_exist():
    product = Product(1, 'Woda', 10.99)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.99


def test_print_info(capsys):
    product = Product(1, 'Woda', 10.99)
    product.print_info()
    wyjscie = capsys.readouterr()
    out = wyjscie[0]
    assert out == '"Woda", id: 1, cena: 10.99 PLN\n'
    product = Product(1, 'Piwo', 10.99)
    product.print_info()
    wyjscie = capsys.readouterr()
    out = wyjscie[0]
    assert out == '"Piwo", id: 1, cena: 10.99 PLN\n'


def test_basket_initialization():
    basket = Basket()
    assert basket.entries == []


def test_basket_add_product():
    basket = Basket()
    product = Product(1, 'Piwo', 10)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1


def test_basket_add_two_products():
    basket = Basket()
    product1 = Product(1, 'Woda', 10)
    product2 = Product(1, 'Piwo', 10)
    basket.add_product(product1, 5)
    basket.add_product(product2, 5)
    assert len(basket.entries) == 2


def test_basket_add_product_twice():
    basket = Basket()
    product = Product(1, 'Piwo', 10)
    basket.add_product(product, 5)
    basket.add_product(product, 5)
    assert len(basket.entries) == 1


def test_count_entry_price():
    product = Product(1, 'Piwo', 10)
    entry = BasketEntry(product, 10)
    assert entry.count_entry_price() == 10 * 10


def test_basket_count_total_price():
    basket = Basket()
    product1 = Product(1, 'Woda', 10)
    product2 = Product(1, 'Piwo', 10)
    basket.add_product(product1, 5)
    basket.add_product(product2, 5)
    assert basket.count_total_price() == 50 + 50


def test_generate_report():
    basket = Basket()
    product1 = Product(1, 'Woda', 10)
    product2 = Product(1, 'Piwo', 10)
    basket.add_product(product1, 5)
    basket.add_product(product2, 5)
    assert basket.generate_report() == 'Produkty w koszyku:\n- Woda (1), cena: 10.00 x 10\n- Piwo (1), cena: 10.00 x 10\nW sumie: 100.00'
