'''
Zaimplementuj klasę CashMachine umożliwiającą wpłacanie i wypłacanie pieniędzy. Zadbaj o to, aby stan bankomatu
przetwarzany był w zmiennych prywatnych.
Przykład użycia:
>> cach_machine = CashMachine()
>> cash_machine.is_available()
False
>> cash_machine.put_money([200, 100, 100, 50])
>> cash_machine.is_available()
True
>> cash_machine.withdraw_money(150)
[100, 50]
'''


class CashMachine:
    def __init__(self):
        self._bills = {}

    def is_available(self):
        return sum(self._bills.values()) > 0

    def put_money(self, list_of_money):
        for bill in list_of_money:
            self._bills[bill] = self._bills.get(bill, 0) + 1

    def withdraw_money(self, amount):
        list_of_bills = sorted(self._bills.keys(), reverse=True)
        ret_value = []  # return value - zwyczajowa nazwa zwracanej zmiennej
        for bill in list_of_bills:
            while self._bills[bill] > 0 and amount - bill >= 0:
                ret_value.append(bill)
                self._bills[bill] -= 1
                amount -= bill
        if amount == 0:
            return ret_value
        else:
            self.put_money(ret_value)
            return []

# dodać do kodu, aby przeszło ostatnie testy

def test_cash_machine_initialization():
    cash_machine = CashMachine()
    assert cash_machine._bills == {}


def test_cash_is_available_false():
    cash_machine = CashMachine()
    assert not cash_machine.is_available()


def test_put_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.is_available()


def test_cash_machine_withdraw_money():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(150) == [100, 50]


def test_cash_machine_withdraw_money_more_than_available():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(500) == []


def test_cash_machine_withdraw_money_not_fullfilled_withdrawal():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    cash_machine.withdraw_money(500)
    assert cash_machine.is_available()


def test_cash_machine_withdraw_money_wrong_amount():
    cash_machine = CashMachine()
    cash_machine.put_money([200, 100, 100, 50])
    assert cash_machine.withdraw_money(330) == []


def test_cash_machine_withdraw_money_good_amount_wrong_withdrawal():
    cash_machine = CashMachine()
    cash_machine.put_money([50, 20, 20, 20, 20, 20])
    assert cash_machine.withdraw_money(100) == [20, 20, 20, 20, 20]
    cash_machine = CashMachine()
    cash_machine.put_money([200, 50, 20, 20, 20, 20, 20])
    assert cash_machine.withdraw_money(300) == [200, 20, 20, 20, 20, 20]
