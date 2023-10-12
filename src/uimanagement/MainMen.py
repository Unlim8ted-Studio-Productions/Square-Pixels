import pygame
import sys
import eastereggs.credits_Easteregg as egg
from soundmanagement.music import play_music
import random

# Initialize Pygame
pygame.init()
# Constants
infoObject: object = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

backround = pygame.transform.scale(
    pygame.image.load(r"terraria_styled_game\ui\mainmen\backround\cover.png"),
    (infoObject.current_w + 20, infoObject.current_h + 20),
)
# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square Pixel")
pygame_icon = pygame.image.load(
    r"terraria_styled_game\program recources\Screenshot 2023-09-21 181742.png"
)
pygame.display.set_icon(pygame_icon)

# Define fonts
font = pygame.font.Font(None, 36)

# Define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)

white = (255, 255, 255)


# Cloud class
class Cloud:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.alpha = 0

    def move(self):
        self.x -= self.speed
        self.alpha += 1
        if self.alpha >= 255:
            self.alpha = 255

    def draw(self):
        self.image.set_alpha(self.alpha)
        screen.blit(self.image, (self.x, self.y))


# Load cloud images
cloud_images = [
    pygame.transform.scale(
        pygame.image.load(r"terraria_styled_game\ui\mainmen\backround\clouds1.png"),
        (infoObject.current_w / 4, infoObject.current_h / 4),
    ),
    pygame.transform.scale(
        pygame.image.load(r"terraria_styled_game\ui\mainmen\backround\clouds2.png"),
        (infoObject.current_w / 4, infoObject.current_h / 4),
    ),
]

# Create a list to hold cloud objects
clouds = []
# Game state
play_music(r"terraria_styled_game\sounds\music\Menu.mp3")
game_state = "menu"  # Initial state is the main menu
show_play_buttons = False  # Flag to control visibility of play buttons
show_multiplayer_options = False  # Flag to control visibility of multiplayer options


class Button:
    """Button class for creating interactive buttons in the game."""

    def __init__(self, text, x, y, width, height, command):
        """
        Initialize a button.

        Args:
            text (str): The text displayed on the button.
            x (int): The x-coordinate of the button's top-left corner.
            y (int): The y-coordinate of the button's top-left corner.
            width (int): The width of the button.
            height (int): The height of the button.
            command (function): The function to be executed when the button is clicked.
        """
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.command = command
        self.hovered = False

    def draw(self):
        """Draw the button on the screen."""
        color = BUTTON_HOVER_COLOR if self.hovered else BUTTON_COLOR
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        text = font.render(self.text, True, WHITE)
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
                self.command()


