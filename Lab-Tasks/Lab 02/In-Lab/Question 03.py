class BankAccount:
    def __init__(self, name, initialDeposit):
        self.name = name
        self.__balance = initialDeposit 

    def deposit(self, amount):
            self.__balance += amount
            print("Deposited ", amount, " New Balance " ,self.__balance)

    def withdraw(self, amount):
            self.__balance -= amount
            print("Withdrew", amount, "Remaining balance: ", self.__balance)

    def get_balance(self):
        return self.__balance

acc1 = BankAccount("Mutahir", 1000)

acc1.deposit(500)
acc1.withdraw(200)
print("Current Balance for ", acc1.name, " is ", acc1.get_balance())
