class Mammal:
    def walk(self):
        print("walk")

    def sound(self):
        print("sound!")

class Dog(Mammal):
    def sound(self): #overwirtes the class methods.
        print("bark!")

    def be_annoying(self):
        print("Dogs are lovely!")


class Cat(Mammal):
    def sound(self):
        print("meow!")


dog1 = Dog()
dog1.sound()
dog1.be_annoying()

cat1 = Cat()
cat1.sound()
cat1.walk()


