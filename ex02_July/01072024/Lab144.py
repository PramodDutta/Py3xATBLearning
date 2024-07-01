# Method Overriding - Same name in the parent and child
# child always override the parent functions
# super means call my parent function

class Father:
    def home(self):
        print("1BHK")

class Son(Father):
    def home(self):
        super().home()
        print("No House")


pramod = Son()
pramod.home()

