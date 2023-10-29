import pygame
import sys
import playfab
from playfab.PlayFabClientAPI import (
    LoginWithEmailAddress,
    RegisterPlayFabUser,
    LoginWithGoogleAccount,
)
from playfab import PlayFabSettings
from captcha.image import ImageCaptcha

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
font = pygame.font.Font(None, 36)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)

# Initialize Pygame screen with the RESIZABLE flag
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Authentication Example")

# Initialize PlayFab
PlayFabSettings.TitleId = "4AAA9"


# Create an InputField class for text input
class InputField:
    def __init__(self, x, y, width, height, placeholder):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.placeholder = placeholder
        self.text = ""
        self.active = False

    def draw(self):
        color = BUTTON_COLOR if not self.active else BUTTON_HOVER_COLOR
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        font_color = (0, 0, 0) if not self.active else (255, 255, 255)
        text = font.render(
            self.text if self.text else self.placeholder, True, font_color
        )
        screen.blit(text, (self.x + 10, self.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                screen.fill(WHITE)
                self.text = self.text[:-1]
            else:
                self.text += event.unicode


# Create a screen for the sign-up process
class SignUpScreen:
    def __init__(self):
        self.buttons = []
        self.username_input = InputField(200, 50, 400, 40, "Username")
        self.email_input = InputField(200, 100, 400, 40, "Email")
        self.password_input = InputField(200, 150, 400, 40, "Password")
        self.create_account_button = Button(
            "Create Account", 200, 200, 200, 50, self.create_account
        )
        self.google_login_button = Button(
            "Google Login", 200, 260, 200, 50, self.google_login
        )
        self.buttons.extend(
            [
                self.username_input,
                self.email_input,
                self.password_input,
                self.create_account_button,
                self.google_login_button,
            ]
        )

    def render(self):
        for button in self.buttons:
            button.draw()

    # Function to create an account with an email address

    def create_account(self):
        global signed_in
        email = self.email_input.text
        password = self.password_input.text
        username = self.username_input.text

        def callback(success, failure):
            if success:
                display_message("Account created and signed in.", (0, 255, 0))
            else:
                display_message("Account creation failed.")
                if failure:
                    display_message("Here's some debug information:")
                    display_message(failure)

        try:
            request = {"CreateAccount": True}
            request["TitleId"] = PlayFabSettings.TitleId
            request["Email"] = email
            request["Password"] = password
            request["Username"] = username
            result = playfab.PlayFabClientAPI.RegisterPlayFabUser(request, callback)

            if result is not None and "SessionTicket" in result:
                signed_in = True
                print("Account created and signed in.", (0, 255, 0))
            else:
                None
        except Exception as e:
            display_message(f"Account creation failed: {e}")

    def google_login(self):
        request = {"CreateAccount": True}
        request["TitleId"] = PlayFabSettings.TitleId
        request[
            "ServerAuthCode"
        ] = "95487563442-ta5a931frpcrsm78js4q5eb2sjvi927m.apps.googleusercontent.com"

        def callback(success, failure):
            if success:
                display_message("Account created and signed in.", (0, 255, 0))
            else:
                display_message("Account creation failed.")
                if failure:
                    display_message("Here's some debug information:")
                    display_message(str(failure))

        result = playfab.PlayFabClientAPI.LoginWithGoogleAccount(request, callback)

    # Function to send a verification code to the provided email
    def send_verification_code(self):
        email = self.email_input.text


# Create a screen for the sign-in process
class SignInScreen:
    def __init__(self):
        self.buttons = []
        self.email_input = InputField(200, 100, 400, 40, "Email")
        self.password_input = InputField(200, 150, 400, 40, "Password")
        self.sign_in_button = Button(
            "Sign In", 200, 200, 200, 50, self.sign_in_with_email
        )
        self.buttons.extend(
            [self.email_input, self.password_input, self.sign_in_button]
        )

    def render(self):
        for button in self.buttons:
            button.draw()

    # Function to sign in with an email address

    def sign_in_with_email(self):
        global signed_in
        email = self.email_input.text
        password = self.password_input.text

        def callback(success, failure):
            if success:
                display_message("Account created and signed in.", (0, 255, 0))
            else:
                display_message("Account creation failed.")
                if failure:
                    display_message("Here's some debug information:")
                    display_message(str(failure))

        try:
            request = {}
            request["TitleId"] = PlayFabSettings.TitleId
            request["Email"] = email
            request["Password"] = password
            result = playfab.PlayFabClientAPI.LoginWithEmailAddress(request, callback)

            if result is not None and "SessionTicket" in result:
                signed_in = True
                display_message("Signed in.", (0, 255, 0))
            else:
                display_message("Sign-in failed.")
        except Exception as e:
            display_message(f"Sign-in failed: {e}")

    # Function to send a verification code to the provided email
    def send_verification_code(self):
        email = self.email_input.text

    # Add code to send a verification code to the email
    # You would typically use an email service or other means to send the code


# Function to display a message on the screen
def display_message(message, color=(255, 0, 0)):
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface, text_rect)


# Create a Button class with text input fields
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


# Create a "Not a Robot" button
# not_a_robot_button = Button("Not a Robot", 100, 350, 200, 50)


# Create pages for different states
class Page:
    def __init__(self):
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def render(self):
        for button in self.buttons:
            button.draw()


# Create a page for email input and verification
email_verification_page = Page()

# Initialize the current page to the email verification page
current_page = email_verification_page


# Define a function to switch the current page to the sign-up screen
def switch_to_sign_up():
    global current_page
    screen.fill(WHITE)
    current_page = SignUpScreen()


# Define a function to switch the current page to the sign-in screen
def switch_to_sign_in():
    global current_page
    screen.fill(WHITE)
    current_page = SignInScreen()


# Update the button click handlers to switch to the respective screens
email_verification_page.add_button(
    Button("Create Account", 100, 250, 200, 50, switch_to_sign_up)
)
email_verification_page.add_button(
    Button("Sign In", 350, 250, 200, 50, switch_to_sign_in)
)

running = True
screen.fill(WHITE)
# Main game loop
while running:
    current_page.render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        # Handle button events based on the current page
        for button in current_page.buttons:
            button.handle_event(event)

    pygame.display.update()

# Clean up and exit
pygame.quit()
sys.exit()
