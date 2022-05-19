"""Dog Class definition."""


class Dog:
    happiness = 0
    hunger = 0

    def play(self):
        self.happiness += 2
        self.hunger += 2

    def play_with(self, toy):
        self.happiness += toy.play()
        self.hunger += 2

    def eat(self, food):
        self.hunger -= food.eat()
        self.hunger = self.hunger if self.hunger >= 0 else 0
