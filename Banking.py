from Bank.Account_class import Account

class Customer():
    def __init__(self, first_name, last_name):
        self.__fn = first_name
        self.__ln = last_name

    def getFirstName(self):
        return self.__fn

    def getLastName(self):
        return self.__ln

    def getAccount(self):
        return Account.getBalance(self)

    def setAccount(self, amount):
        return Account.setBalance(self, amount)

class Bank():
    def __init__(self, bname):
        self.__name = bname

    def addCustomer(self, fn, ln):
        self.customer.append([fn, ln])

    def getNumOfCustomer(self):
        return len(self.customer)

    def getCustomer(self, index):
        return " ".join(self.customer[index])





