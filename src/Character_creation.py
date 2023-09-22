import pygame
import sys
import tkinter as tk
from tkinter import filedialog
import os

path = os.getcwd()
# Initialize Pygame
pygame.init()

# Initialize the screen with transparency
infoObject = pygame.display.Info()
WIDTH, HEIGHT = 800, 600  # infoObject.current_w, infoObject.current_h
WHITE = (255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)
CHARACTER_COLOR = (50, 150, 200)

# Character properties
head_size = 50
body_height = 100

# Shapes
shapes = []
trails = True

# Create a tkinter root window for file dialogs
root = tk.Tk()
root.withdraw()  # Hide the main tkinter window

# Pygame screen
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
pygame.display.set_caption("Character Customization")
background = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
font = pygame.font.Font(None, 36)

character_list = [
    r"terraria_styled_game\characters\thumbnails\blue.gif",
    r"terraria_styled_game\characters\thumbnails\red.gif",
    # Add more character paths here
]

# Load pre-made character thumbnails
character_thumbnails = []
for character_path in character_list:
    character_thumbnail = pygame.image.load(character_path)
    character_thumbnail = pygame.transform.scale(character_thumbnail, (100, 100))
    character_thumbnails.append(character_thumbnail)

# Sidebar position and size
sidebar_width = 150
sidebar_rect = pygame.Rect(infoObject.current_w - (sidebar_width+20), 0, sidebar_width, infoObject.current_h)

# Button position and size
button_height = 100
button_spacing = 10
button_rects = [
    pygame.Rect(
        infoObject.current_w - sidebar_width-7,
        10 + (button_height + button_spacing) * idx,
        sidebar_width - 20,
        button_height,
    )
    for idx in range(len(character_thumbnails))
]

def draw_sidebar(buttoncount):
    color=[(100,100,100),(150,150,150)]
    # Fill the sidebar background
    pygame.draw.rect(background, (50, 50, 50), sidebar_rect)

    # Draw character thumbnails as buttons
    for idx, thumbnail in enumerate(character_thumbnails):
        count=0
        button_rect = button_rects[idx]
        for button in buttoncount:
            if button == idx:
                count=1
        pygame.draw.rect(background, (color[count]), button_rect)
        background.blit(thumbnail, (button_rect.x + 10, button_rect.y + 10))


