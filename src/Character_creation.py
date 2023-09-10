import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)
CHARACTER_COLOR = (50, 150, 200)

# Character properties
head_size = 50
body_height = 100
leg_length = 100

# Shapes
shapes = []
trails = True

# Initialize the screen with transparency
infoObject: object = pygame.display.Info()
screen: pygame.Surface = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h)
)
pygame.display.set_caption("Character Customization")
background = pygame.Surface(screen.get_size(), pygame.SRCALPHA)

font = pygame.font.Font(None, 36)

def draw_character():
    # Draw head
    pygame.draw.circle(background, CHARACTER_COLOR, (WIDTH // 2, 150), head_size)

    # Draw body
    pygame.draw.rect(background, CHARACTER_COLOR, (WIDTH // 2 - 20, 200, 40, body_height))

    # Draw legs
    pygame.draw.line(background, CHARACTER_COLOR, (WIDTH // 2, 300), (WIDTH // 2 - 30, 400), 10)
    pygame.draw.line(background, CHARACTER_COLOR, (WIDTH // 2, 300), (WIDTH // 2 + 30, 400), 10)

def draw_shapes():
    for shape in shapes:
        pygame.draw.rect(background, shape["color"], shape["rect"])

    # Draw buttons
    for button in buttons:
        pygame.draw.rect(background, (100, 100, 100), button["rect"])  # Button background color
        text_surface = font.render(button["text"], True, (255, 255, 255))  # Button text color
        text_rect = text_surface.get_rect(center=button["rect"].center)
        background.blit(text_surface, text_rect)

def add_shape(x, y, width, height, color):
    shape = {"rect": pygame.Rect(x, y, width, height), "color": color, "dragging": False}
    shapes.append(shape)

def main():
    global head_size, body_height, trails

    while True:
        if trails:
            screen.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check for button clicks
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["text"] == "Finish":
                            return button["callback"]()
                        else:
                             button["callback"]()

                # Check for shape dragging
                for shape in shapes:
                    if shape["rect"].collidepoint(event.pos):
                        shape["dragging"] = True
                        shape["offset_x"] = shape["rect"].x - event.pos[0]
                        shape["offset_y"] = shape["rect"].y - event.pos[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                for shape in shapes:
                    shape["dragging"] = False

        # Clear the screen with transparency
        background.fill(TRANSPARENT)

        # Draw the character
        draw_character()

        # Draw shapes
        draw_shapes()

        # Update shape positions while dragging
        for shape in shapes:
            if shape["dragging"]:
                shape["rect"].x = pygame.mouse.get_pos()[0] + shape["offset_x"]
                shape["rect"].y = pygame.mouse.get_pos()[1] + shape["offset_y"]

        # Update the display
        screen.blit(background, (0, 0))
        pygame.display.update()

# Create buttons
buttons = [
    {"rect": pygame.Rect(600, 50, 150, 50), "text": "Increase Head Size", "callback": lambda: increase_size("head")},
    {"rect": pygame.Rect(600, 110, 150, 50), "text": "Decrease Head Size", "callback": lambda: decrease_size("head")},
    {"rect": pygame.Rect(600, 170, 150, 50), "text": "Increase Body Height", "callback": lambda: increase_size("body")},
    {"rect": pygame.Rect(600, 230, 150, 50), "text": "Decrease Body Height", "callback": lambda: decrease_size("body")},
    {"rect": pygame.Rect(600, 290, 150, 50), "text": "Add Square", "callback": lambda: add_square()},
    {"rect": pygame.Rect(600, 350, 150, 50), "text": "Finish", "callback": lambda: finish()},
    {"rect": pygame.Rect(600, 410, 150, 50), "text": "Reset", "callback": lambda: reset_character()},
    {"rect": pygame.Rect(600, 470, 150, 50), "text": "Toggle Trails", "callback": lambda: toggle_trails()},
]

def increase_size(part):
    global head_size, body_height
    if part == "head":
        head_size += 5
    elif part == "body":
        body_height += 10

def decrease_size(part):
    global head_size, body_height
    if part == "head":
        head_size -= 5
    elif part == "body":
        body_height -= 10

def add_square():
    #global clear_trails
    x, y, width, height, color = 50, 400, 50, 50, (255, 0, 0)
    
    #if clear_trails:
    #    background.fill(TRANSPARENT)
    
    add_shape(x, y, width, height, color)

def finish():
    global character_sprite, shapes_sprites, head_size, body_height, leg_length


    pygame.draw.rect(background, (0, 0, 0, 0), pygame.Rect(500, 50, 400, 1000))


    # Divide the character sizes by 4
    head_size //= 4
    body_height //= 4
    leg_length //= 4

    character_sprite = pygame.sprite.GroupSingle()
    character_sprite.add(pygame.sprite.Sprite())
    character_sprite.sprite.image = background.copy()
    shapes_sprites = pygame.sprite.Group()
    for shape in shapes:
        shape_sprite = pygame.sprite.Sprite()
        # Divide the shape sizes by 4
        shape_width = shape["rect"].width // 4
        shape_height = shape["rect"].height // 4
        shape_sprite.image = pygame.Surface((shape_width, shape_height), pygame.SRCALPHA)
        shape_sprite.image.fill(TRANSPARENT)
        pygame.draw.rect(shape_sprite.image, shape["color"], (0, 0, shape_width, shape_height))
        shape_sprite.rect = shape_sprite.image.get_rect()
        shape_sprite.rect.x = shape["rect"].x // 4
        shape_sprite.rect.y = shape["rect"].y // 4
        shape_sprite.rect.width = shape["rect"].width // 4
        shape_sprite.rect.height = shape["rect"].height // 4
        shapes_sprites.add(shape_sprite)
    shapes.clear()
    return character_sprite


def reset_character():
    global head_size, body_height, shapes
    head_size = 50
    body_height = 100
    shapes = []
    background.fill(TRANSPARENT)

def toggle_trails():
    global trails
    if trails:
        trails = False
    else:
        trails = True

if __name__ == "__main__":
    main()



#import pygame
#import sys
#
## Initialize pygame
#pygame.init()
#
## Constants
#WIDTH, HEIGHT = 800, 600
#TILE_SIZE = 32
#GRID_WIDTH, GRID_HEIGHT = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE
#WHITE = (255, 255, 255)
#BLACK = (0, 0, 0)
#
## Create the screen
#screen = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("Tile Map Editor")
#
## Create a 2D array to represent the grid
#grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
#
## Define a function to draw the grid
#def draw_grid():
#    for row in range(GRID_HEIGHT):
#        for col in range(GRID_WIDTH):
#            if grid[row][col] == 1:
#                pygame.draw.rect(screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
#
## Game loop
#running = True
#drawing = False  # Indicates whether the user is drawing tiles
#erasing = False  # Indicates whether the user is erasing tiles
#
#while running:
#    for event in pygame.event.get():
#        if event.type == pygame.QUIT:
#            running = False
#        elif event.type == pygame.MOUSEBUTTONDOWN:
#            if event.button == 1:  # Left mouse button
#                drawing = True
#            elif event.button == 3:  # Right mouse button
#                erasing = True
#        elif event.type == pygame.MOUSEBUTTONUP:
#            drawing = False
#            erasing = False
#        elif event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_s:  # Save the grid to a file when 's' key is pressed
#                with open("grid.txt", "w") as file:
#                    for row in grid:
#                        file.write(" ".join(map(str, row)) + "\n")
#
#    # Get the mouse position
#    mouse_x, mouse_y = pygame.mouse.get_pos()
#
#    # Convert mouse position to grid coordinates
#    col = mouse_x // TILE_SIZE
#    row = mouse_y // TILE_SIZE
#
#    # Draw or erase tiles based on mouse input
#    if drawing:
#        if 0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT:
#            grid[row][col] = 1
#    elif erasing:
#        if 0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT:
#            grid[row][col] = 0
#
#    # Fill the screen with white
#    screen.fill(WHITE)
#
#    # Draw the grid
#    draw_grid()
#
#    # Update the display
#    pygame.display.flip()
#
## Quit pygame
#pygame.quit()
#sys.exit()
#