class Dog:
    def __init__(self, name="Default", id="99"):
        self.name = name
        self.id = id

    def sleep(self):
        print("Who is sleeping ->" + self.name)


dog1 = Dog("Chow", "1")
dog2 = Dog("Mow", "2")
dog3 = Dog()


print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')
print(f'{dog3.name} has ID {dog3.id}')

dog1.sleep()
dog2.sleep()
dog3.sleep()
