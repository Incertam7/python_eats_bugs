import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 640, 480
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Python Eats Bugs 🐛")
clock = pygame.time.Clock()

# Load Assets
SNAKE_IMG = pygame.image.load("assets/snake.png")
BUG_IMG = pygame.image.load("assets/bug.png")
EAT_SOUND = pygame.mixer.Sound("assets/eat.wav")

# Game variables
snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)
bug = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
score = 0

def draw_snake():
    for segment in snake:
        x, y = segment
        screen.blit(SNAKE_IMG, (x * CELL_SIZE, y * CELL_SIZE))

def draw_bug():
    x, y = bug
    screen.blit(BUG_IMG, (x * CELL_SIZE, y * CELL_SIZE))

def move_snake():
    global bug, score
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    if head == bug:
        EAT_SOUND.play()
        score += 1
        while True:
            bug = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if bug not in snake:
                break
    else:
        snake.pop()

def check_collision():
    head = snake[0]
    return (
        head in snake[1:] or
        head[0] < 0 or head[0] >= GRID_WIDTH or
        head[1] < 0 or head[1] >= GRID_HEIGHT
    )

def draw_score():
    font = pygame.font.SysFont("monospace", 20)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

# Main game loop
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != (0, 1):
        direction = (0, -1)
    elif keys[pygame.K_DOWN] and direction != (0, -1):
        direction = (0, 1)
    elif keys[pygame.K_LEFT] and direction != (1, 0):
        direction = (-1, 0)
    elif keys[pygame.K_RIGHT] and direction != (-1, 0):
        direction = (1, 0)

    move_snake()
    if check_collision():
        break

    draw_snake()
    draw_bug()
    draw_score()
    pygame.display.flip()
    clock.tick(10)
