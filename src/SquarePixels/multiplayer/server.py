import pygame
import socket
import select
import time
import random
import typing
import pickle
from SquarePixels.player.player import Player
from SquarePixels.render.render import Nametag, render_chat, render_scores
import SquarePixels.render.render as render
from SquarePixels.terraingen import terrain_gen as tgen
from SquarePixels.player import player as pl


def main(max_players, server_name):
    
    # Set up the game window
    infoObject: object = pygame.display.Info()
    screen_width, screen_height = infoObject.current_w, infoObject.current_h
    screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(f"Square Pixels - Server - {server_name}")
    
    # Initialize the game
    pygame.init()
    terrain_gen = tgen.TerrainGenerator(
        width=(-100, infoObject.current_w // 15), height=infoObject.current_h // 15
    )
    terrain_gen.generate_terrain(screen)



    # Set the desired time interval for sending updates (in seconds)
    update_interval: float = 0.1  # 100 milliseconds

    # Initialize a variable to keep track of the last update time
    last_update_time: float = time.time()
    dotr: bool = True
    circle_x: int = 0
    circle_y: int = 0
    points: typing.Dict[str, int] = dict()
    DayTime = 0
    Morning = 0

    # Initialize the game state
    players: typing.List[Player] = [pl.Player(200, 200, infoObject.current_w - 40, 0)]
    chat_messages: typing.List[str] = []

    # Set up the server socket
    server_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", 12345))
    server_socket.listen(5)

    sockets_list: typing.List[socket.socket] = [server_socket]

    print("Server started. Waiting for connections...")
    clock = pygame.time.Clock()
    # Game loop
    running: bool = True
    while running:
        clock.tick(120)
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Accept new connections
        read_sockets, _, _ = select.select(sockets_list, [], [], 0)
        for sock in read_sockets:
            if sock == server_socket:
                if len(sockets_list) >= max_players:
                    print("no more room on this server")
                else:
                    client_socket, client_address = server_socket.accept()
                    sockets_list.append(client_socket)
                    print("New client connected:", client_address)

        # Receive and process client data
        for client_socket in sockets_list[1:]:
            try:
                data = client_socket.recv(4096)
                if data:
                    received_data = pickle.loads(data)
                    if isinstance(received_data, str):
                        if received_data == "PING":
                            print("ping")
                            client_socket.sendall(b"PONG")
                        else:
                            chat_messages.append(received_data)
                    elif isinstance(received_data, list):
                        print(received_data)
                        points[received_data[0]] = received_data[1]
                        if received_data[2] == True:
                            dotr = True
                        else:
                            dotr = False
                    else:
                        player_data = received_data
                        for player in players:
                            if player.name == player_data.name:
                                player.x = player_data.x
                                player.y = player_data.y
                                break
                        else:
                            players.append(
                                Player(
                                    player_data.x, player_data.y, player_data.name
                                )
                            )
            except:
                print("Client disconnected")
                sockets_list.remove(client_socket)

        # Update the game state
        # ...

        # Calculate the elapsed time since the last update
        # current_time = time.time()
        # elapsed_time = current_time - last_update_time

        # Check if the desired update interval has passed
        # if elapsed_time >= update_interval:
        #     # Update the last update time
        #     last_update_time = current_time
        #     # Send the updated game state to all clients

        if dotr == True:
            circle_x = random.randint(10, screen_width - 10)
            circle_y = random.randint(10, screen_height - 10)
            dotr = False

        game_state = {
            "players": players,
            "chat_messages": chat_messages,
            "circle_x": circle_x,
            "circle_y": circle_y,
            "points": points,
        }
        for client_socket in sockets_list[1:]:
            client_socket.sendall(pickle.dumps(game_state))  # .encode())

        # Render the game state
        screen.fill((0, 0, 0))
        if Morning == 0:
            DayTime = DayTime + 0.005
        else:
            DayTime = DayTime - 0.005
            if DayTime <= 0:
                Morning = 0
        sky, colliders, hidden_area = render.render_terrain(
            screen,
            terrain_gen.width,
            terrain_gen.height,
            terrain_gen.terrain,
            terrain_gen.pos_x,
            terrain_gen.pos_y,
            terrain_gen.camera_x,
            terrain_gen.camera_y,
            players[0],
            DayTime,
            Morning,
        )

        if DayTime > 6.5:
            Morning = 1
        for player in players:
            pygame.draw.circle(screen, (255, 0, 0), (player.x, player.y), 10)
            nametag = Nametag(player)
            nametag.draw(screen)

        render_chat(chat_messages, screen_height, screen)
        render_scores(points, screen)

        pygame.display.flip()

    # Clean up
    pygame.quit()

if __name__ == "__main__":
    main(5, "")