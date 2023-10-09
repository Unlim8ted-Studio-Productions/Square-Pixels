import pygame
from collections import deque
import terraingen.terrain_gen as tgen
import render.render as render
import player.player as player

# Define your grid size and cell size
GRID_SIZE = 20
CELL_SIZE = 30
# Initialize Pygame
pygame.init()
infoObject: object = pygame.display.Info()
screen: pygame.Surface = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h)
)
# Define your start and end points
start = (1, 1)
end = (18, 18)

# Create a list of obstacles as (x, y) coordinates
terrain_gen = tgen.TerrainGenerator(width=(20, 200), height=50)
terrain_gen.run(screen)

colliders = render.render_terrain(
    screen,
    terrain_gen.width,
    terrain_gen.height,
    terrain_gen.terrain,
    terrain_gen.pos_x,
    terrain_gen.pos_y,
    terrain_gen.camera_x,
    terrain_gen.camera_y,
    player.Player(0, 0),
    1,
    0,
)

obstacles = []
for rect in colliders:
    obstacles.append((rect.x, rect.y))


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


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Find the path
    mouse_x, mouse_y = pygame.mouse.get_pos()
    end = (mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)
    path = bfs(start, end, obstacles)
    screen.fill((0, 0, 0))

    # Draw grid and obstacles
    for rect in colliders:
        pygame.draw.rect(screen, (200, 200, 100), rect)

    # Render the path
    if path:
        for point in path:
            x, y = point
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

    # Draw start and end points
    pygame.draw.rect(
        screen,
        (255, 0, 0),
        pygame.Rect(start[0] * CELL_SIZE, start[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    )
    pygame.draw.rect(
        screen,
        (0, 0, 255),
        pygame.Rect(end[0] * CELL_SIZE, end[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE),
    )

    pygame.display.flip()
