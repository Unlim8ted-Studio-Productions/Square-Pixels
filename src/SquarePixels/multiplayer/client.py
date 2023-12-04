import pygame
import socket
import pickle
import SquarePixels.player.player as play

# import playerdatc
import typing as typi
import pickle
import SquarePixels.render.render as render


def main(ip, name):
    # Initialize the game
    pygame.init()

    # Set up the game window
    o_p_c: list = []
    infoObject: object = pig.display.Info()
    sceen_width, screen_height = infoObject.current_w, infoObject.current_h
    screen: pig.Surface = pig.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    pygame.display.set_caption("Multiplayer Platform Game - Client")

    # Information
    print(
        "press p to toggle paint mode on and off, press g to toggle gravity on and off, press i to toggle inverted trail, press r to toggle rainbow trail, move with arrows, hit enter to send start typing message hit enter again to send."
    )
    paint: bool = False
    typing: bool = False
    gravity: bool = True
    dotr: bool = True
    points: typi.List[typi.Union[str, int, bool]] = ["", 0, True]
    ai: bool = False

    # Define AI player class
    class AIPlayer:
        def __init__(self, x: int, y: int):
            self.x: int = x
            self.y: int = y
            self.speed: int = 1

        def update(self, dot_x: int, dot_y: int) -> None:
            if self.x < dot_x:
                self.x += self.speed
            elif self.x > dot_x:
                self.x -= self.speed

            if self.y < dot_y:
                self.y += self.speed
            elif self.y > dot_y:
                self.y -= self.speed

    # Set up the client socket
    client_socket: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((ip, 12345))
    except:
        print("error connecting to device.")
        print(socket.error)

    # Prompt the player to enter their name
    # name: str = input("Enter your name: ")
    points[0] = name

    player: play.Player(0, 0)
    aiplayer: AIPlayer = AIPlayer(0, 0)
    # Initialize the input box and chat that player has connected
    client_socket.sendall(pickle.dumps(f"{name} has joined this server"))
    input_box: str = ""
    clock: object = pygame.time.Clock()
    FPS: int = 120
    
    import SquarePixels.render.render as render
    import pygame as pig
    import SquarePixels.enemymanagement.enemy_manager as enemy_manager
    from SquarePixels.uimanagement import death, MainMen
    import SquarePixels.soundmanagement.music as music
    import random

    hidden_area = []



    music.play_music(r"Recources\sounds\music\ingame\music\Ingame1.mp3", volume=0.2)
    enemymanager = enemy_manager.Enemy_manager([(0, infoObject.current_w)])
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and player.y == infoObject.current_h - 20:
                    player.velocity_y -= 1
                elif event.key == pygame.K_LEFT:
                    player.velocity_x = -player.speed
                elif event.key == pygame.K_RIGHT:
                    player.velocity_x = player.speed
                elif event.key == pygame.K_RETURN and typing == False:
                    typing = True
                elif event.key == pygame.K_RETURN and len(input_box) > 0 and typing:
                    sendmessage = player.name + ": " + input_box
                    client_socket.sendall(pickle.dumps(sendmessage))
                    input_box = ""
                    typing = False
                elif event.key == pygame.K_BACKSPACE:
                    input_box = input_box[:-1]
        clicked = False
        if reset_terrain:
            terrain_gen.run(screen)
            reset_terrain = False
        # pig.draw.rect(screen,(.100,.100,.100,50),rect)
        screen.fill((0.035, 206, 235))

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
            player,
            DayTime,
            Morning,
        )

        if DayTime > 6.5:
            Morning = 1
        result = player.move(screen, infoObject, tile, terrain_gen.terrain)
        if result != None:
            if len(result) <= 5:
                reset_terrain = result[0]
                clicked = result[1]
                try:
                    objectheld = result[2]
                except:
                    pass
            else:
                terrain_gen.terrain = result
        tile = [-1, 0]
        if clicked:
            if random.randint(0, 1) == 1:
                music.play_music(
                    r"Recources\sounds\block break\block break.mp3",
                    0,
                    channel=1,
                    volume=5,
                )
            else:
                music.play_music(
                    r"Recources\sounds\block break\blockbreak1.mp3",
                    0,
                    channel=1,
                    volume=5,
                )
            tile = player.delete_tile(terrain_gen.terrain, tile)
        player.update(
            infoObject.current_h, infoObject.current_w, colliders, screen
        )  # terrain_gen.colliders)
        enemymanager.update(
            player.x, player.y, sky, infoObject, colliders, screen, player, Morning
        )
        if player.current_health <= 0:
            if death.draw_death_screen(
                screen, infoObject.current_w, infoObject.current_h, player.xp
            ):
                player.respawn(sky, infoObject, [(0, infoObject.current_w)])
            else:
                player.respawn(sky, infoObject, [(0, infoObject.current_w)])
                MainMen.mainfunc()
        terrain_gen.camera_x += vx
        terrain_gen.camera_y += vy
        player.draw(screen, player_sprite)
        # print(player.xp)
        # player.draw_trail(screen)
        pig.display.flip()
        
        client_socket.sendall(pickle.dumps(player))

        # Receive and update the game state from the server
        data = client_socket.recv(4096)
        game_state = pickle.loads(data)
        players = game_state["players"]
        chat_messages = game_state["chat_messages"]
        circle_x = game_state["circle_x"]
        circle_y = game_state["circle_y"]
        allpoints = game_state["points"]
        
        clock.tick(60)

    # Game loop
    running: bool = True
    while running:
        #clock.tick(FPS)
        ## Handle events

        #        elif event.key == pygame.K_p and typing == False:
        #            if paint == False:
        #                paint = True
        #            else:
        #                paint = False
        #        elif event.key == pygame.K_g and typing == False:
        #            if gravity == False:
        #                gravity = True
        #                player.gravityi = gravity
        #            else:
        #                gravity = False
        #                player.gravityi = gravity
        #        elif event.key == pygame.K_i and typing == False:
        #            if player.inverse == False:
        #                player.inverse = True
        #            else:
        #                player.inverse = False
        #        elif event.key == pygame.K_r and typing == False:
        #            if player.rainbow == False:
        #                player.rainbow = True
        #            else:
        #                player.rainbow = False
        #        elif event.key == pygame.K_0 and typing == False:
        #            if ai == False:
        #                print("AI activated")
        #                ai = True
        #            else:
        #                print("AI deactivated")
        #                ai = False
        #        elif event.key == pygame.K_g and typing:
        #            input_box += "g"
        #        elif event.key == pygame.K_p and typing:
        #            input_box += "p"
        #        elif event.key == pygame.K_i and typing == True:
        #            input_box += "i"
        #        elif event.key == pygame.K_r and typing == True:
        #            input_box += "r"
        #        elif event.key <= 127 and typing:
        #            input_box += chr(event.key)
        #    elif event.type == pygame.KEYUP:
        #        if event.key == pygame.K_LEFT:
        #            player.velocity_x = -0.9
        #        if event.key == pygame.K_RIGHT:
        #            player.velocity_x = 0.9
