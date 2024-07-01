class A:
    def method(self):
        return "Method A"

class B:
    def method(self):
        return "Method B"


# class C(A,B):
#     pass

class C(B,A):
    pass


c = C()
print(c.method())