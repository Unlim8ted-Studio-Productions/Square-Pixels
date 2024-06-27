import os
import PIL
import pygame
import sys
import SquarePixels.eastereggs.credits_Easteregg as egg
from SquarePixels.soundmanagement.music import play_music
import random
import playfab
from playfab import PlayFabSettings
from captcha.image import ImageCaptcha
from playfab.PlayFabClientAPI import IsClientLoggedIn
from playfab.PlayFabClientAPI import (
    LoginWithEmailAddress,
    RegisterPlayFabUser,
    LoginWithGoogleAccount,
)
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import hashlib
from SquarePixels.uimanagement.easy_ui_maker import start
import http.client
from SquarePixels.uimanagement.get_user_avatar import get_user_avatar
from SquarePixels.uimanagement.elements.Image import ImageElement


# from account_mannagement.authentication import SignInScreen, SignUpScreen
from SquarePixels.uimanagement.leaderboard import (
    display_leaderboard,
    update_leaderboard,
    get_leaderboard,
    next_leadeboard_page,
    previous_leadeboard_page,
    search_input_callback_l,
)
from SquarePixels.uimanagement.elements.input_feild import InputField
from SquarePixels.uimanagement.elements.checkbox import CheckBox
from SquarePixels.uimanagement.elements.button import Button
from SquarePixels.uimanagement.elements.TextElement import TextElement
from SquarePixels.uimanagement.elements.slider import Slider
from SquarePixels.uimanagement.clouds import Cloud
from SquarePixels.uimanagement.friends import instance

# Initialize Pygame
pygame.init()
# Add the signed_in flag
signed_in = IsClientLoggedIn()
em = ""
p = ""
current_message = ""
# Constants
infoObject: object = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60
good = False
backround = pygame.transform.scale(
    pygame.image.load(r"Recources\ui\mainmen\backround\cover.png"),
    (infoObject.current_w + 100, infoObject.current_h + 80),
)
# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square Pixel")
pygame_icon = pygame.image.load(
    r"Recources\program recources\Screenshot 2023-09-21 181742.png"
)
pygame.display.set_icon(pygame_icon)

playfabsettings = PlayFabSettings
playfabsettings.TitleId = "4AAA9"
# Define fonts
font = pygame.font.Font(None, 36)

# Define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)

white = (255, 255, 255)

# Initial position of the background
bg_x, bg_y = 0, 0

# Load cloud images
cloud_images = [
    pygame.transform.scale(
        pygame.image.load(r"Recources\ui\mainmen\backround\clouds1.png"),
        (infoObject.current_w / 4, infoObject.current_h / 4),
    ),
    pygame.transform.scale(
        pygame.image.load(r"Recources\ui\mainmen\backround\clouds2.png"),
        (infoObject.current_w / 4, infoObject.current_h / 4),
    ),
]
volume, fogofwar, shadefogofwar = 1, False, False
# Create a list to hold cloud objects
clouds = []
# Game state
play_music(r"Recources\sounds\music\Menu.mp3")
game_state = "menu"  # Initial state is the main menu
show_play_buttons = False  # Flag to control visibility of play buttons
show_multiplayer_options = False  # Flag to control visibility of multiplayer options


