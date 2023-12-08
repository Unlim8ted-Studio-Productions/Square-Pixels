import pygame


if __name__ == "__main__":
    # Constants
    infoObject: object = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    BACKGROUND_COLOR = (0, 0, 0)
font = pygame.font.Font("Recources\Fonts\PixelifySans-Regular.ttf", 36)
# Define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)
white = (255, 255, 255)


class Button:
    """Button class for creating interactive buttons in the game."""

    def __init__(
        self,
        text,
        x,
        y,
        width,
        height,
        command,
        additional_data: list = None,
        color=(255, 255, 255),
    ):
        """
        Initialize a button.

        Args:
            text (str): The text displayed on the button.
            x (int): The x-coordinate of the button's top-left corner.
            y (int): The y-coordinate of the button's top-left corner.
            width (int): The width of the button.
            height (int): The height of the button.
            command (function): The function to be executed when the button is clicked.
            aditional data (list): arguments the buttons command needs to run
        """
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.command = command
        self.additional_data = additional_data
        self.hovered = False
        self.size = 36
        self.active = False
        self.bold = False
        self.italics = False
        self.underlined = False
        self.font_name = "Recources\Fonts\PixelifySans-Regular.ttf"
        self.color = color

    def draw(self, screen):
        """Draw the button on the screen."""
        font = pygame.font.Font(self.font_name, self.size)
        font.set_bold(self.bold)
        font.set_italic(self.italics)
        font.set_underline(self.underlined)
        color = BUTTON_HOVER_COLOR if self.hovered else BUTTON_COLOR
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        text = font.render(self.text, True, self.color)
        screen.blit(
            text,
            (
                self.x + self.width // 2 - text.get_width() // 2,
                self.y + self.height // 2 - text.get_height() // 2,
            ),
        )

    def handle_event(self, event):
        """
        Handle events related to the button.

        Args:
            event: The Pygame event to be processed.
        """
        if event.type == pygame.MOUSEMOTION:
            self.hovered = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.active = True
                if self.additional_data != None:
                    a = self.command(*self.additional_data)
                else:
                    a = self.command()
                if a:
                    return a
            else:
                self.active = False

    def selected(self):
        self.hovered = True

    def change_text(self, event):
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
