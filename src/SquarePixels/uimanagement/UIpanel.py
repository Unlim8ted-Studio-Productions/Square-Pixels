# UI panel for editing properties
import pygame

# UI panel background color
UI_PANEL_COLOR = (200, 200, 200)


class UIPanel:
    def __init__(self, x, y, width, height):
        """
        Initialize a UI panel object
        Args:
            x: X coordinate of panel
            y: Y coordinate of panel
            width: Width of panel
            height: Height of panel
        Returns:
            None: Does not return anything
        - Sets x, y, width and height attributes of panel from arguments
        - Sets default background color
        - Initializes empty elements list to add UI elements later"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = UI_PANEL_COLOR
        self.elements = []

    def draw(self, screen):
        """Draws a rectangle on the screen.
        Args:
            screen: The screen surface to draw on.
        Returns:
            None: Does not return anything.
        - Draws a filled rectangle on the screen surface using the object's position, size and background color attributes.
        - Loops through the object's elements list and draws each element."""
        pygame.draw.rect(
            screen, self.bg_color, (self.x, self.y, self.width, self.height)
        )

        for element in self.elements:
            element.draw(screen)
