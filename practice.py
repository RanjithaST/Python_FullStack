class A:
    def verifyUser(func):
        def wrapper():
            print("Hi")
            func()
            print("Hi")
        return wrapper
    @verifyUser
    @verifyUser
    def start():
        print("Start")
A.start()