def draw_character():
    # Draw head
    pygame.draw.circle(background, CHARACTER_COLOR, (WIDTH // 2, 150), head_size)

    # Draw body
    pygame.draw.rect(
        background, CHARACTER_COLOR, (WIDTH // 2 - 20, 200, 40, body_height)
    )

    # Draw legs
    pygame.draw.line(
        background, CHARACTER_COLOR, (WIDTH // 2, 300), (WIDTH // 2 - 30, 400), 10
    )
    pygame.draw.line(
        background, CHARACTER_COLOR, (WIDTH // 2, 300), (WIDTH // 2 + 30, 400), 10
    )


def draw_shapes():
    for shape in shapes:
        pygame.draw.rect(background, shape["color"], shape["rect"])

    # Draw buttons
    for button in buttons:
        pygame.draw.rect(
            background, (100, 100, 100), button["rect"]
        )  # Button background color
        text_surface = font.render(
            button["text"], True, (255, 255, 255)
        )  # Button text color
        text_rect = text_surface.get_rect(center=button["rect"].center)
        background.blit(text_surface, text_rect)


def add_shape(x, y, width, height, color):
    shape = {
        "rect": pygame.Rect(x, y, width, height),
        "color": color,
        "dragging": False,
    }
    shapes.append(shape)


def main():
    global head_size, body_height, trails
    running = True
    buttoncount= 0
    hoveredbuttons=[]
    drawchar = (False,0)
    while running:
        if trails:
            screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            buttoncount=0
            hoveredbuttons=[]
            for precharacter in button_rects:
                if precharacter.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]):
                    hoveredbuttons.append(buttoncount)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        drawchar = (True,buttoncount)
                buttoncount+=1
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Check for button clicks
                for button in buttons:
                    if button["rect"].collidepoint(event.pos):
                        if button["text"] == "Finish":
                            running = False
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

        if drawchar[0]:
            char=character_thumbnails[drawchar[1]]
            char = pygame.transform.scale(char, (550, 550))
            screen.blit(char,(infoObject.current_w // 20, infoObject.current_h/200, 40, body_height))
        # Draw the character
        if not drawchar[0]:
            draw_character()
        
        #Draw the sidebar
        draw_sidebar(hoveredbuttons)

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
    {
        "rect": pygame.Rect(600, 50, 150, 50),
        "text": "Increase Head Size",
        "callback": lambda: increase_size("head"),
    },
    {
        "rect": pygame.Rect(600, 110, 150, 50),
        "text": "Decrease Head Size",
        "callback": lambda: decrease_size("head"),
    },
    {
        "rect": pygame.Rect(600, 170, 150, 50),
        "text": "Increase Body Height",
        "callback": lambda: increase_size("body"),
    },
    {
        "rect": pygame.Rect(600, 230, 150, 50),
        "text": "Decrease Body Height",
        "callback": lambda: decrease_size("body"),
    },
    {
        "rect": pygame.Rect(600, 290, 150, 50),
        "text": "Add Square",
        "callback": lambda: add_square(),
    },
    {
        "rect": pygame.Rect(600, 350, 150, 50),
        "text": "Finish",
        "callback": lambda: finish(),
    },
    {
        "rect": pygame.Rect(600, 410, 150, 50),
        "text": "Reset",
        "callback": lambda: reset_character(),
    },
    {
        "rect": pygame.Rect(600, 470, 150, 50),
        "text": "Toggle Trails",
        "callback": lambda: toggle_trails(),
    },
    {
        "rect": pygame.Rect(600, 530, 150, 50),
        "text": "Export Character",
        "callback": lambda: save_character_dialog(),
    },
    {
        "rect": pygame.Rect(600, 590, 150, 50),
        "text": "Load Character",
        "callback": lambda: load_character_dialog(),
    },
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
    x, y, width, height, color = 50, 400, 50, 50, (255, 0, 0)
    add_shape(x, y, width, height, color)


def finish():
    global character_sprite, shapes_sprites, head_size, body_height, leg_length

    pygame.draw.rect(background, (0, 0, 0, 0), pygame.Rect(500, 50, 400, 1000))
    pygame.draw.rect(background, (0, 0, 0, 0), sidebar_rect)

    # Divide the character sizes by 4
    # head_size //= 8
    # body_height //= 4
    # leg_length //= 4
    # draw_character()
    # character_sprite = pygame.sprite.GroupSingle()
    # character_sprite.add(pygame.sprite.Sprite())
    # character_sprite.sprite.image = background.copy()
    # shapes.clear()
    export_character(path + r"\\terraria_styled_game\\characters\\current.png")
    return path + r"\\terraria_styled_game\\characters\\current.png"


def reset_character():
    global head_size, body_height, shapes
    head_size = 50
    body_height = 100
    shapes = []
    background.fill(TRANSPARENT)


def toggle_trails():
    global trails
    trails = not trails


def save_character_dialog():
    filename = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")],
        initialdir=path + r"\\terraria_styled_game\\characters\\",
    )
    if filename:
        export_character(filename)


def load_character_dialog():
    filename = filedialog.askopenfilename(
        filetypes=[("PNG files", "*.png")],
        initialdir=path + r"\\terraria_styled_game\\characters\\",
    )
    if filename:
        load_character(filename)


def export_character(filename):
    pygame.draw.rect(background, (0, 0, 0, 0), pygame.Rect(500, 50, 400, 1000))
    pygame.image.save(background, filename)


def load_character(filename):
    loaded_image = pygame.image.load(filename)
    screen.blit(loaded_image, (0, 0), (WIDTH, HEIGHT))
    pygame.display.update()


if __name__ == "__main__":
    main()


# import pygame
# import sys
#
## Initialize pygame
# pygame.init()
#
## Constants
# WIDTH, HEIGHT = 800, 600
# TILE_SIZE = 32
# GRID_WIDTH, GRID_HEIGHT = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
#
## Create the screen
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Tile Map Editor")
#
## Create a 2D array to represent the grid
# grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
#
## Define a function to draw the grid
# def draw_grid():
#    for row in range(GRID_HEIGHT):
#        for col in range(GRID_WIDTH):
#            if grid[row][col] == 1:
#                pygame.draw.rect(screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
#
## Game loop
# running = True
# drawing = False  # Indicates whether the user is drawing tiles
# erasing = False  # Indicates whether the user is erasing tiles
#
# while running:
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
# pygame.quit()
# sys.exit()
#
