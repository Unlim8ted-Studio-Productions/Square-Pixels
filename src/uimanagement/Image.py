import pygame
from PIL import Image, ImageDraw, ImageOps


class ImageElement:
    def __init__(self, x, y, image, crop_mode="None"):
        self.x = x
        self.y = y
        self.image = image
        self.crop_mode = crop_mode  # "None" or "Circle"

    def draw(self, screen):
        # Optionally apply cropping based on the selected cropping mode
        if self.crop_mode == "Circle":
            # Crop the image to a circle using PIL
            mask = Image.new("L", self.image.size, 0)
            draw = ImageDraw.Draw(mask)
            width, height = self.image.size
            draw.ellipse((0, 0, width, height), fill=255)
            self.image.putalpha(mask)

        # Draw the image on the screen
        pygame_image = pygame.image.fromstring(
            self.image.tobytes(), self.image.size, self.image.mode
        )
        screen.blit(pygame_image, (self.x, self.y))
