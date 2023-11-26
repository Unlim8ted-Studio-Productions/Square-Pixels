
import pygame
from PIL import Image, ImageDraw, ImageOps


class ImageElement:
    def __init__(self, x, y, image, crop_mode="None"):
        self.x = x
        self.y = y
        self.image = image
        self.crop_mode = crop_mode  # "None" or "Circle"
        self.active = False
        self.width, self.height = self.image.size
        self.widtho, self.heighto = self.image.size
        self.text = ""
        self.bold = False
        self.italics = False
        self.underlined = False
        self.font_name = "Recources\Fonts\PixelifySans-Regular.ttf"
        self.color = (0, 0, 0)
        self.size = self.width * self.height

    def draw(self, screen):
        # Optionally apply cropping based on the selected cropping mode
        if self.crop_mode == "Circle":
            # Crop the image to a circle using PIL
            mask = Image.new("L", (self.widtho, self.heighto), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, self.widtho, self.heighto), fill=255)
            self.image.putalpha(mask)

        # Draw the image on the screen
        pygame_image = pygame.image.fromstring(
            self.image.tobytes(), self.image.size, self.image.mode
        )
        pygame_image = pygame.transform.scale(pygame_image, (self.width, self.height))
        screen.blit(pygame_image, (self.x, self.y))
