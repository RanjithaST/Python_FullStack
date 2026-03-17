class Test:
    def __init__(self):
        self.x=10 #public variable
        self.__y=20 #private variable
class RunTest:
    def run(self):
        test=Test()
        print("Public variable x",test.x)
        print("Private variable y",test.y)#Attribute error because __y is a private variable and it is stored as _Test__y in object dictionary by name mangling.
        print(test.__dict__) #{'x': 10, '_Test__y': 20}
        print("Private variable y",test._Test__y)
r=RunTest()
r.run()
