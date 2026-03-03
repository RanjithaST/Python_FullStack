class Calculate:
    def add(self):#this will not be picked
        x=10
        y=20
        z=x+y
    def add(self,a,b):#this will not be picked
        return a+b
    def add(self,x,y): #this will be picked
        a=x
        b=y
        c=x+y
        return c
c=Calculate()
print(c.add(10,20))