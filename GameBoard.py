from Snake import Snake
from Food import Food
from random import randint

class GameBoard:
    def __init__(self):
        self.size = 12
        self.game_board = list()

        self.create_game_board()
        self.snake = Snake(5,5)
        self.food = Food(2, 2)
        self.show_game_board()

    def create_game_board(self):
        for _ in range(self.size):
            temp = list()
            for _ in range(self.size):
                temp.append('#')
            self.game_board.append(temp)

    def show_game_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] in self.snake.body:
                    print ('S', end=' ')
                elif i == self.food.x and j == self.food.y:
                    print ('F', end=' ')
                else:
                    print ('#', end=' ')
            print ('')

    def update_game_board(self, direction):
        self.snake.update_position(direction)
        if self.food.x == self.snake.x and self.food.y == self.snake.y:
            self.snake.update_length()
            # create new food 
            self.food = Food(6, 6)
        
        self.show_game_board()

    def get_board_cell(self, i, j):
        if [i, j] in self.snake.body:
            return 'S'
        elif i == self.food.x and j == self.food.y:
            return 'F'
        else:
            return '#'

    def get_board_size(self):
        return self.size

