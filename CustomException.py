class InvalidAgeException(Exception):
    def __init__(self):
        pass
class CheckAge:
    def validate(self,age):
        if(age>=18):
            print("Age is valid for voting")
        else:
            raise InvalidAgeException()
c=CheckAge()
try:
    c.validate(17)
except InvalidAgeException as e:
    print(f"Invalid Age Exception",{e})