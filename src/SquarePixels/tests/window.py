import ctypes
import random
import time
import pygame


# Define RECT structure
class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]


def generate_terrain(width, height):
    terrain = []
    for x in range(width):
        terrain.append(random.randint(0, height // 2))  # Adjusted terrain generation
    return terrain


# Set up the window width and height
window_width, window_height = 800, 600

# Initialize Pygame
pygame.init()

# Set up Pygame window
screen_info = pygame.display.Info()
screen = pygame.display.set_mode(
    (window_width, window_height), pygame.NOFRAME, pygame.RESIZABLE
)
pygame.display.set_caption("Cool Pattern")

# Calculate the size of each square piece
square_size = 40
num_horizontal = window_width // square_size
num_vertical = window_height // square_size
total_squares = num_horizontal * num_vertical

loading_speed = 1  # Speed of loading squares
loaded_squares = 0  # Counter for loaded squares

# Generate terrain on each side of the window
left_terrain = generate_terrain(num_horizontal // 2, window_height)
right_terrain = generate_terrain(num_horizontal // 2, window_height)

# Store created regions
regions = []

starting = True
while starting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starting = False

    hwnd = pygame.display.get_wm_info()["window"]

    squares_to_load = min(total_squares, loaded_squares + loading_speed)

    combined_region = None
    for i in range(squares_to_load):
        x = i % num_horizontal
        y = i // num_horizontal

        # Adjust position for the desired effect
        x, y = x - num_horizontal // 2, y - num_vertical // 2
        x, y = x * square_size, y * square_size

        # Calculate the position for the pattern
        left, top = window_width // 2 + x, window_height // 2 + y
        right, bottom = left + square_size, top + square_size

        rect = RECT(left, top, right, bottom)
        region = ctypes.windll.gdi32.CreateRectRgnIndirect(ctypes.byref(rect))

        if combined_region:
            temp_region = ctypes.windll.gdi32.CreateRectRgn(0, 0, 0, 0)
            ctypes.windll.gdi32.CombineRgn(temp_region, combined_region, region, 2)
            ctypes.windll.gdi32.DeleteObject(combined_region)
            ctypes.windll.gdi32.DeleteObject(region)
            combined_region = temp_region
        else:
            combined_region = region

    regions.append(combined_region)
    ctypes.windll.user32.SetWindowRgn(hwnd, combined_region, True)

    loaded_squares = squares_to_load

    pygame.display.update()

    if loaded_squares >= total_squares:
        break

for region in regions:
    ctypes.windll.gdi32.DeleteObject(region)

pygame.quit()
