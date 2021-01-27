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

# assets 
snake_assets = pygame.image.load('./assets/SnakeAssets.png')
asset_rect = snake_assets.get_rect()

def draw_snake(name, direction, x, y):
    if name == 'HEAD' and direction == 'RIGHT':
        screen.blit(snake_assets, (x, y), (0, 32, 32, 32))
    elif name == 'BODY' and direction == 'RIGHT':
        screen.blit(snake_assets, (x, y), (128, 0, 32, 32))
    elif name == 'HEAD' and direction == 'LEFT':
        screen.blit(snake_assets, (x, y), (96, 64, 32, 32))
    elif name == 'BODY' and direction == 'LEFT':
        screen.blit(snake_assets, (x, y), (64, 64, 32, 32))
    elif name == 'HEAD' and direction == 'UP':
        screen.blit(snake_assets, (x, y), (0, 64, 32, 32))
    elif name == 'BODY' and direction == 'UP':
        screen.blit(snake_assets, (x, y), (96, 32, 32, 32))
    elif name == 'HEAD' and direction == 'DOWN':
        screen.blit(snake_assets, (x, y), (32, 0, 32, 32))
    elif name == 'BODY' and direction == 'DOWN':
        screen.blit(snake_assets, (x, y), (0, 0, 32, 32))


def draw_food(name, x, y):
    if name == 'food':
        screen.blit(snake_assets, (x, y), (32, 128, 32, 32))

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARK_GREEN = (93, 206, 157)

font = pygame.font.SysFont("monospace", 40)
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
SQUARE_SIZE = 32
screen = pygame.display.set_mode(SCREEN_SIZE)

game = SnakeGame()
game.start_game()
board_size = game.get_board().get_board_size()


def draw_board(snake_direction):
    for c in range(board_size):
        for r in range(board_size):
            cell_value = game.get_board().get_board_cell(c, r)
            pygame.draw.rect(screen, DARK_GREEN, (r*SQUARE_SIZE, c*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            if cell_value == 'S':
                cell_type = game.get_board().snake.body_part(c, r)
                draw_snake(cell_type, snake_direction, r*SQUARE_SIZE, c*SQUARE_SIZE)
            elif cell_value == 'F':
                draw_food('food', r*SQUARE_SIZE, c*SQUARE_SIZE)

    label = font.render(str(game.get_board().snake.lenght-2), 1, BLACK)
    screen.blit(label, (0, 0))    
    pygame.display.update()

def draw_game_over():
    end_game_text = 'GAME OVER'
    label = font.render(end_game_text, 1, WHITE)
    screen.blit(label, (0, 0))
    end_game_text = 'POINTS: ' + str(game.get_board().snake.lenght-2)
    label = font.render(end_game_text, 1, WHITE)
    screen.blit(label, (0, 50))
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
        if game.get_board().game_over == True:
            draw_game_over()
        else:
            game.update_game(snake_direction)
            draw_board(snake_direction)

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