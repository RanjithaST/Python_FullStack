class BookMyShow:
    def makePayment(self,paymentType):#paymentType is local variable as it is declared inside method signature and stored in stack whose reference is stored in class object memory
        print(paymentType,"Payment is successful")#after this line execution it will be erased from stack memory
    def makePayment1(self,paymentType):
        self.type=paymentType
        print(self.type,"Payment is successful")
b=BookMyShow()
#b.makePayment()#error
b.makePayment("Card")
b.makePayment("UPI")
b.makePayment(None)
print("*********************************************************")
b.makePayment1("Card")
b.makePayment1("UPI")
b.makePayment1(None)
'''
b.type="Internet banking"
print(b.__dict__)
b.makePayment(b.type)

Not recommended as we already have paymentType as a parameter
'''

