from GameObject import GameObject

class Food(GameObject):
    def __init__(self, x=2, y=2):
        super().__init__(x, y)

    def __str__(self):
        return 'F'

