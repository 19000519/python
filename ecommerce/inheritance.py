#inheritance is all about making a parent classa and reuse many times in other classes

class Mammal:
    def walk(self):
        print("walk")

class Cat(Mammal):
    def annoy(self):
        print("i am tired")

class Dog(Mammal):
    def bark(self):
        print("bark")


dog1 = Dog()
dog1.walk()