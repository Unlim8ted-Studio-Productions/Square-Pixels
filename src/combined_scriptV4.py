import pygame as pig
import typing as tp
import SquarePixels.player.player as player
import SquarePixels.render.Lighting as Lit
import random
import math


black_rectangles = []
infoObject: object = pig.display.Info()
# Fill the screen with black rectangles
for x in range(infoObject.current_w // 20 + 50):
    for y in range(infoObject.current_h // 20 + 50):
        black_rect = pig.Rect((x * 20, y * 20, 20, 20))
        black_rectangles.append(black_rect)


def render_terrain(
    screen: pig.Surface,
    width: float | int,
    height: float | int,
    terrain: list,
    pos_x: float | int,
    pos_y: float | int,
    camera_x: float | int,
    camera_y: float | int,
    playerpos,
    DayTime,
    morning,
) -> list:
    """
    Render the game terrain.

    Args:
        screen (pig.Surface): The game screen surface.
        width (float | int): The width of the terrain.
        height (float | int): The height of the terrain.
        terrain (list): The terrain data.
        pos_x (float | int): X-coordinate position of the player.
        pos_y (float | int): Y-coordinate position of the player.
        camera_x (float | int): X-coordinate of the camera.
        camera_y (float | int): Y-coordinate of the camera.
        playerpos: Player position.
        DayTime: The current time of day.
        morning: Indicates whether it's morning or not.

    Returns:
        list: A list containing sky and colliders.
    """
    tile_size = 15
    block_images = [
        r"Recources\Textures\grass.jpg",
        r"Recources\Textures\stone.jpg",
        r"Recources\Textures\wood.png",
    ]
    colors = [
        (100, 100, 100),  # Stone
        (139, 69, 19),  # Dirt
        (139, 115, 85),  # Wood
        (34, 139, 34),  # Leaves
        (0, 128, 0),  # Coal
        (211, 211, 211),  # Iron
        (255, 223, 0),  # Gold
        (128, 128, 128),  # Diamond
        (0, 0, 0, 0),  # Sky (Blue)
        (255, 255, 255),  # Clouds (White)
    ]  # Color palette for blocks
    NewColors = (
        []
    )  # stores colors with lighting applied, blank and a placeholder at this point in the script
    colliders = []
    sky = []
    place_blocks = [
        13,
    ]
    if morning == 0:
        pig.draw.rect(
            screen, (255, 255, 51), ((DayTime * 250) + 300, (DayTime * 200), 100, 100)
        )
    for x in range(width[0], width[1]):
        for y in range(height):
            block_type = terrain[y][x]
            currentblock = pig.Rect(
                (
                    (x + pos_x - camera_x) * tile_size,
                    (y + pos_y - camera_y) * tile_size,
                ),
                (tile_size, tile_size),
            )
            if not block_type in place_blocks:
                color = colors[block_type]
                if color == (255, 255, 255):
                    if random.randint(0, 1) == 1:
                        color = (255, 255, 255)
                    else:
                        color = (211, 211, 211)
                NewColors = Lit.LightAlgorithm(
                    colors, x, y, (playerpos.x), (playerpos.y), DayTime
                )
                if not color == (211, 211, 211):
                    color = NewColors[block_type]
                else:
                    PlayerPos = [(DayTime * 25), (DayTime * 25)]
                    blockPos = [x, y]
                    Darken = round(math.dist(blockPos, PlayerPos))
                    Darken = Darken * DayTime
                    color = (211 - Darken, 211 - Darken, 211 - Darken)
                try:
                    pig.draw.rect(
                        screen,
                        color,
                        (currentblock),
                    )
                except:
                    pig.draw.rect(
                        screen,
                        (0, 0, 0),
                        (currentblock),
                    )

                ## Load and blit the corresponding block image
                # if block_type < len(block_images):
                #    block_image = block_images[block_type]
                #    screen.blit(pig.image.load(block_image), currentblock)
                color = colors[block_type]
                if color == (0, 0, 0, 0):
                    sky.append(currentblock)
                if (
                    color != (135, 206, 235)
                    and color != (139, 115, 85)
                    and color != (255, 255, 255)
                    and color != (211, 211, 211)
                    and color != (0, 0, 0, 0)
                ):
                    colliders.append(currentblock)
            else:
                if block_type == 10:
                    screen.blit(block_images[2], currentblock)
                if block_type == 11:
                    screen.blit(block_images[1], currentblock)
                colliders.append(currentblock)

    for rect in black_rectangles:
        # Calculate the center point of the black rectangle
        rect_center = rect.center

        # Calculate the distance from the player to the center of the black rectangle
        distance = math.sqrt(
            (rect_center[0] - playerpos.x) ** 2 + (rect_center[1] - playerpos.y) ** 2
        )
        # Calculate the transparency based on the distance to the center
        transparency = int(distance)
        # Closer is less transparent
        if transparency >= 255:
            transparency = 255
        if transparency <= 0:
            transparency = abs(transparency)
        if transparency >= 255:
            transparency = 255
        # Define a radius for the sphere

        # Create a transparent black color
        transparent_black = (0, 0, 0, transparency)
        # Create a surface with the transparent black color and same dimensions as the rectangle
        transparent_surface = pig.Surface(rect.size, pig.SRCALPHA)
        pig.draw.rect(transparent_surface, transparent_black, (0, 0, *rect.size))
        # Blit the transparent surface onto the main screen
        screen.blit(transparent_surface, rect.topleft)
        # Remove the black rectangle if it's fully transparent
        if transparency == 0 or distance <= 60:
            black_rectangles.remove(rect)
    return sky, colliders


def render_player(
    screen: pig.Surface,
    x: float | int,
    y: float | int,
    size: int,
    color: tuple,
    character,
):
    """
    Render the player character on the screen.

    Args:
        screen (pig.Surface): The game screen surface.
        x (float | int): X-coordinate of the player character.
        y (float | int): Y-coordinate of the player character.
        size (int): Size of the player character.
        color (tuple): Color of the player character.
        character: Character data.

    Returns:
        None
    """
    pig.draw.circle(screen, (0, 0, 0, 0), (x, y), size, size)


def render_other_players(screen: pig.Surface, players: list):
    """
    Render other player characters on the screen.

    Args:
        screen (pig.Surface): The game screen surface.
        players (list): List of other player data.

    Returns:
        None
    """
    for player in players:
        pig.draw.circle(
            screen, player.color, (player.x, player.y), player.size, player.size
        )


def sort_leaderboard(allpoints: tp.Dict[str, int]) -> tp.List[tp.Tuple[str, int]]:
    """
    Sort the leaderboard based on player points.

    Args:
        allpoints (tp.Dict[str, int]): Dictionary of player names and their points.

    Returns:
        tp.List[tp.Tuple[str, int]]: Sorted list of player names and points as tuples.
    """
    sorted_points = sorted(allpoints.items(), key=lambda x: x[1], reverse=True)
    return sorted_points


def render_chat(
    chat_messages: tp.List[str], screen_height: int, screen: pig.Surface
) -> None:
    """
    Render chat messages on the screen.

    Args:
        chat_messages (tp.List[str]): List of chat messages.
        screen_height (int): Height of the game screen.
        screen (pig.Surface): The game screen surface.

    Returns:
        None
    """
    # Render the chat messages
    font = pig.font.Font(None, 20)
    for i, message in enumerate(chat_messages):
        text = font.render(message, True, (255, 255, 255))
        if 10 + i * 20 >= screen_height - 30:
            save = chat_messages[i]
            i = 0
            chat_messages.clear()
            chat_messages.append(save)
            text_rect = text.get_rect(left=10, top=10 + i * 20)
            screen.blit(text, text_rect)
        else:
            text_rect = text.get_rect(left=10, top=10 + i * 20)
            screen.blit(text, text_rect)


def render_scores(allpoints: tp.Dict[str, int], screen: pig.Surface) -> None:
    """
    Render the leaderboard on the screen.

    Args:
        allpoints (tp.Dict[str, int]): Dictionary of player names and their points.
        screen (pig.Surface): The game screen surface.

    Returns:
        None
    """
    # sort scores
    sorted_points = sort_leaderboard(allpoints)
    # Render the leaderboard
    font = pig.font.Font(None, 20)
    for i, entry in enumerate(sorted_points):
        name, score = entry
        text = font.render(f"{name}: {score}", True, (255, 255, 255))
        # playeronlead[name] = pig.Rect((700, 10 + i * 20, 20, 10))
        text_rect = text.get_rect(left=700, top=10 + i * 20)
        screen.blit(text, text_rect)


def score_hitboxes(allpoints: tp.Dict[str, int]) -> dict:
    """
    Generate hitboxes for leaderboard entries.

    Args:
        allpoints (tp.Dict[str, int]): Dictionary of player names and their points.

    Returns:
        dict: Dictionary of hitboxes for leaderboard entries.
    """
    # sort scores
    sorted_points = sort_leaderboard(allpoints)
    playeronlead = {}
    for i, entry in enumerate(sorted_points):
        name, score = entry
        playeronlead[name] = pig.Rect((700, 10 + i * 20, 30, 10))
    return playeronlead


def kick_players(
    hitboxes: dict, players: list, screen, points: dict, kicked: list
) -> tuple:
    """
    Kick players from the game based on hitboxes.

    Args:
        hitboxes (dict): Dictionary of hitboxes for player entries in the leaderboard.
        players (list): List of player data.
        screen: The game screen.
        points (dict): Dictionary of player names and their points.
        kicked (list): List of kicked players.

    Returns:
        tuple: Updated players, points, and kicked lists.
    """
    for hitbox in hitboxes:
        if hitboxes[hitbox].collidepoint(pig.mouse.get_pos()):
            pig.draw.rect(screen, (255, 0, 0), rect=hitboxes[hitbox])
            if pig.mouse.get_pressed()[0]:
                # Get the name of the player associated with the hitbox
                player_name = hitbox
                print(players)
                if player_name is not None:
                    # Remove the player from the players dictionary
                    for player in players:
                        if player.name == player_name:
                            players.remove(player)
                            break
                    for player in points:
                        if player == player_name:
                            points.pop(player)
                            kicked.append(player)
                            break

    # Kick the socket associated with the player

    # print("Player", player_name, "kicked.")
    # print(players, points, kicked)
    return players, points, kicked


# Define nametag class
class Nametag:
    def __init__(self, player: player.Player):
        """
        Initialize a Nametag instance.

        Args:
            player (player.Player): The player associated with the nametag.
        """
        self.player: player.Player = player

    def draw(self, screen: pig.Surface) -> None:
        """
        Draw the nametag on the screen.

        Args:
            screen (pig.Surface): The game screen surface.

        Returns:
            None
        """
        font = pig.font.Font(None, 20)
        text = font.render(self.player.name, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.player.x, self.player.y - 15))
        screen.blit(text, text_rect)

import pygame
from PIL import Image, ImageDraw, ImageOps


class ImageElement:
    def __init__(self, x, y, image, crop_mode="None"):
        self.x = x
        self.y = y
        self.image = image
        self.crop_mode = crop_mode  # "None" or "Circle"
        self.active = False
        self.width, self.height = self.image.size
        self.widtho, self.heighto = self.image.size
        self.text = ""
        self.bold = False
        self.italics = False
        self.underlined = False
        self.font_name = "Recources\Fonts\PixelifySans-Regular.ttf"
        self.color = (0, 0, 0)
        self.size = self.width * self.height

    def draw(self, screen):
        # Optionally apply cropping based on the selected cropping mode
        if self.crop_mode == "Circle":
            # Crop the image to a circle using PIL
            mask = Image.new("L", (self.widtho, self.heighto), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, self.widtho, self.heighto), fill=255)
            self.image.putalpha(mask)

        # Draw the image on the screen
        pygame_image = pygame.image.fromstring(
            self.image.tobytes(), self.image.size, self.image.mode
        )
        pygame_image = pygame.transform.scale(pygame_image, (self.width, self.height))
        screen.blit(pygame_image, (self.x, self.y))
