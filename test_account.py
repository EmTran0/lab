from pytest import *
from account import *


class Test:
    def setup_method(self):
        self.a1 = Account('John')
        self.a1.deposit(20.50)

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'

    def test_deposit(self):
        assert self.a1.deposit(10) == True
        assert self.a1.get_balance() == 30.50
        assert self.a1.deposit(6.50) == True
        assert self.a1.get_balance() == 37.00
        assert self.a1.deposit(0) == False
        assert self.a1.deposit(-1) == False
        assert self.a1.deposit(-6.50) == False

    def test_withdraw(self):
        assert self.a1.withdraw(10) == True
        assert self.a1.get_balance() == 10.50
        assert self.a1.withdraw(6.50) == True
        assert self.a1.get_balance() == 4.00
        assert self.a1.withdraw(0) == False
        assert self.a1.withdraw(-1) == False
        assert self.a1.withdraw(-6.50) == False
