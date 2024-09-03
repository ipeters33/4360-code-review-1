from exceptions import InsufficientFundsException
from exceptions import InvalidNumberException

class Account:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            raise InsufficientFundsException
    
    def deposit(self, amount):
        if (amount <= 0):
            raise InvalidNumberException
        else:
            self.balance += amount
            return self.balance