# UI panel for editing properties
import pygame

# UI panel background color
UI_PANEL_COLOR = (200, 200, 200)


class UIPanel:
    def __init__(self, x, y, width, height):
        """
        Initialize a UI panel object
        Args:
            x: X coordinate of panel
            y: Y coordinate of panel
            width: Width of panel
            height: Height of panel
        Returns:
            None: Does not return anything
        - Sets x, y, width and height attributes of panel from arguments
        - Sets default background color
        - Initializes empty elements list to add UI elements later"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = UI_PANEL_COLOR
        self.elements = []

    def draw(self, screen):
        """Draws a rectangle on the screen.
        Args:
            screen: The screen surface to draw on.
        Returns:
            None: Does not return anything.
        - Draws a filled rectangle on the screen surface using the object's position, size and background color attributes.
        - Loops through the object's elements list and draws each element."""
        pygame.draw.rect(
            screen, self.bg_color, (self.x, self.y, self.width, self.height)
        )

        for element in self.elements:
            element.draw(screen)
import pygame


if __name__ == "__main__":
    # Constants
    infoObject: object = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    BACKGROUND_COLOR = (0, 0, 0)
font = pygame.font.Font("Recources\Fonts\PixelifySans-Regular.ttf", 36)
# Define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)
white = (255, 255, 255)


