from Snake import Snake
from Food import Food

class GameBoard:
    def __init__(self):
        self.size = 12
        self.game_board = list()
        self.create_game_board()
        
        # create player
        self.snake = Snake(5, 5)
        self.update_game_board(5, 5, self.snake)
        
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
                print (self.game_board[i][j], end=' ')
            print ('')

    def update_game_board(self, i, j, value):
        self.game_board[i][j] = value

    

