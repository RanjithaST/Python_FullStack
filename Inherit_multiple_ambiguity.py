'''
class Father:
    def drive(self):
        print("Father knows to drive")
class Mother:
    def drive(self):
        print("Mother knows to drive")
    def cook(self):
        print("Mother knows to cook")
class Son(Father,Mother): #inherits father drive()
    def play(self):
        print("Son knows to play")
class Daughter(Mother,Father):#inherits mother drive()
    def read(self):
        print("Daughter knows to read")
s=Son()
s.play()
s.cook()
s.drive()
d=Daughter()
d.read()
d.cook()
d.drive()
'''
'''
Son knows to play
Mother knows to cook
Father knows to drive
Daughter knows to read
Mother knows to cook
Mother knows to drive
'''

class Father:
    pass
class Mother:
    def drive(self):
        print("Father knows to drive")
    def cook(self):
        print("Mother knows to cook")
class Son(Father,Mother): #Father dont have functionality so inherits from Mother
    def play(self):
        print("Son knows to play")
class Daughter(Mother,Father):#inherits mother drive()
    def read(self):
        print("Daughter knows to read")
s=Son()
s.play()
s.cook()
s.drive()
d=Daughter()
d.read()
d.cook()
d.drive()
'''
Son knows to play
Mother knows to cook
Father knows to drive
Daughter knows to read
Mother knows to cook
Father knows to drive
'''