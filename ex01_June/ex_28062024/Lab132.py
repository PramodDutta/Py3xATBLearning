class Password:
    def __init__(self, password):
        self.__password = password
        self.public_var = 10

    def get_pwd(self, is_auth):
        if is_auth:
            print(self.__password)
        else:
            print("Invalid password")

    def set_pwd(self, password):
        if password.endswith("9"):
            if len(password) > 10:
                self.__password = password
                print("Set to correct", self.__password)
            else:
                print("Not allowed, weak password")

pwd = Password("Hacker123")
pwd.get_pwd(True)
pwd.set_pwd("piuytrewqfghj9")