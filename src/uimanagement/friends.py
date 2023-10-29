import pygame
from playfab.PlayFabClientAPI import (
    GetFriendLeaderboard,
    AddFriend,
    RemoveFriend,
    CreateSharedGroup,
    SetFriendTags,
)
import playfab.PlayFabErrors as PlayFabErrors
import playfab.PlayFabSettings as PlayFabSettings
import requests
import json

pygame.init()
if __name__ == "__main__":
    from button import Button
    from input_feild import InputField
else:
    from uimanagement.button import Button
    from uimanagement.input_feild import InputField


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
font = pygame.font.Font("terraria_styled_game\Fonts\PixelifySans-Regular.ttf", 36)

WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h


# Function to display a message on the screen
def display_message(message, color=(255, 0, 0)):
    global current_message
    current_message = message
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text_surface, text_rect)


class Friends:
    def __init__(self):
        self.font = None  # You should initialize this appropriately
        self.current_message = ""
        self.friends = []

    def DoPost(
        self,
        urlPath,
        request,
        authKey,
        authVal,
        callback,
        customData=None,
        extraHeaders=None,
    ):
        """
        Note this is a blocking call and will always run synchronously
        the return type is a dictionary that should contain a valid dictionary that
        should reflect the expected JSON response
        if the call fails, there will be a returned PlayFabError
        """

        url = PlayFabSettings.GetURL(
            urlPath, PlayFabSettings._internalSettings.RequestGetParams
        )

        try:
            j = json.dumps(request)
        except Exception as e:
            raise PlayFabErrors.PlayFabException(
                "The given request is not json serializable. {}".format(e)
            )

        requestHeaders = {}

        if extraHeaders:
            requestHeaders.update(extraHeaders)

        requestHeaders["Content-Type"] = "application/json"
        requestHeaders[
            "X-PlayFabSDK"
        ] = PlayFabSettings._internalSettings.SdkVersionString
        requestHeaders[
            "X-ReportErrorAsSuccess"
        ] = "true"  # Makes processing PlayFab errors a little easier

        if authKey and authVal:
            requestHeaders[authKey] = authVal

        httpResponse = requests.post(url, data=j, headers=requestHeaders)
        # print(httpResponse)

        error = response = None

        if httpResponse.status_code != 200:
            # Failed to contact PlayFab Case
            error = PlayFabErrors.PlayFabError()

            error.HttpCode = httpResponse.status_code
            error.HttpStatus = httpResponse.reason
        else:
            # Contacted playfab
            responseWrapper = json.loads(httpResponse.content.decode("utf-8"))
            # print(responseWrapper)
            if responseWrapper["code"] != 200:
                # contacted PlayFab, but response indicated failure
                error = responseWrapper
                return None
            else:
                # successful call to PlayFab
                response = responseWrapper["data"]
                return response

        if error and callback:
            self.callGlobalErrorHandler(error)

            try:
                # Notify the caller about an API Call failure
                callback(None, error)
            except Exception as e:
                # Global notification about exception in caller's callback
                PlayFabSettings.GlobalExceptionLogger(e)
        elif (response or response == {}) and callback:
            try:
                # Notify the caller about an API Call success
                # User should also check for {} on the response as it can still be a valid call
                callback(response, None)
            except Exception as e:
                # Global notification about exception in caller's callback
                PlayFabSettings.GlobalExceptionLogger(e)
        elif callback:
            try:
                # Notify the caller about an API issue, response was none
                emptyResponseError = PlayFabErrors.PlayFabError()
                emptyResponseError.Error = "Empty Response Recieved"
                emptyResponseError.ErrorMessage = (
                    "PlayFabHTTP Recieved an empty response"
                )
                emptyResponseError.ErrorCode = PlayFabErrors.PlayFabErrorCode.Unknown
                callback(None, emptyResponseError)
            except Exception as e:
                # Global notification about exception in caller's callback
                PlayFabSettings.GlobalExceptionLogger(e)

        # Your existing DoPost function with "self" references

    def callGlobalErrorHandler(self, error):
        if PlayFabSettings.GlobalErrorHandler:
            try:
                # Global notification about an API Call failure
                PlayFabSettings.GlobalErrorHandler(error)
            except Exception as e:
                # Global notification about exception in caller's callback
                PlayFabSettings.GlobalExceptionLogger(e)

    def display_message(self, message, color=(255, 0, 0)):
        self.current_message = message
        text_surface = self.font.render(message, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        self.screen.blit(text_surface, text_rect)

    def GetFriendsList_http(
        self, request, callback, customData=None, extraHeaders=None
    ):
        """
        Retrieves the current friend list for the local user, constrained to users who have PlayFab accounts. Friends from
        linked accounts (Facebook, Steam) are also included. You may optionally exclude some linked services' friends.
        https://docs.microsoft.com/rest/api/playfab/client/friend-list-management/getfriendslist
        """
        if not PlayFabSettings._internalSettings.ClientSessionTicket:
            raise PlayFabErrors.PlayFabException(
                "Must be logged in to call this method"
            )

        def wrappedCallback(playFabResult, error):
            if callback:
                callback(playFabResult, error)

        return self.DoPost(
            "/Client/GetFriendsList",
            request,
            "X-Authorization",
            PlayFabSettings._internalSettings.ClientSessionTicket,
            wrappedCallback,
            customData,
            extraHeaders,
        )

    def get_friends(self):
        request = {}

        def callback(success, failure):
            if success:
                print("success")
                self.display_message("success")
            else:
                self.display_message("failed")
                print("failed")
                if failure:
                    self.display_message("Here's some debug information:")
                    self.display_message(str(failure) + "leader board")

        try:
            result = self.GetFriendsList_http(request, callback)
        except:
            result = None
        if result is not None:
            print(result)
            return result
        else:
            return []

    def display_friends(self, friends):
        y = 100
        for friend in friends:
            friend_text = self.font.render(friend.username, True, (255, 255, 255))
            self.screen.blit(friend_text, (50, y))
            y += 50

    def add_friends(self, friend_identifier):
        if "@" in friend_identifier:
            # If the friend_identifier contains "@" symbol, it's an email
            request = {"FriendEmail": friend_identifier}
        else:
            # Otherwise, it's a username
            request = {"FriendUsername": friend_identifier}

        def callback(success, failure):
            if success:
                print("success")
                self.display_message("success")
            else:
                self.display_message("failed")
                print("failed")
                if failure:
                    self.display_message("Here's some debug information:")
                    self.display_message(str(failure) + "leader board")

        # Call the AddFriend method
        try:
            result = AddFriend(request, callback)
        except:
            print("error")


class FriendScreen:
    def __init__(self):
        self.activebuttons = []
        self.friend_list = [
            "Friends will appear here"
        ]  # Initialize a list to store friend names
        self.pending_friend_list = []  # List to store pending friend requests
        self.friend_list_offset = 0  # Offset for displaying friends
        self.show_pending_friends = (
            False  # To toggle between "Friends" and "Pending Friends" tabs
        )
        self.selected_tab = "Friends"  # Initialize the selected tab
        self.search_bar = InputField(50, 50, 400, 40, "Search Friends")
        self.search_bar.size = 30
        self.add_friend_input = InputField(50, 220, 400, 40, "Enter Username/Email")
        self.friends_instance = Friends()
        self.add_friend_tab = Button(
            "Add Friend",
            50,
            150,
            200,
            50,
            self.show_add_friends,
        )
        self.add_friend_button = Button(
            "Send Friend Request",
            150,
            270,
            200,
            50,
            self.add_friend,
        )
        self.refresh_button = Button(
            "Refresh",
            50,
            100,
            200,
            50,
            self.refresh_friends,
        )
        self.friends_tab_button = Button(
            "Friends",
            270,
            95,
            200,
            50,
            self.show_friends,
        )
        self.pending_friends_tab_button = Button(
            "Pending Friends",
            300,
            150,
            200,
            50,
            self.show_pending_friends_list,
        )
        # self.back_button = Button(
        #    "Back",
        #    50,
        #    HEIGHT - 100,
        #    200,
        #    50,
        #    self.back,
        # )
        self.activebuttons.extend(
            [
                self.search_bar,
                self.refresh_button,
                self.friends_tab_button,
                self.add_friend_tab,
                self.pending_friends_tab_button,
            ]
        )

    def render(self):
        # Background for the friend list
        # Highlight the selected tab
        backround = pygame.Surface(
            (525, pygame.display.Info().current_h), pygame.SRCALPHA
        )

        pygame.draw.rect(
            backround,
            (0, 0, 0, 100),
            (0, 0, 525, pygame.display.Info().current_h),
        )
        screen.blit(
            backround,
            (
                0,
                0,
            ),
        )
        if self.selected_tab == "Friends":
            self.friends_tab_button.selected()
            # Display the list of friends
            self.display_friends()

            self.activebuttons = []
            self.activebuttons.extend(
                [
                    self.search_bar,
                    self.refresh_button,
                    self.friends_tab_button,
                    self.add_friend_tab,
                    self.pending_friends_tab_button,
                ]
            )

        elif self.selected_tab == "Pending Friends":
            # Display the list of pending friends
            self.display_pending_friends()
            self.pending_friends_tab_button.selected()

        elif self.selected_tab == "Add Friends":
            self.activebuttons = []
            self.activebuttons.extend(
                [
                    self.search_bar,
                    self.refresh_button,
                    self.friends_tab_button,
                    self.add_friend_tab,
                    self.pending_friends_tab_button,
                    self.add_friend_input,
                    self.add_friend_button,
                ]
            )

        for button in self.activebuttons:
            button.draw(screen)

    def refresh_friends(self):
        # Call a method to refresh the friend list
        self.friend_list = self.friends_instance.get_friends()
        # Also, update the pending friend list if needed

    def show_friends(self):
        self.show_pending_friends = False
        self.selected_tab = "Friends"

    def show_pending_friends_list(self):
        # Call a method to get pending friend requests
        self.selected_tab = "Pending Friends"
        self.pending_friend_list = self.friends_instance.get_pending_friend_requests()
        self.show_pending_friends = True

    def get_friends(self):
        self.friends = self.friends_instance.get_friends()

    def show_add_friends(self):
        self.selected_tab = "Add Friends"

    # Function to add a friend
    def add_friend(self):
        friend_name = self.add_friend_input.text
        if friend_name:
            self.friend_list.append(friend_name)
            self.friends_instance.add_friends(friend_name)
            # Send a request to the server to add the friend
            self.add_friend_input.clear()

    # Function to display the list of friends
    def display_friends(self):
        # Filter friends based on the search bar input
        search_text = self.search_bar.text.lower()
        filtered_friends = [
            friend for friend in self.friend_list if search_text in friend.lower()
        ]

        # Display a portion of the filtered friend list (e.g., 10 friends at a time)
        y = 200
        for friend in filtered_friends[
            self.friend_list_offset : self.friend_list_offset + 10
        ]:
            friend_text = font.render(friend, True, (255, 255, 255))
            screen.blit(friend_text, (50, y))
            y += 50

    # Function to go back to the main menu
    def back(self):
        global current_page, main_page
        current_page = main_page


# Usage Example:
instance = FriendScreen()


if __name__ == "__main__":
    # instance.friend_list = instance.get_friends()

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle user input events
            for button in instance.activebuttons:
                button.handle_event(event)

        # Update your friend list or other game logic as needed
        # friend_screen.update()

        # Clear the screen
        screen.fill((255, 255, 255))

        instance.render()
        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
