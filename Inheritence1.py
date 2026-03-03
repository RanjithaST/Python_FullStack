class Car:
    def __init__(self):
        self.brand="MG"
class Windsor(Car):
    pass
w=Windsor()
print(w)
print(w.__dict__)#{} initially then after mro -> {'brand': 'MG'}
print(w.__class__.__mro__)
print(Windsor.__mro__)#(<class '__main__.Windsor'>, <class '__main__.Car'>, <class 'object'>)