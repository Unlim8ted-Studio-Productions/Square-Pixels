import pygame


class Slider:
    """Slider class for creating interactive sliders in the game."""

    def __init__(
        self,
        x,
        y,
        width,
        height,
        min_value,
        max_value,
        default_value,
        command=None,
        additional_data: list = None,
        color=(255, 255, 255),
        colortwo=(200, 200, 200),
        text="",
        text_position_below=True,
        size=26,
    ):
        """
        Initialize a slider.

        Args:
            x (int): The x-coordinate of the slider's top-left corner.
            y (int): The y-coordinate of the slider's top-left corner.
            width (int): The width of the slider.
            height (int): The height of the slider.
            min_value (float): The minimum value of the slider.
            max_value (float): The maximum value of the slider.
            default_value (float): The default value of the slider.
            command (function): The function to be executed when the slider is changed.
            additional_data (list): Arguments the slider's command needs to run.
            color (tuple): The color of the slider.
            text (str): The text to be displayed above or below the slider bar.
            text_position_below (bool): True if the text should be below the slider bar, False if above.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.min_value = min_value
        self.max_value = max_value
        self.value = default_value
        self.command = command
        self.additional_data = additional_data
        self.active = False
        self.color = color
        self.colortwo = colortwo
        self.text = text
        self.text_position_below = text_position_below
        self.size = size
        self.font_name = None
        self.bold = False
        self.italics = False
        self.underlined = False
        self.hovered = False

    def draw(self, screen):
        """Draw the slider on the screen."""
        pygame.draw.rect(
            screen, self.colortwo, (self.x, self.y, self.width, self.height)
        )
        slider_width = int(
            (self.value - self.min_value)
            / (self.max_value - self.min_value)
            * self.width
        )
        pygame.draw.rect(
            screen, self.color, (self.x, self.y, slider_width, self.height)
        )

        if self.text is not None:
            font = pygame.font.Font(self.font_name, self.size)
            font.set_bold(self.bold)
            font.set_italic(self.italics)
            font.set_underline(self.underlined)
            text_surface = font.render(self.text, True, self.color)
            text_rect = text_surface.get_rect()

            if self.text_position_below:
                text_rect.midtop = (self.x + self.width / 2, self.y + self.height)
            else:
                text_rect.midbottom = (self.x + self.width / 2, self.y)

            screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        """
        Handle events related to the slider.

        Args:
            event: The Pygame event to be processed.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            ):
                self.active = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.active = False
        elif event.type == pygame.MOUSEMOTION and self.active:
            mouse_x = max(self.x, min(event.pos[0], self.x + self.width))
            normalized_value = (mouse_x - self.x) / self.width
            self.value = self.min_value + normalized_value * (
                self.max_value - self.min_value
            )
            self.value = round(self.value, 10)
            if self.command is not None:
                if self.additional_data is not None:
                    self.command(self.value, *self.additional_data)
                else:
                    self.command(self.value)
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


if __name__ == "__main__":
    # Initialize Pygame
    pygame.init()
    import pygame
    import sys
    from button import Button

    # Constants
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    BACKGROUND_COLOR = (0, 0, 0)

    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Slider Example")

    # Define colors
    WHITE = (255, 255, 255)
    BUTTON_COLOR = (50, 50, 50)
    BUTTON_HOVER_COLOR = (100, 100, 100)

    # Create a button
    button = Button("Click me", 50, 50, 150, 50, lambda: print("Button Clicked"))

    # Create a slider
    def slider_callback(value):
        print("Slider Value:", value)

    slider = Slider(50, 150, 200, 20, 0, 100, 50, slider_callback)

    # Main game loop
    while True:
        screen.fill(BACKGROUND_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle events for the button and slider
            button.handle_event(event)
            slider.handle_event(event)

        # Draw the button and slider
        button.draw(screen)
        slider.draw(screen)

        # Update the display
        pygame.display.flip()
