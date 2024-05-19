class BankAccount:
    def __init__(self, accountnum, accounttype, ifsccode, name, balance):
        print("This method was called automatically when the class is created")
        self.accountnum = accountnum
        self.accounttype = accounttype
        self.ifsccode = ifsccode
        self.name = name
        self.balance = balance

    def display(self):
        print(self.accountnum)
        print(self.accounttype)
        print(self.ifsccode)
        print(self.name)
        print(self.balance)

    def checkbalance(self):
        print(self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount


obj1 = BankAccount(accountnum=1234567890, accounttype="Savings", ifsccode="KKBK00120", name="Moulali", balance=100000.00)
obj1.display()
obj1.checkbalance()
obj1.withdraw(1000)
obj1.checkbalance()
obj1.deposit(2000)
obj1.checkbalance()
