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


class Bone(Toy):
    fun = 4
