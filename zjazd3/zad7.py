'''
Zaimplementuj klasę PremiumEmployee, która będzie klasą pochodną Employee. Klasa ta powinna umożliwiać dodatkowo
przyznawanie bonusów pracownikowi.

>> employee = PremiumEmployee('Jan', 'Nowak', 100.0)
>> employee.register_time(5)
>> employee.give_bonus(1000.0)
>> employee.pay_salary()
1500.0
'''
from zjazd3.zad2 import Employee


class PremiumEmployee(Employee):

    count = 0

    def __init__(self, first_name='Jan', last_name='Kowalski', salary=50, bonus=0):
        super().__init__(first_name, last_name, salary)
        self.bonus = bonus
        self.__class__.count += 1

    def give_bonus(self, bonus):
        self.bonus += bonus

    def pay_salary(self):
        sal = super().pay_salary()
        # sal = super(PremiumEmployee, self).pay_salary()
        sal += self.bonus
        self.bonus = 0
        return sal

    @classmethod
    def create_hero(cls):
        cls.count = 0
        return PremiumEmployee('Pracownik', 'Miesiąca', 0, 0)

    @classmethod
    def emp_from_string(cls, str_param):
        list_param = str_param.split(';')
        return PremiumEmployee(list_param[0], list_param[1], int(list_param[2]))

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod  # nie odwołuje się do stanu wewnętrzbego obiektu (nie potrzebuje self'a)
    def say_hello():
        return 'Hello'

def test_count():
    assert PremiumEmployee.get_count() == 0
    emp = PremiumEmployee()
    emp = PremiumEmployee()
    assert PremiumEmployee.get_count() == 2
    emp = PremiumEmployee.create_hero()
    assert PremiumEmployee.get_count() == 1


def test_import_from_text():
    param = 'Henryk;Zdun;50'
    employee = PremiumEmployee.emp_from_string(param)  # potocznie nazywa to się Fabryką
    assert employee.first_name == 'Henryk'
    assert employee.last_name == 'Zdun'
    assert employee.salary == 50


def test_PremiumEmployee_create():
    employee = PremiumEmployee('Jan', 'Nowak', 100)
    assert employee.first_name == 'Jan'
    assert employee.last_name == 'Nowak'
    assert employee.salary == 100.0
    assert employee.bonus == 0


def test_PremiumEmployee_create_with_bonus():
    employee = PremiumEmployee('Jan', 'Nowak', 100, 2000)
    assert employee.first_name == 'Jan'
    assert employee.last_name == 'Nowak'
    assert employee.salary == 100.0
    assert employee.bonus == 2000.0


def test_register_time():
    employee = PremiumEmployee('Jan', 'Nowak', 100)
    employee.register_time(5)
    assert employee.pay_salary() == 500.0


def test_register_time_and_give_bonus():
    employee = PremiumEmployee('Jan', 'Nowak', 100)
    employee.register_time(5)
    employee.give_bonus(1000.0)
    employee.give_bonus(400.0)
    assert employee.bonus == 1400
    assert employee.pay_salary() == 1900.0


def test_emploee_of_the_month():
    employee = PremiumEmployee.create_hero()
    assert employee.pay_salary() == 0
