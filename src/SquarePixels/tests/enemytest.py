import pygame
import random
import heapq
import math

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("AI Cube Attack")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)


# Function to generate a random Rect
def random_rect():
    x = random.randint(0, width - 50)  # Random x position
    y = random.randint(0, height - 50)  # Random y position
    w = random.randint(20, 100)  # Random width
    h = random.randint(20, 100)  # Random height
    return pygame.Rect(x, y, w, h)


# Create a player and an AI cube
player = pygame.Rect(50, 50, 30, 30)
ai_cube = pygame.Rect(700, 500, 30, 30)

# Initialize player and AI cube velocities
player_velocity = 3
ai_velocity = 2
gravity = 0.5
jump_power = 200
on_ground = False

# Create terrain
terrain = []
for _ in range(10):
    terrain_rect = random_rect()
    terrain_rect.y = (
        height - terrain_rect.height
    )  # Place it at the bottom of the screen
    terrain.append(terrain_rect)


# A* pathfinding for AI movement
def heuristic(node, goal):
    return math.sqrt((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2)


def astar(graph, start, goal):
    queue = [(0, start)]
    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic(start, goal)

    while queue:
        _, current = heapq.heappop(queue)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path

        for neighbor in graph[current]:
            tentative_g_score = g_score[current] + 1
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                if neighbor not in [node[1] for node in queue]:
                    heapq.heappush(queue, (f_score[neighbor], neighbor))

    return None


# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and on_ground:
        player.y -= jump_power
        on_ground = False

    if keys[pygame.K_LEFT]:
        player.x -= player_velocity
    if keys[pygame.K_RIGHT]:
        player.x += player_velocity

    screen.fill(WHITE)  # Fill the screen with white

    # Draw terrain
    for terrain_rect in terrain:
        pygame.draw.rect(screen, GRAY, terrain_rect)

    # Draw player and AI cube
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, GREEN, ai_cube)

    # Check for collision with terrain
    for terrain_rect in terrain:
        if player.colliderect(terrain_rect):
            player.y = terrain_rect.top - 20  # Snap player to the top of the terrain
            on_ground = True

    # Apply gravity
    if not on_ground:
        player.y += gravity

    # A* pathfinding for AI cube to reach the player
    graph = {terrain_rect.topleft: [] for terrain_rect in terrain}
    for terrain_rect in terrain:
        for other_terrain_rect in terrain:
            if terrain_rect != other_terrain_rect:
                path = astar(graph, terrain_rect.topleft, other_terrain_rect.topleft)
                if path:
                    graph[terrain_rect.topleft].append(path[1])

    # Move AI cube towards the player
    if ai_cube.x < player.x:
        ai_cube.x += ai_velocity
    elif ai_cube.x > player.x:
        ai_cube.x -= ai_velocity
    if ai_cube.y < player.y:
        ai_cube.y += ai_velocity
    elif ai_cube.y > player.y:
        ai_cube.y -= ai_velocity

    # Check for collision between AI cube and player
    if ai_cube.colliderect(player):
        # Player is attacked (you can implement attack logic here)
        print("Player is attacked!")

    pygame.display.flip()

# Quit pygame
pygame.quit()