class Button:
    """Button class for creating interactive buttons in the game."""

    def __init__(
        self,
        text,
        x,
        y,
        width,
        height,
        command,
        additional_data: list = None,
        color=(255, 255, 255),
    ):
        """
        Initialize a button.

        Args:
            text (str): The text displayed on the button.
            x (int): The x-coordinate of the button's top-left corner.
            y (int): The y-coordinate of the button's top-left corner.
            width (int): The width of the button.
            height (int): The height of the button.
            command (function): The function to be executed when the button is clicked.
            aditional data (list): arguments the buttons command needs to run
        """
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.command = command
        self.additional_data = additional_data
        self.hovered = False
        self.size = 36
        self.active = False
        self.bold = False
        self.italics = False
        self.underlined = False
        self.font_name = "Recources\Fonts\PixelifySans-Regular.ttf"
        self.color = color

    def draw(self, screen):
        """Draw the button on the screen."""
        font = pygame.font.Font(self.font_name, self.size)
        font.set_bold(self.bold)
        font.set_italic(self.italics)
        font.set_underline(self.underlined)
        color = BUTTON_HOVER_COLOR if self.hovered else BUTTON_COLOR
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        text = font.render(self.text, True, self.color)
        screen.blit(
            text,
            (
                self.x + self.width // 2 - text.get_width() // 2,
                self.y + self.height // 2 - text.get_height() // 2,
            ),
        )

    def handle_event(self, event):
        """
        Handle events related to the button.

        Args:
            event: The Pygame event to be processed.
        """
        if event.type == pygame.MOUSEMOTION:
            self.hovered = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.active = True
                if self.additional_data != None:
                    self.command(*self.additional_data)
                else:
                    self.command()
            else:
                self.active = False

    def selected(self):
        self.hovered = True

    def change_text(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
import pygame
from pygame import RESIZABLE
import socket
import threading
import ipaddress
import SquarePixels.multiplayer.client as client

SERVER_PORT = 12345
TIMEOUT = 1.0  # Timeout value for socket operations
SCAN_TIMEOUT = 2.0  # Timeout value for server scanning
SCAN_THREADS = 50  # Number of threads for concurrent scanning
pygame.init()
infoObject: object = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
ip = ""
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("Server Finder")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

running = True
servers = []
selected_server = None
input_text = "Name"
settings = True


def check_server(server_ip):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((server_ip, SERVER_PORT))
            if result == 0 and server_ip not in servers:
                servers.append(server_ip)
    except:
        pass


def scan_servers(ip_range):
    network = ipaddress.ip_network(ip_range)
    for ip_address in network.hosts():
        server_ip = str(ip_address)
        threading.Thread(target=check_server, args=(server_ip,)).start()


def find_servers():
    global running
    if running:
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        network = ipaddress.ip_network(ip_address, strict=False)
        ip_range = f"{network.network_address}/{network.prefixlen}"

        print("Automatically selected IP range:", ip_range)
        print("Scanning for servers...")
        scan_servers(ip_range)

        threading.Timer(SCAN_TIMEOUT, find_servers).start()


def draw_text(text, x, y):
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


def handle_server_click(selected_server):
    if selected_server is not None:
        # Perform actions based on the selected server
        print("Clicked on server:", selected_server)
        ip = selected_server
        # client.main(selected_server)
        handle_server_options(ip)


def handle_server_options(ip) -> None:
    global player_name, character_image, input_text, settings

    input_rect = pygame.Rect(10, 400, 200, 30)
    character_rect = pygame.Rect(220, 400, 100, 100)
    input_active = True

    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if input_rect.collidepoint(event.pos):
                        input_active = True
                    else:
                        input_active = False
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        # Save the player name and character image
                        settings = False
                        client.main(ip, input_text)
                        player_name = input_text
                        # character_image = ...  # Save the selected character image
                        print("Player Name:", player_name)
                        print("Character Image:", character_image)
                        pygame.quit()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, (200, 200, 200), input_rect, 2)

        if input_active:
            pygame.draw.rect(screen, (200, 200, 200), input_rect, 0)

        input_surface = font.render(input_text, True, TEXT_COLOR)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.draw.rect(screen, (200, 200, 200), character_rect, 2)
        # Draw the selected character image in the character_rect

        pygame.display.flip()
        clock.tick(60)


