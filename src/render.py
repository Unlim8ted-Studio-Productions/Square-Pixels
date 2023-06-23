import pygame as pig
import typing as tp
import player


def render_terrain(
    screen: pig.Surface,
    width: float | int,
    height: float | int,
    terrain: list,
    pos_x: float | int,
    pos_y: float | int,
    camera_x: float | int,
    camera_y: float | int,
):
    tile_size = 10
    colors = [
        (100, 100, 100),  # Stone
        (139, 69, 19),  # Dirt
        (139, 115, 85),  # Wood
        (34, 139, 34),  # Leaves
        (0, 128, 0),  # Coal
        (211, 211, 211),  # Iron
        (255, 223, 0),  # Gold
        (128, 128, 128),  # Diamond
        (135, 206, 235),  # Sky (Blue)
    ]  # Color palette for blocks

    for x in range(width[0], width[1]):
        for y in range(height):
            block_type = terrain[y][x]
            color = colors[block_type]
            pig.draw.rect(
                screen,
                color,
                (
                    (x + pos_x - camera_x) * tile_size,
                    (y + pos_y - camera_y) * tile_size,
                    tile_size,
                    tile_size,
                ),
            )


def render_player(
    screen: pig.Surface, x: float | int, y: float | int, size: int, color: tuple
):
    pig.draw.circle(screen, color, (x, y), size, size)


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
