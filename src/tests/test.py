from playfab import PlayFabClientAPI, PlayFabSettings

PlayFabSettings.TitleId = "4AAA9"

request = {"CustomId": input("enter username:\n"), "CreateAccount": True}


def callback(success, failure):
    if success:
        print("Congratulations, you made your first successful API call!")
    else:
        print("Something went wrong with your first API call.  :(")
        if failure:
            print("Here's some debug information:")
            print(failure.GenerateErrorReport())


PlayFabClientAPI.LoginWithCustomID(request, callback)
