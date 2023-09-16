import pygame
import sys
import server

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

# Constants
infoObject: object = pygame.display.Info()
SCREEN_WIDTH, SCREEN_HEIGHT = infoObject.current_w, infoObject.current_h
BACKGROUND_COLOR = (0, 0, 0)
FPS = 60

# Define font
FONT_SIZE = 20
FONT = pygame.font.Font(None, FONT_SIZE)

# Define server configuration variables
current_server = None
max_players = "max players"
mplayall = []

# Create a list to store created servers
servers = []

# Create a list to store delete buttons
server_buttons = []

# File to save the servers
SERVERS_FILE = "servers.txt"
MPLAYERS_FILE = "mplayers.txt"


# Load servers from file
def load_servers():
    try:
        with open(SERVERS_FILE, "r") as file:
            for line in file:
                server = line.strip()
                servers.append(server)
    except FileNotFoundError:
        pass


# Load max_players values from file
def load_mplayers() -> None:
    try:
        with open(MPLAYERS_FILE, "r") as file:
            for line in file:
                mp = int(line.strip())
                mplayall.append(mp)
    except FileNotFoundError:
        pass


# Save servers to file
def save_servers():
    with open(SERVERS_FILE, "w") as file:
        for server in servers:
            file.write(server + "\n")
    with open(MPLAYERS_FILE, "w") as file:
        for mpla in mplayall:
            file.write(str(mpla) + "\n")


# Create a Pygame screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Server Manager")


# Function to draw the sidebar
def draw_sidebar():
    pygame.draw.rect(screen, GRAY, (0, 0, 200, SCREEN_HEIGHT))

    y = 50
    server_buttons.clear()  # Clear the server buttons list
    for i, server in enumerate(servers):
        text = FONT.render(server, True, BLACK)
        screen.blit(text, (10, y))

        # Draw the delete button for each server
        delete_button_rect = pygame.Rect(180, y - 15, 15, 15)
        pygame.draw.rect(screen, BLACK, delete_button_rect)
        server_buttons.append(delete_button_rect)  # Add the button rect to the list

        y += 30


# Function to draw the server configuration area
def draw_server_configuration():
    pygame.draw.rect(screen, WHITE, (220, 50, SCREEN_WIDTH - 240, SCREEN_HEIGHT - 100))

    if current_server:
        text = FONT.render("Server: " + current_server, True, BLACK)
        screen.blit(text, (230, 60))

        text = FONT.render("Max Players: " + str(max_players), True, BLACK)
        screen.blit(text, (230, 90))

        pygame.draw.rect(screen, BLACK, (230, 130, 120, 30))
        text = FONT.render("Save Server", True, WHITE)
        screen.blit(text, (250, 135))

        pygame.draw.rect(screen, BLACK, (230, 160, 120, 30))
        text = FONT.render("Run Server", True, WHITE)
        screen.blit(text, (250, 165))


# Function to start the server
def start_server():
    if current_server:
        print("Starting server:", current_server)
        server.main(5, current_server)


# Function to delete a server
def delete_server(index):
    if index >= 0 and index < len(servers):
        del servers[index]
        del mplayall[index]
        save_servers()


# Main game loop
def game_loop():
    # Create the input box
    global max_players, current_server
    name = False
    numbers = False
    input_box = pygame.Rect(SCREEN_WIDTH - 230, SCREEN_HEIGHT - 40, 150, 20)
    number_box = pygame.Rect(SCREEN_WIDTH - 340, SCREEN_HEIGHT - 40, 100, 20)
    input_text = "server Name"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    # Scroll down event
                    pass
                elif event.key == pygame.K_BACKSPACE:
                    # Handle backspace in the input box
                    input_text = input_text[:-1]
                    max_players = max_players[:-1]
                else:
                    if event.unicode.isdigit():
                        max_players += event.unicode
                    else:
                        # Add typed characters to the input box
                        input_text += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if mouse_pos[0] < 200:
                        # Clicked on sidebar
                        selected_index = (mouse_pos[1] - 50) // 30
                        if selected_index >= 0 and selected_index < len(servers):
                            current_server = servers[selected_index]
                            max_players = mplayall[selected_index]
                    elif (
                        mouse_pos[0] >= 230
                        and mouse_pos[1] >= 130
                        and mouse_pos[1] <= 160
                    ):
                        # Clicked on Save Server button
                        if current_server and max_players > 0:
                            servers.append(current_server)
                            current_server = None
                            mplayall.append(max_players)
                            save_servers()
                    elif input_box.collidepoint(mouse_pos):
                        # Clicked inside the input box
                        name = True
                        pass
                    else:
                        name = False

                    if number_box.collidepoint(mouse_pos):
                        # Clicked inside the input box
                        numbers = True
                        pass
                    else:
                        numbers = False

                    if pygame.Rect((230, 160), (120, 30)).collidepoint(mouse_pos):
                        start_server()

                    # Check if any delete button was clicked
                    for i, button_rect in enumerate(server_buttons):
                        if button_rect.collidepoint(mouse_pos):
                            delete_server(i)
                            break

                    if (
                        mouse_pos[0] >= SCREEN_WIDTH - 40
                        and mouse_pos[1] >= SCREEN_HEIGHT - 40
                    ):
                        # Clicked on the create server button
                        if input_text and max_players:
                            try:
                                max_players = int(max_players)
                            except ValueError:
                                print("not a valid number for max players")
                                break
                            servers.append(input_text)
                            mplayall.append(max_players)
                            input_text = ""
                            save_servers()

        screen.fill(WHITE)

        draw_sidebar()
        draw_server_configuration()

        # Draw the input box
        pygame.draw.rect(screen, BLACK, input_box, 2)
        text_surface = FONT.render(input_text, True, BLACK)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

        # draw the number box
        pygame.draw.rect(screen, BLACK, number_box, 2)
        text_surface = FONT.render(str(max_players), True, BLACK)
        screen.blit(text_surface, (number_box.x + 5, number_box.y + 5))

        # Draw the create server button
        pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40, 30, 30))
        text = FONT.render("+", True, WHITE)
        screen.blit(text, (SCREEN_WIDTH - 35, SCREEN_HEIGHT - 35))

        pygame.display.flip()


# Load servers from file
load_servers()
load_mplayers()

# Start the game loop
game_loop()
