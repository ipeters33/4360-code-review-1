class BankingException(Exception):
    pass

class InsufficientFundsException(BankingException):
    def message(self):
        return 'An error occurred: Insufficent Funds'

class InvalidAccountNumberException(BankingException):
    def message(self):
        return "An error occurred: Invalid Account Number"
    
class InvalidNumberException(BankingException):
    def message(self):
        return "An error occurred: Invalid Amount to Deposit, please enter a number above 0."