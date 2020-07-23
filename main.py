import pygame
import sys
import random

pygame.init()
# ---- INIT GAME CELL SIZE AND MARGIN FOR TOP WINDOW
CELL_SIZE = 20
GAME_FIELD_SIZE = 20
MARGIN_TOP = 80

# ------ COLORS ---------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
LIGHT_YELLOW = (255, 255, 224)
LIGHT_GRAY = (211, 211, 211)
WHITE_SMOKE = (245, 245, 245)
DEEP_SKY_BLUE = (0, 191, 255)
LIGHT_CYAN = (224, 255, 255)
GAINSBORO = (220,220,220)
SNAKE_COLOR = (46,139,87)
BACKGROUND_COLOR = LIGHT_CYAN


# ----- Init speed -----------
speed = pygame.time.Clock()

# ------ GAME FIELD -----------
SIZE = [2 * CELL_SIZE + GAME_FIELD_SIZE * CELL_SIZE + GAME_FIELD_SIZE,
        2 * CELL_SIZE + GAME_FIELD_SIZE * CELL_SIZE + GAME_FIELD_SIZE + MARGIN_TOP]
game_field = pygame.display.set_mode(SIZE)
game_field.fill(BACKGROUND_COLOR)
pygame.display.set_caption('Simple Snake')



# --- INIT VARIABLES
score = 0
speed_value = 1

# INIT FONTS
font = pygame.font.SysFont('arial', 48, bold=1)



class snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def is_inside(self):
        return 0 <= self.x <= GAME_FIELD_SIZE - 1 and 0 <= self.y <= GAME_FIELD_SIZE - 1
    def bump_body(snake_blocks):
        head_x = snake_blocks[-1].x
        head_y = snake_blocks[-1].y
        for i in range(len(snake_blocks) - 1):
            if head_x == snake_blocks[i].x and head_y == snake_blocks[i].y:
                return False
                break
            else:
                pass
        return True

def draw_game_cell(CELL_COLOR, cols, rows):
    pygame.draw.rect(game_field, CELL_COLOR, [CELL_SIZE + CELL_SIZE * cols + 1 * cols,
                                                 MARGIN_TOP + CELL_SIZE + CELL_SIZE * rows + 1 * rows,
                                                 CELL_SIZE, CELL_SIZE])


def food_generate(GAME_FIELD_SIZE):
    food_x = int(random.randint(0, GAME_FIELD_SIZE - 1))
    food_y = int(random.randint(0, GAME_FIELD_SIZE - 1))
    return food_x, food_y

def show_points(score, speed_value):
    score, speed_value = str(score), str(speed_value)
    score, speed_value = 'Score: ' + score, 'Speed: ' + speed_value
    game_field.blit(font.render(score, 1, WHITE), (20, 0))
    game_field.blit(font.render(speed_value, 1, WHITE), (250, 0))



snake_blocks = [snake(2, 1),snake(3, 1), snake(4, 1),snake(5, 1), snake(6, 1), snake(7, 1), snake(8, 1), snake(9, 1)]
# snake_blocks = [snake(2, 1),snake(3, 1), snake(4, 1)]
dx = 1
dy = 0
food_x, food_y = food_generate(GAME_FIELD_SIZE)
speed_value = 4

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Exit ok')
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dx != 0:
                dy = -1
                dx = 0
            if event.key == pygame.K_DOWN and dx != 0:
                dy = 1
                dx = 0
            if event.key == pygame.K_LEFT and dy != 0:
                dy = 0
                dx = -1
            if event.key == pygame.K_RIGHT and dy != 0:
                dy = 0
                dx = 1
            if event.key == pygame.K_LALT:
                print('LAlt')
                print(snake_blocks[0])
                last_cell = snake(snake_blocks[0].x, snake_blocks[0].y)
                snake_blocks.insert(0, last_cell)

    pygame.draw.rect(game_field, DEEP_SKY_BLUE, [0, 0, SIZE[0], MARGIN_TOP])
    show_points(score, speed_value)

    for rows in range(GAME_FIELD_SIZE):
        for cols in range(GAME_FIELD_SIZE):
            if (rows + cols) % 2 == 0:
                CELL_COLOR = GAINSBORO
            else:
                CELL_COLOR = WHITE
            draw_game_cell(CELL_COLOR, cols, rows)

    snake_head = snake_blocks[-1]
    if not snake_head.is_inside():
        print('exit')
        pygame.quit()
        sys.exit()
    for block in snake_blocks:
        draw_game_cell(SNAKE_COLOR, block.x, block.y)

    draw_game_cell(RED, food_x, food_y)
    new_head = snake(snake_head.x + dx, snake_head.y + dy)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    if not snake.bump_body(snake_blocks):
        print('babah')
        pygame.quit()
        sys.exit()



    if snake_blocks[-1].x == food_x and snake_blocks[-1].y == food_y:
        last_cell = snake(snake_blocks[0].x, snake_blocks[0].y)
        snake_blocks.insert(0, last_cell)
        food_x, food_y = food_generate(GAME_FIELD_SIZE)
        score += 1
        speed_value += speed_value/4


    pygame.display.flip()
    speed.tick(speed_value)



