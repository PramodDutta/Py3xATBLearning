# Decorators
# What is a Decorator?
# A decorator is essentially a function that takes another function as an argument
# returns a new function that usually extends the behavior

def my_decorator(func):
    def wrapper():
        print("Starting.....")
        print("****************")
        say_hello()
        print("****************")
        print("Ending")

    return wrapper()


@my_decorator
def say_hello():
    print("Say Hello")

