import pygame
import numpy as np

# Set dimensions of the grid
GRID_WIDTH = 100
GRID_HEIGHT = 100

# Set size of each cell
CELL_SIZE = 5

# Define neon green color (R, G, B)
NEON_GREEN = (57, 255, 20)

# Initialize Pygame
pygame.init()

# Set window size
WINDOW_SIZE = (GRID_WIDTH * CELL_SIZE, GRID_HEIGHT * CELL_SIZE)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Game of Life")

# Create initial grid
grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=bool)

# Function to update the grid
def update_grid():
    global grid

    new_grid = np.copy(grid)

    # Iterate over each cell
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            # Count the number of live neighbors
            neighbors = np.sum(grid[max(0, x - 1):min(x + 2, GRID_WIDTH),
                                    max(0, y - 1):min(y + 2, GRID_HEIGHT)]) - grid[x, y]

            # Apply the rules of the game
            if grid[x, y] and (neighbors < 2 or neighbors > 3):
                new_grid[x, y] = False
            elif not grid[x, y] and neighbors == 3:
                new_grid[x, y] = True

    grid = new_grid

# Function to draw the grid
def draw_grid():
    screen.fill((0, 0, 0))

    # Iterate over each cell and draw live cells
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x, y]:
                pygame.draw.rect(screen, NEON_GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.display.flip()

# Main game loop
running = True
paused = False
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        update_grid()
        draw_grid()
        clock.tick(10)  # Adjust the speed of the game by changing the tick rate

pygame.quit()
