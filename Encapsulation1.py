class ATM:
    def __init__(self):
        self.__balance=100
    def getBalance(self):
        return self.__balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
        else:
            print("Invalid Transaction")
    def withdraw(self,amount):
        if amount>=0 and amount<self.__balance:
            self.__balance-=amount
        else:
            print("Invalid Transaction")
a=ATM()
print("Initial Balance")
print(a.getBalance())
print("Balance after deposit")
a.deposit(500)
print(a.getBalance())
print("Balance after withdraw")
a.withdraw(200)
print(a.getBalance())

'''
Initial Balance
100
Balance after deposit
600
Balance after withdraw
400
'''
