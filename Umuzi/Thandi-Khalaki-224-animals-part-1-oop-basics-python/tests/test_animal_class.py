from src.animal_class import *
import pytest


class TestsAnimal():
    def test_dog_sound(self):
        tom = Dog("Tom")
        assert tom.sound() == "Bark", "Incorrect dog sound"

    def test_dog_eat(self):
        tom = Dog("Tom")
        assert tom.eats() == "Food", "Incorrect dog eats"

    def test_cat_eat(self):
        tim = Cat("Tim")
        assert tim.sound() == "Meow", "Incorrect cat sound"

    def test_cat_sound(self):
        tim = Cat("Tim")
        assert tim.eats() == "Food","Incorrect cat eats"
