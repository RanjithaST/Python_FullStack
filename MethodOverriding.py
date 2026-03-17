'''
class Animal:
    def makeSound(self):
        print("All animals make sound")
class Dog(Animal):
    def makeSound(self): #method overriding
        print("Bow Bow")

  #  def makeSound(self,name="Pinky"): #Not method overriding.Its a different method
   #     print("Bow Bow",name)
    
 #   def makeSound(self,name): #This last method will be considered and its not overriding.its different method
  #      print("Bow Bow",name)
dog1=Dog()
dog1.makeSound()
an=Animal()
print(dog1.makeSound.__func__==an.makeSound.__func__)
'''
class Animal:
    def makeSound(self):
        print("All animals make sound")
class Dog(Animal):#inheritance is required bcz the inside method belongs only to dog.if we dont have inside anything the t should inherit from animal.
    pass

dog1=Dog()
dog1.makeSound()
an=Animal()
print(dog1.makeSound.__func__==an.makeSound.__func__)#refers to same method