def main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()

        screen.fill(BACKGROUND_COLOR)
        draw_text("Found Servers:", 10, 10)

        for i, server in enumerate(servers):
            text = f"Server {i+1}: {server}"
            text_surface = font.render(text, True, TEXT_COLOR)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (10, 40 + i * 30)
            if text_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (200, 200, 200), text_rect)
                if pygame.mouse.get_pressed()[0]:
                    selected_server = server
                    running = False
                    handle_server_click(selected_server)
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    find_servers()
    main()
# Color picker input field for customizing color
import math
import pygame


class ColorPickerInputField:
    def __init__(self, x, y, width, height, label, default_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.color = default_color
        self.active = False
        self.color_dialog_radius = 50  # Radius of the circular color picker
        self.brightness_control_x = self.x + 130
        self.brightness_control_y = self.y
        self.brightness_control_width = 15
        self.brightness_control_height = 120
        self.brightness = 50  # Default brightness
        self.brightness_control_dragging = False

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(self.label, True, (0, 0, 0))
        screen.blit(text, (self.x, self.y - 40))

        # Draw circular color picker dialog
        pygame.draw.circle(
            screen,
            (
                255 - self.brightness * 2,
                255 - self.brightness * 2,
                255 - self.brightness * 2,
            ),
            (self.x + 60, self.y + 60),
            self.color_dialog_radius + 10,
        )

        for angle in range(360):
            radians = math.radians(angle)
            color = pygame.Color(255, 0, 0)  # Initialize with red
            color.hsla = (angle, 100, self.brightness, 100)
            x = int(self.x + 60 + self.color_dialog_radius * math.cos(radians))
            y = int(self.y + 60 + self.color_dialog_radius * math.sin(radians))
            pygame.draw.circle(screen, color, (x, y), 5)

        # Draw selected color
        pygame.draw.circle(screen, self.color, (self.x + 60, self.y + 60), 30)

        # Draw gray background for brightness control
        pygame.draw.rect(
            screen,
            (200, 0, 200),
            (
                self.brightness_control_x,
                self.brightness_control_y,
                self.brightness_control_width,
                self.brightness_control_height,
            ),
        )

        # Draw the brightness control
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                self.brightness_control_x,
                self.brightness_control_y
                + int(
                    (self.brightness_control_height - 15) * (1 - self.brightness / 100)
                ),
                self.brightness_control_width,
                15,
            ),
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_color_picker_clicked(event.pos):
                self.active = True
            if (
                self.brightness_control_x
                <= event.pos[0]
                <= self.brightness_control_x + self.brightness_control_width
                and self.brightness_control_y
                <= event.pos[1]
                <= self.brightness_control_y + self.brightness_control_height
            ):
                self.brightness_control_dragging = True
        if event.type == pygame.MOUSEMOTION:
            if self.active:
                if self.is_color_picker_clicked(event.pos):
                    self.color = self.get_color_at(event.pos)
            if self.brightness_control_dragging:
                # Move the brightness control up and down
                new_y = event.pos[1] - 7.5
                new_y = max(self.brightness_control_y, new_y)
                new_y = min(
                    self.brightness_control_y + self.brightness_control_height - 15,
                    new_y,
                )
                self.brightness = (
                    100
                    - (
                        (new_y - self.brightness_control_y)
                        / (self.brightness_control_height - 15)
                    )
                    * 100
                )
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.active = False
            self.brightness_control_dragging = False

    def is_color_picker_clicked(self, pos):
        return (
            math.hypot(pos[0] - (self.x + 60), pos[1] - (self.y + 60))
            <= self.color_dialog_radius
        )

    def get_color_at(self, pos):
        angle = math.degrees(math.atan2(pos[1] - (self.y + 60), pos[0] - (self.x + 60)))
        if angle < 0:
            angle += 360
        color = pygame.Color(255, 0, 0)
        color.hsla = (angle, 100, self.brightness, 100)
        return color
import pygame
import sys
import pyperclip  # Required for clipboard copy
import tkinter as tk
from tkinter import filedialog
from PIL import Image


# Initialize Pygame
pygame.init()

from SquarePixels.uimanagement.button import Button
from SquarePixels.uimanagement.input_feild import InputField
from SquarePixels.uimanagement.TextElement import TextElement
from SquarePixels.uimanagement.checkbox import CheckBox
from SquarePixels.uimanagement.color import ColorPickerInputField
from SquarePixels.uimanagement.Image import ImageElement
from SquarePixels.uimanagement.numeric_input import NumericInputField
from SquarePixels.uimanagement.script import Script
from SquarePixels.uimanagement.UIpanel import UIPanel


# Constants
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)
WHITE = (255, 255, 255)


# Set the screen size
infoObject: object = pygame.display.Info()
screen_width, screen_height = infoObject.current_w, infoObject.current_h
screen: pygame.Surface = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h)
)
pygame_icon = pygame.image.load(
    r"Recources\program recources\Screenshot 2023-09-21 181742.png"
)
pygame.display.set_icon(pygame_icon)  # pygame.display.toggle_fullscreen()
pygame.display.set_caption("Square Pixel")
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

buttons = []
input_fields = []
sidebar_buttons = []
text_elements = []
checkboxes = []
scripts = []
images = []


# Element that is currently being moved or scaled
selected_element = None
scaling = False
scale_start_x = 0
scale_start_y = 0
scale_start_width = 0
scale_start_height = 0

