import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
FONT = pygame.font.Font(None, 36)

# Sample list of games
games = [
    {
        "name": "Square Pixel",
        "description": "This is the description of Game 1",
        "url": "https://github.com/Unlim8ted-Studio-Productions/Square-Pixels/releases/download/V1/SquarePixelInstaller.exe",
    },
    {"name": "Game 2", "description": "This is the description of Game 2"},
    {"name": "Game 3", "description": "This is the description of Game 3"},
    {"name": "Game 4", "description": "This is the description of Game 4"},
]

# Initialize the Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Installer")

# Search bar input field
search_bar_rect = pygame.Rect(WIDTH // 2 - 200, 50, 400, 50)
search_text = ""
search_font = pygame.font.Font(None, 32)
search_active = False

# Sign-in state
signed_in = False


# Function to draw the sidebar
def draw_sidebar(selected_tab):
    pygame.draw.rect(screen, (150, 150, 150), (0, 0, 200, HEIGHT))
    for i, tab in enumerate(["Games", "Store"]):
        tab_text = FONT.render(tab, True, (0, 0, 0))
        tab_rect = tab_text.get_rect(topleft=(10, 10 + i * 50))
        if i == selected_tab:
            pygame.draw.rect(
                screen, (200, 200, 200), (5, tab_rect.y - 5, 190, tab_rect.height + 10)
            )
        screen.blit(tab_text, tab_rect)


# Function to draw the game selection menu
def draw_game_menu(selected_game):
    screen.fill(WHITE)
    for i, game in enumerate(games):
        if search_text.lower() in game["name"].lower():
            text = FONT.render(game["name"], True, (0, 0, 0))
            text_rect = text.get_rect(center=(WIDTH // 2, 100 + i * 50))
            if i == selected_game:
                pygame.draw.rect(
                    screen,
                    (200, 200, 200),
                    (
                        text_rect.x - 10,
                        text_rect.y - 10,
                        text_rect.width + 20,
                        text_rect.height + 20,
                    ),
                )
            screen.blit(text, text_rect)


# Function to display game details and install button
def draw_game_details(selected_game):
    screen.fill(WHITE)
    game = games[selected_game]
    text = FONT.render(game["name"], True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, 100))
    description_text = FONT.render(game["description"], True, (0, 0, 0))
    description_rect = description_text.get_rect(center=(WIDTH // 2, 200))
    screen.blit(text, text_rect)
    screen.blit(description_text, description_rect)

    install_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 100, 200, 50)
    if signed_in:
        pygame.draw.rect(screen, (0, 0, 0), install_button)
        install_text = FONT.render("Install", True, WHITE)
        install_text_rect = install_text.get_rect(center=install_button.center)
        screen.blit(install_text, install_text_rect)


selected_tab = 0  # 0 for "Games," 1 for "Store"
selected_game = None

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not signed_in:
                # Simulate sign-in with the 's' key
                if event.key == pygame.K_s:
                    signed_in = True
            else:
                if selected_tab == 0:
                    if event.key == pygame.K_UP:
                        selected_game = (
                            max(0, selected_game - 1)
                            if selected_game is not None
                            else 0
                        )
                    elif event.key == pygame.K_DOWN:
                        selected_game = (
                            min(len(games) - 1, selected_game + 1)
                            if selected_game is not None
                            else 0
                        )
                    elif event.key == pygame.K_RETURN:
                        selected_tab = 1
                elif selected_tab == 1:
                    if event.key == pygame.K_BACKSPACE:
                        search_text = search_text[:-1]
                    elif event.key == pygame.K_RETURN:
                        if selected_game is not None:
                            # Install game here (You can replace this with your actual logic)
                            print(f"Installing {games[selected_game]['name']}...")
                    else:
                        search_text += event.unicode

        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected_tab == 0:
                if event.pos[0] < 200:
                    selected_tab = 0
                    selected_game = event.pos[1] // 50
                else:
                    selected_tab = 1

    if selected_tab == 0:
        draw_game_menu(selected_game)
    elif selected_tab == 1:
        if selected_game is not None:
            draw_game_details(selected_game)

    draw_sidebar(selected_tab)

    # Draw the search bar
    pygame.draw.rect(
        screen,
        (200, 200, 200) if search_active else (255, 255, 255),
        search_bar_rect,
        3,
    )
    text_surface = search_font.render(search_text, True, (0, 0, 0))
    screen.blit(text_surface, (search_bar_rect.x + 10, search_bar_rect.y + 10))

    pygame.display.flip()

pygame.quit()
sys.exit()
