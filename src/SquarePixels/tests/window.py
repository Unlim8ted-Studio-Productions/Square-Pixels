import ctypes
import random
import time
import pygame

from SquarePixels.uimanagement import logo


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
        terrain.append(random.randint(height // 2, height - 1))
    return terrain


# Set up the window width and height
window_width, window_height = 800, 600

# Get a handle to the current window
hwnd = ctypes.windll.kernel32.GetConsoleWindow()
dc = ctypes.windll.user32.GetDC(hwnd)

# Initialize Pygame
pygame.init()

# Set up Pygame window
screen_info = pygame.display.Info()
screen = pygame.display.set_mode(
    (window_width, window_height), pygame.NOFRAME, pygame.RESIZABLE
)
pygame.display.set_caption("Square Pixels")

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

regions = []  # Store created regions

starting = True
while starting:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            starting = False
    # Get the Pygame window's handle
    hwnd = pygame.display.get_wm_info()["window"]

    # Calculate the number of squares to load in this iteration
    squares_to_load = min(total_squares, loaded_squares + loading_speed)

    # Load squares incrementally or update existing regions
    combined_region = None  # Initialize combined region variable
    for i in range(squares_to_load):
        left = (i % num_horizontal) * square_size
        top = (i // num_horizontal) * square_size
        right = left + square_size
        bottom = top + square_size

        rect = RECT(left, top, right, bottom)
        region = ctypes.windll.gdi32.CreateRectRgnIndirect(ctypes.byref(rect))

        # Combine the new region with the existing combined region
        if combined_region:
            temp_region = ctypes.windll.gdi32.CreateRectRgn(0, 0, 0, 0)
            ctypes.windll.gdi32.CombineRgn(temp_region, combined_region, region, 2)
            ctypes.windll.gdi32.DeleteObject(combined_region)
            ctypes.windll.gdi32.DeleteObject(region)
            combined_region = temp_region
        else:
            combined_region = region

    regions.append(combined_region)  # Store the combined region in the list
    ctypes.windll.user32.SetWindowRgn(
        hwnd, combined_region, True
    )  # Set the window shape to the combined region

    # Update the loaded squares counter
    loaded_squares = squares_to_load

    pygame.display.update()

    # If all squares are loaded, exit the loop
    if loaded_squares >= total_squares:
        break


## Generate terrain on each side of the window
# for x, height in enumerate(left_terrain):
#    left = x * square_size
#    top = window_height - height
#    right = left + square_size
#    bottom = window_height
#    rect = RECT(left, top, right, bottom)
#  v  region = ctypes.windll.gdi32.CreateRectRgnIndirect(ctypes.byref(rect))
#    regions.append(region)
#
# for x, height in enumerate(right_terrain):
#    left = (num_horizontal // 2 + x) * square_size
#    top = window_height - height
#    right = left + square_size
#    bottom = window_height
#    rect = RECT(left, top, right, bottom)
#   v region = ctypes.windll.gdi32.CreateRectRgnIndirect(ctypes.byref(rect))
#   regions.append(region)


for region in regions:
    ctypes.windll.gdi32.DeleteObject(region)


pygame.quit()