# UI panel properties
ui_panel_x = screen_width - 200
ui_panel_y = 0
ui_panel_width = 200
ui_panel_height = screen_height

# Create a font for displaying instructions
instruction_font = pygame.font.Font(None, 13)
# Add instructions for updating the selected element
instruction_text = "Click and drag to move, right-click to resize element and scroll to change font size. "
instruction_text += "Edit properties in the UI panel, then press Enter to apply changes to the selected element. "
instruction_text += "To use color wheel hold mouse button down and then move it around the inner circle. "
instruction_text += "The bar on the right of the wheel controls brightness. "
instruction_text += (
    "Once you find the color you want then just click the element you want to recolor. "
)


# Function for updating font size when scrolling
def update_font_size(selected_element, scroll_direction):
    """
    Updates the font size of a selected element based on scroll direction
    Args:
        selected_element: The element to update font size for
        scroll_direction: The direction of scrolling ('up' or 'down')
    Returns:
        None: Does not return anything
    - Check if selected element is a Button
    - If scroll direction is 'up', increase font size by 1 point
    - If scroll direction is 'down', decrease font size by 1 point
    - Set the new font size on the selected element"""
    if isinstance(selected_element, Button):
        selected_element.font_size += scroll_direction * 2


def create_button(text, x, y, width, height, command, additional_data=None):
    """
    Create a button widget
    Args:
        text: Button text
        x: x-coordinate of button
        y: y-coordinate of button
        width: Width of button
        height: Height of button
        command: Command to execute on click
        additional_data: Optional additional data to pass to command
    Returns:
        Button: Button widget object
    - Create a Button object with the given parameters
    - Return the Button object
    """
    return Button(text, x, y, width, height, command, additional_data)


def create_input_field(x, y, width, height, placeholder):
    """
    Creates an input field widget
    Args:
        x: X coordinate of input field
        y: Y coordinate of input field
        width: Width of input field
        height: Height of input field
        placeholder: Placeholder text for input field
    Returns:
        InputField: Input field widget object
    - Creates an InputField object with the provided x, y, width, height
    - Sets the placeholder text on the input field
    - Returns the InputField object
    """
    return InputField(x, y, width, height, placeholder)


def create_button_on_sidebar(text, y, create_function, extra=None):
    """
    Creates a button on the sidebar.
    Args:
        text: The text to display on the button.
        y: The y coordinate for the button.
        create_function: The function to call when button is clicked.
        extra: Optional additional data to pass to create_function.
    Returns:
        new_button: The created button object.
    - A new Button object is created with the given parameters
    - The button is added to the sidebar_buttons list
    - The button can now be clicked to call create_function, passing extra data
    """
    button_width = 120
    button_height = 40
    button_x = 10
    new_button = Button(
        text,
        button_x,
        y,
        button_width,
        button_height,
        create_function,
        additional_data=extra,
    )
    sidebar_buttons.append(new_button)


def add_image(circle=None):
    """
    Add an image to the canvas
    Args:
        circle: The circle object to add the image to
    Returns:
        None: Does not return anything
    - Opens a file dialog to select an image file
    - Checks if a file was selected
    - If file selected, adds the image to the canvas"""
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )

    if file_path:
        # Load the selected image using PIL
        image = Image.open(file_path)

        # Create an ImageElement object and add it to your list of elements
        if circle:
            image_element = ImageElement(200, 400, image, "Circle")
        else:
            image_element = ImageElement(200, 400, image)
        images.append(image_element)


# Function for creating a new button
def create_new_button():
    """Creates a new button and adds it to the buttons list

    Args:
        None
    Returns:
        None: No value is returned

    - A new button object is created with the label "Button", positioned at (200,200) with dimensions of 100x50 pixels
    - The new button is appended to the global buttons list
    - No value is returned as the button is added directly to the buttons list"""
    button = create_button("Button", 200, 200, 100, 50, None)
    buttons.append(button)


# Function for creating a new text element
def create_new_text_element():
    """
    Creates and adds a new text element to the list
    Args:
        None
    Returns:
        None: No value is returned
    - Creates a new TextElement object with default values
    - Adds the new TextElement to the text_elements list
    - No value is returned, only side effect is adding to list"""
    text_element = TextElement(200, 300, "Text", 24)
    text_elements.append(text_element)


def delete_selected_element():
    """Deletes currently selected element
    Args:
        None
    Returns:
        None: Selected element is deleted from list
    - Check if a selected element exists
    - If it does, remove it from the global list storing all elements
    - Clear the selected element variable
    - Refresh the UI to remove the selected element"""
    global selected_element

    if selected_element:
        if isinstance(selected_element, Button):
            buttons.remove(selected_element)
        elif isinstance(selected_element, InputField):
            input_fields.remove(selected_element)
        elif isinstance(selected_element, TextElement):
            text_elements.remove(selected_element)
        elif isinstance(selected_element, CheckBox):
            checkboxes.remove(selected_element)
        elif isinstance(selected_element, ImageElement):
            images.remove(selected_element)

        selected_element = None


def create_delete_button(y=280):
    """
    Create and add a delete button to the sidebar
    Args:
        y: Position of the button from the top of the sidebar in pixels
    Returns:
        None: No value is returned
    - Create a Button object with text "Delete", x position 10, y position from argument, width 120 and height 40
    - Assign the delete_selected_element function to the button's command
    - Append the button object to the sidebar_buttons list"""
    delete_button = Button("Delete", 10, y, 120, 40, delete_selected_element)
    sidebar_buttons.append(delete_button)


