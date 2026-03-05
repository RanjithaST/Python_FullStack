class Animal:
    def eat(self):
        print("All animals eat")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class Cat(Animal):
    def meow(self):
        print("Cat meows")
class Lion(Animal):
    def roar(self):
        print("Lion roars")
print("****************Dog properties*********************")
d=Dog()
d.bark()
d.eat()
print("****************Dog properties*********************")
c=Cat()
c.meow()
c.eat()
print("****************Dog properties*********************")
l=Lion()
l.roar()
l.eat()
print("**************Animal properties*********************")
a=Animal()
a.eat()

