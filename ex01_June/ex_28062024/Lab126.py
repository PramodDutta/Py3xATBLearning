# Encapsulation -
# bind the data variables with the methods
# Data Member - / Class Variables
# Methods - Def function within the class
# Wrapping or binding the data variables with the methods - Encapsulation.

# Hide the data members(class variables, instance variables) by using only the methods.

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when a OBject is created")

    def change_password(self):
        self.password = "345"
# This is end of the class

xuv = Car()
xuv.password = "345"