# Create a screen for the sign-up process
class SignUpScreen:
    def __init__(self):
        self.buttons = []
        self.username_input = InputField(
            WIDTH // 2 - 100, HEIGHT // 2 - 100, 400, 40, "Username"
        )
        self.email_input = InputField(
            WIDTH // 2 - 100, HEIGHT // 2 - 50, 400, 40, "Email"
        )
        self.password_input = InputField(
            WIDTH // 2 - 100, HEIGHT // 2, 400, 40, "Password"
        )
        self.profile_picture_button = Button(
            "Upload Profile Picture",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 50,
            200,
            50,
            self.upload_profile_picture,
        )
        self.create_account_button = Button(
            "Create Account",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 100,
            200,
            50,
            self.create_account,
        )
        self.google_login_button = Button(
            "Google Login",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 150,
            200,
            50,
            self.google_login,
        )
        self.back_button = Button(
            "Back",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 200,
            200,
            50,
            self.back,
        )
        self.buttons.extend(
            [
                self.username_input,
                self.email_input,
                self.password_input,
                self.profile_picture_button,
                self.create_account_button,
                self.google_login_button,
                self.back_button,
            ]
        )
        self.profile_picture = None

    def render(self):
        for button in self.buttons:
            button.draw(screen)
        if self.profile_picture:
            self.profile_picture.draw(screen)

    def back(self):
        global current_page, main_page
        current_page = main_page

    def google_login(self):
        request = {"CreateAccount": True}
        request["TitleId"] = playfabsettings.TitleId
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

        result = LoginWithGoogleAccount(request, callback)

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
                    display_message(str(failure))

        try:
            conn = http.client.HTTPSConnection("api.eva.pingutil.com")
            payload = ""
            headers = {}
            conn.request("GET", f"/email?email={email}", payload, headers)
            res = conn.getresponse()
            data = res.read()
            # https://www.loginradius.com/blog/engineering/email-verification-api/
            email_data = data.decode("utf-8")
            if email_data["status"] == "success":
                email_data = email_data["data"]
                if email_data["disposible"] == False:
                    if email_data["valid_syntax"] == True:
                        if email_data["deliverable"] == True:
                            request = {"CreateAccount": True}
                            request["TitleId"] = playfabsettings.TitleId
                            request["Email"] = email
                            request["Password"] = password
                            request["Username"] = username

                            # Upload the profile picture if it has been selected
                            if self.profile_picture:
                                request["ProfilePicture"] = self.profile_picture

                            result = RegisterPlayFabUser(request, callback)

                            if result is not None and "SessionTicket" in result:
                                signed_in = True
                                display_message(
                                    "Account created and signed in.", (0, 255, 0)
                                )
                            else:
                                None
                        else:
                            display_message("Invalid Email.", (0, 255, 0))
                    else:
                        display_message("Invalid Email Syntax.", (0, 255, 0))
                else:
                    display_message("Don't use a disposible email.", (0, 255, 0))
            else:
                display_message("Couldn't check for email validness.", (0, 255, 0))
        except Exception as e:
            display_message(f"Account creation failed: {e}")

    # Function to upload a profile picture
    def upload_profile_picture(self) -> None:
        """Uploads a selected profile picture
        Args:
            self: The class instance
        Returns:
            None: No value is returned
        - Opens a file dialog window to select a profile picture file
        - Gets the file path of the selected picture
        - Checks if a file was selected before closing the dialog
        """
        # Open a file dialog to select a profile picture
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename(title="Select a Profile Picture")
        root.destroy()  # Close the hidden root window

        if file_path:
            self.profile_picture = Image.open(file_path, "r")
            self.profile_picture = self.profile_picture.resize(
                [HEIGHT // 2 + 50, HEIGHT // 2 + 50]
            )
            self.profile_picture = ImageElement(
                (WIDTH - 25) - self.profile_picture.width,
                25,
                self.profile_picture,
                "Circle",
            )


# Create a screen for the sign-in process
class SignInScreen:
    def __init__(self):
        self.buttons = []
        self.email_input = InputField(
            WIDTH // 2 - 100, HEIGHT // 2 - 50, 400, 40, "Email"
        )
        self.password_input = InputField(
            WIDTH // 2 - 100, HEIGHT // 2, 400, 40, "Password"
        )
        self.sign_in_button = Button(
            "Sign In",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 50,
            200,
            50,
            self.sign_in_with_email,
        )
        self.back_button = Button(
            "Back",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 100,
            200,
            50,
            self.back,
        )
        self.buttons.extend(
            [
                self.email_input,
                self.password_input,
                self.sign_in_button,
                self.back_button,
            ]
        )
        self.remember_me = True

    def render(self):
        for button in self.buttons:
            button.draw(screen)

    # Function to sign in with an email address

    def sign_in_with_email(self, email=None, password=None):
        global signed_in, good, em, p  # , user
        if email == None and password == None:
            email = self.email_input.text
            password = self.password_input.text
        # print(email + "\n" + password)

        def callback(success, failure):
            global good
            if success:
                good = True
                display_message("Account created and signed in.", (0, 255, 0))
            else:
                display_message("Account creation failed.")
                if failure:
                    display_message("Here's some debug information:")
                    display_message(str(failure))

        try:
            request = {}
            request["TitleId"] = playfabsettings.TitleId
            request["Email"] = email
            request["Password"] = password
            result = LoginWithEmailAddress(request, callback)
            print(good)
            if good:
                signed_in = True
                em = request["Email"]
                p = request["Password"]
                # TODO #24 make keep logged in more secure
                if self.remember_me:  # TODO #26 #25 add remember me checkbox
                    # with open("h.h", "x") as x:
                    # Create peekaboo.py and add var1 and var2
                    with open(
                        "SquarePixels/eastereggs/peekaboo.py", "w"
                    ) as peekaboo_file:
                        peekaboo_file.write(f"var1 = {em}\n")
                        peekaboo_file.write(f"var2 = {p}\n")
                #
                ## Compile peekaboo.py to peekaboo.pyc
                # import py_compile
                #
                # py_compile.compile("peekaboo.py")
                # import peekaboo
                #
                # os.remove("peekaboo.py")
                #
                ## Create remember.cfg with the value True
                # with open("remember.py", "w") as cfg_file:
                #    cfg_file.write("t = True\n")
                #
                ## playfab.PlayFabClientAPI.GetPlayerProfile
                # user = {""}
                display_message("Signed in.", (0, 255, 0))
                return
            else:
                print("signed in failed")
                display_message("Sign-in failed.")
        except Exception as e:
            display_message(f"Sign-in failed: {e}")

    # Function to toggle the "Remember Me" checkbox
    def toggle_remember_me(self):
        self.remember_me = not self.remember_me

    # Function to send a verification code to the provided email
    def send_verification_code(self):
        email = self.email_input.text

    def back(self):
        global current_page, main_page
        current_page = main_page

    # Add code to send a verification code to the email
    # You would typically use an email service or other means to send the code


# Main Menu
def main_menu(
    host_button,
    join_button,
    leaderboard_data,
    leaderboard_page,
    next_button,
    previous_button,
    search_input,
    search_button,
):
    """
    Display the main menu and handle user interactions.

    Args:
        host_button (Button): The button for hosting a multiplayer game.
        join_button (Button): The button for joining a multiplayer game.
    """
    global bg_x, bg_y, clouds, game_state, volume, fogofwar, shadefogofwar
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
    UImaker = Button(
        "Make UI (for testing purposes only) <unless future mod system...>",
        infoObject.current_w / 2 - 411,
        800,
        822,
        50,
        start,
    )
    UImaker.size = 20
    store = Button(
        "Store",
        infoObject.current_w / 2 - 411,
        800,
        822,
        50,
        None,
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
    quit_button = Button("Quit", WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50, quit)

    fogwareffect = CheckBox(
        WIDTH / 3.5489833641404807,
        HEIGHT / 3.857142857142857,
        "fog of war effect",
        False,
        15,
    )
    shadefogwareffect = CheckBox(
        WIDTH / 3.5489833641404807,
        HEIGHT / 2.857142857142857,
        "shade fog of war effect",
        False,
        15,
    )
    volumet = Slider(
        WIDTH / 2.591093117408907,
        HEIGHT / 3.8028169014084505,
        WIDTH / 19.2,
        HEIGHT / 108.0,
        0,
        3,
        1.0,
        None,
        None,
        (255, 255, 255, 255),
        (200, 200, 200),
        "volume",
        True,
        26,
    )

    savesettings = Button(
        "save",
        WIDTH / 2.4935064935064934,
        HEIGHT / 2.4107142857142856,
        WIDTH / 19.2,
        HEIGHT / 21.6,
        savesettingstofile,
    )

    exitsettings = Button(
        "back",
        WIDTH / 3.1578947368421053,
        HEIGHT / 2.4053452115812917,
        WIDTH / 19.2,
        HEIGHT / 21.6,
        exitsettingsmenu,
    )

    while running:
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
            if game_state == "settings":
                volumet.handle_event(event)
                fogwareffect.handle_event(event)
                shadefogwareffect.handle_event(event)
                savesettings.handle_event(event)
                exitsettings.handle_event(event)

            # Handle events for buttons
            if not game_state == "settings":
                for button in instance.activebuttons:
                    button.handle_event(event)
                play_button.handle_event(event)
                settings_button.handle_event(event)
                quit_button.handle_event(event)
                credits_button.handle_event(event)
                UImaker.handle_event(event)
                update_leaderboard(
                    event, search_input, next_button, search_button, previous_button
                )
            if show_play_buttons and not game_state == "settings":
                singleplayer_button.handle_event(event)
                multiplayer_button.handle_event(event)
                back_button.handle_event(event)
            if show_multiplayer_options and not game_state == "settings":
                host_button.handle_event(event)
                join_button.handle_event(event)

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)
        volume, fogofwar, shadefogofwar = (
            volumet.value,
            fogwareffect.is_checked,
            shadefogwareffect.is_checked,
        )
        # Draw buttons
        x, y = pygame.mouse.get_pos()
        #print(shadefogwareffect.is_checked)
        # Calculate the offset for the panoramic effect
        offset_x = (infoObject.current_w / 2 - x) / 20
        offset_y = (infoObject.current_h / 2 - y) / 20

        # Apply smoothing to gradually move toward the target position
        smoothing_factor = 0.1
        bg_x += (offset_x - bg_x) * smoothing_factor
        bg_y += (offset_y - bg_y) * smoothing_factor

        # Blit the background with the calculated offset
        screen.blit(backround, (round(-50 - bg_x), round(-50 - bg_y)))

        # Move and draw clouds
        for cloud in clouds:
            cloud.move()
            cloud.draw(screen)
        if game_state == "settings":
            volumet.draw(screen)
            fogwareffect.draw(screen)
            shadefogwareffect.draw(screen)
            exitsettings.draw(screen)
            savesettings.draw(screen)

        if not show_play_buttons and not game_state == "settings":
            credits_button.draw(screen)
            play_button.draw(screen)
            settings_button.draw(screen)
            quit_button.draw(screen)
            UImaker.draw(screen)
        # Render the friends ui
        instance.render()
        # render the leaderboard
        display_leaderboard(
            leaderboard_data,
            "",
            next_button,
            previous_button,
            search_input,
            search_button,
            screen,
            WIDTH,
            WHITE,
        )
        if show_play_buttons:
            singleplayer_button.draw(screen)
            multiplayer_button.draw(screen)
            back_button.draw(screen)

        if show_multiplayer_options:
            host_button.draw(screen)
            join_button.draw(screen)

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
    import SquarePixels.uimanagement.server_ui as server_ui

    server_ui.load_servers()
    server_ui.load_mplayers()
    server_ui.game_loop()


# Join Multiplayer Game
def join_multiplayer_game():
    """
    Join a multiplayer game.
    """
    import SquarePixels.uimanagement.client_ui as client_ui

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


# Function to display a message on the screen
def display_message(message, color=(255, 0, 0)):
    global current_message
    current_message = message
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text_surface, text_rect)


