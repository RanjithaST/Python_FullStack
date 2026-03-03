'''
class Car:
    def assignBrand(self):
        self.brand="MG"
class Windsor(Car):
    def __init__(self):
        self.engineCountry='British'
w=Windsor()
print(w)
print(w.__dict__)#{} initially then after mro -> {'brand': 'MG'}
w.assignBrand()
print(w.__dict__)
{'engineCountry': 'British'}
{'engineCountry': 'British', 'brand': 'MG'}
'''
class Car:
    def __init__(self):
        self.model=2025
    def assignBrand(self):
        self.brand="MG"
class Windsor(Car):
    def __init__(self):
        self.engineCountry='British'
w=Windsor()
print(w)
print("Before",w.__dict__)#{} initially then after mro -> {'brand': 'MG'}
w.assignBrand()
print("After",w.__dict__)

'''
Before {'engineCountry': 'British'}
After {'engineCountry': 'British', 'brand': 'MG'}
'''