import pygame as pig
import typing as tp
import player
import Lighting as Lit
import random
import math

# Define global variables for screen width and height
SCREEN_WIDTH = 800  # Adjust this to your screen width
SCREEN_HEIGHT = 600  # Adjust this to your screen height
black_rectangles = []
infoObject: object = pig.display.Info()
# Fill the screen with black rectangles
for x in range(infoObject.current_w // 20):
    for y in range(infoObject.current_h // 20):
        black_rect = pig.Rect((x * 20, y * 20, 20, 20))
        black_rectangles.append(black_rect)
# Rest of your code...


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
    tile_size = 15
    block_images = [
        r"terraria_styled_game\Textures\grass.jpg",
        r"terraria_styled_game\Textures\stone.jpg",
        r"terraria_styled_game\Textures\wood.png",
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
        sphere_radius = 100  # You can adjust this radius as needed
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
    return colliders


def render_player(
    screen: pig.Surface,
    x: float | int,
    y: float | int,
    size: int,
    color: tuple,
    character,
):
    pig.draw.circle(screen, (0, 0, 0, 0), (x, y), size, size)


def render_other_players(screen: pig.Surface, players: list):
    for player in players:
        pig.draw.circle(
            screen, player.color, (player.x, player.y), player.size, player.size
        )


def sort_leaderboard(allpoints: tp.Dict[str, int]) -> tp.List[tp.Tuple[str, int]]:
    sorted_points = sorted(allpoints.items(), key=lambda x: x[1], reverse=True)
    return sorted_points


def render_chat(
    chat_messages: tp.List[str], screen_height: int, screen: pig.Surface
) -> None:
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
        self.player: player.Player = player

    def draw(self, screen: pig.Surface) -> None:
        font = pig.font.Font(None, 20)
        text = font.render(self.player.name, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.player.x, self.player.y - 15))
        screen.blit(text, text_rect)
