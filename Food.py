from GameObject import GameObject
from random import randint

class Food(GameObject):
    def __init__(self, x=2, y=2):
        super().__init__(x, y)
        self.food_type = randint(0, 4)

    def __str__(self):
        return 'F'

