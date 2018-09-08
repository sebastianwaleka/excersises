class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def print_info(self):
        print(f'Produkt: "{self.name}", id: {self.id}, cena: {self.price} PLN')


def test_product_exist():
    product = Product(1, 'Woda', 10.99)
    assert product.id == 1
    assert product.name == 'Woda'
    assert product.price == 10.99


def test_print_info(capsys):
    product = Product(1, 'Woda', 10.99)
    product.print_info()
    out, err = capsys.readouterr()
    assert out == 'Produkt: "Woda", id: 1, cena: 10.99 PLN\n'
    product = Product(11, 'Chleb', 2.99)
    product.print_info()
    out, err = capsys.readouterr()
    assert out == 'Produkt: "Chleb", id: 11, cena: 2.99 PLN\n'
