class A:
    def display(self,*args):
        print(args)
    def show(self,**kwargs):
        print(kwargs)
a=A()
a.display(1,2,3,4,5) #(1, 2, 3, 4, 5)
a.show(sid=101,sname="Ram",sno=9018291820) #{'sid': 101, 'sname': 'Ram', 'sno': 9018291820}
'''
a.show(sid=101,sid=102,sname="Ram",sno=9018291820)
 a.show(sid=101,sid=102,sname="Ram",sno=9018291820)
                ^^^^^^^
SyntaxError: keyword argument repeated: sid
'''
