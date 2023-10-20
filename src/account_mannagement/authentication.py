import pygame
from playfab.PlayFabClientAPI import (
    LoginWithEmailAddress,
    RegisterPlayFabUser,
    LoginWithGoogleAccount,
)
from playfab import PlayFabSettings
from captcha.image import ImageCaptcha
from playfab.PlayFabClientAPI import IsClientLoggedIn
import tkinter as tk
from tkinter import filedialog
import hashlib
from uimanagement.input_feild import InputField
from uimanagement.button import Button

infoObject: object = pygame.display.Info()
screen: pygame.Surface = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h)
)
pygame_icon = pygame.image.load(
    r"terraria_styled_game\program recources\Screenshot 2023-09-21 181742.png"
)
pygame.display.set_icon(pygame_icon)
# pygame.display.toggle_fullscreen()

pygame.display.set_caption("Square Pixel")


# Function to display a message on the screen
def display_message(message, color=(255, 0, 0)):
    global current_message
    current_message = message
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text_surface, text_rect)


# Constants
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
BACKGROUND_COLOR = (0, 0, 0)

font = pygame.font.Font("terraria_styled_game\Fonts\PixelifySans-Regular.ttf", 36)
# Define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)
white = (255, 255, 255)

PlayFabSettings.TitleId = "4AAA9"


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

    def back(self):
        global current_page, main_page
        current_page = main_page

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
            request = {"CreateAccount": True}
            request["TitleId"] = PlayFabSettings.TitleId
            request["Email"] = email
            request["Password"] = password
            request["Username"] = username

            # Upload the profile picture if it has been selected
            if self.profile_picture:
                request["ProfilePicture"] = self.profile_picture

            result = RegisterPlayFabUser(request, callback)

            if result is not None and "SessionTicket" in result:
                signed_in = True
                display_message("Account created and signed in.", (0, 255, 0))
            else:
                None
        except Exception as e:
            display_message(f"Account creation failed: {e}")

    # Function to upload a profile picture
    def upload_profile_picture(self):
        # Open a file dialog to select a profile picture
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        file_path = filedialog.askopenfilename(title="Select a Profile Picture")
        root.destroy()  # Close the hidden root window

        if file_path:
            with open(file_path, "rb") as profile_picture:
                self.profile_picture = profile_picture.read()


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
        global signed_in, good  # , user
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
            request["TitleId"] = PlayFabSettings.TitleId
            request["Email"] = email
            request["Password"] = password
            result = LoginWithEmailAddress(request, callback)
            print(good)
            if good:
                signed_in = True
                em = hashlib.sha256(bytes(request["Email"]))
                p = hashlib.sha256(
                    bytes(request["Password"])
                )  # TODO #24 make keep logged in more secure
                if self.remember_me:  # TODO #26 #25 add remember me checkbox
                    # with open("h.h", "x") as x:
                    x = open("h.h", "w")
                    x.write(str(em + "\n" + p))
                    x.close()
                    # playfab.PlayFabClientAPI.GetPlayerProfile
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
