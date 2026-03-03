class Car:
    def assignBrand(self):
        self.brand="MG"
class Windsor(Car):
    pass
w=Windsor()
print(w)
print(w.__dict__)#{} initially then after mro -> {'brand': 'MG'}
w.assignBrand()
print(w.__dict__)