"""Interactable class definitions."""


class Toy:
    fun: int

    def play(self):
        return self.fun


class Food:
    nutrition: int

    def eat(self):
        return self.nutrition


class Ball(Toy):
    fun = 10


class Bone(Toy, Food):
    fun = 4
    nutrition = 2


class Biscuit(Food):
    nutrition = 4
