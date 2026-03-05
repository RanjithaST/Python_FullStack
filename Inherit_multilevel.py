class Animal:
    def eat(self):
        print("All Animals eat")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class BabyDog(Dog):
    def weep(self):
        print("Baby dog weeps")
print("*************Baby Dog Properties****************")
b=BabyDog()
b.weep()
b.bark()
b.eat()
print("****************Dog properties*********************")
d=Dog()
d.bark()
d.eat()
print("**************Animal properties*********************")
a=Animal()
a.eat()

