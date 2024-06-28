class VWOLogin:

    def __init__(self, email, password,name):
        self.__email = email
        self.__password = password
        self.name = name
        self.__name = "abc" #private

    def login_confirm(self):
        if self.__email == "abc@gmail.com" and self.__password == 123:
            print("Allowed")
        else:
            print("Not Allowed")


# This is end of class

page1 = VWOLogin("abc@gmail.com", 123,"Pramod")
print(page1.name)
#print(page1.__email)
page1.login_confirm()
# page1.__email = "??"
# page1.__password = "??"
