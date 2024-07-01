# Method Overloading:
# Python does not support method overloading
# in the traditional sense.

# Method - overloading - Not supported!

class MathUtil(object):
    def add(self, a, b=0, c=0):
        return a + b + c

    # def add(self,a,b):
    #     pass
    #
    # def add(self,a,b,c,d):
    #     pass

math = MathUtil()
op0 = math.add(1)
op1 = math.add(1, 2)
op2 = math.add(1, 2, 3)
print(op0)
print(op1)
print(op2)
