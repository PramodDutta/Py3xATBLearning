class Person:
    # Class Variables / instance variables
    name = "Amit"
    age = None

    def walk(self):
        a = 10 # Local Varaible
        print("I am am Method")
        print("Hi", self.age)


amit = Person()
amit.walk()
