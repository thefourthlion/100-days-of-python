import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 640, 480
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up game parameters
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_RADIUS = 5
PADDLE_SPEED = 5
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Set up the paddles and ball
left_paddle = pygame.Rect(0, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)

# Set up ball direction
ball_direction = pygame.Vector2(-1, 1).normalize()

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Get the state of the keys
    keys = pygame.key.get_pressed()

    # Update left paddle position
    if keys[K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED

    # Update right paddle position
    if keys[K_UP] and right_paddle.top > 0:
        right_paddle.y -= PADDLE_SPEED
    if keys[K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += PADDLE_SPEED

    # Update ball position
    ball.x += ball_direction.x * BALL_SPEED_X
    ball.y += ball_direction.y * BALL_SPEED_Y

    # Check for collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_direction.x *= -1

    # Check for collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_direction.y *= -1

    # Clear the window
    WINDOW.fill(BLACK)

    # Draw the paddles and ball
    pygame.draw.rect(WINDOW, WHITE, left_paddle)
    pygame.draw.rect(WINDOW, WHITE, right_paddle)
    pygame.draw.ellipse(WINDOW, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()

