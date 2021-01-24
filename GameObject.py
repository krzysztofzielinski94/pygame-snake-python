from random import randint

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def random_object(self, size, without):
        new_x = randint(0, size)
        new_y = randint(0, size)
        
        return [new_x, new_y]
        
            
    def __str__(self):
        print ('#')

    