# Create a "Not a Robot" button
# not_a_robot_button = Button("Not a Robot", 100, 350, 200, 50)


# Create pages for different states
class Page:
    def __init__(self):
        """Initializes registration form fields and buttons
        Args:
            self: {The class instance}: Initializes registration form fields and buttons
        Returns:
            None: Does not return anything, initializes form fields and buttons
        {Processing Logic}:
            - Initializes InputField objects for username, email, password
            - Initializes Button objects for profile picture upload, account creation, Google login, back
            - Adds all InputField and Button objects to a buttons list
            - Sets initial profile picture to None"""
        self.buttons = []

    def add_button(self, button):
        self.buttons.append(button)

    def render(self):
        for button in self.buttons:
            button.draw(screen)


# Create a page for email input and verification
main_page = Page()

# Initialize the current page to the email verification page
current_page = main_page


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


def guest():
    global signed_in
    signed_in = "Guest"


# Add a function to show the sign-in or guest popup
def show_signin_popup(leaderboard_page):
    global WIDTH, HEIGHT, screen, BACKGROUND_COLOR, signed_in, current_message
    ########################DEVELOPMENTAL TESTING ONLY##############################
    signin_as_test_user = Button(
        "signin_as_test_user",
        WIDTH // 2 - 100,
        HEIGHT // 2 - 325,
        200,
        50,
        SignInScreen.sign_in_with_email,
        [None, "testuser@gmail.com", "test123"],
    )
    ########################DEVELOPMENTAL TESTING ONLY##############################
    create_account = Button(
        "Create Acount", WIDTH // 2 - 100, HEIGHT // 2 - 225, 200, 50, switch_to_sign_up
    )
    popup_font = pygame.font.Font(None, 24)
    popup_text = "Please sign in to play the game and save your progress."
    popup_text2 = "If you choose to play as a guest, your progress will reset daily because we won't be able to verify your ownership of the game."
    sign_in_button = Button(
        "Sign In", WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, switch_to_sign_in
    )
    guest_button = Button(
        "Play as Guest",
        WIDTH // 2 - 100,
        HEIGHT // 2 + 50,
        200,
        50,
        guest,  # play_as_guest
    )

    while True:
        global clouds, bg_x, bg_y

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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

        x, y = pygame.mouse.get_pos()

        # Calculate the offset for the panoramic effect
        offset_x = (infoObject.current_w / 2 - x) / 20
        offset_y = (infoObject.current_h / 2 - y) / 20

        # Apply smoothing to gradually move toward the target position
        smoothing_factor = 0.1
        bg_x += (offset_x - bg_x) * smoothing_factor
        bg_y += (offset_y - bg_y) * smoothing_factor

        # Blit the background with the calculated offset
        screen.blit(backround, (round(-50 - bg_x), round(-50 - bg_y)))

        # Move and draw clouds
        for cloud in clouds:
            cloud.move()
            cloud.draw(screen)

        display_message(current_message)
        popup_text_render = popup_font.render(popup_text, True, WHITE)
        popup_text2_render = popup_font.render(popup_text2, True, WHITE)
        if current_page == main_page:
            screen.blit(
                popup_text_render,
                (WIDTH // 2 - popup_text_render.get_width() // 2, HEIGHT // 2 - 100),
            )
            screen.blit(
                popup_text2_render,
                (WIDTH // 2 - popup_text2_render.get_width() // 2, HEIGHT // 2),
            )
            sign_in_button.draw(screen)
            guest_button.draw(screen)
            create_account.draw(screen)
            ########################DEVELOPMENTAL TESTING ONLY##############################
            signin_as_test_user.draw(screen)
            ########################DEVELOPMENTAL TESTING ONLY##############################
        current_page.render()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

            # Handle button events based on the current page
            if current_page != main_page:
                for button in current_page.buttons:
                    button.handle_event(event)
            else:
                sign_in_button.handle_event(event)
                guest_button.handle_event(event)
                create_account.handle_event(event)
                ########################DEVELOPMENTAL TESTING ONLY##############################
                signin_as_test_user.handle_event(event)
                ########################DEVELOPMENTAL TESTING ONLY##############################
        if signed_in != False:
            leaderboard_data = get_leaderboard(leaderboard_page, display_message)
            return leaderboard_data

        pygame.display.update()
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)


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


def exitsettingsmenu():
    global game_state
    game_state = "menu"


def savesettingstofile():
    global volume, fogofwar, shadefogofwar
    with open("config.py", "r") as file:
        lines = file.readlines()

    # Find and replace the values in the lines list
    for i, line in enumerate(lines):
        if "volume" in line:
            lines[i] = f"volume = {volume}\n"
        elif "fogofwar" in line:
            lines[i] = f"fogofwar = {fogofwar}\n"
        elif "shadefogofwar" in line:
            lines[i] = f"shadefogofwar = {shadefogofwar}\n"

    # Write the modified contents back to the config.py file
    os.remove("config.py")
    with open("config.py", "x") as file:
        file.writelines(lines)


def mainfunc():
    """
    Main function to run the game.
    """
    global running, current_leader_page
    # Add these constants to control pagination
    ENTRIES_PER_PAGE = 10
    current_leader_page = 1
    leaderboard_data = get_leaderboard(current_leader_page, display_message)
    # Initialize multiplayer and singleplayer buttons
    host_button = Button(
        "Host", WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, host_multiplayer_game
    )
    join_button = Button(
        "Join", WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50, join_multiplayer_game
    )
    # Add buttons for next and previous page
    next_button = Button(
        "Next Page",
        WIDTH - 120,
        HEIGHT - 40,
        100,
        30,
        next_leadeboard_page,
        [current_leader_page, leaderboard_data, display_message],
    )
    previous_button = Button(
        "Previous Page",
        WIDTH - 500,
        HEIGHT - 40,
        120,
        30,
        previous_leadeboard_page,
        [current_leader_page, leaderboard_data, display_message],
    )

    # Add the search button in the display_leaderboard function
    search_button = Button("Search", WIDTH - 320, 20, 80, 30, search_input_callback_l)
    # Add the search bar for filtering leaderboard entries
    search_input = InputField(WIDTH - 500, 20, 200, 30, "Search by Player Name")
    running = True
    fetch_leaderboard = False
    # Main game loop
    while running:
        # Generate a random cloud
        if (
            signed_in == False
        ):  # DO NOT CHANGE TO "IF NOT SIGNED_IN: because singed_in can also be a string"
            try:
                with open("h.h", "r") as a:
                    leaderboard_data = SignInScreen.sign_in_with_email(
                        SignInScreen(), a.readline(0), a.readline(1)
                    )
            except:
                leaderboard_data = show_signin_popup(current_leader_page)

        if signed_in == True:
            if not fetch_leaderboard:
                leaderboard_data = get_leaderboard(current_leader_page, display_message)
                # print(leaderboard_data)
                fetch_leaderboard = True
                # get_user_avatar(SignInScreen)

        if signed_in == "Guest":
            pass  # TODO:implement #22 guest logic in future
        # TODO #23 add function checking acount variable for having bought this game
        if game_state == "menu" or "settings":
            main_menu(
                host_button,
                join_button,
                leaderboard_data,
                current_leader_page,
                next_button,
                previous_button,
                search_input,
                search_button,
            )
        elif game_state == "multiplayer":
            if show_multiplayer_options:
                host_button.draw(screen)
                join_button.draw(screen)
        elif game_state == "singleplayer":
            import SquarePixel

            SquarePixel.main()

        # Add other game states as needed
        pygame.display.update()
        pygame.time.Clock().tick(FPS)


# Get a player's friends list
def get_friends_list():
    request = {}
    result = playfab.PlayFabClientAPI.GetFriendsList(request)
    if result is not None:
        friends = result.data.Friends
        # Process and display friends list in your game's UI


# Add a friend
def add_friend(player_id):
    request = {"FriendPlayFabId": player_id}
    playfab.PlayFabClientAPI.AddFriend(request)


# Handle friend requests, accept or decline
def handle_friend_request(friend_playfab_id, accept):
    if accept:
        request = {"FriendPlayFabId": friend_playfab_id}
        playfab.PlayFabClientAPI.AddFriend(request)
    else:
        request = {"FriendPlayFabId": friend_playfab_id}
        playfab.PlayFabClientAPI.RemoveFriend(request)


if __name__ == "__main__":
    mainfunc()
