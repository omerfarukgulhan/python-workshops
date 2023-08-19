class Animal():
    def __init__(self, name, number_of_legs, height, weight, sound):
        self.name = name
        self.number_of_legs = number_of_legs
        self.height = height
        self.weight = weight
        self.sound = sound

    def show_information(self):
        print("name: {}\nnumber of legs: {}\nheight: {}\nweight: {}".format(
            self.name, self.number_of_legs, self.height, self.weight))

    def make_sound(self):
        print(self.sound)

class Cat(Animal):
    pass

class Dog(Animal):
    pass

cat = Cat("Tekir",4,20,5,"Miyav")
dog = Dog("",4,65,15,"Hav Hav")

cat.show_information()
print("***********")
cat.make_sound()
print("***********")
print("***********")
dog.show_information()
print("***********")
dog.make_sound()