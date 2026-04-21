class Test:
    def add(self,b):
        a=int(input("Enter 'a' value:"))#passing 10.5 and making it to convert into int gives error as 10.5 is float
        print(type(a))
        #a=input("Enter 'a' value")
        #a1=int(a) or a=int(a)-->overriding previous variable
        c=a+b
        print(c)
t=Test()
t.add(30)
#concatination happens only in string.int+string=string(but gives error as different type)