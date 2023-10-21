import pygame as pig
from playfab import PlayFabSettings, PlayFabErrors
import json
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


def GetPlayerStatistics(request, callback, customData=None, extraHeaders=None):
    """
    Retrieves the indicated statistics (current version and values for all statistics, if none are specified), for the local
    player.
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getplayerstatistics
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    return DoPost(
        "/Client/GetPlayerStatistics",
        request,
        "X-Authorization",
        PlayFabSettings._internalSettings.ClientSessionTicket,
        wrappedCallback,
        customData,
        extraHeaders,
    )


def UpdatePlayerStatistics(request, callback, customData=None, extraHeaders=None):
    """
    Updates the values of the specified title-specific statistics for the user. By default, clients are not permitted to
    update statistics. Developers may override this setting in the Game Manager > Settings > API Features.
    https://docs.microsoft.com/rest/api/playfab/client/player-data-management/updateplayerstatistics
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    return DoPost(
        "/Client/UpdatePlayerStatistics",
        request,
        "X-Authorization",
        PlayFabSettings._internalSettings.ClientSessionTicket,
        wrappedCallback,
        customData,
        extraHeaders,
    )


def draw_death_screen(screen, width, height, xp):
    clock: object = pig.time.Clock()
    death_text = pig.font.Font(
        "terraria_styled_game\Fonts\PixelifySans-Regular.ttf", 50
    )
    d_text = death_text.render("You Died", True, (255, 255, 255))
    xp_text = death_text.render(f"Your Score: {xp}", True, (255, 255, 255))
    death_text_rect = d_text.get_rect(center=(width // 2, height // 3))
    xp_text_rect = xp_text.get_rect(center=(width // 2, height // 3 + 50))
    # Define buttons
    respawn_button = pig.Rect(width // 4, height // 2, 200, 50)
    menu_button = pig.Rect(3 * width // 4, height // 2, 200, 50)
    # Function to display a message on the screen

    def display_message(message, color=(255, 0, 0)):
        global current_message
        current_message = message
        text_surface = death_text.render(message, True, color)
        text_rect = text_surface.get_rect(center=(width // 2, height // 3))
        screen.blit(text_surface, text_rect)

    def callback(success, failure):
        if success:
            None  # leaderboard_data = success.data.Leaderboard
        # good = True
        # display_message("Account created and signed in.", (0, 255, 0))
        else:
            print("failed to fetch leaderboard position")
            display_message("failed to fetch leaderboard position")
            if failure:
                display_message("Here's some debug information:")
                display_message(str(failure) + "leader board position")
                print("Here's some debug information:")
                print(str(failure) + "leader board")

    request = {"StatisticNames": "XP"}
    cxp = GetPlayerStatistics(
        request, callback
    )  # example output {"Statistics": [{"StatisticName": "XP", "Value": 900, "Version": 0}]}
    if cxp:
        cxp = cxp["Statistics"][0]["Value"]
        print(cxp)
        if cxp:
            if cxp < xp:
                request = {"Statistics": [{"StatisticName": "XP", "Value": xp}]}
                UpdatePlayerStatistics(request, callback)
        else:
            request = {"StatisticName": "XP", "Value": xp}
            UpdatePlayerStatistics(request, callback)
    else:
        request = {"StatisticName": "XP", "Value": xp}
        UpdatePlayerStatistics(request, callback)

    while True:
        for event in pig.event.get():
            if event.type == pig.QUIT:
                pig.quit()
                quit()
        screen.fill((0, 0, 0))
        screen.blit(d_text, death_text_rect)
        screen.blit(xp_text, xp_text_rect)
        # Check if the mouse is hovering over the buttons
        if respawn_button.collidepoint(pig.mouse.get_pos()):
            pig.draw.rect(screen, (150, 150, 150), respawn_button)
            respawn_text = death_text.render("Respawn", True, (0, 0, 0))
            respawn_text_rect = respawn_text.get_rect(center=respawn_button.center)
            screen.blit(respawn_text, respawn_text_rect)
            if pig.mouse.get_pressed()[0]:
                return True
        else:
            pig.draw.rect(screen, (255, 255, 255), respawn_button)
            respawn_text = death_text.render("Respawn", True, (0, 0, 0))
            respawn_text_rect = respawn_text.get_rect(center=respawn_button.center)
            screen.blit(respawn_text, respawn_text_rect)

        if menu_button.collidepoint(pig.mouse.get_pos()):
            pig.draw.rect(screen, (150, 150, 150), menu_button)
            menu_text = death_text.render("Main Menu", True, (0, 0, 0))
            menu_text_rect = menu_text.get_rect(center=menu_button.center)
            screen.blit(menu_text, menu_text_rect)
            if pig.mouse.get_pressed()[0]:
                return False
        else:
            pig.draw.rect(screen, (255, 255, 255), menu_button)
            menu_text = death_text.render("Main Menu", True, (0, 0, 0))
            menu_text_rect = menu_text.get_rect(center=menu_button.center)
            screen.blit(menu_text, menu_text_rect)
        pig.display.flip()
        clock.tick(60)
