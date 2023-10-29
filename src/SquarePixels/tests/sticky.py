import pygame
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Path to Cursor")


# Function to generate a random Rect
def random_rect():
    x = random.randint(0, width - 50)  # Random x position
    y = random.randint(0, height - 50)  # Random y position
    w = random.randint(20, 100)  # Random width
    h = random.randint(20, 100)  # Random height
    return pygame.Rect(x, y, w, h)


# Create a graph to represent rectangles and their positions
graph = {}
rectangles = []
rects = []


def generate_rects():
    for _ in range(10):  # Generate 10 random rectangles
        rect = random_rect()
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )  # Random color
        pygame.draw.rect(screen, color, rect)
        rect_center = rect.center
        rectangles.append(rect_center)
        rects.append(rect)


# Function to find the closest rectangle to the cursor
def find_closest_rect(cursor_pos):
    closest_rect = None
    min_distance = float("inf")
    for rect in rectangles:
        distance = (
            (rect[0] - cursor_pos[0]) ** 2 + (rect[1] - cursor_pos[1]) ** 2
        ) ** 0.5
        if distance < min_distance:
            min_distance = distance
            closest_rect = rect
    return closest_rect


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                generate_rects()
            if event.button == 3:
                rects = []
                rectangles = []
                generate_rects()
            if event.button == 2:
                None  # switch between pathfinding and sticky wires

    screen.fill((255, 255, 255))  # Fill the screen with white

    cursor_pos = pygame.mouse.get_pos()
    closest_rect = find_closest_rect(cursor_pos)
    for recto in rects:
        pygame.draw.rect(screen, (43, 122, 222), recto)
    if closest_rect:
        pygame.draw.line(screen, (0, 0, 0), cursor_pos, closest_rect, 2)

    pygame.display.flip()

# Quit pygame
pygame.quit()
