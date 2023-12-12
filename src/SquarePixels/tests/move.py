import pygame
import sys

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Satisfying Movement System")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 0, 255)

# Player attributes
player_size = 50
player_speed = 0.0
player_max_speed = 15
player_acceleration = 0.2
player_dash_speed = 25.0
player_jump_strength = 15.0
gravity = 0.8
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_velocity = [0, 0]
is_dashing = False
dash_cooldown = 60  # Cooldown frames for dash
dash_timer = 0
is_jumping = False
is_on_ground = False
is_on_wall = False
wall_jump_cooldown = 10
wall_jump_timer = 0

# Tile attributes
TILE_SIZE = 32
GRID_WIDTH, GRID_HEIGHT = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


# Define a function to draw the grid
def draw_grid():
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 1:
                pygame.draw.rect(
                    screen,
                    GREEN,
                    (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE),
                )


# Update collision logic
def check_tile_collision():
    global is_on_ground, is_on_wall, player_x, player_y, player_velocity

    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] == 1:
                tile_rect = pygame.Rect(
                    col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE
                )

                if player_rect.colliderect(tile_rect):
                    # Collision resolution in x-axis
                    if (
                        player_rect.y < tile_rect.top
                        and player_rect.y > tile_rect.bottom
                    ):
                        if player_velocity[0] > 0:
                            if player_rect.x > tile_rect.left:
                                player_x = tile_rect.right + player_size + 4
                            else:
                                player_x = tile_rect.left - player_size - 4
                        elif player_velocity[0] < 0:
                            player_x = tile_rect.right

                    # Collision resolution in y-axis
                    if player_velocity[1] > 0:
                        player_y = tile_rect.top - player_size
                        player_velocity[1] = 0
                        is_on_ground = True
                    elif player_velocity[1] < 0:
                        player_y = tile_rect.bottom
                        player_velocity[1] = 0

    # Check screen boundaries
    player_x = max(0, min(player_x, WIDTH - player_size))
    player_y = max(0, min(player_y, HEIGHT - player_size))


# Main game loop
clock = pygame.time.Clock()
running = True
drawing = False  # Indicates whether the user is drawing tiles
erasing = False  # Indicates whether the user is erasing tiles
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                drawing = True
            elif event.button == 3:  # Right mouse button
                erasing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            erasing = False
        elif event.type == pygame.KEYDOWN:
            if (
                event.key == pygame.K_s
            ):  # Save the grid to a file when 's' key is pressed
                with open("grid.txt", "w") as file:
                    for row in grid:
                        file.write(" ".join(map(str, row)) + "\n")

    # Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    # Convert mouse position to grid coordinates
    col = mouse_x // TILE_SIZE
    row = mouse_y // TILE_SIZE
    # Draw or erase tiles based on mouse input
    if drawing:
        if 0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT:
            grid[row][col] = 1
    elif erasing:
        if 0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT:
            grid[row][col] = 0

    keys = pygame.key.get_pressed()

    player_velocity[1] += gravity

    if keys[pygame.K_LEFT]:
        if player_speed > 0:
            player_speed /= 1.1
        player_speed -= player_acceleration
    elif keys[pygame.K_RIGHT]:
        if player_speed < 0:
            player_speed /= 1.1
        player_speed += player_acceleration
    else:
        if player_speed > 0:
            player_speed -= player_acceleration
        elif player_speed < 0:
            player_speed += player_acceleration

    if player_speed > player_max_speed:
        player_speed = player_max_speed
    elif player_speed < -player_max_speed:
        player_speed = -player_max_speed

    is_dashing = False
    if keys[pygame.K_SPACE] and not is_dashing and dash_timer <= 0:
        is_dashing = True
        player_speed += player_dash_speed if player_speed >= 0 else -player_dash_speed
        dash_timer = dash_cooldown

    if keys[pygame.K_UP] and not is_jumping and (is_on_ground or is_on_wall):
        is_jumping = True
        player_velocity[1] = -player_jump_strength
        if is_on_wall:
            wall_jump_timer = wall_jump_cooldown
            if player_x < WIDTH / 2:
                player_speed = player_max_speed
            else:
                player_speed = -player_max_speed

    player_velocity[0] = player_speed

    player_x += player_velocity[0]
    player_y += player_velocity[1]

    is_jumping = False

    is_on_ground = player_y >= HEIGHT - player_size
    is_on_wall = player_x <= 0 or player_x >= WIDTH - player_size

    # Inside the game loop, after updating player position
    check_tile_collision()

    pygame.draw.rect(screen, RED, (player_x, player_y, player_size, player_size))
    draw_grid()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
