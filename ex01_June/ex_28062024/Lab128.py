class MyClass:
    def __init__(self):
        self.name = "Amit"
        self._email = "amit@gmail.com"

    def public_func(self):
        print("Public Func()")

    def __private_func(self):
        print("You can only access me via a another method,This is private")

    def public_fn_private(self):
        self.__private_func()
        print(self._email)

# Security -> Not everyone can access your variables/methods, f(n)
a = MyClass()
a.public_func()
a.public_fn_private()