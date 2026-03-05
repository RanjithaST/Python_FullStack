'''
class A:
    def display(self):
        print("A is displaying")
class B(A):
    def run(self):
        print("B is running")
class C(A):
    def runner(self):
        print("C is runner")
class D(B,C):
    def sleep(self):
        print("C is sleeping")
d=D()
d.sleep()
d.run()
d.runner()
d.display()
'''
'''
C is sleeping
B is running
C is runner
A is displaying
'''
class Manager:
    def head(self):
        print("Manager is head")
class SeniorDeveloper(Manager):
    def senior(self):
        print("Senior developer is expert in tech")
class TeamLead(Manager):
    def lead(self):
        print("Team lead have good knowledge")
class TeamLead(SeniorDeveloper,TeamLead):
    def junior(self):
        print("I am junior developer")
t=TeamLead()
t.junior()
t.lead()
t.senior()
t.head()
