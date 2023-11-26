import pygame


class TextElement:
    def __init__(self, x, y, text, font_size):
        """
        Initialize a button object
        Args:
            x: x-coordinate of the button
            y: y-coordinate of the button 
            text: Text to display on the button
            font_size: Font size of the text
        Returns: 
            self: Button object
        - Sets the x and y coordinates
        - Sets the text and font size
        - Sets default color, size and other attributes
        - Initializes other properties like hover, width, height etc.
        """
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.color = (255, 255, 255)  # Default text color
        self.size = font_size
        self.hovered = False
        self.width = 50
        self.height = 25
        self.bold = False
        self.italics = False
        self.underlined = False
        self.font_name = None

    def draw(self, screen):
        """
        Renders text on a screen surface.
        Args:
            screen: The screen surface to render text on
        Returns: 
            None: Does not return anything
        - Loads the font based on properties of the Text object
        - Renders the text surface using the font and text properties  
        - Blits/draws the text surface onto the screen surface at the x,y position"""
        font = pygame.font.Font(self.font_name, self.size)
        font.set_bold(self.bold)
        font.set_italic(self.italics)
        font.set_underline(self.underlined)
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))

    def change_text(self, event):
        """
        Change text on mouse events
        Args: 
            event: pygame event object
        Returns: 
            None
        Processing Logic:
        - Check if mouse is hovering over button on MOUSEMOTION
        - Set button to active if mouse is pressed on button on MOUSEBUTTONDOWN 
        - Change text if a key is pressed while button is active on KEYDOWN
        """
        if event.type == pygame.MOUSEMOTION:
            self.hovered = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
