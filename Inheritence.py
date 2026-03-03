class Animal:
    zoo="City zoo"
    def __init__(self):
        self.name="Animal"
    def sleep(self):
        print("Animal is sleeping")

    @classmethod
    def eat(cls):
        print("Animal is eating")

    @staticmethod
    def dance():
        print("Animal is dancing")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

dog1=Dog()
Dog.eat()
dog1.sleep()
Dog.dance()
dog1.bark()
print(Dog.zoo)
print(dog1.zoo)
