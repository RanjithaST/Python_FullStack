class LoveException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
        self.msg=msg
class A:
    def expressLove(self,bfname):
        if bfname=="Yash":
            print("I am your fan, Lets meet")
        else:
            raise LoveException("Not interested")
a=A()
try:
    a.expressLove("Yash")
except LoveException as e:
    print(e.msg)
else:
    print("Accepted")#else execeuted only if try executed successfully
finally:
    print("Marriage happens!!!")#independent of try and except block execution