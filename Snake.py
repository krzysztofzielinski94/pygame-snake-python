from GameObject import GameObject


class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.directions = {
            'UP'    : [-1, 0],
            'DOWN'  : [1, 0],
            'RIGHT' : [0, 1],
            'LEFT'  : [-1, 0]
        }

        self.direction = self.directions['RIGHT']


    def __str__(self):
        return 'S'