#
        ## Update AI player if AI flag is True
        #if ai:
        #    aiplayer.update(circle_x, circle_y)
#
        ## Update player location
        #player.update(screen_height, screen_width)

        # Send player data to the server
        client_socket.sendall(pickle.dumps(player))

        # Receive and update the game state from the server
        data = client_socket.recv(4096)
        game_state = pickle.loads(data)
        players = game_state["players"]
        chat_messages = game_state["chat_messages"]
        circle_x = game_state["circle_x"]
        circle_y = game_state["circle_y"]
        allpoints = game_state["points"]

        # Render the game state
        if not paint:
            screen.fill((0, 0, 0))

        # render trail
        player.draw_trail(screen)

        rect = pygame.Rect((circle_x, circle_y), (5, 5))
        prect = pygame.Rect((player.x, player.y), (10, 10))

        # f#or otherplayer in players:
        #    o_p_c.append(pygame.Rect(otherplayer.x,otherplayer.y))
        collide = rect.colliderect(prect)
        pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), 5)
        if collide:
            dotr = True
            points[2] = dotr
            points[1] += 1
            client_socket.sendall(pickle.dumps(points))  # .encode())
            dotr = False

        for other_player in players:
            if other_player.name != player.name:
                pygame.draw.circle(
                    screen, (255, 0, 0), (other_player.x, other_player.y), 10
                )
                nametag = render.Nametag(other_player)
                nametag.draw(screen)
        pygame.draw.circle(screen, (0, 0, 255), (player.x, player.y), 10)
        nametag = render.Nametag(player)
        nametag.draw(screen)

        render.render_chat(chat_messages, screen_height, screen)
        render.render_scores(allpoints, screen)

        # Render the input box
        font = pygame.font.Font(None, 20)
        input_box_text = font.render(
            "Enter message: " + input_box, True, (255, 255, 255)
        )
        input_box_rect = input_box_text.get_rect(left=10, top=screen_height - 30)
        screen.blit(input_box_text, input_box_rect)

        pygame.display.flip()

    # Clean up
    pygame.quit()


if __name__ == "__main__":
    main()
