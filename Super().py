class Parent:
    x=10
    def __init__(self):
        print("I am in A's init")
    def show(self):
        print("I am in A class")
class Child(Parent):
    def show(self):
        super().__init__()
       # self.show()  #if child and parent both have same method means it wont work so we use self
        '''
          self.show()  #if child and parent both have same method means it wont work so we use self
    ^^^^^^^^^^^
  [Previous line repeated 995 more times]
  File "d:\Python\Super().py", line 9, in show
    super().__init__()
RecursionError: maximum recursion depth exceeded
        '''
        super().show()
        print(super().x) #class variables can be accessed bcz it is stored in class memory
        #print(super().y) # instance variables cant be accessed as thy are stored in obj memory
        #super() alone no output
        s=super() 
        print(s) #<super: <class 'Child'>, <Child object>>
c=Child()
c.show()

# I am in A's init - This init during child object creation
# I am in A's init - due to super()__init__
# I am in A class
# <super: <class 'Child'>, <Child object>>