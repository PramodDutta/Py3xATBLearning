class Parent:
    gold = "2kg"

    def BHK2(self):
        print("2BHK")


class Child(Parent):

    def BHK3(self):
        print("3BHK")



child_object= Child()
child_object.BHK3()
child_object.BHK2()
print(child_object.gold)


father_obect_ref = Parent()
#father_obect_ref.BHK2()
#father_obect_ref.gold