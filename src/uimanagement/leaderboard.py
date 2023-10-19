import playfab
import pygame


font = pygame.font.Font(None, 36)


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
    current_page,
    search_query,
    ENTRIES_PER_PAGE,
    next_button,
    previous_button,
    search_input,
    search_button,
    screen,
    WIDTH,
    WHITE,
):
    # Filter leaderboard data based on the search query
    filtered_data = []
    for entry in leaderboard_data:
        player_name = entry["DisplayName"]
        if search_query.lower() in player_name.lower():
            filtered_data.append(entry)

    # Calculate the start and end indices for the current page
    start_index = (current_page - 1) * ENTRIES_PER_PAGE
    end_index = start_index + ENTRIES_PER_PAGE

    # Display leaderboard entries for the current page
    y = 50  # Initial y-coordinate for rendering leaderboard entries

    for entry in filtered_data[start_index:end_index]:
        player_name, score = entry["DisplayName"], entry["Value"]
        leaderboard_text = f"{player_name}: {score}"

        # Render the leaderboard text on the right side of the screen
        text_surface = font.render(leaderboard_text, True, WHITE)
        text_rect = text_surface.get_rect(right=WIDTH - 20, top=y)
        screen.blit(text_surface, text_rect)

        y += 30  # Adjust the y-coordinate for the next entry

    next_button.draw()
    previous_button.draw()

    search_input.text = search_query
    search_input.draw()

    search_button.draw()


def update_leaderboard(
    event, search_input, next_button, search_button, previous_button
):
    search_input.handle_event(event)
    next_button.handle_event(event)
    previous_button.handle_event(event)
    search_button.handle_event(event)


def get_leaderboard(current_leader_page, display_message):
    start = (current_leader_page - 1) * 10
    end = start + 10
    request = {
        "StatisticName": "XP",  # Replace with your leaderboard name
        "StartPosition": start,
        "MaxResultsCount": end,  # Get the top 10 scores
    }

    def callback(success, failure):
        global good
        if success:
            None
        # good = True
        # display_message("Account created and signed in.", (0, 255, 0))
        else:
            None  # display_message("Account creation failed.")
            if failure:
                display_message("Here's some debug information:")
                display_message(str(failure) + "leader board")

    try:
        result = playfab.PlayFabClientAPI.GetLeaderboard(request, callback)
        if result is not None:
            leaderboard_data = result.data.Leaderboard
            return leaderboard_data
    except Exception as e:
        print(e)
    return []  # Return an empty list if no data is available
