class Employee:
    def __init__(self):
        self.empName=None
        self.empRoll=None
emp=Employee()
print(emp)
print("**********BEFORE DATA ASSIGN**************")
print(emp.empName)
print(emp.empRoll)
emp.empName="John"
emp.empRoll=101
print("**********AFTER DATA ASSIGN**************")
print(emp.empName)
print(emp.empRoll)
emp1=Employee()
print(emp1)