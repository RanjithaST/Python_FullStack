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
# class Test:
#     a=int(input("Enter the value of a:"))
#     b=int(input("Enter the valur of b:"))
#     def divide(self):
#         try:
#             c=Test.a/Test.b #RISKIER
#             print(c)
#             print(type(c))
#         except Exception:
#             print("Please enter a valid denominator")
#         except Exception:
#             print("If nothing works,I works")
# t=Test()
# t.divide()

# class Calculate:
#     def divide(self,a,b):
#         try:
#             print("I am in the Outer try block")#if something happens here then outer except and it dont go inside inner loop
#             try:
#                 c=a/b #error
#                 print(c)
#             except ZeroDivisionError:#handled
#                 print("Denominator cannot be zero")
#         except Exception:#fail safe
#             print("All is well")
# c=Calculate()
# c.divide(10,0)

class Calculate:
    def divide(self,b):
        try:
            a=int(input("Enter the value of a:"))#if something happens here then outer except and it dont go inside inner loop
            try:
                c=a/b #error
                print(c)
            except ZeroDivisionError:#handled
                print("Denominator cannot be zero")
        except Exception:#fail safe
            print("Please enter number value")
c=Calculate()
c.divide(10)