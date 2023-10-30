import playfab
from SquarePixels.uimanagement.leaderboard import DoPost
from playfab import PlayFabSettings, PlayFabErrors


def GetAccountInfo(request, callback, customData = None, extraHeaders = None):
    """
    Retrieves the user's PlayFab account details
    https://docs.microsoft.com/rest/api/playfab/client/account-management/getaccountinfo
    """
    if not PlayFabSettings._internalSettings.ClientSessionTicket:
        raise PlayFabErrors.PlayFabException("Must be logged in to call this method")

    def wrappedCallback(playFabResult, error):
        if callback:
            callback(playFabResult, error)

    return DoPost("/Client/GetAccountInfo", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)


class PlayerProfileViewConstraints:
    def __init__(self, ShowAvatarUrl=False):
        self.ShowAvatarUrl = ShowAvatarUrl
        
def get_user_avatar(email):
    request = {"Email":email}
    def callback(success, failure):
            if success:
                print("Retrieved account details.")
            else:
                print("failed to retrieve account details.")
                if failure:
                    print("Here's some debug information:")
                    print(str(failure))
                    
    result = playfab.PlayFabClientAPI.GetAccountInfo(request, callback)
    print(result)
    request = {"ProfileConstraints":PlayerProfileViewConstraints(True),"PlayFabId":resultm}
    playfab.PlayFabClientAPI.GetPlayerProfile()