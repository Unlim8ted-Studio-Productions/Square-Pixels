import pygame

if __name__ == "__main__":
    # Constants
    infoObject: object = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    BACKGROUND_COLOR = (0, 0, 0)
font = pygame.font.Font(None, 36)
# Define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)

white = (255, 255, 255)


# Create an InputField class for text input
class InputField:
    def __init__(self, x, y, width, height, placeholder, command=None, parameters=None):
        """
        Initialize a text input box object
        Args:
            x: X position of the text input box
            y: Y position of the text input box
            width: Width of the text input box
            height: Height of the text input box
            placeholder: Placeholder text to display when empty
            command: function to run when the return key is pressed
            parameters: List of aditional arguments to pass to command
        Returns:
            self: The text input box object
        Processing Logic:
            - Sets the x, y, width and height attributes from the arguments
            - Sets the placeholder text
            - Initializes other attributes like text, active state etc
            - Sets the command and parameters if provided
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.placeholder = placeholder
        self.text = ""
        self.active = False
        self.size = 36
        self.hovered = False
        self.font_name = "Recources\Fonts\PixelifySans-Regular.ttf"
        self.bold = False
        self.italics = False
        self.underlined = False
        self.command = command
        self.parameters = parameters

    def draw(self, screen):
        """
        Draws a button on the provided screen.
        Args:
            screen: The screen surface to draw the button on.
        Returns:
            None: Does not return anything, draws the button directly to the screen.
        Processing Logic:
            - Loads the font based on the button's font properties
            - Sets the font style based on bold, italics, underline properties
            - Draws the button rectangle based on position and size
            - Sets the font color based on active state
            - Renders the text and blits it to the screen
        """
        font = pygame.font.Font(self.font_name, self.size)
        font.set_bold(self.bold)
        font.set_italic(self.italics)
        font.set_underline(self.underlined)
        color = BUTTON_COLOR if not self.active else BUTTON_HOVER_COLOR
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        font_color = (0, 0, 0) if not self.active else (255, 255, 255)
        text = font.render(
            self.text if self.text else self.placeholder, True, font_color
        )
        screen.blit(text, (self.x + 10, self.y + 10))

    def handle_event(self, event):
        """Handle mouse and keyboard events for a button
        Args:
            event: The pygame event to handle
        Returns:
            self.active: Whether the button is currently pressed
        - Check if mouse button 1 was pressed within button bounds and set self.active
        - Check if a key was pressed and button is active
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            if event.key == pygame.K_RETURN:
                if self.command:
                    if self.parameters:
                        self.command(*self.parameters)
                    else:
                        self.command()

    def change_text(self, event):
        """
        Change text on mouse events
        Args:
            event: The pygame event object
        Returns:
            None: No value is returned
        Processing Logic:
        - Check if mouse is hovering over button on MOUSEMOTION
        - Check if mouse is clicked on button on MOUSEBUTTONDOWN
        - Check if a key is pressed while button is active on KEYDOWN
        - Set hovered and active flags based on above checks
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

    def clear(self):
        """Clears the text in the object
        Args:
            self: The object whose text needs to be cleared
        Returns:
            None: Does not return anything
        - Sets the text attribute of the object to an empty string ""
        - This empties out any existing text in the object"""
        self.text = ""
