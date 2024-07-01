# Hierarchical Inheritance

# Father - Multiple Children

class Father:
    def BHK1(self):
        print("1BHK")


class Pramod(Father):
    def BHK2(self):
        print("2BHK")


class Amit(Father):
    def BHK3(self):
        print("3BHK")


class Lucky(Father):
    def no_house(self):
        print("NO house")


pramod = Pramod()
pramod.BHK1()
pramod.BHK2()

amit = Amit()
amit.BHK1()
amit.BHK3()
# amit.BHK2()? This belong to Pramod

lucky  = Lucky()
lucky.BHK1()
lucky.no_house()
#lucky.BHK2()