# Main Menu
def main_menu(host_button, join_button):
    """
    Display the main menu and handle user interactions.

    Args:
        host_button (Button): The button for hosting a multiplayer game.
        join_button (Button): The button for joining a multiplayer game.
    """
    multiplayer_button = Button(
        "Multiplayer",
        WIDTH // 2 - 100,
        HEIGHT // 2 + 50,
        200,
        50,
        toggle_multiplayer_options,
    )
    singleplayer_button = Button(
        "Singleplayer",
        WIDTH // 2 - 100,
        HEIGHT // 2 + 100,
        200,
        50,
        start_singleplayer_game,
    )
    back_button = Button("Back", WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50, back)
    play_button = Button(
        "Play", WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, toggle_play_buttons
    )
    settings_button = Button(
        "Settings", WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, open_settings
    )
    credits_button = Button(
        "Credits", WIDTH // 2 - 100, HEIGHT // 4 + 50, 200, 50, egg.start
    )
    quit_button = Button(
        "Quit", WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50, quit_game
    )

    while running:
        global clouds
        if len(clouds) <= 6:
            if random.randint(0, 100) < 2:
                cloud_image = random.choice(cloud_images)
                cloud_x = random.randint(0, infoObject.current_w)
                cloud_y = random.randint(0, 200)
                cloud_speed = random.uniform(0.1, 20)  # Random speed between 1 and 4
                new_cloud = Cloud(cloud_x, cloud_y, cloud_image, cloud_speed)
                clouds.append(new_cloud)

        # Remove clouds that are off-screen
        for cloud in clouds:
            if cloud.image == cloud_images[1]:
                if cloud.x <= -300:
                    clouds.remove(cloud)
            else:
                if cloud.x <= -500:
                    clouds.remove(cloud)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle events for buttons
            play_button.handle_event(event)
            settings_button.handle_event(event)
            quit_button.handle_event(event)
            credits_button.handle_event(event)
            if show_play_buttons:
                singleplayer_button.handle_event(event)
                multiplayer_button.handle_event(event)
                back_button.handle_event(event)
            if show_multiplayer_options:
                host_button.handle_event(event)
                join_button.handle_event(event)

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw buttons
        screen.blit(
            backround, (0, 0, infoObject.current_w / 20, infoObject.current_h / 20)
        )
        # Move and draw clouds
        for cloud in clouds:
            cloud.move()
            cloud.draw()
        if not show_play_buttons:
            credits_button.draw()
            play_button.draw()
            settings_button.draw()
            quit_button.draw()

        if show_play_buttons:
            singleplayer_button.draw()
            multiplayer_button.draw()
            back_button.draw()

        if show_multiplayer_options:
            host_button.draw()
            join_button.draw()

        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


# Multiplayer Game
def start_game():
    """
    Start the multiplayer game.
    """
    global game_state, show_play_buttons
    game_state = "multiplayer"
    show_play_buttons = False


# Singleplayer Game
def start_singleplayer_game():
    """
    Start the singleplayer game.
    """
    global running
    pygame.mixer.music.fadeout(2)
    running = False


# Host Multiplayer Game
def host_multiplayer_game():
    """
    Host a multiplayer game.
    """
    import uimanagement.server_ui as server_ui

    server_ui.load_servers()
    server_ui.load_mplayers()
    server_ui.game_loop()


# Join Multiplayer Game
def join_multiplayer_game():
    """
    Join a multiplayer game.
    """
    import uimanagement.client_ui as client_ui

    client_ui.find_servers()
    client_ui.main()


# Toggle the visibility of play buttons
def toggle_play_buttons():
    """
    Toggle the visibility of play buttons.
    """
    global show_play_buttons
    show_play_buttons = not show_play_buttons


# Toggle the visibility of multiplayer options
def toggle_multiplayer_options():
    """
    Toggle the visibility of multiplayer options.
    """
    global show_multiplayer_options
    show_multiplayer_options = not show_multiplayer_options


# Open the settings menu
def open_settings():
    """
    Open the settings menu.
    """
    global game_state
    game_state = "settings"


def back():
    """
    Go back to the previous menu.
    """
    global show_play_buttons, game_state
    show_play_buttons = not show_play_buttons
    game_state = "menu"


# Quit the game
def quit_game():
    """
    Quit the game.
    """
    pygame.quit()
    sys.exit()


def mainfunc():
    """
    Main function to run the game.
    """
    global running
    # Initialize multiplayer and singleplayer buttons
    host_button = Button(
        "Host", WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, host_multiplayer_game
    )
    join_button = Button(
        "Join", WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50, join_multiplayer_game
    )
    running = True
    # Main game loop
    while running:
        # Generate a random cloud
        if game_state == "menu":
            main_menu(host_button, join_button)
        elif game_state == "multiplayer":
            if show_multiplayer_options:
                host_button.draw()
                join_button.draw()
        elif game_state == "singleplayer":
            import SquarePixel

            SquarePixel.main()
        elif game_state == "settings":
            # Implement the settings menu here
            pass

        # Add other game states as needed
        pygame.display.update()
        pygame.time.Clock().tick(FPS)


if __name__ == "__main__":
    mainfunc()
