class Car:
    name = None

    def __init__(self):
        self.public_var = "public"
        self._protected_var = "protected123"
        self.__private_var = "pass@123"

    def __private_method(self):
        print("Protected!")

    def printName(self):
        self.__private_method()
        if self.__private_var == "123":
            print("Hi, 123")
        print("I am allowed public")

# This is end of the class

alto = Car()
alto.printName()
# alto.__private_var

