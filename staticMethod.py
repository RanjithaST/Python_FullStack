class DMART:
    @staticmethod #by using this decorator we can access method using both classname and object reference.
    #without this we get error if we call it through object reference
    def friskTheCustomer():
        print("Customer is checked and verified")

print("**********Excecuting static method***********")
DMART.friskTheCustomer()
d=DMART()
d.friskTheCustomer()
