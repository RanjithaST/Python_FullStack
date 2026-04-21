class InsufficientBalanceException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg
balance=1000
class Withdraw:
    def withdrawal(self,amount):
        if amount>balance:
            raise InsufficientBalanceException("Insuffient balance")
        else:
            print(f"{amount} withdrawn successfully")
w=Withdraw()
try:
    w.withdrawal(1100)
except InsufficientBalanceException as i:
    print(i) #with init only this works
    print(i.msg)#with super and without any init it works
    print(i.args)#with super and without any init it works
    
'''
Case	         print(e)	e.msg	e.args
Without __init__	✅	❌	✅
With custom __init_ ❌	✅	❌
With super()	    ✅	✅	✅
'''