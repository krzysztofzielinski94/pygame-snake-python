import pygame
from GameBoard import GameBoard

class SnakeGame:
    def __init__(self):
        self.board = GameBoard()


    def start_game(self):
        pass

    def update_game(self, direction):
        self.board.update_game_board(direction)

    def finish_game(self):
        pass

    def get_board(self):
        return self.board

# PYGAME 
pygame.init()
SCREEN_WIDTH = 384
SCREEN_HEIGHT = 384 

pygame.display.set_caption('Snake')
icon = pygame.image.load('./assets/icon.png')
pygame.display.set_icon(icon)

# colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_GREEN = (93, 206, 157)

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SQUARE_SIZE = 32
screen = pygame.display.set_mode(SCREEN_SIZE)

game = SnakeGame()
game.start_game()
board_size = game.get_board().get_board_size()

def draw_board():
    for c in range(board_size):
        for r in range(board_size):
            cell_value = game.get_board().get_board_cell(c, r)
            if cell_value == '#':
                pygame.draw.rect(screen, DARK_GREEN, (r*SQUARE_SIZE, c*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif cell_value == 'S':
                pygame.draw.rect(screen, BLACK, (r*SQUARE_SIZE, c*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            elif cell_value == 'F':
                pygame.draw.rect(screen, RED, (r*SQUARE_SIZE, c*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    pygame.display.update()

running = True
clock = pygame.time.Clock()
delta = 0.0
max_tps = 5.0 
snake_direction = 'RIGHT'

while running:
    screen.fill(BLACK)
    delta += clock.tick()/1000.0
    while delta > 1/max_tps:
        delta -= 1/max_tps
        game.update_game(snake_direction)
        print (snake_direction)
        draw_board()
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False    
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
            snake_direction = 'LEFT'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
            snake_direction = 'RIGHT'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_w:
            snake_direction = 'UP'
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            snake_direction = 'DOWN'