def export_ui_elements():
    """
    Exports UI elements to Python code
    Args:
        None: No arguments
    Returns:
        None: Does not return anything
    Processes Logic:
        - Loops through button, input_field, checkbox, image lists and generates Python code to recreate each element
        - Copies generated code to clipboard
        - Displays message that code was copied
    """
    global buttons, input_fields, checkboxes, images
    code = [
        "from SquarePixels.uimanagement.button import Button",
        "from SquarePixels.uimanagement.input_feild import InputField",
        "from SquarePixels.uimanagement.TextElement import TextElement",
        "from SquarePixels.uimanagement.checkbox import CheckBox",
        "from SquarePixels.uimanagement.color import ColorPickerInputField",
        "from SquarePixels.uimanagement.Image import ImageElement",
    ]

    # Create buttons
    for index, button in enumerate(buttons):
        code.append(
            f"button{index + 1} = Button('{button.text}',{button.x}, {button.y}, {button.width}, {button.height}, {button.command})"
        )

    # Create input fields
    for index, input_field in enumerate(input_fields):
        code.append(
            f"input_field{index + 1} = InputField({input_field.x}, {input_field.y}, {input_field.width}, {input_field.height}, '{input_field.text}')"
        )
    for index, text_element in enumerate(text_elements):
        code.append(
            f"TextElement{index + 1} = TextElement({text_element.x}, {text_element.y}, {text_element.width}, {text_element.height}, '{text_element.text}')"
        )
    for index, checkbox in enumerate(checkboxes):
        code.append(
            f"CheckBox{index + 1} = CheckBox({checkbox.x}, {checkbox.y}, {checkbox.width}, {checkbox.height}, '{checkbox.text}')"
        )
    for index, image in enumerate(images):
        code.append(
            f"Image{index + 1} = ImageElement({image.x}, {image.y}, {image.width}, {image.height})"
        )
    code.append("code copied to clipboard")
    result = "\n".join(code)
    pyperclip.copy(result)
    screen.fill((0, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Display the generated code on the screen
        font = pygame.font.Font(None, 15)
        for index, t in enumerate(code):
            if index == len(code) - 1:
                index += 5
                font = pygame.font.Font(None, 25)
            code_surface = font.render(t, True, (255, 255, 255))
            screen.blit(
                code_surface, (10, 60 + (15 * index))
            )  # Adjust position as needed
            pygame.display.flip()


# Function for creating a new input field
def create_new_input_field():
    """
    Creates and adds a new input field to the list of input fields
    Args:
        None: No arguments are passed to this function
    Returns:
        None: This function does not return anything
    - Creates a new input field object using the create_input_field function and default parameters
    - Appends the newly created input field object to the list of existing input fields
    - This allows adding multiple input fields dynamically to the UI"""
    input_field = create_input_field(300, 300, 200, 30, "Enter text")
    input_fields.append(input_field)


def create_new_checkbox():
    """Creates a new checkbox object and appends it to the checkboxes list

    Args:
        None
    Returns:
        None: No value is returned
    - A CheckBox object is instantiated with coordinates (380, 40) and label "Label"
    - The new CheckBox object is appended to the checkboxes list
    - This allows the checkbox to be drawn and interacted with through the checkboxes list
    """
    checkbox = CheckBox(380, 40, "Label")
    checkboxes.append(checkbox)


create_button_on_sidebar("New Button", 10, create_new_button)
create_button_on_sidebar("New Input", 60, create_new_input_field)
create_button_on_sidebar("New Text", 110, create_new_text_element)
create_button_on_sidebar("Checkbox", 170, create_new_checkbox)
create_button_on_sidebar("Add Image", 230, add_image)
create_button_on_sidebar("Add Circle Image", 290, add_image, [True])  # circle
create_button_on_sidebar("Save UI", 350, export_ui_elements)
create_delete_button(410)


class Node:
    def __init__(self, node_type, x, y, node_id):
        self.type = node_type
        self.x = x
        self.y = y
        self.id = node_id
        self.logic = lambda: None  # Default logic for the node


# Text input field for customizing text
class TextInputField:
    def __init__(self, x, y, width, height, label, default_text):
        """
        Initialize a graph object
        Args:
            None: No arguments required
        Returns:
            None: Does not return anything
        - Initialize an empty list to store nodes
        - Initialize an empty list to store connections between nodes"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.default_text = default_text
        self.text = default_text
        self.active = False

    def draw(self, screen):
        """Draws a rectangle on the screen.
        Args:
            screen: The screen surface to draw on.
        Returns:
            None: Does not return anything.
        - Draws a filled rectangle on the screen surface using the object's position, size and background color attributes.
        - Loops through the object's elements list and draws each element."""
        font = pygame.font.Font(None, 36)
        text = font.render(self.label, True, (0, 0, 0))
        screen.blit(text, (self.x, self.y))
        pygame.draw.rect(
            screen, (255, 255, 255), (self.x, self.y + 30, self.width, self.height), 2
        )
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + 5, self.y + 35))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = (
                self.x < event.pos[0] < self.x + self.width
                and self.y + 30 < event.pos[1] < self.y + 30 + self.height
            )
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode


# Create UI panel
ui_panel = UIPanel(ui_panel_x, ui_panel_y, ui_panel_width, ui_panel_height)

# Create input fields for customization
text_input_field = TextInputField(
    ui_panel_x + 10, 30, ui_panel_width - 20, 30, "Text:", ""
)
text_size_input_field = NumericInputField(
    ui_panel_x + 10, 100, ui_panel_width - 20, 30, "Text Size:", 0
)
width_input_field = NumericInputField(
    ui_panel_x + 10, 170, ui_panel_width - 20, 30, "Width:", 0
)
height_input_field = NumericInputField(
    ui_panel_x + 10, 250, ui_panel_width - 20, 30, "Height:", 0
)

