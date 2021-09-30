class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"sound...")

    def eats(self):
        return "Food"


class Dog(Animal):
    def sound(self):
        return f"Bark"


class Cat(Animal):
    def sound(self):
        return f"Meow"


class Home:
    def __init__(self, pets=[]):
        self.pets = pets

    def adopt_pet(self, animal):
        if animal in self.pets:
            raise Exception("A house cannot adopt the same pet more than once")
        self.pets.append(animal)

    def make_all_sounds(self):
        for animal in self.pets:
            print(animal.sound())


if __name__ == "__main__":
    tom = Dog("Tom")
    print(tom.eats())
    print(tom.sound())
    tim = Cat("Tim")
    print(tim.eats())
    print(tim.sound())
    home = Home()
    home.adopt_pet(tim)
    home.adopt_pet(tom)
    home.make_all_sounds()
