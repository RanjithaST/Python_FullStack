'''
class Test:
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the valur of b:"))
    def divide(self):
        try:
            c=Test.a/Test.b #RISKIER
            print(c)
            print(type(c))
        except ZeroDivisionError:
            print("Please enter a valid denominator")
t=Test()
t.divide()
'''
'''
Before handling exception:

Enter the value of a:10
Enter the valur of b:0
Traceback (most recent call last):
  File "d:\Python\ExceptionHandling.py", line 8, in <module>
    t.divide()
  File "d:\Python\ExceptionHandling.py", line 5, in divide  
    c=Test.a/Test.b
      ~~~~~~^~~~~~~
ZeroDivisionError: division by zero

**************************************************************************
After exception handling:

Enter the value of a:10
Enter the valur of b:0
Please enter a valid denominator
'''

#Multiple except blocks
class Test:
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the valur of b:"))
    def divide(self):
        try:
            c=Test.a/Test.b #RISKIER
            print(c)
            print(type(c))
        except Exception:
            print("Please enter a valid denominator")
        except Exception:
            print("If nothing works,I works")
t=Test()
t.divide()