font_name_input_field = TextInputField(
    ui_panel_x + 10, 330, ui_panel_width - 20, 30, "Font Name:", "Arial"
)
bold_checkbox = CheckBox(ui_panel_x + 10, 450, "Bold", False, color=(0, 0, 0))
italic_checkbox = CheckBox(ui_panel_x + 10, 500, "Italic", False, color=(0, 0, 0))
underline_checkbox = CheckBox(ui_panel_x + 10, 550, "Underline", False, color=(0, 0, 0))
# Create color picker input field for customizing color
color_picker_input_field = ColorPickerInputField(
    ui_panel_x + 10, 630, ui_panel_width - 20, 40, "Color:", (255, 0, 0)
)

ui_panel.elements = [
    text_input_field,
    text_size_input_field,
    width_input_field,
    height_input_field,
    font_name_input_field,
    bold_checkbox,
    italic_checkbox,
    underline_checkbox,
    color_picker_input_field,
]
for el in ui_panel.elements:
    el.size = 20


def handle_events():
    global selected_element, scaling, scale_start_x, scale_start_y, scale_start_width, scale_start_height
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if scaling:
                scaling = False
            for button in buttons:
                if (
                    button.x < event.pos[0] < button.x + button.width
                    and button.y < event.pos[1] < button.y + button.height
                ):
                    button.selected()
                    selected_element = button
            for input_field in input_fields:
                if (
                    input_field.x < event.pos[0] < input_field.x + input_field.width
                    and input_field.y
                    < event.pos[1]
                    < input_field.y + input_field.height
                ):
                    input_field.active = True
                    selected_element = input_field
            for text in text_elements:
                if text.x < event.pos[0] < text.x + (
                    text.width + text.size
                ) and text.y < event.pos[1] < text.y + (text.height + text.size):
                    text.active = True
                    selected_element = text
            for check in checkboxes:
                if check.x < event.pos[0] < check.x + (
                    check.width + check.size
                ) and check.y < event.pos[1] < check.y + (check.height + check.size):
                    check.active = True
                    selected_element = check
            for image in images:
                if (
                    image.x < event.pos[0] < image.x + image.width
                    and image.y < event.pos[1] < image.y + image.height
                ):
                    image.active = True
                    selected_element = image
            for sidebar_button in sidebar_buttons:
                if (
                    sidebar_button.x
                    < event.pos[0]
                    < sidebar_button.x + sidebar_button.width
                    and sidebar_button.y
                    < event.pos[1]
                    < sidebar_button.y + sidebar_button.height
                ):
                    if sidebar_button.additional_data:
                        sidebar_button.command(*sidebar_button.additional_data)
                    else:
                        sidebar_button.command()
            if selected_element:
                if not (
                    selected_element.x
                    < event.pos[0]
                    < selected_element.x + selected_element.width
                    and selected_element.y
                    < event.pos[1]
                    < selected_element.y + selected_element.height
                ):
                    selected_element = None
        elif (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 3
            and selected_element
        ):
            scaling = True
            scale_start_x = event.pos[0]
            scale_start_y = event.pos[1]
            scale_start_width = selected_element.width
            scale_start_height = selected_element.height

        for input_field in input_fields:
            input_field.change_text(event)
        for button in buttons:
            button.change_text(event)
        for text_element in text_elements:
            text_element.change_text(event)
        for checkbox in checkboxes:
            checkbox.change_text(event)
            checkbox.handle_event(event)
        if selected_element:
            # Update UI panel with the selected element's properties
            text_input_field.text = selected_element.text
            text_size_input_field.value = selected_element.size
            width_input_field.value = selected_element.width
            height_input_field.value = selected_element.height
            font_name_input_field.text = selected_element.font_name
            bold_checkbox.checked = selected_element.bold
            italic_checkbox.checked = selected_element.italics
            underline_checkbox.checked = selected_element.underlined

            if scaling and event.type == pygame.MOUSEMOTION:
                selected_element.width = scale_start_width + (
                    event.pos[0] - scale_start_x
                )
                selected_element.height = scale_start_height - (
                    scale_start_y - event.pos[1]
                )
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # Left mouse button is held
                    selected_element.x += event.rel[0]
                    selected_element.y += event.rel[1]
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                selected_element.size += 1
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                selected_element.size -= 1
        for inspect in ui_panel.elements:
            if isinstance(inspect, ColorPickerInputField):
                inspect.handle_event(event)
            else:
                inspect.handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Update the selected element's properties with the UI panel values
            if selected_element:
                selected_element.text = text_input_field.text
                selected_element.size = text_size_input_field.value
                selected_element.width = width_input_field.value
                selected_element.height = height_input_field.value
                selected_element.font_name = font_name_input_field.text
                selected_element.bold = bold_checkbox.checked
                selected_element.italics = italic_checkbox.checked
                selected_element.underlined = underline_checkbox.checked
        # Update the selected element's color based on the color picker value
        if selected_element:
            selected_element.color = color_picker_input_field.color


def main():
    while True:
        handle_events()
        screen.fill((0, 0, 0))

        # Draw the sidebar buttons
        for sidebar_button in sidebar_buttons:
            sidebar_button.draw(screen)

        # Add text elements to the drawing loop
        for text_element in text_elements:
            text_element.draw(screen)
        # Draw the elements (buttons and input fields)
        for button in buttons:
            button.draw(screen)
        for input_field in input_fields:
            input_field.draw(screen)
        for checkbox in checkboxes:
            checkbox.draw(screen)
        for image in images:
            image.draw(screen)
            # Blit instructions on the screen
        instruction_surface = instruction_font.render(
            instruction_text, True, (255, 255, 255)
        )
        screen.blit(instruction_surface, (10, screen_height - 30))
        # Draw the UI panel
        ui_panel.draw(screen)

        pygame.display.flip()


def start():
    for bu in sidebar_buttons:
        bu.size = 20
    main()


