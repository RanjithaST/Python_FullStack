class Test:
    def divide(self,a,b):
        try:
            result=a/b
            print("Result",result)
        except ZeroDivisionError:
            print("Error:Cannot be divided by zero")
        except Exception as e:
            print("An unexpected error occured:",str(e))
        finally:
            print("Exception of divide method is complete")
t=Test()
t.divide(10,0)