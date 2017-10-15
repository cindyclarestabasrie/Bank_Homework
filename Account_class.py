class Account:
    def __init__(self):
        self.__balance = 0

    def setBalance(self, amount):
        self.__balance = amount

    def getBalance (self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            return False

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            return False

    def transfer(self, account, amt):
        self.__balance = self.__balance - amt
        account.__balance = account.__balance + amt
        return "Transfer Successful!"
