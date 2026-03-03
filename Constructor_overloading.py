class Calculate:
    def __init__(self):
        print("Constructor without parameter")
    def __init__(self,a,b): #this will be picked
        print("Constructor with parameter")
#c=Calculate()#Calculate.__init__() missing 2 required positional arguments: 'a' and 'b'
c=Calculate(10,20)
#pvm- ob class-new-without parameter(b4 creating ob in memory it checks with init) but init have parameters so error

'''
class Calculate:
    def __init__(self,a,b): 
        print("Constructor with parameter")
        return "Hi" #not allowed bcz default return statement is already there(early exit)
        return None
        return 
    def __init__(self):->#this will be picked
        print("Constructor without parameter")
   
#c=Calculate()

# c=Calculate(10,20)#error

'''