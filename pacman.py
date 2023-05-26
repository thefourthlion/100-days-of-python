import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")

# Set up colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# Set up Pac-Man's initial position and movement
pacman_pos = [400, 300]
pacman_radius = 15
pacman_direction = 0  # 0: right, 1: down, 2: left, 3: up

# Set up the game loop
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move Pac-Man based on the arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        pacman_direction = 0
        pacman_pos[0] += 5
    elif keys[pygame.K_DOWN]:
        pacman_direction = 1
        pacman_pos[1] += 5
    elif keys[pygame.K_LEFT]:
        pacman_direction = 2
        pacman_pos[0] -= 5
    elif keys[pygame.K_UP]:
        pacman_direction = 3
        pacman_pos[1] -= 5

    # Draw the game window
    win.fill(BLACK)
    pygame.draw.circle(win, YELLOW, pacman_pos, pacman_radius)
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)
