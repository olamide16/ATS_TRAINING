class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Cat(Pet):
    def speak(self):
        print("Moew")


class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Tim", 19)
p.show()
c = Cat("Bill", 18)
d = Dog("Hill", 26)
d.show()
c.show()
