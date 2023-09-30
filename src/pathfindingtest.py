import pygame
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
import terrain_gen as tgen
import render
import player

# Constants for display
WIDTH, HEIGHT = 1000, 800
matrix = [[1 for _ in range(HEIGHT)] for _ in range(WIDTH)]
CELL_SIZE = 20


infoObject: object = pygame.display.Info()
screen: pygame.Surface = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame_icon = pygame.image.load(
    r"terraria_styled_game\program recources\Screenshot 2023-09-21 181742.png"
)
pygame.display.set_icon(pygame_icon)
# pygame.display.toggle_fullscreen()
pygame.display.set_caption("Square Pixel")
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
# Path to the folder to save the extracted frames
image_folder: str = r"terraria_styled_game\\frames"
colliders: list = []
# Extract frames from the video
# logo.extract_frames(video_file, image_folder)
vx, vy = 0, 0  # infoObject.current_w/2, 0#infoObject.current_h /2
# Call the function to play the video

# Rest of game code goes here...
terrain_gen = tgen.TerrainGenerator(
    width=(0, infoObject.current_w // 10), height=infoObject.current_h // 15
)
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
        player.Player(0,0),
        1,
        0,
    )

positions=[]
# Define the positions you want to change to '0'
for rect in colliders:
    positions.append((rect.x,rect.y))

# Call the function to update the grid
for x, y in positions:
    if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]):
        matrix[y][x] = 0

grid = Grid(matrix=matrix)

# Get start and end point
start = grid.node(100, 200)
end = grid.node(500, 300)

# Create a finder with the movement style
finder = AStarFinder()

# Returns a list with the path and the amount of times the finder had to run to get the path
path, runs = finder.find_path(start, end, grid)

# Initialize Pygame
pygame.init()


# Create a Pygame window

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Translate mouse coordinates to matrix coordinates
            end = grid.node(mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)
            path, runs = finder.find_path(start, end, grid)  # Recalculate the path
            print(path, runs)

    # Draw the grid
    screen.fill((255, 255, 255))
    for y, row in enumerate(matrix):
        for x, value in enumerate(row):
            color = (0, 0, 0) if value == 1 else (255, 0, 0)
            pygame.draw.rect(
                screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )
    for rect in colliders:
        pygame.draw.rect(screen,(200,100,200),rect)
    # Draw the path
    if path:
        for x, y in path:
            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

    pygame.display.flip()

pygame.quit()