if __name__ == "__main__":
    start()
import pygame

if __name__ == "__main__":
    # Constants
    infoObject: object = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    BACKGROUND_COLOR = (0, 0, 0)
font = pygame.font.Font(None, 36)
# Define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)

white = (255, 255, 255)


# Create an InputField class for text input
class InputField:
    def __init__(self, x, y, width, height, placeholder, command=None, parameters=None):
        """
        Initialize a text input box object
        Args:
            x: X position of the text input box
            y: Y position of the text input box
            width: Width of the text input box
            height: Height of the text input box
            placeholder: Placeholder text to display when empty
            command: function to run when the return key is pressed
            parameters: List of aditional arguments to pass to command
        Returns:
            self: The text input box object
        Processing Logic:
            - Sets the x, y, width and height attributes from the arguments
            - Sets the placeholder text
            - Initializes other attributes like text, active state etc
            - Sets the command and parameters if provided
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.placeholder = placeholder
        self.text = ""
        self.active = False
        self.size = 36
        self.hovered = False
        self.font_name = "Recources\Fonts\PixelifySans-Regular.ttf"
        self.bold = False
        self.italics = False
        self.underlined = False
        self.command = command
        self.parameters = parameters

    def draw(self, screen):
        """
        Draws a button on the provided screen.
        Args:
            screen: The screen surface to draw the button on.
        Returns:
            None: Does not return anything, draws the button directly to the screen.
        Processing Logic:
            - Loads the font based on the button's font properties
            - Sets the font style based on bold, italics, underline properties
            - Draws the button rectangle based on position and size
            - Sets the font color based on active state
            - Renders the text and blits it to the screen
        """
        font = pygame.font.Font(self.font_name, self.size)
        font.set_bold(self.bold)
        font.set_italic(self.italics)
        font.set_underline(self.underlined)
        color = BUTTON_COLOR if not self.active else BUTTON_HOVER_COLOR
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        font_color = (0, 0, 0) if not self.active else (255, 255, 255)
        text = font.render(
            self.text if self.text else self.placeholder, True, font_color
        )
        screen.blit(text, (self.x + 10, self.y + 10))

    def handle_event(self, event):
        """Handle mouse and keyboard events for a button
        Args:
            event: The pygame event to handle
        Returns:
            self.active: Whether the button is currently pressed
        - Check if mouse button 1 was pressed within button bounds and set self.active
        - Check if a key was pressed and button is active
        """
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            if event.key == pygame.K_RETURN:
                if self.command:
                    if self.parameters:
                        self.command(*self.parameters)
                    else:
                        self.command()

    def change_text(self, event):
        """
        Change text on mouse events
        Args:
            event: The pygame event object
        Returns:
            None: No value is returned
        Processing Logic:
        - Check if mouse is hovering over button on MOUSEMOTION
        - Check if mouse is clicked on button on MOUSEBUTTONDOWN
        - Check if a key is pressed while button is active on KEYDOWN
        - Set hovered and active flags based on above checks
        """
        if event.type == pygame.MOUSEMOTION:
            self.hovered = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def clear(self):
        """Clears the text in the object
        Args:
            self: The object whose text needs to be cleared
        Returns:
            None: Does not return anything
        - Sets the text attribute of the object to an empty string ""
        - This empties out any existing text in the object"""
        self.text = ""
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
# Numeric input field for customizing numeric properties
import pygame


class NumericInputField:
    def __init__(self, x, y, width, height, label, default_value):
        """
        Initialize a NumericInputField GUI element
        Args:
            x: X coordinate of element
            y: Y coordinate of element
            width: Width of element
            height: Height of element
            label: Label for element
            default_value: Default value for element
        Returns:
            None: Does not return anything
        - Sets x, y, width, height, label and default value attributes of element
        - Sets active attribute to False by default
        - Initializes element with given parameters"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.value = default_value
        self.active = False

    def draw(self, screen):
        """Draw the player on the screen.
        Args:
            screen: The screen surface to draw on.
        Returns:
            None: Does not return anything.
        - Get the player's position, width and height from its attributes
        - Draw a rectangle on the screen using pygame at the player's position with its dimensions and color
        - Loop through the player's elements and draw them"""
        font = pygame.font.Font(None, 36)
        """Draws a rectangle on the screen.
        Args:
            screen: The screen surface to draw on.
        Returns: 
            None: Does not return anything.
        - Draws a filled rectangle on the screen surface using the object's position, size and background color attributes.
        - Loops through the object's elements list and draws each element."""
        text = font.render(self.label, True, (0, 0, 0))
        screen.blit(text, (self.x, self.y))
        pygame.draw.rect(
            screen, (255, 255, 255), (self.x, self.y + 30, self.width, self.height), 2
        )
        text = font.render(str(self.value), True, (0, 0, 0))
        screen.blit(text, (self.x + 5, self.y + 35))

    def handle_event(self, event):
        """Handle mouse and keyboard events for a button.
        Args:
            event: The pygame event to handle
        Returns:
            None: Does not return anything
        - Check if mouse button 1 was pressed and mouse position is over button
        - Set button to active if mouse press conditions are met
        - Check if a key was pressed and button is active
        - Does not return anything, only checks conditions"""
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = (
                self.x < event.pos[0] < self.x + self.width
                and self.y + 30 < event.pos[1] < self.y + 30 + self.height
            )
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.value = int(str(self.value)[:-1])
            elif event.key in [
                pygame.K_0,
                pygame.K_1,
                pygame.K_2,
                pygame.K_3,
                pygame.K_4,
                pygame.K_5,
                pygame.K_6,
                pygame.K_7,
                pygame.K_8,
                pygame.K_9,
            ]:
                self.value = int(str(self.value) + event.unicode)
import pygame
import sys
import SquarePixels.multiplayer.server as server

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
