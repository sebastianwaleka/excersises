'''
Zaimplementuj klasę Employee umożliwiającą rejestrowanie czasu pracy oraz wypłacanie pensji na podstawie
zadanej stawki godzinowej. Jeżeli pracownik będzie pracował więcej niż 8 godzin (podaczas pojedynczej rejestracji
czasu) to kolejne godziny policz jko nadgodziny (z podwójną stawką godzinową).
Przykład użycia:
>> employee = Employee('Jan', 'Nowak', 100.0)
>> employee.register_time(5)
>> employee.pay_salary()
500.0
>> employee.pay_salary()
0.0
>> employee.register_time(10)
>> employee.pay_salary()
1200.0
'''
import pytest


class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.time = 0

    def register_time(self, time):
        self.time += time
        if time > 24:
            raise ValueError('Day has only 24h')

    def pay_salary(self):
        if self.time <= 8:
            pay = self.time * self.salary
        elif self.time > 8:
            pay = 8 * self.salary + ((self.time - 8) * (self.salary * 2))
        self.time = 0
        return pay


def test_employee_exist():
    employee = Employee('Jan', 'Nowak', 100.0)
    assert employee.first_name == 'Jan'
    assert employee.last_name == 'Nowak'
    assert employee.salary == 100.0


def test_pay_salary_and_pay_salary():
    employee = Employee('Jan', 'Nowak', 100.0)
    employee.register_time(5)
    assert employee.pay_salary() == 500.00
    assert employee.pay_salary() == 0.00
    employee.register_time(10)
    assert employee.pay_salary() == 1200.0
    assert employee.pay_salary() == 0.0
    employee.register_time(5)
    employee.register_time(5)
    assert employee.pay_salary() == 1200.0
    assert employee.pay_salary() == 0.0


def test_value_error():
    employee = Employee('Jan', 'Nowak', 100.0)
    with pytest.raises(ValueError) as e:
        employee.register_time(25)
