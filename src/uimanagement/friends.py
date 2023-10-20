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


font = pygame.font.Font("terraria_styled_game\Fonts\PixelifySans-Regular.ttf", 36)


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


# Function to display a message on the screen
def display_message(message, color=(255, 0, 0)):
    global current_message
    current_message = message
    text_surface = font.render(message, True, color)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text_surface, text_rect)


def callback(success, failure):
    if success:
        print("success")  # leaderboard_data = success.data.Leaderboard
        display_message("success")
    # good = True
    # display_message("Account created and signed in.", (0, 255, 0))
    else:
        display_message("failed")
        print("failed")
        if failure:
            display_message("Here's some debug information:")
            display_message(str(failure) + "leader board")
            print("Here's some debug information:")
            print(str(failure) + "leader board")


def GetFriendsList_http(request, callback, customData=None, extraHeaders=None):
    """
    Retrieves the current friend list for the local user, constrained to users who have PlayFab accounts. Friends from
    linked accounts (Facebook, Steam) are also included. You may optionally exclude some linked services' friends.
    https://docs.microsoft.com/rest/api/playfab/client/friend-list-management/getfriendslist
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    return DoPost(
        "/Client/GetFriendsList",
        request,
        "X-Authorization",
        PlayFabSettings._internalSettings.ClientSessionTicket,
        wrappedCallback,
        customData,
        extraHeaders,
    )


def get_friends():
    request = {}
    result = GetFriendsList_http(request, callback)
    if result != None:
        print(result)
        return result
    else:
        return []


def display_friends(screen, friends):
    y = 100
    for friend in friends:
        friend_text = font.render(friend.username, True, (255, 255, 255))
        screen.blit(friend_text, (50, y))
        y += 50
