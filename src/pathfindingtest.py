import pygame
from collections import deque

# Define your grid size and cell size
GRID_SIZE = 20
CELL_SIZE = 30

# Define your start and end points
start = (1, 1)
end = (18, 18)

# Create a list of obstacles as (x, y) coordinates
obstacles = [(5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (15, 15), (15, 16), (15, 17), (15, 18)]

# Breadth-First Search (BFS) Pathfinding
def bfs(start, goal, obstacles):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if neighbor not in obstacles and neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Find the path
    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    end = (mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)
    path = bfs(start, end, obstacles)
    screen.fill((0, 0, 0))

    # Draw grid and obstacles
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, (255, 255, 255), rect)
            if (x, y) in obstacles:
                pygame.draw.rect(screen, (0, 0, 0), rect)
    
    # Render the path
    if path:
        for point in path:
            x, y = point
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw start and end points
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(end[0] * CELL_SIZE, end[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    pygame.display.flip()
