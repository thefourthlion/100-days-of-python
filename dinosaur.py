import pygame
import random

# Window dimensions
WIDTH = 800
HEIGHT = 300

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player dimensions
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_INITIAL_X = 50
PLAYER_INITIAL_Y = HEIGHT - PLAYER_HEIGHT - 50
PLAYER_JUMP_SPEED = 10
PLAYER_GRAVITY = 0.6

# Obstacle dimensions
OBSTACLE_WIDTH = 20
OBSTACLE_HEIGHT = 50
OBSTACLE_MIN_DISTANCE = 300
OBSTACLE_MAX_DISTANCE = 600
OBSTACLE_SPEED = 5

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Google Dinosaur Game")
clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load("dino.png")
player_img = pygame.transform.scale(player_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
obstacle_img = pygame.image.load("cactus.png")
obstacle_img = pygame.transform.scale(obstacle_img, (OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

def draw_player(x, y):
    screen.blit(player_img, (x, y))

def draw_obstacle(x, y):
    screen.blit(obstacle_img, (x, y))

def is_collision(player_x, player_y, obstacle_x, obstacle_y):
    if player_x + PLAYER_WIDTH >= obstacle_x and player_x <= obstacle_x + OBSTACLE_WIDTH:
        if player_y + PLAYER_HEIGHT >= obstacle_y and player_y <= obstacle_y + OBSTACLE_HEIGHT:
            return True
    return False

def game():
    player_x = PLAYER_INITIAL_X
    player_y = PLAYER_INITIAL_Y
    player_y_change = 0

    obstacle_x = WIDTH
    obstacle_y = HEIGHT - OBSTACLE_HEIGHT - 50

    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_y == PLAYER_INITIAL_Y:
                        player_y_change = -PLAYER_JUMP_SPEED

        player_y += player_y_change
        player_y_change += PLAYER_GRAVITY

        if player_y >= PLAYER_INITIAL_Y:
            player_y = PLAYER_INITIAL_Y
            player_y_change = 0

        screen.fill(WHITE)
        draw_player(player_x, player_y)
        draw_obstacle(obstacle_x, obstacle_y)

        obstacle_x -= OBSTACLE_SPEED

        if obstacle_x <= -OBSTACLE_WIDTH:
            obstacle_x = WIDTH + random.randint(OBSTACLE_MIN_DISTANCE, OBSTACLE_MAX_DISTANCE)
            score += 1

        if is_collision(player_x, player_y, obstacle_x, obstacle_y):
            running = False

        # Display score
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(text, (10, 10))

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Start the game
game()
