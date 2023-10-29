import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fading Clouds")


# Cloud class
class Cloud:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.alpha = 255

    def move(self):
        self.x -= self.speed
        self.alpha -= 1
        if self.alpha < 0:
            self.alpha = 0

    def draw(self):
        self.image.set_alpha(self.alpha)
        screen.blit(self.image, (self.x, self.y))


# Load cloud images
cloud_images = [pygame.image.load("clouds1.png"), pygame.image.load("clouds2.png")]

# Create a list to hold cloud objects
clouds = []

# Main loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Generate a random cloud with varying speed
    if len(clouds) <= 6:
        if random.randint(0, 100) < 5:
            cloud_image = random.choice(cloud_images)
            cloud_x = random.
            cloud_y = random.randint(0, screen_height // 2)
            cloud_speed = random.uniform(1, 4)  # Random speed between 1 and 4
            new_cloud = Cloud(cloud_x, cloud_y, cloud_image, cloud_speed)
            clouds.append(new_cloud)

    screen.fill((0, 0, 0))
    # Move and draw clouds
    for cloud in clouds:
        cloud.move()
        cloud.draw()

    # Remove clouds that are off-screen or completely faded
    clouds = [
        cloud
        for cloud in clouds
        if cloud.x + cloud.image.get_width() > 0 and cloud.alpha > 0
    ]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
