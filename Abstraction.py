from abc import ABC,abstractmethod
@abstractmethod
class Payment(ABC):
    def makePayment(self,amount):
        pass
class CreditCardDetails(Payment):
    def makePayment(self, amount):
        print(f"Processing credit card payment of {amount}...")
class UPI(Payment):
    def makePayment(self, amount):
        print(f"Processing UPI payment of {amount}...")
c=CreditCardDetails()
c.makePayment(100)
u=UPI()
u.makePayment(200)
'''
p=Payment() -> Error: We cant able to create object of abstract class because of the presence of
abstractn(incomplete) method.even if we dont have method also we can create object.
1.All abstarct class methods (maybe even 100) must be overriden in the subclass.
2.subclass may have other methods but abstract methods must be overriden.
3.abstrat class can have concreet method.and concreet method is not mandatory to override in subclass.
4.we even cant create object of abstract class if we have both abstract method + concrete method
5.we can create object of abstract class if there is only concrete method or no method at all.
6.100% abstration means abstarct class only with abstarct method
7.one abstract class can be inherited by another abstract class.
class A(ABC)
class B (A)
class B(ABC,B) ->leads to mro conflit
we cant create object of A as well as B
even B dont have abstract method we cant able to create as it inherts abstract class A's abstract method
'''