'''
Zaimplementuj klasę Vector dostarczającą funkcjonalność wektora swobodnego na dwuwymiarowej płaszczyźnie.
Wektory powinny mieć możliwość dodawania, odejmowania, mnożenia (przez liczbę), porównania (po długości) oraz
powinny posiadać czytelną reprezentację napisową.
Przykład użycia:
vector_1 = Vector(x=1, y=2)
vector_2 = Vector(x=1, y=2)
vector_3 = vector_1 + vector_2
'''
from math import sqrt


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
        # or:
        # new_x = self.x + other.x
        # new_y = self.y + other.y
        # ret_vector = Vector(new_x, new_y)
        # return ret_vector

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    @property
    def length(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __eq__(self, other):
        return self.length == other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length

    def __ne__(self, other):
        return self.length != other.length

    def __str__(self):
        return f'V({self.x},{self.y}): {self.length}'


#
# vector_1 = Vector(3, 4)
# vector_2 = Vector(1, 2)
# vector_3 = Vector(4, 5)
# vector_list = [vector_1, vector_2, vector_3]
# for vector in sorted(vector_list):
#     print(f'{vector} ', end='')

def test_vector_create():
    vector_1 = Vector(1, 2)
    vector_2 = Vector(3, 4)
    assert vector_1.x == 1
    assert vector_1.y == 2
    assert vector_2.x == 3
    assert vector_2.y == 4


def test_vector_add():
    vector_1 = Vector(1, 2)
    vector_2 = Vector(3, 4)
    vector_3 = vector_1 + vector_2
    assert vector_3.x == 4
    assert vector_3.y == 6


def test_substract_vector():
    vector_1 = Vector(1, 2)
    vector_2 = Vector(3, 4)
    vector_3 = vector_1 - vector_2
    assert vector_3.x == -2
    assert vector_3.y == -2


def test_multi_vector_with_number():
    vector_1 = Vector(1, 2)
    vector_2 = vector_1 * 4.5
    assert vector_2.x == 4.5
    assert vector_2.y == 9


def test_vector_length():
    vector_1 = Vector(3, 4)
    assert vector_1.length == 5


def test_vector_length_comparision_equal():
    vector_1 = Vector(3, 4)
    vector_2 = Vector(3, 4)
    assert vector_1 == vector_2


def test_vector_length_comparision_equal2():
    vector_1 = Vector(3, 4)
    vector_2 = Vector(-3, 4)
    assert vector_1 == vector_2


def test_vector_length_comparision_equal3():
    vector_1 = Vector(3, 4)
    vector_2 = Vector(0, 5)
    assert vector_1 == vector_2


def test_vector_length_comparision_greater_than():
    vector_1 = Vector(4, 4)
    vector_2 = Vector(3, 4)
    assert vector_1 > vector_2


def test_vector_length_comparision_greater_than_or_equal():
    vector_1 = Vector(4, 4)
    vector_2 = Vector(4, 4)
    assert vector_1 >= vector_2


def test_vector_length_comparision_less_than():
    vector_1 = Vector(3, 4)
    vector_2 = Vector(4, 4)
    assert vector_1 < vector_2


def test_vector_length_comparision_less_than_or_equal():
    vector_1 = Vector(4, 4)
    vector_2 = Vector(4, 4)
    assert vector_1 <= vector_2
    vector_1 = Vector(3, 4)
    vector_2 = Vector(4, 4)
    assert vector_1 <= vector_2


def test_vector_length_comparision_not_equal():
    vector_1 = Vector(3, 4)
    vector_2 = Vector(4, 4)
    assert vector_1 != vector_2


def test_sorting_vectors():
    vector_1 = Vector(3, 4)
    vector_2 = Vector(1, 2)
    vector_3 = Vector(4, 5)
    vector_list = [vector_1, vector_2, vector_3]
    assert sorted(vector_list) == [vector_2, vector_1, vector_3]


def test_sorting_vectors2():
    vector_1 = Vector(3, 4)
    vector_2 = Vector(1, 2)
    vector_3 = Vector(4, 5)
    vector_4 = Vector(1, 2)
    vector_list = [vector_1, vector_2, vector_3, vector_4]
    assert sorted(vector_list) == [vector_4, vector_2, vector_1, vector_3]
    assert sorted(vector_list) == [vector_2, vector_4, vector_1, vector_3]
