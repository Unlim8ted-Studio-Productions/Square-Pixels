import playfab
import pygame
import json
import playfab.PlayFabSettings as PlayFabSettings
import playfab.PlayFabErrors as PlayFabErrors
import requests


def DoPost(
    urlPath, request, authKey, authVal, callback, customData=None, extraHeaders=None
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
    requestHeaders["X-PlayFabSDK"] = PlayFabSettings._internalSettings.SdkVersionString
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
        callGlobalErrorHandler(error)

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
            emptyResponseError.ErrorMessage = "PlayFabHTTP Recieved an empty response"
            emptyResponseError.ErrorCode = PlayFabErrors.PlayFabErrorCode.Unknown
            callback(None, emptyResponseError)
        except Exception as e:
            # Global notification about exception in caller's callback
            PlayFabSettings.GlobalExceptionLogger(e)


def callGlobalErrorHandler(error):
    if PlayFabSettings.GlobalErrorHandler:
        try:
            # Global notification about an API Call failure
            PlayFabSettings.GlobalErrorHandler(error)
        except Exception as e:
            # Global notification about exception in caller's callback
            PlayFabSettings.GlobalExceptionLogger(e)


font = pygame.font.Font("Recources\Fonts\PixelifySans-Regular.ttf", 36)
l_font = pygame.font.Font("Recources\Fonts\PixelifySans-Regular.ttf", 50)


# Functions for handling next and previous page
def next_leadeboard_page(current_leader_page, leaderboard_data, display_message):
    current_leader_page += 1
    leaderboard_data = get_leaderboard(current_leader_page, display_message)


def previous_leadeboard_page(current_leader_page, leaderboard_data, display_message):
    if current_leader_page > 1:
        current_leader_page -= 1
        leaderboard_data = get_leaderboard(current_leader_page, display_message)


# Function for handling search input
def search_input_callback_l(search_input):
    global search_query
    search_query = search_input.text


def display_leaderboard(
    leaderboard_data,
    search_query,
    next_button,
    previous_button,
    search_input,
    search_button,
    screen,
    WIDTH,
    WHITE,
):
    # Display leaderboard entries for the current page
    y = (
        pygame.display.Info().current_h
    ) / 3  # Initial y-coordinate for rendering leaderboard entries
    w = (pygame.display.Info().current_h) / 3
    # Create a transparent black color
    transparent_black = (0, 0, 0, 100)
    # Create a surface with the transparent black color and same dimensions as the rectangle
    transparent_surface = pygame.Surface(
        (w, pygame.display.Info().current_h - (y / 2)), pygame.SRCALPHA
    )
    pygame.draw.rect(
        transparent_surface,
        transparent_black,
        (
            0,
            0,
            w,
            y * 2,
        ),
    )

    screen.blit(transparent_surface, (WIDTH - w, y - 100, 1, 1))

    text_surface = l_font.render("Leader Board", True, WHITE)
    text_rect = text_surface.get_rect(right=WIDTH - 20, top=y - 50)
    screen.blit(text_surface, text_rect)

    for entry in leaderboard_data:
        player_name, score = entry["DisplayName"], entry["Value"]
        leaderboard_text = f"{player_name}: {score}"

        # Render the leaderboard text on the right side of the screen
        text_surface = font.render(leaderboard_text, True, WHITE)
        text_rect = text_surface.get_rect(right=WIDTH - 20, top=y)
        screen.blit(text_surface, text_rect)

        y += 30  # Adjust the y-coordinate for the next entry

    next_button.draw(screen)
    previous_button.draw(screen)

    search_input.text = search_query
    search_input.draw(screen)

    search_button.draw(screen)


def update_leaderboard(
    event, search_input, next_button, search_button, previous_button
):
    search_input.handle_event(event)
    next_button.handle_event(event)
    previous_button.handle_event(event)
    search_button.handle_event(event)


def Getleader_http(request, callback, customData=None, extraHeaders=None):
    """
    Retrieves a list of ranked users for the given statistic, starting from the indicated point in the leaderboard
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getleaderboard
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    return DoPost(
        "/Client/GetLeaderboard",
        request,
        "X-Authorization",
        PlayFabSettings._internalSettings.ClientSessionTicket,
        wrappedCallback,
        customData,
        extraHeaders,
    )


def get_leaderboard(current_leader_page, display_message):
    start = (current_leader_page - 1) * 10
    end = start + 10
    request = {
        "StatisticName": "XP",  # Replace with your leaderboard name
        "StartPosition": start,
        "MaxResultsCount": end,  # Get the top 10 scores
    }
    leaderboard_data = None

    def callback(success, failure):
        if success:
            None  # leaderboard_data = success.data.Leaderboard
        # good = True
        # display_message("Account created and signed in.", (0, 255, 0))
        else:
            display_message("failed to fetch leaderboard")
            print("failed to fetch leaderboard")
            if failure:
                display_message("Here's some debug information:")
                display_message(str(failure) + "leader board")
                print("Here's some debug information:")
                print(str(failure) + "leader board")

    try:
        leaderboard_data = Getleader_http(request, callback)
        # print(leaderboard_data["Leaderboard"])
        if leaderboard_data["Leaderboard"] is not None:
            # Filter leaderboard data
            filtered_data = []
            for entry in leaderboard_data["Leaderboard"]:
                player_name = entry["DisplayName"]
                player_score = entry["StatValue"]
                player_position = entry["Position"]
                filtered_data.insert(
                    player_position, {"DisplayName": player_name, "Value": player_score}
                )
        return filtered_data
    except Exception as e:
        print(e)
    return []  # Return an empty list if no data is available
