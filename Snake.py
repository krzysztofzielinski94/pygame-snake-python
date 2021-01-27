from GameObject import GameObject

class Snake(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.directions = {
            'UP'    : [-1, 0],
            'DOWN'  : [1, 0],
            'RIGHT' : [0, 1],
            'LEFT'  : [0, -1]
        }

        self.lenght = 2
        self.body = [[self.x, self.y], [self.x, self.y]]
        
    def update_position(self, direction, size):
        del self.body[0]
        self.x = (self.directions[direction][0] + self.x) % size
        self.y = (self.directions[direction][1] + self.y) % size
        if [self.x, self.y] in self.body:
            self.body.append([self.x, self.y])
            return True
        self.body.append([self.x, self.y])
        return False

    def update_length(self):
        self.lenght += 1
        self.body.append([self.x, self.y])

    def __str__(self):
        return 'S'

    def body_part(self, x, y):
        if [x, y] == self.body[self.lenght-1]:
            return 'HEAD'
        else:
            return 'BODY'