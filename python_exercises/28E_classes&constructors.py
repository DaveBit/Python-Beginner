class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi I am {self.name}")


Person1 = Person("Antonio")
Person1.talk()

Person2 = Person("John Wick")
Person2.talk()