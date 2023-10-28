# Numeric input field for customizing numeric properties
import pygame


class NumericInputField:
    def __init__(self, x, y, width, height, label, default_value):
        """
        Initialize a NumericInputField GUI element
        Args:
            x: X coordinate of element
            y: Y coordinate of element
            width: Width of element
            height: Height of element
            label: Label for element
            default_value: Default value for element
        Returns:
            None: Does not return anything
        - Sets x, y, width, height, label and default value attributes of element
        - Sets active attribute to False by default
        - Initializes element with given parameters"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.value = default_value
        self.active = False

    def draw(self, screen):
        """Draw the player on the screen.
        Args:
            screen: The screen surface to draw on.
        Returns:
            None: Does not return anything.
        - Get the player's position, width and height from its attributes
        - Draw a rectangle on the screen using pygame at the player's position with its dimensions and color
        - Loop through the player's elements and draw them"""
        font = pygame.font.Font(None, 36)
        """Draws a rectangle on the screen.
        Args:
            screen: The screen surface to draw on.
        Returns: 
            None: Does not return anything.
        - Draws a filled rectangle on the screen surface using the object's position, size and background color attributes.
        - Loops through the object's elements list and draws each element."""
        text = font.render(self.label, True, (0, 0, 0))
        screen.blit(text, (self.x, self.y))
        pygame.draw.rect(
            screen, (255, 255, 255), (self.x, self.y + 30, self.width, self.height), 2
        )
        text = font.render(str(self.value), True, (0, 0, 0))
        screen.blit(text, (self.x + 5, self.y + 35))

    def handle_event(self, event):
        """Handle mouse and keyboard events for a button.
        Args:
            event: The pygame event to handle
        Returns:
            None: Does not return anything
        - Check if mouse button 1 was pressed and mouse position is over button
        - Set button to active if mouse press conditions are met
        - Check if a key was pressed and button is active
        - Does not return anything, only checks conditions"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = (
                self.x < event.pos[0] < self.x + self.width
                and self.y + 30 < event.pos[1] < self.y + 30 + self.height
            )
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.value = int(str(self.value)[:-1])
            elif event.key in [
                pygame.K_0,
                pygame.K_1,
                pygame.K_2,
                pygame.K_3,
                pygame.K_4,
                pygame.K_5,
                pygame.K_6,
                pygame.K_7,
                pygame.K_8,
                pygame.K_9,
            ]:
                self.value = int(str(self.value) + event.unicode)
