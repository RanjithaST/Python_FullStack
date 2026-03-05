class Father:
    def drive(self):
        print("Knows to drive")
class Mother:
    def cook(self):
        print("Knows to cook")
class Son(Father,Mother):
    def play(self):
        print("Son knows to play")
s=Son()
s.play()
s.cook()
s.drive()