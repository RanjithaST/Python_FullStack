class Student:
    def __init__(self):
        self.stuId=101
        self.__marks=50
    def getStuMarks(self):
        return self.__marks
    def setStuMarks(self,marks):
        if marks>=0 and marks<=100:
            self.__marks=marks
            print("Marks updated successfully. Current Marks:",self.getStuMarks())
        else:
            print("Invalid marks")
class Teacher:
    #pass by reference
    def modifyMarks(self,studentObjectAddress,marks):
        studentObjectAddress.setStuMarks(marks)
s=Student()
print("***Initial marks***")
print(s.getStuMarks())
print("***Modify marks***")
t=Teacher()
t.modifyMarks(s,80)
'''
***Initial marks***
50
***Modify marks***
Marks updated successfully. Current Marks: 80
'''
