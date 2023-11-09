if __name__ == '__main__':
    if __name__ == "__main__":
        
        import pygame as pig
        from SquarePixels.terraingen import terrain_gen as tgen
        from SquarePixels.uimanagement import logo, MainMen
        from SquarePixels.player import player as pl
        from SquarePixels.uimanagement.Character_creation import main
        from SquarePixels.game.game import game
        from SquarePixels.soundmanagement.music import play_music
    
        OOO0O0OO0O000OOOOOO000OO0OOOOOO0 = [-1, 0]
    
        pig.init()
        clock: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pig.time.Clock()
        not_skipped: OOOOOOOO0OO000O00OO000O0OOO000OO = True
        reset_terrain: OOOOOOOO0OO000O00OO000O0OOO000OO = False
        clicked: OOOOOOOO0OO000O00OO000O0OOO000OO = False
        # Path to your video file
        video_file: O0OO0OO0OOO0O0OO00OOOOOO = r"Recources\\Company Animated Logo.mov"
        infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pig.display.Info()
        screen: pig.OOOOOOO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = pig.display.set_mode(
            (infoObject.current_w, infoObject.current_h)
        )
        OOOOO0OOOOOO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOO00O0OOOO0OO000O0OOO0O0O0 = pig.image.load(
            r"Recources\program recources\Screenshot 2023-09-21 181742.png"
        )
        pig.display.set_icon(pygame_icon)  # pig.display.toggle_fullscreen()
    
        pig.display.set_caption("Square Pixel")
        pig.mouse.set_cursor(pig.SYSTEM_CURSOR_CROSSHAIR)
        # Path to the folder to save the extracted frames
        image_folder: O0OO0OO0OOO0O0OO00OOOOOO = r"Recources\\frames"
        colliders: OOO000OO0O000OOOO0OO0OO0OOO0O0OO = []
        # Extract frames from the video
        # logo.extract_frames(video_file, image_folder)
        vx, O0O000OOOOOO0OOO = 0, 0  # infoObject.current_w/2, 0#infoObject.current_h /2
        # Call the function to play the video
        logo.play_intro_video(image_folder, not_skipped, screen, 0)
        image_folder: O0OO0OO0OOO0O0OO00OOOOOO = r"Recources\\NewHorizonsFrames"
        logo.play_intro_video(image_folder, not_skipped, screen, 1)
        play_music(r"Recources\sounds\music\Menu.mp3")
        MainMen.mainfunc()
        # Rest of game code goes here...
        OOO0O0OO0OOOOOO000OOOOOO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0O0OO0OOOO0OOOOOO0OOOOOO0OOO0O0O0 = tgen.TerrainGenerator(
            OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO=(0, infoObject.current_w // 10), _OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO=infoObject.current_h // 15
        )
        OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOOO0OO0OO0OOOOO0OO00OOOOOO0O000OOOOOO0O0OO0OOOOOO0 = main()
        terrain_gen.generate_terrain(screen)
        OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOO = pl.Player(vx, vy, infoObject.current_w - 40, 0)
        _OOOOO00OO0OOOOOOOOO0OOO00OO0OO00O000OOOO0O0OO000OOOOOO0 = 0
        OOOO00OO0OO000O000OOOOOOOOO0O0O00O000OOOOOO0O0O0O0OOOOOO = 0
        # world:_OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = tgen.generate()
        # for square in world.tiles:
        #    render.draw(screen, square)
        # print(terrain_gen.terrain)
        # quit()
        # _OOOOOO0OOOOOO000O0OOOOOOO0O0OO=pig.Rect((0,0),(infoObject.current_w,infoObject.current_h))
        _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
        game(
            screen,
            running,
            terrain_gen,
            player,
            infoObject,
            player_sprite,
            clock,
            vx,
            vy,
            reset_terrain,
            Morning,
            DayTime,
            tile,
        )    
        import pygame
    
    import sys
    
    import random
    from collections import deque
    from SquarePixels.soundmanagement.music import play_music
    
    
    # Function to generate a random maze using Recursive Backtracking algorithm
    def O0OOOOOO0OOOOOO0OOO0O0O00OOOOOO000OOOOOOOO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOO0O0OO00OO0OOOOO0OOOOOOO0OOOOOO0(WIDTH, CELL_SIZE, HEIGHT):
        O0O0OO00OO0OOOOO0OOOOOOO0OOOOOO0 = [
            ["#" for _ in range(WIDTH // CELL_SIZE)] for _ in range(HEIGHT // CELL_SIZE)
        ]
        O0O000OO0O000OOOO0OO0OO00O000OOOOOO0O0OO0OOOOOO0O0OOO0OO = set()
    
        def _O0OOOOOO0OOOOOOOO0O0O0O0OO0OOOO0O000OO0O000OOOO0OO0OO00O000OOOOOO0O0OO(x, y):
            return (
                0 < x < WIDTH // CELL_SIZE - 1
                and 0 < y < HEIGHT // CELL_SIZE - 1
                and maze[y][x] == "#"
            )
    
        def _O0OOOOOO0OOOOO00OOOOOOO0O000OO0OOOOOO0O0OO0OOOOOOOO0OOOO0OOOOOOOO0O0OO00000OOO(x, y):
            maze[y][x] = " "
            visited.add((x, y))
    
            O0OOO0OO0O000OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OO0 = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
            random.shuffle(directions)
    
            for nx, ny in directions:
                if (nx, ny) not in visited and can_visit(nx, ny):
                    maze[(y + ny) // 2][(x + nx) // 2] = " "
                    carve_path(nx, ny)
    
        start_x, O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOOOOO0OOO = (
            random.randint(1, WIDTH // (2 * CELL_SIZE)) * 2 - 1,
            random.randint(1, HEIGHT // (2 * CELL_SIZE)) * 2 - 1,
        )
        carve_path(start_x, start_y)
    
        return maze
    
    
    # Breadth-First Search (BFS) Pathfinding
    def OOOOOOOOO00OOOOOO0OO0OO0(maze, start, goal):
        OOO0OOOOOOOOOOO00OOOOOO0OOOOOOO00OOOOOO0 = deque([(start, [])])
        O0O000OO0O000OOOO0OO0OO00O000OOOOOO0O0OO0OOOOOO0O0OOO0OO = set()
    
        while queue:
            current, OOOOO0OOOO0OOOOOOOO0O0OO00000OOO = queue.popleft()
    
            if _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OO == goal:
                return path
    
            if current in visited:
                continue
    
            visited.add(current)
    
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                OOO0O0O00OOOOOO00O000OOOO0OOOOOO00000OOOOOOOOOOO0OO000O000OOOOOO = (current[0] + dx, current[1] + dy)
                if (
                    0 <= neighbor[0] < len(maze[0])
                    and 0 <= neighbor[1] < len(maze)
                    and maze[neighbor[1]][neighbor[0]] != "#"
                ):
                    queue.append((neighbor, path + [neighbor]))
    
        return None
    
    
    def O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OO():
        # Initialize Pygame
        pygame.init()
        infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.display.Info()
        screen: pygame.OOOOOOO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = pygame.display.set_mode(
            (infoObject.current_w, infoObject.current_h)
        )
        OOOOO0OOOOOO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOO00O0OOOO0OO000O0OOO0O0O0 = pygame.image.load(
            r"Recources\program recources\Screenshot 2023-09-21 181742.png"
        )
        pygame.display.set_icon(pygame_icon)
    
        # Constants
        WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = infoObject.current_w, infoObject.current_h
        OOOO00OO000O00OOOO0O0O0O00OO0OO0OO0O0OOO = (0, 0, 0)
        OOOO0OO0OO0O0OOO0OOOOO00 = (255, 0, 0)
        OO0OOOOOOO0O0OOOOOO00OOOOOO00OOOO0OO0OOOOOOOOOO0OO0O0O0OOOOO0000OO0O0OOO = 40
    
        # Create the screen
    
        # pygame.display.toggle_fullscreen()
        pygame.display.set_caption("Square Pixel")
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    
        # Player
        OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOO = pygame.Rect(40, 40, CELL_SIZE // 2, CELL_SIZE // 2)
    
        # Goal
        O0OOOOOO0OO000O0OO0OOOOOOOO000OO = pygame.Rect(680, 440, CELL_SIZE, CELL_SIZE)
        O0O0OO00OO0OOOOO0OOOOOOO0OOOOOO0 = generate_maze(WIDTH, CELL_SIZE, HEIGHT)
    
        # Game loop
        _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
        OO0OOOO00OO000O0OOO0O0O0 = False
        _O0OOOO00OOOOOO0OOOOOO0O0OOO0OO0O000OOOOOO0O0OOO0OO0OO0O0OO0OOOO00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(
            "Recources\Fonts\PixelifySans-Regular.ttf", 50
        )
        while running:
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN:
                    return None
    
            # Get the current mouse position
            mouse_x, O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0O0OO0OOOOOOO0OOO = pygame.mouse.get_pos()
    
            # Calculate the path from player to mouse using BFS algorithm
            O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOOOOOO0OO0OO000O0O0OO0OO0 = (player.centerx // CELL_SIZE, player.centery // CELL_SIZE)
            O0OOOOOO0OO000O0OO0OOOOOOOO000OOO0OO0OOOOOOOO0OO0OO000O0O0OO0OO0 = (mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)
            OOOOO0OOOO0OOOOOOOO0O0OO00000OOO = bfs(maze, start_pos, goal_pos)
    
            if path:
                # Move player towards the next position in the path
                OOO0O0O00OOOOOO0O00OO000OOO0O0OOO0OO0OOOOOOOO0OO0OO000O0O0OO0OO0 = path[1] if len(path) >= 2 else path[0]
                O0OOO0OOO00OO000 = (next_pos[0] * CELL_SIZE + CELL_SIZE / 2) - player.centerx
                O0OOO0OOOOOO0OOO = (next_pos[1] * CELL_SIZE + CELL_SIZE / 2) - player.centery
                OOO000OO0OOOOOO0OOO0O0O0O0OOOOOOOOO0O0OO00000OOO = max(1, (dx**2 + dy**2) ** 0.5)
                dx /= length
                dy /= length
                player.x += dx
                player.y += dy
    
            # Check if player reaches the goal
            if player.colliderect(goal):
                OO0OOOO00OO000O0OOO0O0O0 = True
    
            # Clear the screen
            screen.fill(WHITE)
    
            # Draw maze, player, and goal
            if not won:
                for y, row in enumerate(maze):
                    for x, cell in enumerate(row):
                        if _O0OOOO0OOOOOO0OOO000OOOOO000OO == "#":
                            pygame.draw.rect(
                                screen,
                                RED,
                                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                            )
    
            pygame.draw.rect(screen, (200, 231, 193), player)
            pygame.draw.rect(screen, (123, 143, 233), goal)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = credits_font.render(
                "press anything to escape", True, (100, 100, 100)
            )
            screen.blit(
                text_surface,
                (
                    WIDTH // 4 - text_surface.get_width() // 2,
                    HEIGHT - 50,
                ),
            )
            pygame.display.flip()
    
            # Scroll credits down the screen if the player won
            if won:
                play_music(r"Recources\sounds\music\EndCredits.mp3")
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = credits_font.render(
                    "press anything to skip", True, (100, 100, 100)
                )
                screen.blit(
                    text_surface,
                    (
                        WIDTH // 4 - text_surface.get_width() // 2,
                        HEIGHT - 50,
                    ),
                )
                _O0OOOO00OOOOOO0OOOOOO0O0OOO0OO0O000OOOOOO0O0OOO0OO0OO0O0OO0OOOOOOO0OOO = HEIGHT
                _O0OOOO00OOOOOO0OOOOOO0O0OOO0OO0O000OOOOOO0O0OOO0OO0OO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = [
                    "Congratulations! You won!",
                    "Credits:",
                    "Game developed by [Augustus R. Angelides]",
                    "Block Artwork by [Sam Cook]",
                    "Creature Artwork by [Finn]",
                    "Music by [Finn]",
                    "Sounds by [Augustus R. Angelides]",
                    "Software Developers: [Teo, Augustus R. Angelides]",
                    "Playtesters: [Augustus R. Angelides, Ada, Abe]",
                    "Music from #Uppbeat (free for Creators!):",
                    "https://uppbeat.io/t/michael-grubb/threshold",
                    "License code: AVGIIL4ZOS36UYVZ ",
                    "Music from #Uppbeat (free for Creators!):",
                    "https://uppbeat.io/t/kevin-macleod/cyborg-ninja",
                    "License code: CYD3DXMQBEOXDEAY",
                    "  ---JOSHUA CHIVERS---",
                    "Combat - body smack,",
                    "Combat - heavy hit,",
                    "Combat - heavy punch",
                    "  ----Michael Grubb----   ",
                    "[main menu] End Credits (We Stay Ready)",
                    "[end credits] Threshold",
                    " ---Kevin MacLeod---",
                    "[ingame] Cyborg Ninja",
                    "----AugustusAngelides----",
                    "_-playtester-_",
                    "_-developer-_",
                    "_-project admin-_",
                    "_-artist-_",
                    "_-animator-_",
                    "_-moderator-_",
                    "-_musician-_",
                    "-_security researcher-_",
                    "-----Fingall O'Callaghan-----",
                    "_-artist-_",
                    "_-animator-_",
                    "-_musician-_",
                    "------Matthew Rivera-----",
                    "_-playtester-_",
                    "_-developer-_",
                    "-----Samuel Cook----",
                    "_-artist-_",
                    "_-animator-_",
                    "  _____     ____      __    __     ____     ______      _____      _____     _____   __     __    _____   _____      ",
                    " / ____\   / __ \     ) )  ( (    (    )   (   __ \    / ___/     (  __ \   (_   _) (_ \   / _)  / ___/  (_   _)     ",
                    "( (___    / /  \ \   ( (    ) )   / /\ \    ) (__) )  ( (__        ) )_) )    | |     \ \_/ /   ( (__      | |       ",
                    " \___ \  ( (    ) )   ) )  ( (   ( (__) )  (    __/    ) __)      (  ___/     | |      \   /     ) __)     | |       ",
                    "     ) ) ( (  /\) )  ( (    ) )   )    (    ) \ \  _  ( (          ) )        | |      / _ \    ( (        | |   __  ",
                    " ___/ /   \ \_\ \/    ) \__/ (   /  /\  \  ( ( \ \_))  \ \___     ( (        _| |__  _/ / \ \_   \ \___  __| |___) ) ",
                    "/____/     \___\ \_   \______/  /__(  )__\  )_) \__/    \____\    /__\      /_____( (__/   \__)   \____\ \________/  ",
                    "                \__)                                                                                                 ",
                ]
                _O0OOOO00OOOOOO0OOOOOO0O0OOO0OO0O000OOOOOO0O0OOO0OO0OO0O0OO0OOOO00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(
                    r"Recources\Fonts\PixelifySans-Regular.ttf", 36
                )
                OO0OOOOOO0OO0OO000O0OOOO0O000OOO0O000OOOOO0OOOOO00OOOOOOOOO0O0OOO00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.SysFont("monospace", 20)
    
                while credits_y >= -len(credits_text) * 40 and won:
                    screen.fill(WHITE)
                    for i, text in enumerate(credits_text):
                        if i <= 42:
                            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = credits_font.render(text, True, RED)
                            screen.blit(
                                text_surface,
                                (
                                    WIDTH // 2 - text_surface.get_width() // 2,
                                    credits_y + i * 40,
                                ),
                            )
                        else:
                            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = asciiartfont.render(text, True, (100, 255, 100))
                            screen.blit(
                                text_surface,
                                (
                                    WIDTH // 2 - text_surface.get_width() // 2,
                                    credits_y + i * 40,
                                ),
                            )
                    pygame.display.flip()
                    credits_y -= 2
                    for event in pygame.event.get():
                        if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                            _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
                            OO0OOOO00OO000O0OOO0O0O0 = False
                            pygame.quit()
                            sys.exit()
                        if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN:
                            return None
                    pygame.time.delay(50)
                if not credits_y >= -len(credits_text) * 40:
                    return None
    
        # Quit Pygame
        pygame.quit()
        sys.exit()
    
    
    if __name__ == "__main__":
        start()    
        import SquarePixels.enemymanagement.enemy as enemy
    from random import randint as rand
    
    OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0O0OO0OOO00O0OOOO00000OOOOOOOOOO0OOO0O0O00OOOOO0OO0OO0OO0 = [(int, int)]
    _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OOOOOOOOO000OOOOOO0OOOOOO0O0OO0OO0 = []
    O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O00OOOOOO0O0OOO0OO = False
    OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0OOOO0OOO = int
    OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0O00OO000 = int
    
    
    class OO0O0OOOOOO0O0O00OOOOOO0O0O0OO00OOOO0OOOO0OO0OOOO0O0OO00OO0OOOOOOOO0O0O0OO0OOOOOO0OOOOOO0OOOOOO000OOOOOO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0O0OO0OOO00O0OOOO00000OOOOOOOOOO0OOO0O0O00OOOOO0OO0OO0OO0=[(int, int)], _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OOOOOOOOO000OOOOOO0OOOOOO0O0OO0OO0=[]) -> None:
            """
            Initializes an Enemy_manager object.
    
            Parameters:
            - active_chunks (list of tuples): List of active chunks represented as tuples of two integers.
            - creatures (list): List to store Enemy objects.
    
            Returns:
            None
            """
            self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0O0OO0OOO00O0OOOO00000OOOOOOOOOO0OOO0O0O00OOOOO0OO0OO0OO0 = active_chunks
            self._O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OOOOOOOOO000OOOOOO0OOOOOO0O0OO0OO0 = creatures
    
        def O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O0(self, air, objectinfo):
            """
            Spawns enemy creatures within active chunks.
    
            Parameters:
            - air (list): List of rectangles representing empty spaces.
            - objectinfo (object): Object with information about the game environment.
    
            Returns:
            None
            """
            for i in self.active_chunks:
                if len(self.creatures) <= rand(1, 2):
                    O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O00OOOOOO0O0OOO0OO = False
                    while not spawned:
                        OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0OOOO0OOO = rand(0, objectinfo.current_h)
                        OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0O00OO000 = rand(i[0], i[1])
                        if any(a.collidepoint(placex, placey) for a in air):
                            self.creatures.append(enemy.Enemy(placey, placex))
                            O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O00OOOOOO0O0OOO0OO = True
    
        def OOOOOOO0OOOOO0OOO0OOO0OOOO0OOOOOOOO0O0OO0OOOOOO0(self, x, y, air, objectinfo, colliders, screen, player, day):
            """
            Updates the state of the enemy manager.
    
            Parameters:
            - x (int): X-coordinate of the player character.
            - y (int): Y-coordinate of the player character.
            - air (list): List of rectangles representing empty spaces.
            - objectinfo (object): Object with information about the game environment.
            - colliders (list): List of collidable objects.
            - screen (object): Object representing the game screen.
            - player (object): Object representing the player character.
    
            Returns:
            None
            """
            if len(self.creatures) <= rand(1, 2):  # and O0OOO0OOOO0OOOOOOOOO0OOO == 1:
                self.spawn(air, objectinfo)
    
            # if O0OOO0OOOO0OOOOOOOOO0OOO == 0 and len(self.creatures) > 0:
            #    self.creatures.pop(rand(0, len(self.creatures)))
            for creature in self.creatures:
                creature.update(x, y, colliders, air, player, screen)    
                import pygame as pig
    
    import random
    
    import math
    from PIL import Image, ImageSequence
    
    
    def OOO000OO0OO000O0OO0OOOOOO0OOO0OOO0OO0OOOO0OOOOOO0O000OOOO00OOOOOO0OO0OOOOO0OOOOOOOO0O0O00O000OOOO0O0OO00OO0OOOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0(gif_path):
        """
        Loads a GIF animation 
        from a file and converts it into a list of Pygame surfaces.
    
        Parameters:
        - gif_path (str): The file path to the GIF image to be loaded.
    
        Returns:
        list: A list of Pygame surfaces, each representing a frame of the GIF animation.
    
        Note:
        - This function uses the Pillow library to load the GIF image.
        - The returned list contains Pygame surfaces representing each frame of the animation.
        - The first frame (static image) is removed 
        from the list, as GIFs typically start 
            from the second frame.
    
        Example:
        O00OOOOO00OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OO0 = load_gif_animation("example.gif")
        for frame_surface in frames:
            # Display or manipulate each frame_surface as needed
            # (e.g., blit it onto a Pygame display)
        """
        # Load the GIF image using Pillow
        O0OOOOOO0O000OOOO00OOOOOO0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = Image.open(gif_path)
    
        # Convert the GIF frames to pig surfaces
        O00OOOOO00OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OO0 = []
        for frame in ImageSequence.Iterator(gif_image):
            O00OOOOO00OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = pig.image.fromstring(frame.tobytes(), frame.size, frame.mode)
            frames.append(frame_surface)
        frames.pop(0)
        return frames
    
    
    class OO0O0OOOOOO0O0O00OOOOOO0O0O0OO00OOOO0OOO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(
            self,
            _OOOOOO0OOO0O0O00OOOOOO0O0O0OO00OOOO0OOOOOOO0OOO=random.randint(0, pig.display.get_window_size()[1]),
            _OOOOOO0OOO0O0O00OOOOOO0O0O0OO00OOOO0OOOO00OO000=random.randint(0, pig.display.get_window_size()[0]),
            _OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO=random.randint(3, 7),
            O0OOO0OO0OOOOOO0O00OOOOO0OOOOOO0OOO0O0O000O0OOOO0OOOOOO0=random.randint(1, 4),
            OOOOO0OOOO0OOOOOO0OO0OO0O0OO0OO00O000OOOO0O000OO0OOOOOO0=False,
            O0OOO0OOOO0OOOOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0OO0OOOOOO0O0OO000OO000O0OOOOOOO0OOO0O0O0OOO0O0OO=random.randint(2, 5),
            OO0OOOOOOOO0O0OOOOO0O0OOOO0OOOOO00O0OOOO0OOOOO0OO0OO0OO0OOO0O0OO00OOOOOO0OOOOOO0OOO0O0O0O0OOOOOOOOO0O0OO00000OOO=random.randint(2, 5),
        ):
            self._OOOOOO0OOO0O0O00OOOOOO0O0O0OO00OOOO0OOOOOOO0OOO = enemyy
            self._OOOOOO0OOO0O0O00OOOOOO0O0O0OO00OOOO0OOOO00OO000 = enemyx
            self._OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO = health
            self.O0OOO0OO0OOOOOO0O00OOOOO0OOOOOO0OOO0O0O000O0OOOO0OOOOOO0 = defence
            self.OOOOO0OOOO0OOOOOO0OO0OO0O0OO0OO00O000OOOO0O000OO0OOOOOO0 = passive
            self.OO0OOOOOOOO0O0OOOOO0O0OOOO0OOOOO00O0OOOO0OOOOO0OO0OO0OO0OOO0O0OO00OOOOOO0OOOOOO0OOO0O0O0O0OOOOOOOOO0O0OO00000OOO = attackstrength
            self.O0OOO0OOOO0OOOOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0OO0OOOOOO0O0OO000OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = damageamount
            self.O0OOO0OO0O000OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0 = False  # left
            self.O0OO0OO0OOOOO0OO0O000OOOOOO0O0OO = False
            self.OOO000OO0OOOOOO0O00OOOOOOOO0O0OO = load_gif_animation(
                r"Recources\creatures\enemies\Little Demon\wall climbing\Little demon(1)(1)(1).gif"
            )
            self._OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OO = load_gif_animation(
                r"Recources\creatures\enemies\Little Demon\wall climbing\Little demon(2)(1).gif"
            )
            self._OOOOOOO0OO0OO0OOOOO0OO0O000OOOOOO0O0OOOO0OOOOOOOO0O0OOOOO0O0OOOO0OOOOO00O0OOOO0OOOOO0O = load_gif_animation(
                r"Recources\creatures\enemies\Little Demon\attack\Little demon(1)(1).gif"
            )
            self.OOO000OOO0OO0OO0OOOOO0OO0O000OOOOOO0O0OOOO0OOOOOOOO0O0OOOOO0O0OOOO0OOOOO00O0OOOO0OOOOO0O = load_gif_animation(
                r"Recources\creatures\enemies\Little Demon\attack\Little demon(1).gif"
            )
    
        def _OOOOOO0OO000O0OOOOOOO0OOO0O0O0O0OOO0OOOOO0O0OO0OO000O0OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0O(self, x, OOOOOOOOOO0OOOOOO0OO0OO00OOOOOO0=15):
            """
            Rounds a number 'x' to the nearest multiple of 'base'.
    
            Parameters:
            - x (float): The number to be rounded.
            - base (float, optional): The multiple to which 'x' should be rounded. Default is 15 which is the block size in the world.
    
            Returns:
            float: The rounded value of 'x' to the nearest multiple of 'base'.
            """
            return base * round(x / base)
    
        def OOOOOOO0OOOOO0OOO0OOO0OOOO0OOOOOOOO0O0OO0OOOOOO0(self, x, y, colliders, sky, player, screen):
            """
            Controlls the enemy's behavior.
    
            This method handles the enemy's movement, checks if it's close enough to the player
            for an attack, calls the enemy's move function, and updates its appearance on the screen.
    
            Parameters:
                x (float): The x-coordinate of the player's current position.
                y (float): The y-coordinate of the player's current position.
                colliders (list): A list of collidable pygame.Rect objects in the game world.
                sky (object): A list of pygame.Rect objects which make up the empty space or air.
                player (object): The player object representing the player character.
                screen (object): The screen or canvas where the game is displayed.
    
            Returns:
                None
            """
            self.move(x, colliders, sky)
            # Calculate the distance from the player to the enemy
            O0OOO0OO0O000OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0O000O0OOOO0OOOOOO0 = math.sqrt((self.enemyx - x) ** 2 + (self.enemyy - y) ** 2)
            if distance <= 30:  # two blocks
                self.attack(player)
            self.draw(screen)
            self.O0OO0OO0OOOOO0OO0O000OOOOOO0O0OO = False
    
        def OO0OOOOOOOO0O0OOOOO0O0OOOO0OOOOO00O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO(self):
            pass
    
        def OO0OOOOOOOO0O0OOOOO0O0OOOO0OOOOO00O0OOOO0OOOOO0O(self, player):
            """
            Perform an attack on the specified player.
    
            This method causes the attacking entity to inflict a random amount of damage
            on the target player within the range of 3 to 7 (inclusive). After the attack,
            the 'spit' attribute of the attacker is set to True.
    
            Parameters:
            - player (Player): The player object to attack.
    
            Returns:
            None
            """
            player.get_damage(random.randint(3, 7))
            self.O0OO0OO0OOOOO0OO0O000OOOOOO0O0OO = True
    
        def O0O0OO000OO000O0O0O000OO0OOOOOO0(self, x, colliders, sky):
            """
            Move the enemy controlled by this object.
    
            Args:
                x (int): The target x-coordinate of the player.
                colliders (list): A list of pygame.Rect objects representing collidable blocks.
                sky (list): A list of pygame.Rect objects representing empty space or air.
    
            Notes:
                This function handles the movement of the enemy, considering collision
                with collidable blocks and adjusting the character's position accordingly.
                If the character is not passive, it will attempt to move towards (under construction)
    
            Returns:
                None
            """
            if not self.passive:
                if any(block.collidepoint(self.enemyx, self.enemyy) for block in colliders):
                    if not any(
                        block.collidepoint(
                            self.enemyx, (self.roundtoblock(self.enemyy) - 16)
                        )
                        for block in colliders
                    ):
                        self.enemyy -= 5
                        if self.enemyx <= x:
                            self.enemyx += 1
                            self.O0OOO0OO0O000OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0 = True
                        else:
                            self.O0OOO0OO0O000OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0 = False
                            self.enemyx -= 1
                    else:
                        self._OOOOOO0OOO0O0O00OOOOOO0O0O0OO00OOOO0OOOO00OO000 = self.roundtoblock(self.enemyx)
                        if self.enemyx <= x:
                            self.enemyx -= 1
                        else:
                            self.enemyx += 1
                if any(air.collidepoint(self.enemyx, self.enemyy + 3) for air in sky):
                    self.enemyy += 5
            else:
                # implement passive logic
                pass
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen: pig.display):
            """__Draws enemy animation to the screen__
    
            Args:
                screen (_pig.display_): _a pygame screen object_
            """
            if self.direction:
                if len(self.right) != 0:
                    if not self.spit:
                        screen.blit(
                            pig.transform.scale(self.right[0], (65, 30)),
                            (self.enemyx, self.enemyy - 15, 25, 25),
                        )
                        self.right.pop(0)
    
                else:
                    self._OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OO = load_gif_animation(
                        r"Recources\creatures\enemies\Little Demon\wall climbing\Little demon(2)(1).gif"
                    )
                    if not self.spit:
                        screen.blit(
                            pig.transform.scale(self.right[0], (65, 30)),
                            (self.enemyx, self.enemyy - 15, 25, 25),
                        )
                        self.right.pop(0)
                if self.spit:
                    if len(self.rspitattack) != 0:
                        screen.blit(
                            pig.transform.scale(self.rspitattack[0], (100, 100)),
                            (self.enemyx, self.enemyy - 15, 25, 25),
                        )
                        self.rspitattack.pop(0)
                    else:
                        self._OOOOOOO0OO0OO0OOOOO0OO0O000OOOOOO0O0OOOO0OOOOOOOO0O0OOOOO0O0OOOO0OOOOO00O0OOOO0OOOOO0O = load_gif_animation(
                            r"Recources\creatures\enemies\Little Demon\attack\Little demon(1)(1).gif"
                        )
                        screen.blit(
                            pig.transform.scale(self.rspitattack[0], (100, 100)),
                            (self.enemyx, self.enemyy - 15, 25, 25),
                        )
                        self.rspitattack.pop(0)
            else:
                if len(self.left) != 0:
                    if not self.spit:
                        screen.blit(
                            pig.transform.scale(self.left[0], (65, 30)),
                            (self.enemyx, self.enemyy - 15, 25, 25),
                        )
                        self.left.pop(0)
    
                else:
                    self.OOO000OO0OOOOOO0O00OOOOOOOO0O0OO = load_gif_animation(
                        r"Recources\creatures\enemies\Little Demon\wall climbing\Little demon(1)(1)(1).gif"
                    )
                    if not self.spit:
                        screen.blit(
                            pig.transform.scale(self.left[0], (65, 30)),
                            (self.enemyx, self.enemyy - 15, 25, 25),
                        )
                        self.left.pop(0)
    
                if self.spit:
                    if len(self.lspitattack) != 0:
                        screen.blit(
                            pig.transform.scale(self.lspitattack[0], (100, 80)),
                            (self.enemyx, self.enemyy - 15, 25, 25),
                        )
                        self.lspitattack.pop(0)
                    else:
                        self.OOO000OOO0OO0OO0OOOOO0OO0O000OOOOOO0O0OOOO0OOOOOOOO0O0OOOOO0O0OOOO0OOOOO00O0OOOO0OOOOO0O = load_gif_animation(
                            r"Recources\creatures\enemies\Little Demon\attack\Little demon(1).gif"
                        )
                        screen.blit(
                            pig.transform.scale(self.lspitattack[0], (100, 80)),
                            (self.enemyx, self.enemyy - 15, 25, 25),
                        )
                        self.lspitattack.pop(0)    
                        import SquarePixels.render.render as render
    
    import pygame as pig
    
    import SquarePixels.enemymanagement.enemy_manager as enemy_manager
    from SquarePixels.uimanagement import death, MainMen
    
    import SquarePixels.soundmanagement.music as music
    
    import random
    
    
    def O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0(
        screen,
        running,
        terrain_gen,
        player,
        infoObject,
        player_sprite,
        clock,
        vx,
        vy,
        reset_terrain,
        Morning,
        DayTime,
        tile,
    ):
        music.play_music(r"Recources\sounds\music\ingame\music\Ingame1.mp3", O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=0.2)
        _OOOOOO0OOO0O0O00OOOOOO0O0O0OO00OOOO0OOOO0O0OO00OO0OOOOOOOO0O0O0OO0OOOOOO0OOOOOO0OOOOOO000OOOOOO = enemy_manager.Enemy_manager([(0, infoObject.current_w)])
        while running:
            _O0OOOOOOO000OO0O000OOO00O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO = False
            if reset_terrain:
                terrain_gen.run(screen)
            # pig.draw.rect(screen,(.100,.100,.100,50),rect)
            screen.fill((0.035, 206, 235))
    
            if OOOO00OO0OO000O000OOOOOOOOO0O0O00O000OOOOOO0O0O0O0OOOOOO == 0:
                _OOOOO00OO0OOOOOOOOO0OOO00OO0OO00O000OOOO0O0OO000OOOOOO0 = DayTime + 0.005
            else:
                _OOOOO00OO0OOOOOOOOO0OOO00OO0OO00O000OOOO0O0OO000OOOOOO0 = DayTime - 0.005
                if DayTime <= 0:
                    OOOO00OO0OO000O000OOOOOOOOO0O0O00O000OOOOOO0O0O0O0OOOOOO = 0
            sky, _O0OOOO0OO000O0OOO000OOOOO000OO0O000OOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0 = render.render_terrain(
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
                OOOO00OO0OO000O000OOOOOOOOO0O0O00O000OOOOOO0O0O0O0OOOOOO = 1
            _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = player.move(screen, infoObject, tile, terrain_gen.terrain)
            if result != None:
                if len(result) <= 5:
                    _OOOOOO0OOOOOO0O0OO0OO00OOOOOO0OOO0O0OOO0OO0OOOOOO0O0OO0OOOOOO000OOOOOO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0 = result[0]
                    _O0OOOOOOO000OO0O000OOO00O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO = result[1]
                    try:
                        _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO00000OOO0OOOOOO0OOO000OOO0OOO0OO = result[2]
                    except:
                        pass
                else:
                    terrain_gen.OOO0O0OO0OOOOOO000OOOOOO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0 = result
            OOO0O0OO0O000OOOOOO000OO0OOOOOO0 = [-1, 0]
            if clicked:
                if random.randint(0, 1) == 1:
                    music.play_music(
                        r"Recources\sounds\block break\block break.mp3",
                        0,
                        _O0OOOO00000OOOOO0OOOOOOOO0O0O0OOO0O0O00OOOOOO0OOO000OO=1,
                        O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=5,
                    )
                else:
                    music.play_music(
                        r"Recources\sounds\block break\blockbreak1.mp3",
                        0,
                        _O0OOOO00000OOOOO0OOOOOOOO0O0O0OOO0O0O00OOOOOO0OOO000OO=1,
                        O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=5,
                    )
                OOO0O0OO0O000OOOOOO000OO0OOOOOO0 = player.delete_tile(terrain_gen.terrain, tile)
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
            #print(player.xp)
            # player.draw_trail(screen)
            pig.display.flip()
            clock.tick(60)    
            import pygame
    
    import socket
    
    import pickle
    
    import SquarePixels.player.player as play
    
    # import playerdatc
    
    import typing as typi
    
    import pickle
    
    import SquarePixels.render.render as render
    
    
    def O0O0OO00OO0OOOOO0O000OOOOOO0O0O0(ip, name):
        # Initialize the game
        pygame.init()
    
        # Set up the game window
        o_p_c: OOO000OO0O000OOOO0OO0OO0OOO0O0OO = []
        screen_width: _O000OOOOOO0O0O0OOO0O0OO = 800
        screen_height: _O000OOOOOO0O0O0OOO0O0OO = 600
        screen: pygame.OOOOOOO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Multiplayer Platform Game - Client")
    
        # Information
        print(
            "press p to toggle paint mode on and off, press g to toggle gravity on and off, press i to toggle inverted trail, press r to toggle rainbow trail, move with arrows, hit enter to send start typing message hit enter again to send."
        )
        paint: OOOOOOOO0OO000O00OO000O0OOO000OO = False
        typing: OOOOOOOO0OO000O00OO000O0OOO000OO = False
        gravity: OOOOOOOO0OO000O00OO000O0OOO000OO = True
        dotr: OOOOOOOO0OO000O00OO000O0OOO000OO = True
        points: typi.List[typi.Union[str, int, bool]] = ["", 0, True]
        ai: OOOOOOOO0OO000O00OO000O0OOO000OO = False
    
        # Define AI player class
        class OOOOO0OOOO0O0O0OOOO0OOOOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOO:
            def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x: int, y: int):
                self.x: _O000OOOOOO0O0O0OOO0O0OO = x
                self.y: _O000OOOOOO0O0O0OOO0O0OO = y
                self.speed: _O000OOOOOO0O0O0OOO0O0OO = 1
    
            def OOOOOOO0OOOOO0OOO0OOO0OOOO0OOOOOOOO0O0OO0OOOOOO0(self, dot_x: int, dot_y: int) -> None:
                if self.x < dot_x:
                    self.x += self.speed
                elif self.x > dot_x:
                    self.x -= self.speed
    
                if self.y < dot_y:
                    self.y += self.speed
                elif self.y > dot_y:
                    self.y -= self.speed
    
        # Set up the client socket
        client_socket: socket.O0OO0OO00OO000O000O0OOOO0OOOOO0O0OOOOOO0OOO0O0OO = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((ip, 12345))
        except:
            print("error connecting to device.")
            print(socket.error)
    
        # Prompt the player to enter their name
        # name: O0OO0OO0OOO0O0OO00OOOOOO = input("Enter your name: ")
        points[0] = name
    
        player: play.Player(0, 0)
        aiplayer: OOOOO0OOOO0O0O0OOOO0OOOOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOO = AIPlayer(0, 0)
        # Initialize the input box and chat that player has connected
        client_socket.sendall(pickle.dumps(f"{name} has joined this server"))
        input_box: O0OO0OO0OOO0O0OO00OOOOOO = ""
        clock: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.time.Clock()
        FPS: _O000OOOOOO0O0O0OOO0O0OO = 120
        # Game loop
        running: OOOOOOOO0OO000O00OO000O0OOO000OO = True
        while running:
            clock.tick(FPS)
            # Handle events
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN:
                    if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_UP and player.OOOO0OOO == screen_height - 20:
                        player.velocity_y -= 1
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_LEFT:
                        player.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOO00OO000 = -player.speed
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_RIGHT:
                        player.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOO00OO000 = player.speed
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_RETURN and OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO == False:
                        OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO = True
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_RETURN and len(input_box) > 0 and typing:
                        O0OO0OO00OOOOOO0OOO0O0O0O0OOO0OOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0 = player.name + ": " + input_box
                        client_socket.sendall(pickle.dumps(sendmessage))
                        _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOOOOOOO0OO000O0O00OO000 = ""
                        OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO = False
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_BACKSPACE:
                        _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOOOOOOO0OO000O0O00OO000 = input_box[:-1]
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_p and OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO == False:
                        if OOOOO0OOOO0OOOOO0O000OOOOOO0O0O0OOO0O0OO == False:
                            OOOOO0OOOO0OOOOO0O000OOOOOO0O0O0OOO0O0OO = True
                        else:
                            OOOOO0OOOO0OOOOO0O000OOOOOO0O0O0OOO0O0OO = False
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_g and OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO == False:
                        if O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO == False:
                            O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO = True
                            player.O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO0O000OOO = gravity
                        else:
                            O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO = False
                            player.O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO0O000OOO = gravity
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_i and OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO == False:
                        if player._O000OOOOOO0O0O0O0O000OO0OOOOOO000OOOOOOO0OO0OO00OOOOOO0 == False:
                            player._O000OOOOOO0O0O0O0O000OO0OOOOOO000OOOOOOO0OO0OO00OOOOOO0 = True
                        else:
                            player._O000OOOOOO0O0O0O0O000OO0OOOOOO000OOOOOOO0OO0OO00OOOOOO0 = False
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_r and OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO == False:
                        if player._OOOOOOOO0OOOOO0O000OOOOOO0O0O0OOOOOOOO0OO000O0OO0OOOO0 == False:
                            player._OOOOOOOO0OOOOO0O000OOOOOO0O0O0OOOOOOOO0OO000O0OO0OOOO0 = True
                        else:
                            player._OOOOOOOO0OOOOO0O000OOOOOO0O0O0OOOOOOOO0OO000O0OO0OOOO0 = False
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_0 and OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO == False:
                        if OO0OOOOO0O000OOO == False:
                            print("AI activated")
                            OO0OOOOO0O000OOO = True
                        else:
                            print("AI deactivated")
                            OO0OOOOO0O000OOO = False
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_g and typing:
                        input_box += "g"
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_p and typing:
                        input_box += "p"
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_i and OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO == True:
                        input_box += "i"
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_r and OOO0O0OOOOOO0OOOOOOOO0OO0O000OOOOOO0O0O0O0OOOOOO == True:
                        input_box += "r"
                    elif event.key <= 127 and typing:
                        input_box += chr(event.key)
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYUP:
                    if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_LEFT:
                        player.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOO00OO000 = -0.9
                    if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_RIGHT:
                        player.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOO00OO000 = 0.9
    
            # Update AI player if AI flag is True
            if ai:
                aiplayer.update(circle_x, circle_y)
    
            # Update player location
            player.update(screen_height, screen_width)
    
            # Send player data to the server
            client_socket.sendall(pickle.dumps(player))
    
            # Receive and update the game state from the server
            O0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = client_socket.recv(4096)
            O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0OO0OOOOOO0 = pickle.loads(data)
            OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OO0 = game_state["players"]
            _O0OOOO00000OOOOO0OOOOOOOO0O0OOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0O0OO0OO0 = game_state["chat_messages"]
            _O0OOOO0O000OOO00OOOOOO00O0OOOOOOO000OO0OOOOOO0O0OO0OOOO00OO000 = game_state["circle_x"]
            _O0OOOO0O000OOO00OOOOOO00O0OOOOOOO000OO0OOOOOO0O0OO0OOOOOOO0OOO = game_state["circle_y"]
            OO0OOOOOOOO000OOOOO000OOOOOOO0OO0OO000O00O000OOOOOO0O0O0OOO0O0OOO0OO0OO0 = game_state["points"]
    
            # Render the game state
            if not paint:
                screen.fill((0, 0, 0))
    
            # render trail
            player.draw_trail(screen)
    
            _OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect((circle_x, circle_y), (5, 5))
            OOOOO0OO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect((player.x, player.y), (10, 10))
    
            # f#or otherplayer in players:
            #    o_p_c.append(pygame.Rect(otherplayer.x,otherplayer.y))
            _O0OOOO0OO000O0OOO000OOOOO000OO0O000OOOO0OOO0OO0OOOOOO0 = rect.colliderect(prect)
            pygame.draw.circle(screen, (255, 255, 255), (circle_x, circle_y), 5)
            if collide:
                O0OOO0OO0OO000O0OOO0O0OO00OOOOOO = True
                points[2] = dotr
                points[1] += 1
                client_socket.sendall(pickle.dumps(points))  # .encode())
                O0OOO0OO0OO000O0OOO0O0OO00OOOOOO = False
    
            for other_player in players:
                if other_player.name != player.name:
                    pygame.draw.circle(
                        screen, (255, 0, 0), (other_player.x, other_player.y), 10
                    )
                    OOO0O0O0OO0OOOOOO0O0OO000OOOOOO0OOO0O0OOOO0OOOOOO0OOOOOO = render.Nametag(other_player)
                    nametag.draw(screen)
            pygame.draw.circle(screen, (0, 0, 255), (player.x, player.y), 10)
            OOO0O0O0OO0OOOOOO0O0OO000OOOOOO0OOO0O0OOOO0OOOOOO0OOOOOO = render.Nametag(player)
            nametag.draw(screen)
    
            render.render_chat(chat_messages, screen_height, screen)
            render.render_scores(allpoints, screen)
    
            # Render the input box
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 20)
            _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOOOOOOO0OO000O0O00OO000O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(
                "Enter message: " + input_box, True, (255, 255, 255)
            )
            _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOOOOOOO0OO000O0O00OO000O0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = input_box_text.get_rect(OOO000OO0OOOOOO0O00OOOOOOOO0O0OO=10, OOO0O0OO0OO000O0OOOOO0OO=screen_height - 30)
            screen.blit(input_box_text, input_box_rect)
    
            pygame.display.flip()
    
        # Clean up
        pygame.quit()
    
    
    if __name__ == "__main__":
        main()    
        import pygame
    
    import random
    
    # Initialize Pygame
    pygame.init()
    
    # Set up the screen
    screen_width, O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0O0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 800, 600
    O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bouncing Balls Animation")
    
    # Define colors
    OOOO00OO000O00OOOO0O0O0O00OO0OO0OO0O0OOO = (255, 255, 255)
    
    
    # Define Ball class
    class _O00OOOOOO0OOOOOOOO000OOOOO000OO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x, y, radius):
            self._OOOOOOOO0OOOOOO0OOO0OO0O000OOOOOOOOOO0O0OO0OO0 = radius
            self._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.O0OOO0OOO00OO000 = random.choice([-1, 1]) * random.randint(1, 3)
            self.O0OOO0OOOOOO0OOO = random.choice([-1, 1]) * random.randint(1, 3)
    
        def OOOOOOO0OOOOO0OOO0OOO0OOOO0OOOOOOOO0O0OO0OOOOOO0(self):
            self.x += self.dx
            self.y += self.dy
    
            # Check for collisions with the screen edges
            if self.x - self.radius < 0 or self.x + self.radius > screen_width:
                self.dx *= -1
            if self.y - self.radius < 0 or self.y + self.radius > screen_height:
                self.dy *= -1
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
        def _OOOOOO0OO0OOOOOOOO0O0OO(self, other_ball):
            if self.radius > other_ball.radius:
                self.radius += int(other_ball.radius * 0.2)  # Increase radius
                other_ball.reset()  # Reset the smaller ball
    
        def _OOOOOO0OOOOOO0O0OO0OO00OOOOOO0OOO0O0OO(self):
            self.O00OO000 = random.randint(self.radius, screen_width - self.radius)
            self.OOOO0OOO = random.randint(self.radius, screen_height - self.radius)
            self._OOOOOOOO0OOOOOO0OOO0OO0O000OOOOOOOOOO0O0OO0OO0 = random.randint(10, 30)
            self._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            self.O0OOO0OOO00OO000 = random.choice([-1, 1]) * random.randint(1, 3)
            self.O0OOO0OOOOOO0OOO = random.choice([-1, 1]) * random.randint(1, 3)
    
    
    # Create a list to store the balls
    OOOOOOOOOO0OOOOOOOO000OOOOO000OOO0OO0OO0 = []
    
    # Create some initial balls
    for _ in range(10):
        O00OO000 = random.randint(30, screen_width - 30)
        OOOO0OOO = random.randint(30, screen_height - 30)
        _OOOOOOOO0OOOOOO0OOO0OO0O000OOOOOOOOOO0O0OO0OO0 = random.randint(10, 30)
        OOOOOOOOOO0OOOOOOOO000OOOOO000OO = Ball(x, y, radius)
        balls.append(ball)
    
    # Game loop
    _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
    _O0OOOOOOO000OO0OO000O000O0OOOO0OOOOO0O = pygame.time.Clock()
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
    
        # Clear the screen
        screen.fill(WHITE)
    
        # Update and draw the balls
        for ball in balls:
            ball.update()
            ball.draw()
    
        # Check for collisions between balls
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                O0OOO0OOO00OO000 = balls[i].x - balls[j].x
                O0OOO0OOOOOO0OOO = balls[i].y - balls[j].y
                O0OOO0OO0O000OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0O000O0OOOO0OOOOOO0 = ((dx**2) + (dy**2)) ** 0.5
    
                if distance < balls[i].radius + balls[j].radius:
                    if balls[i].radius > balls[j].radius:
                        balls[i].eat(balls[j])
                    else:
                        balls[j].eat(balls[i])
    
        # Remove balls that are too big
        OOOOOOOOOO0OOOOOOOO000OOOOO000OOO0OO0OO0 = [ball for ball in balls if ball.radius < 500]
    
        # Spawn new balls
        while len(balls) < 10:
            O00OO000 = random.randint(30, screen_width - 30)
            OOOO0OOO = random.randint(30, screen_height - 30)
            _OOOOOOOO0OOOOOO0OOO0OO0O000OOOOOOOOOO0O0OO0OO0 = random.randint(10, 30)
            OOOOOOOOOO0OOOOOOOO000OOOOO000OO = Ball(x, y, radius)
            balls.append(ball)
    
        # Update the display
        pygame.display.flip()
    
        # Limit the frame rate
        clock.tick(60)
    
    # Quit the program
    pygame.quit()    
    import pygame as pig
    
    import typing
    
    import colorsys
    
    import math
    
    import random
    from SquarePixels.uimanagement.inventory import Item
    from SquarePixels.uimanagement.inventory import player_inventory
    from SquarePixels.uimanagement.inventory import item_bar
    from SquarePixels.uimanagement.inventory import crafting_grid
    
    import SquarePixels.soundmanagement.music as music
    
    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = None
    _O000OOOOOO0O0O0O0O000OO0OOOOOO0OOO0O0O0 = False
    _OOO0OO000O0OOO000OOO0OOO0OO0OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = [Item, 999999999999999999]
    OOOOOOO0OOO0O0O0OO0OOOOOOOO0O0OOOOOOOOO000OOOOOOOO0OOOOOOOO000OOOOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OO0OO0OO0 = []
    
    
    class OOO0OOOOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOO:
        """
        Represents the player character in the game.
        """
    
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x, y, health_bar_length, xp):
            """
            Initializes the Player object.
    
            Parameters:
            - x (int): The initial x-coordinate of the player.
            - y (int): The initial y-coordinate of the player.
            - health_bar_length (int): The length of the health bar displayed on the screen.
            """
            # Initialize player attributes
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.O00OO000OOOOO0OO = xp
            self.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = 5
            self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 5
            self.O0OOOO0OOOOOOOO0O0O0OO00OOOOO0OO = False
            self.OOOOOOOOOO0OOOOOO0OO0OO000000OOOO0OO0OOOOOOOO0OO0OO000O0OO0OOOO00OOOOOO000OOOOOO = 3
            self.OOOOOOOOOO0OOOOOO0OO0OO000000OOOO0OO0OOO00O0OOOO0OO000O00OO000O0OOO000OOO0OOO0OO0OO000O0OO0OOOO0OOO0O0O0 = 0
            self.OO0OOOOO0O000OOOO0O0OO000O000OOOOOO0O0O0O0OOOOOO = False
            self.OO0OOOOO00OOOOOO00OOOOOO0OO000O0OO0OOOO0O0OO0OOOOOOOO0OO0OO000O0O0OO0OO0 = pig.mouse.get_pos()
            self.OO0OOOOO00OOOOOO00OOOOOO0OO000O0OO0OOOO0O0OO0OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOOOO0OO0OO000O0O0OO0OO0 = pig.mouse.get_pos()
            self.O0OO0OO0OOOOO0OO0OOOOOO00OOOOOO0O0OOO0OO = 3
            self.O0OOO0OO0O000OOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO = False
            self.O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO0O000OOO = True
            self.O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO = 0.2
            self.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOO00OO000 = 0
            self.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOOOOO0OOO = 0
            self.OOO0O0OO00OOOOOOOO0OOOOO0O000OOOOOO000OO = []
            self._O000OOOOOO0O0O0O0O000OO0OOOOOO000OOOOOOO0OO0OO00OOOOOO0 = False
            self._OOOOOOOO0OOOOO0O000OOOOOO0O0O0OOOOOOOO0OO000O0OO0OOOO0 = True
            self.OOOOO0OOOOO000OOOO0OOOOOOOO0O0OOO00OOOOO0OO000O000OOOOOOO0O0OO00 = False
            self._O0OOOOOOO000OO0O000OOO00O0OOOO0OOOOO0O = (0, 0)
            self.OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0 = (0, 0)
            self._O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOO00000OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO = 200
            self.OOO0O0OOOO0OOOOO00OOOOOOO0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOO00000OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO = 500
            self.O0O0OO00OO0OOOOOO00OO000O0OO0OOO00000OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO = 1000
            self._OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOOO0OO0OOOOOOOOOOOOO0OOOOO00OOOOOOO0OO0OOOOOO000OO0OOOOOO0OOO0O0O0O0OOOOOOOOO0O0OO00000OOO = health_bar_length
            self._OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOOO0OO0OOO00OOOOOOOO0OOOOOOOO0O0OO0O000OOO0OO000O0 = self.max_health / self.health_bar_length
            self._OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOOO0OO0OOO00O0OOOO00000OOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0O0OO0OOOO0OO0OO0OOOOO0OO0OOOOOO00OOOOOO0O0OOO0OO = 5
    
        def _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O0(self, sky, infoObject, OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0O0OO0OOO00O0OOOO00000OOOOOOOOOO0OOO0O0O00OOOOO0OO0OO0OO0=[(int, int)]):
            """
            Respawns the player character on the screen.
    
            Parameters:
            - sky (list): A list of sky objects.
            - infoObject: Pygame display information object.
            - active_chunks (list of tuples): List of active chunks.
    
            Returns:
            None
            """
            # Reset player inventory
            player_inventory._O000OOOOOO0O0OO0OOOOOO0O0O0OO00O0OO0OO0 = [
                [None for _ in range(player_inventory.rows)]
                for _ in range(player_inventory.col)
            ]
            # Reset player health and find a respawn location
            self._O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOO00000OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO = 200
            self.OOO0O0OOOO0OOOOO00OOOOOOO0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOO00000OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO = 500
            self.O00OO000OOOOO0OO = 0
            _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O00OOOOOO0O0OOO0OO = False
            for i in active_chunks:
                while not respawned:
                    OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0OOOO0OOO = random.randint(0, infoObject.current_h)
                    OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0O00OO000 = random.randint(i[0], i[1])
                    if any(a.collidepoint(placex, placey) for a in sky):
                        _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O00OOOOOO0O0OOO0OO = True
                        self.O00OO000 = placex
                        self.OOOO0OOO = placey
                        return None
    
        def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOOO0OOO0OOOO0OOOOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0(self, amount):
            """
            Apply damage to the player character.
    
            Parameters:
            - amount (int): The amount of damage to apply.
    
            Returns:
            None
            """
            if self.target_health > 0:
                self.target_health -= amount
                if not pig.mixer.Channel(4).get_busy():
                    music.play_music(
                        r"Recources\sounds\player\take damage.mp3",
                        0,
                        _O0OOOO00000OOOOO0OOOOOOOO0O0O0OOO0O0O00OOOOOO0OOO000OO=4,
                        O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=4,
                    )
            if self.target_health < 0:
                self.OOO0O0OOOO0OOOOO00OOOOOOO0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOO00000OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO = 0
                if not pig.mixer.Channel(4).get_busy():
                    music.play_music(
                        r"Recources\sounds\player\death.mp3",
                        0,
                        _O0OOOO00000OOOOO0OOOOOOOO0O0O0OOO0O0O00OOOOOO0OOO000OO=4,
                        O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=1,
                    )
    
        def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOO00000OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO(self, amount):
            """
            Increase the player character's health.
    
            Parameters:
            - amount (int): The amount of health to add.
    
            Returns:
            None
            """
            if self.target_health < self.max_health:
                self.target_health += amount
            if self.target_health > self.max_health:
                self.OOO0O0OOOO0OOOOO00OOOOOOO0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOO00000OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO = self.max_health
    
        def OO0OOOOOO0OOO0OOO0O000OOOO0OOOOOOOO0O0O000O0OOOO0OOOOOO0O0OOO0OOO0OO0OOO00000OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOO(self, screen):
            """
            Display the player's health on the screen.
    
            Parameters:
            - screen: Pygame display surface.
    
            Returns:
            None
            """
            # Display health bar and transition color
            screen.blit(
                pig.transform.scale(
                    pig.image.load(r"Recources\ui\icons\healthbar\health.png"),
                    (
                        25,
                        25,
                    ),
                ),
                pig.Rect(3, 45, 10, 10),
            )
            OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO00O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = 0
            OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO00O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOO00O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (255, 0, 0)
            if self.current_health < self.target_health:
                self.current_health += self.health_change_speed
                OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO00O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = int(
                    (self.target_health - self.current_health) / self.health_ratio
                )
                OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO00O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOO00O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (0, 255, 0)
            if self.current_health > self.target_health:
                self.current_health -= self.health_change_speed
                OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO00O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = int(
                    (self.target_health - self.current_health) / self.health_ratio
                )
                OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO00O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOO00O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (255, 255, 0)
            _OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOOO0OO0OOOOOOOOOOOOO0OOOOO00OOOOOOO0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = int(self.current_health / self.health_ratio)
            _OOO0OOOOOO0OO0OOOOOOOO000OOOOO0O0OO00000OOOO0OO0OOOOOOOOOOOOO0OOOOO00OOOOOO = pig.Rect(30, 45, health_bar_width, 25)
            OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO00O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOOOOOOOOOOOO0OOOOO00OOOOOO = pig.Rect(health_bar.right, 45, transition_width, 25)
    
            pig.draw.rect(screen, (255, 0, 0), health_bar)
            pig.draw.rect(screen, transition_color, transition_bar)
            pig.draw.rect(screen, (255, 255, 255), (30, 45, self.health_bar_length, 25), 4)
    
        def _O000OOOO0OO0OO0O0OO0OOO00O0OOOO0OO000O0OOO000OOOOO000OO0O000OOOO0OOO0OO0O000OOOOOO0O0O0O0OOOOOO(self, collider) -> typing.Tuple[str, bool]:
            """
            Check if the player is colliding with a given collider.
    
            Parameters:
            - collider: The object to check for collision.
    
            Returns:
            Tuple[str, bool]: A tuple containing a collision description and a boolean indicating if there is a collision.
            """
            if self.x < collider.x + collider.width and self.x + self.width > collider.x:
                return ("x_axis_collision", True)
            if self.y < collider.y + collider.height and self.y + self.height > collider.y:
                return ("y_axis_collision", True)
    
        def OOOOOOOOOO0OOOOOO0OO0OO000000OOO(self, collider, screen):
            """
            Perform a bash ability on a collider.
    
            Parameters:
            - collider: The object to perform the bash on.
            - screen: Pygame display surface.
    
            Returns:
            None
            """
            if self.bash_power > 0 and self.OOOOOOOOOO0OOOOOO0OO0OO000000OOOO0OO0OOO00O0OOOO0OO000O00OO000O0OOO000OOO0OOO0OO0OO000O0OO0OOOO0OOO0O0O0 == 0:
                self.bash_power -= 1
                self.OOOOOOOOOO0OOOOOO0OO0OO000000OOOO0OO0OOO00O0OOOO0OO000O00OO000O0OOO000OOO0OOO0OO0OO000O0OO0OOOO0OOO0O0O0 = 60  # Cooldown for 60 frames (1 second)
                self.fire(collider, screen)
    
        def O0OOO0OO0O000OOOO0OOOOOO(self, collider, colliders: list):
            """
            Perform dig ability actions on a collider.
    
            Parameters:
            - collider: The object to perform the dig ability on.
            - colliders (list): List of colliders in the game.
    
            Returns:
            None
            """
            # Perform dig ability actions here
            # ...
    
            # Remove the collider from the list
            colliders.remove(collider)
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen, character):
            """
            Draw the player character on the screen.
    
            Parameters:
            - screen: Pygame display surface.
            - character (str): The path to the character image to be drawn.
    
            Returns:
            None
            """
            _O0OOOO00000OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pig.Rect(self.x, self.y, self.width, self.height)
            _O0OOOO0O000OOOO0O0OO00 = pig.image.load(character)
            # O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0 = (float("."+f"{self.width}"), float("."+f"{self.height}"))
            O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0 = (540, 400)
            _O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = pig.transform.scale(cim, scale)
            # add custom character collisions here
            image.get_rect()
            screen.blit(image, (self.x - 100, self.y - 150))
            if self.aiming:
                pig.draw.line(screen, (0, 255, 0), self.arrow_pos, self.arrow_end_pos, 2)
    
        def O00OOOOO0O000OOO00OOOOOO0OOOOOO0(self, collider, screen):
            """
            Fire an arrow 
            from the player character.
    
            Parameters:
            - collider: The object to fire at.
            - screen: Pygame display surface.
    
            Returns:
            None
            """
            O0OOO0OO0O000OOO00OOOOOOO0OO0OOOO0O000OO0OOOOOO000O0OOOOOOO0O0OO0OO000O000OOOOOO = (
                self.arrow_end_pos[0] - self.arrow_pos[0],
                self.arrow_end_pos[1] - self.arrow_pos[1],
            )
            O0O0OO00OO0OOOOOO0OOOOOOOOO0O0O00O000OOOOOO0O0OOOOOOOOO0O0OOO0OO0OOOOOO0 = math.sqrt(dir_vector[0] ** 2 + dir_vector[1] ** 2)
            if magnitude != 0:
                OOO0O0O00OO000O000OOOOOOO0O0OO00OO0OOOOOOOO000OO0O000OOO0OOOOOOO0OOOOOO0O0OOO0OOO0OO0OOOO0O000OO0OOOOOO000O0OOOOOOO0O0OO0OO000O000OOOOOO = (dir_vector[0] / magnitude, dir_vector[1] / magnitude)
                O0OO0OO0OOOOO0OO0OOOOOO00OOOOOO0O0OOO0OO = 10
                O0OOO0OOO00OO000 = normalized_vector[0] * speed
                O0OOO0OOOOOO0OOO = normalized_vector[1] * speed
    
        def O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOO0OOO0OO0O000OOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO(self):
            """
            Start the digging action.
    
            Returns:
            None
            """
            self.O0OOO0OO0O000OOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO = True
    
        def O0OO0OO0OOO0O0OO0OO000O0OOOOO0OOO0OO0OOOO0OOO0OO0O000OOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO(self):
            """
            Stop the digging action.
    
            Returns:
            None
            """
            self.O0OOO0OO0O000OOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO = False
    
        def O0O0OO000OO000O0O0O000OO0OOOOOO0(self, screen, infoObject, tile, terrain):
            """
            Move the player character and handle user inputs.
    
            Parameters:
            - screen: Pygame display surface.
            - infoObject: Pygame display information object.
            - tile: The current tile the player is interacting with.
            - terrain: The terrain map of the game.
    
            Returns:
            Tuple[bool, bool, object]: A tuple containing game state information and the current held object.
            """
            global selected, inven, holdobject
            mousex, O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0OOOO0OOO = pig.mouse.get_pos()
            OOOO00OOOO0OOOOO0O000OOOOOO0O0O0O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pig.font.Font(pig.font.match_font("Impact"), 300)
    
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pig.font.Font(pig.font.match_font("calibri"), 26)
            item_bar.draw(OOOO0OOO00O0OOOO00000OOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0=(False, 0))
            if selected:
                self.render_selection(screen, mousex, mousey, font)
            OOO000OO0OO000O00OO000O00OOOOO0O0O000OOOOOO0O0O0O0OOOOOO = False
            if tile != [-1, 0]:
                self.get_item(tile)
    
            for event in pig.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.QUIT:
                    quit()
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.MOUSEBUTTONDOWN:
                    OOO0O0OOO0O0OO00OOOOO0OO = self.handle_item_bar(event, terrain, holdobject)
                    if tmp != None:
                        return tmp
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.KEYDOWN:
                    if event._OOOOO0O0OOOOOO0OOOO0OOO == pig.K_UP or event._OOOOO0O0OOOOOO0OOOO0OOO == pig.K_SPACE:
                        self.player_jump
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pig.K_LEFT or event._OOOOO0O0OOOOOO0OOOO0OOO == ord("a"):
                        self.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOO00OO000 = -self.speed
                        music.play_music(
                            r"Recources\sounds\player\running.mp3",
                            1,
                            _O0OOOO00000OOOOO0OOOOOOOO0O0O0OOO0O0O00OOOOOO0OOO000OO=2,
                            O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=15,
                        )
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pig.K_RIGHT or event._OOOOO0O0OOOOOO0OOOO0OOO == ord("d"):
                        self.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOO00OO000 = self.speed
                        music.play_music(
                            r"Recources\sounds\player\running.mp3",
                            1,
                            _O0OOOO00000OOOOO0OOOOOOOO0O0O0OOO0O0O00OOOOOO0OOO000OO=2,
                            O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=15,
                        )
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pig.K_r:
                        return True, False
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pig.K_e or event._OOOOO0O0OOOOOO0OOOO0OOO == ord("e"):
                        _O000OOOOOO0O0O0O0O000OO0OOOOOO0OOO0O0O0 = True
                        self.open_inventory(screen, infoObject, Mainfont, font)
    
        def OOOOOOO0OOOOO0OOO0OOO0OOOO0OOOOOOOO0O0OO0OOOOOO0(
            self, screen_height: int, screen_width: int, colliders: list, screen
        ) -> None:
            """
            Update the player character's position and perform collision detection.
    
            Parameters:
            - screen_height (int): The height of the game screen.
            - screen_width (int): The width of the game screen.
            - colliders (list): List of colliders in the game.
            - screen: Pygame display surface.
    
            Returns:
            None
            """
            O0OO0OO00OOOOOO0OOO000OOO00OOOOOOOOOOOOO0OO000O0OOOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0 = pig.Rect(self.x, self.y, self.width, self.width)
            self.advanced_health(screen)
            # Check for collisions with colliders
            self.O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO0O000OOO = True  # Assume gravity is applied unless a collision is detected
    
            for collider in colliders:
                _O000OOOO0OO0OO000O0OOOO0OO000O0OOO000OOOOO000OO0O000OOOO0OOO0OO0O000OOOOOO0O0O0O0OOOOOO = selfbounds.colliderect(collider)
                if iscolliding:
                    self.O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO0O000OOO = False
                    # Adjust the player's position to be on top of the block
                    self.OOOO0OOO = collider.y - self.height  # Place player on top of the block
                    self.OOOOO0OOOOO000OOOO0OOOOOOOO0O0OOO00OOOOO0OO000O000OOOOOOO0O0OO00 = True
                    if self.jump and self.platform:
                        self.y -= 5
                        self.O0OOOO0OOOOOOOO0O0O0OO00OOOOO0OO = False
                        self.OOOOO0OOOOO000OOOO0OOOOOOOO0O0OOO00OOOOO0OO000O000OOOOOOO0O0OO00 = False
                    self.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOOOOO0OOO = 1
    
            if self.gravityi:
                self.velocity_y += self.gravity
    
            self.x += self.velocity_x
            if self.gravityi:
                self.y += self.velocity_y
    
            if self.y > screen_height - 20:
                self.OOOO0OOO = screen_height - 20
                self.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOOOOO0OOO = 0
            if self.x <= 0:
                self.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOO00OO000 = 1
            if self.x >= screen_width:
                self.O0O000OO0OOOOOO0OOO000OO0OO000O000O0OOOO0O000OOOOOO0O0OOOOOO0OOOO0OO0OOOO00OO000 = -1
    
            if self.velocity_x > 0:
                self.velocity_x -= 0.01
            if self.velocity_x < 0:
                self.velocity_x += 0.01
    
            self.trail.append((self.x + 10, self.y - 100))  # Add current position to trail
    
            if len(self.trail) > 20:  # Limit the trail length to 10
                self.trail.pop(0)  # Remove the oldest position
    
                # if iscolliding[1]:
                #    if self.digging:
                #        self.dig(collider)  # Perform dig ability on collision
                #    if iscolliding[0] == 'y_axis_collision':
                #        O0OOOOOO00OOOOOOOO0OOOOOO0O000OO0O000OOOOOO0O0OOOOOO0OOO = 0
                #    #    self.bash(collider, screen)  # Perform bash ability on collision
    
            # Update arrow position if aiming
            if self.aiming:
                self.OO0OOOOO00OOOOOO00OOOOOO0OO000O0OO0OOOO0O0OO0OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOOOO0OO0OO000O0O0OO0OO0 = pig.mouse.get_pos()
    
        def O0OOO0OO0OOOOOO0OOO000OO0OOOOOO0OOO0O0OO0OOOOOO0O0OO0OOOOOO0O0OO0O000OOOOOO000OO0OOOOOO0(self, terrain, tile):
            """
            Delete a tile 
        from the terrain.
    
            Parameters:
            - terrain (list): The terrain map of the game.
            - tile: The tile to delete.
    
            Returns:
            object: The modified tile.
            """
            OOOO0OOO = tile
            # Check if the provided coordinates are within the bounds of the terrain
            # if 0 <= self.click[1] < len(terrain) and 0 <= self.click[0] < len(terrain[self.click[1]]):
            # Set the value at the specified position to 8 (sky block/empty tile)
            try:
                OO0OOOOO = terrain[self.click[1] // 15][self.click[0] // 15]
                OOOOOOOO = terrain[(self.click[1] + 5) // 15][(self.click[0] - 5) // 15]
                _O0OOOO = terrain[(self.click[1] - 5) // 15][(self.click[0] + 5) // 15]
                O0OOO0OO = terrain[(self.click[1] + 5) // 15][self.click[0] // 15]
                _OOOOOO0 = terrain[(self.click[1] - 5) // 15][self.click[0] // 15]
                O00OOOOO = terrain[self.click[1] // 15][(self.click[0] - 5) // 15]
                O0OOOOOO = terrain[self.click[1] // 15][(self.click[0] + 5) // 15]
                _OOO = [a, b, c, d, e, f, g]
                for is_block in h:
                    if is_block != 8:
                        self.xp += is_block
                terrain[self.click[1] // 15][self.click[0] // 15] = 8
                terrain[(self.click[1] + 5) // 15][(self.click[0] - 5) // 15] = 8
                terrain[(self.click[1] - 5) // 15][(self.click[0] + 5) // 15] = 8
                terrain[(self.click[1] + 5) // 15][self.click[0] // 15] = 8
                terrain[(self.click[1] - 5) // 15][self.click[0] // 15] = 8
                terrain[self.click[1] // 15][(self.click[0] - 5) // 15] = 8
                terrain[self.click[1] // 15][(self.click[0] + 5) // 15] = 8
                OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OO0OO0OO0 = [a, b, c, d, e, f, g]
                for x in blocks:
                    if O00OO000 == 2 and y[0] != 1:
                        y[0] = 0
                        y[1] += 1
                    if O00OO000 == 0 and y[0] != 0:
                        y[0] = 1
                        y[1] += 1
                return y
            except:
                # print("tile does not exist")
                None
            # else:
            #   print("Invalid coordinates")
    
        def OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO00O000OOOOOO0O0OO0OOOOOO0O0O0OO00(self, object, terrain):
            """
            Place an item in the game world.
    
            Parameters:
            - object: The item to place.
            - terrain (list): The terrain map of the game.
    
            Returns:
            None
            """
            global unaturalblocks
            _O000OOOOOO0O0OO0OOOOOO0O0O0OO00O0OO0OOO0O000OOOO0OOO0OOO0OO0OO0 = {
                "0": 10,
                "1": 11,
            }
            if terrain[self.place[1] // 15][self.place[0] // 15] == 8:
                print("<_-.-_>")
                OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0O = item_ids[f"{object[0].id}"]
                terrain[self.place[1] // 15][self.place[0] // 15] = block
                object[1] -= 1
                if object[1] == 0:
                    _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = [Item, 999999999999999999]
                return terrain
    
        def OOOOOOOO00OOOOOO0OOOOOO0OO0OOOOO0OOOOO0OOOOOOOO0OOO0O0O0OO0OOOOOOOO0O0OOOOOOOOO000OOOOOOOO0OOOOOOOO000OOOOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0O():
            pass
    
        def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOO0O000OOOOOO0O0OO0OOOOOO0O0O0OO00O0OO0OOOOOOOOOOOOO0OOOOO00OOOOOO(self, event, terrain, holdobject):
            """
            Handle interactions with the item bar.
    
            Parameters:
            - event: The pygame event object.
            - terrain (list): The terrain map of the game.
            - holdobject: The object currently held by the player.
    
            Returns:
            Tuple[bool, bool, object]: A tuple containing game state information and the current held object.
            """
            if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                self._O0OOOOOOO000OO0O000OOO00O0OOOO0OOOOO0O = pig.mouse.get_pos()
                OOOOO0OO0OO000O0O0OO0OO0 = pig.mouse.get_pos()
                try:
                    O0OOOOOO00OOOOOO0O000OOOO0OOO0OOOOOOO0OO0OO000O0O0OO0OO0 = item_bar.Get_pos()
                    if item_bar.In_grid(pos[0], pos[1]):
                        if selected:
                            O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = item_bar.Add(selected, gridpos)
                        elif item_bar.items[gridpos[0]][gridpos[1]]:
                            O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = item_bar.items[gridpos[0]][gridpos[1]]
                            item_bar.items[gridpos[0]][gridpos[1]] = None
                except:
                    None
                    # clicked out of inventory
                return False, True, holdobject
            if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 3 and holdobject != [Item, 999999999999999999]:
                self.OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0 = pig.mouse.get_pos()
                return self.placeitem(holdobject, terrain)
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOO00OO000OOOOO0OO(self):
            pass
    
        def OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOOO0OOOO0OOOOOOOO0O0O0OO00OOOOO0OO(self):
            """makes the player jump"""
            self.velocity_y -= 3
            self.O0OOOO0OOOOOOOO0O0O0OO00OOOOO0OO = True
            music.play_music(
                r"Recources\sounds\player\jump.mp3",
                1,
                _O0OOOO00000OOOOO0OOOOOOOO0O0O0OOO0O0O00OOOOOO0OOO000OO=3,
                O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=5,
            )
    
        def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOO0OO0OOOO0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0(self, screen, mousex, mousey, font):
            """
            Render the selected item next to the mouse cursor.
    
            Parameters:
            - screen: Pygame display surface.
            - mousex: X-coordinate of the mouse cursor.
            - mousey: Y-coordinate of the mouse cursor.
            - font: Pygame font for rendering text.
    
            Returns:
            None
            """
            screen.blit(selected[0].resize(30), (mousex, mousey))
            _OO000O0OOOOOOOOO0OOOO0O = font.render(str(selected[1]), True, (0, 0, 0))
            screen.blit(obj, (mousex + 15, mousey + 15))
    
        def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOO0O000OOOOOO0O0OO0OOOOOO0O0O0OO00(self, tile):
            """
            Get an item and add it to the player's inventory.
    
            Parameters:
            - tile: The item to add to the inventory.
    
            Returns:
            None
            """
            OOO000OO0OO000O00OO000O00OOOOO0O0O000OOOOOO0O0O0O0OOOOOO = True
            O00OO000 = 0
            OOOO0OOO = 0
            _O000OOOOOO0O0OO0OOOOOO0O0O0OO00O0OO0OO000O0OOOO0OO000O0OOO000OOOOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = [Item(tile[0]), tile[1]]
            while looking:
                if player_inventory.items[x][y]:
                    if player_inventory.items[x][y][0]._O000OOOO0OOO0OO == itemscollected[0].id:
                        player_inventory.items[x][y][1] += itemscollected[1]
                        OOO0O0OO0O000OOOOOO000OO0OOOOOO0 = [-1, 0]
                        OOO000OO0OO000O00OO000O00OOOOO0O0O000OOOOOO0O0O0O0OOOOOO = False
                    else:
                        if x <= 27:
                            x += 1
                        else:
                            y += 1
                            O00OO000 = 0
                else:
                    player_inventory.Add(itemscollected, (x, y))
                    OOO0O0OO0O000OOOOOO000OO0OOOOOO0 = [-1, 0]
                    OOO000OO0OO000O00OO000O00OOOOO0O0O000OOOOOO0O0O0O0OOOOOO = False
    
        def _OO000O0OOOOO0OO0OOOOOO0OOO0O0O0O0OO0OOO0O000OOOOOO0O0O0O0O000OO0OOOOOO0OOO0O0O0OOO0O0OO0OO000O000OOOOOOOOOO0OOO(self, screen, infoObject, Mainfont, font):
            """
            Open the player's inventory screen.
    
            Parameters:
            - screen: Pygame display surface.
            - infoObject: Pygame display information object.
            - Mainfont: Pygame font for rendering main titles.
            - font: Pygame font for rendering text.
    
            Returns:
            None
            """
            global inven, selected
            while inven:
                mousex, O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0OOOO0OOO = pig.mouse.get_pos()
                # draw the screen
                screen.fill((0, 0, 0, 50))
                OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O00OOOOOO0OO000O0OOOOOOO0OOO0O0O0O0OOO0OO = pig.Surface([640, 480], pig.SRCALPHA)
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = Mainfont.render("Inventory", True, (255, 255, 255), (100, 100, 100))
                screen.blit(
                    text,
                    (
                        infoObject.current_w / 5,
                        infoObject.current_h - 350,
                    ),  # (infoObject.current_h - infoObject.current_h /1.5, infoObject.current_w / 2 - 150)
                )
                #
                screen.blit(backround, (0, 0))
                player_inventory.draw(OOOO0OOO00O0OOOO00000OOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0=(False, 0))
                item_bar.draw(OOOO0OOO00O0OOOO00000OOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0=(True, infoObject.current_h / 1.64))
                crafting_grid.draw(OOOO0OOO00O0OOOO00000OOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0=(False, 0))
                # if holding something, draw it next to mouse
                if selected:
                    screen.blit(selected[0].resize(30), (mousex, mousey))
                    _OO000O0OOOOOOOOO0OOOO0O = font.render(str(selected[1]), True, (0, 0, 0))
                    screen.blit(obj, (mousex + 15, mousey + 15))
                pig.display.update()
                for event in pig.event.get():
                    if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.QUIT:
                        quit()
                    if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.KEYDOWN:
                        _O000OOOOOO0O0O0O0O000OO0OOOOOO0OOO0O0O0 = False
                    if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.MOUSEBUTTONDOWN:
                        # if right clicked, get a random item
                        if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 3:
                            O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = [Item(random.randint(0, 3)), 1]
                        elif event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                            try:
                                OOOOO0OO0OO000O0O0OO0OO0 = pig.mouse.get_pos()
                                O0OOOOOO00OOOOOO0O000OOOO0OOO0OOOOOOO0OO0OO000O0O0OO0OO0 = player_inventory.Get_pos()
                                if player_inventory.In_grid(pos[0], pos[1]):
                                    if selected:
                                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = player_inventory.Add(selected, gridpos)
                                    elif player_inventory.items[gridpos[0]][gridpos[1]]:
                                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = player_inventory.items[gridpos[0]][
                                            gridpos[1]
                                        ]
                                        player_inventory.items[gridpos[0]][
                                            gridpos[1]
                                        ] = None
                                O0OOOOOO00OOOOOO0O000OOOO0OOO0OOOOOOO0OO0OO000O0O0OO0OO0 = crafting_grid.Get_pos()
                                if crafting_grid.In_grid(pos[0], pos[1]):
                                    if selected:
                                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = crafting_grid.Add(selected, gridpos)
                                    elif crafting_grid.items[gridpos[0]][gridpos[1]]:
                                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = crafting_grid.items[gridpos[0]][
                                            gridpos[1]
                                        ]
                                        crafting_grid.items[gridpos[0]][gridpos[1]] = None
                                O0OOOOOO00OOOOOO0O000OOOO0OOO0OOOOOOO0OO0OO000O0O0OO0OO0 = item_bar.Get_pos()
                                if item_bar.In_grid(pos[0], pos[1]):
                                    if selected:
                                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = item_bar.Add(selected, gridpos)
                                    elif item_bar.items[gridpos[0]][gridpos[1]]:
                                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = item_bar.items[gridpos[0]][gridpos[1]]
                                        item_bar.items[gridpos[0]][gridpos[1]] = None
                            except:
                                None  # Handle errors gracefully
            item_bar.OOOO0OOO = infoObject.current_h / 1.2
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOOOO0O0OO00OOOOOOOO0OOOOO0O000OOOOOO000OO(self, screen: pig.Surface) -> None:
            """
            Draw the trail of the object on the specified Pygame screen.
    
            Args:
                screen (pygame.Surface): The Pygame surface on which to draw the trail.
    
            Returns:
                None
            """
            trail_s_num: _O000OOOOOO0O0O0OOO0O0OO = 1
            trail_l_num: _O000OOOOOO0O0O0OOO0O0OO = len(self.trail)
            add_tsize: _O000OOOOOO0O0O0OOO0O0OO = 1
    
            if self.inverse:
                for position in self.trail:
                    pig.draw.circle(
                        screen, (255, 255, 255), position, (trail_l_num - trail_s_num)
                    )
                    trail_s_num += 1
            else:
                if self.rainbow:
                    _OOOOOOOOOO00OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OO0OOOOOO0OOOOO0OO = 360 / len(self.trail)
                    _OOOOOOOOOO00OOOOOO0 = 0
                    for position in self.trail:
                        _OOOOOOO0OOOOOOOOOOOOOO = colorsys.hsv_to_rgb(hue / 360, 1, 1)
                        r, g, OOOOOOOO = [int(c * 255) for c in rgb]
                        pig.draw.circle(
                            screen, (r, g, b), position, (trail_s_num + add_tsize)
                        )
                        add_tsize += 0.5
                        hue += hue_step
                else:
                    r: _O000OOOOOO0O0O0OOO0O0OO = 255
                    g: _O000OOOOOO0O0O0OOO0O0OO = 255
                    b: _O000OOOOOO0O0O0OOO0O0OO = 255
                    for position in self.trail:
                        pig.draw.circle(
                            screen, (r, g, b), position, (trail_s_num + add_tsize)
                        )
                        add_tsize += 0.5
    
        def _O0OOOOOOO000OO0OOOOOO0OO0OOOOO00OOOOOOO0OO0OOOOOO0O0OO00OOOOOOOO0OOOOO0O000OOOOOO000OO(self) -> None:
            """
            Clear the trail of the object.
    
            Returns:
                None
            """
            self.OOO0O0OO00OOOOOOOO0OOOOO0O000OOOOOO000OO = []  # Clear the trail    import pygame as pig
    
    import typing as tp
    
    import SquarePixels.player.player as player
    
    import SquarePixels.render.Lighting as Lit
    
    import random
    
    import math
    
    
    OOOOOOOOOOO000OOOO0OOOOO00O0OOOO0OOOOO0OO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OOOO0OOOOOOOO0O0O0O0OOOOOOOOO000OO0OOOOOO0O0OO0OO0 = []
    infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pig.display.Info()
    # Fill the screen with black rectangles
    for x in range(infoObject.current_w // 20 + 50):
        for y in range(infoObject.current_h // 20 + 50):
            OOOOOOOOOOO000OOOO0OOOOO00O0OOOO0OOOOO0OO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pig.Rect((x * 20, y * 20, 20, 20))
            black_rectangles.append(black_rect)
    
    
    def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOO0OO0OOOOOO0O0OO0OOOOOO000OOOOOO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0(
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
        OOO0O0OO0O000OOOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = 15
        OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OO0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0O0OO0OO0 = [
            r"Recources\Textures\grass.jpg",
            r"Recources\Textures\stone.jpg",
            r"Recources\Textures\wood.png",
        ]
        _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOOO0OO0OO0 = [
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
        OOOOO0OO0OOOOOO0OO0OOOO0OO0OOOOO0OO000O0OOO000OO0OO000O000OOOOOOO0OO0OO0 = (
            []
        )  # stores colors with lighting applied, blank and a placeholder at this point in the script
        _O0OOOO0OO000O0OOO000OOOOO000OO0O000OOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0 = []
        O0OO0OO00OOOOO0OOOOO0OOO = []
        OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0O0OO0OOOOOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OO0OO0OO0 = [
            13,
        ]
        if O0O0OO000OO000O000OOOOOOOOO0O0O00O000OOOOOO0O0O0O0OOOOOO == 0:
            pig.draw.rect(
                screen, (255, 255, 51), ((DayTime * 250) + 300, (DayTime * 200), 100, 100)
            )
        for x in range(width[0], width[1]):
            for y in range(height):
                OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OO0OO0OOOOOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 = terrain[y][x]
                _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOOOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0O = pig.Rect(
                    (
                        (x + pos_x - camera_x) * tile_size,
                        (y + pos_y - camera_y) * tile_size,
                    ),
                    (tile_size, tile_size),
                )
                if not block_type in place_blocks:
                    _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = colors[block_type]
                    if _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO == (255, 255, 255):
                        if random.randint(0, 1) == 1:
                            _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (255, 255, 255)
                        else:
                            _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (211, 211, 211)
                    OOOOO0OO0OOOOOO0OO0OOOO0OO0OOOOO0OO000O0OOO000OO0OO000O000OOOOOOO0OO0OO0 = Lit.LightAlgorithm(
                        colors, x, y, (playerpos.x), (playerpos.y), DayTime
                    )
                    if not _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO == (211, 211, 211):
                        _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = NewColors[block_type]
                    else:
                        OOO0OOOOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOOOO0OOOO0OO000O0O0OO0OO0 = [(DayTime * 25), (DayTime * 25)]
                        OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OOOO0OOOO0OO000O0O0OO0OO0 = [x, y]
                        _OOOOO00OO0OOOOO00OOOOOO0OOOOO0O0OOOOOO0OOO0O0O0 = round(math.dist(blockPos, PlayerPos))
                        _OOOOO00OO0OOOOO00OOOOOO0OOOOO0O0OOOOOO0OOO0O0O0 = Darken * DayTime
                        _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (211 - Darken, 211 - Darken, 211 - Darken)
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
                    #    OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OO0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = block_images[block_type]
                    #    screen.blit(pig.image.load(block_image), currentblock)
                    _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = colors[block_type]
                    if _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO == (0, 0, 0, 0):
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
                    if OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OO0OO0OOOOOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == 10:
                        screen.blit(block_images[2], currentblock)
                    if OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OO0OO0OOOOOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == 11:
                        screen.blit(block_images[1], currentblock)
                    colliders.append(currentblock)
    
        for rect in black_rectangles:
            # Calculate the center point of the black rectangle
            _OOOOOO0OOOOOO000O0OOOOOOO0O0OOO0OO0OOO00O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO = rect.center
    
            # Calculate the distance from the player to the center of the black rectangle
            O0OOO0OO0O000OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0O000O0OOOO0OOOOOO0 = math.sqrt(
                (rect_center[0] - playerpos.x) ** 2 + (rect_center[1] - playerpos.y) ** 2
            )
            # Calculate the transparency based on the distance to the center
            OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO0OOOOO0OOOO0OOOOO00OOOOOO0OOOOOO0OOO0O0O000O0OOOOOOOO0OOO = int(distance)
            # Closer is less transparent
            if transparency >= 255:
                OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO0OOOOO0OOOO0OOOOO00OOOOOO0OOOOOO0OOO0O0O000O0OOOOOOOO0OOO = 255
            if transparency <= 0:
                OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO0OOOOO0OOOO0OOOOO00OOOOOO0OOOOOO0OOO0O0O000O0OOOOOOOO0OOO = abs(transparency)
            if transparency >= 255:
                OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO0OOOOO0OOOO0OOOOO00OOOOOO0OOOOOO0OOO0O0O000O0OOOOOOOO0OOO = 255
            # Define a radius for the sphere
    
            # Create a transparent black color
            OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO0OOOOO0OOOO0OOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOOOOOOOOOO000OOOO0OOOOO00O0OOOO0OOOOO0O = (0, 0, 0, transparency)
            # Create a surface with the transparent black color and same dimensions as the rectangle
            OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO0OOOOO0OOOO0OOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = pig.Surface(rect.size, pig.SRCALPHA)
            pig.draw.rect(transparent_surface, transparent_black, (0, 0, *rect.size))
            # Blit the transparent surface onto the main screen
            screen.blit(transparent_surface, rect.topleft)
            # Remove the black rectangle if it's fully transparent
            if OOO0O0OO00OOOOOOOO0OOOOOOOO0O0O0O0OO0OO0OOOOO0OOOO0OOOOO00OOOOOO0OOOOOO0OOO0O0O000O0OOOOOOOO0OOO == 0 or distance <= 60:
                black_rectangles.remove(rect)
        return sky, colliders
    
    
    def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOO0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOO(
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
    
    
    def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOO0OO0OOO0OO000O0OOO0O0OO00000OOO0OOOOOO000OOOOOOO0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OO0(screen: pig.Surface, players: list):
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
    
    
    def O0OO0OO00OO000O000OOOOOOOOO0O0OOO0OO0OOOOOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OO(allpoints: tp.Dict[str, int]) -> tp.List[tp.Tuple[str, int]]:
        """
        Sort the leaderboard based on player points.
    
        Args:
            allpoints (tp.Dict[str, int]): Dictionary of player names and their points.
    
        Returns:
            tp.List[tp.Tuple[str, int]]: Sorted list of player names and points as tuples.
        """
        O0OO0OO00OO000O000OOOOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOOOO0OO0OO000O00O000OOOOOO0O0O0OOO0O0OOO0OO0OO0 = sorted(allpoints.items(), _OOOOO0O0OOOOOO0OOOO0OOO=lambda x: x[1], _OOOOOO0OOOOOO0O0O000OO0OOOOOO000OOOOOOO0OO0OO00OOOOOO0=True)
        return sorted_points
    
    
    def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOO0OO0OOO00O0OOOO00000OOOOO0OOOOOOOO0O0OO(
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
        O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pig.font.Font(None, 20)
        for i, message in enumerate(chat_messages):
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(message, True, (255, 255, 255))
            if 10 + i * 20 >= screen_height - 30:
                O0OO0OO0OO0OOOOOO0O000OO0OOOOOO0 = chat_messages[i]
                _O000OOO = 0
                chat_messages.clear()
                chat_messages.append(save)
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text.get_rect(OOO000OO0OOOOOO0O00OOOOOOOO0O0OO=10, OOO0O0OO0OO000O0OOOOO0OO=10 + i * 20)
                screen.blit(text, text_rect)
            else:
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text.get_rect(OOO000OO0OOOOOO0O00OOOOOOOO0O0OO=10, OOO0O0OO0OO000O0OOOOO0OO=10 + i * 20)
                screen.blit(text, text_rect)
    
    
    def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOO0OO0OOOO0OO0OO000O0OOOO0OO000O000OOOOOO0OOOOOO0O0OO0OO0(allpoints: tp.Dict[str, int], screen: pig.Surface) -> None:
        """
        Render the leaderboard on the screen.
    
        Args:
            allpoints (tp.Dict[str, int]): Dictionary of player names and their points.
            screen (pig.Surface): The game screen surface.
    
        Returns:
            None
        """
        # sort scores
        O0OO0OO00OO000O000OOOOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOOOO0OO0OO000O00O000OOOOOO0O0O0OOO0O0OOO0OO0OO0 = sort_leaderboard(allpoints)
        # Render the leaderboard
        O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pig.font.Font(None, 20)
        for i, entry in enumerate(sorted_points):
            name, O0OO0OO000O0OOOO0OO000O000OOOOOO0OOOOOO0 = entry
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(f"{name}: {score}", True, (255, 255, 255))
            # playeronlead[name] = pig.Rect((700, 10 + i * 20, 20, 10))
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text.get_rect(OOO000OO0OOOOOO0O00OOOOOOOO0O0OO=700, OOO0O0OO0OO000O0OOOOO0OO=10 + i * 20)
            screen.blit(text, text_rect)
    
    
    def O0OO0OO000O0OOOO0OO000O000OOOOOO0OOOOOO0O0OO0OOO00000OOO0O000OOOOOO0O0OOOOOOOOOO0OO000O0O00OO0000OOOOOO0O0OO0OO0(allpoints: tp.Dict[str, int]) -> dict:
        """
        Generate hitboxes for leaderboard entries.
    
        Args:
            allpoints (tp.Dict[str, int]): Dictionary of player names and their points.
    
        Returns:
            dict: Dictionary of hitboxes for leaderboard entries.
        """
        # sort scores
        O0OO0OO00OO000O000OOOOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOOOO0OO0OO000O00O000OOOOOO0O0O0OOO0O0OOO0OO0OO0 = sort_leaderboard(allpoints)
        OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOO0OO000O0OOO0O0O0OOO000OO0OOOOOO0OO0OOOOOO0OOO0OO = {}
        for i, entry in enumerate(sorted_points):
            name, O0OO0OO000O0OOOO0OO000O000OOOOOO0OOOOOO0 = entry
            playeronlead[name] = pig.Rect((700, 10 + i * 20, 30, 10))
        return playeronlead
    
    
    def _OOOOO0O0O000OOO00O0OOOO0OOOOO0OO0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OO0(
        hitboxes: dict, players: list, screen, points: dict, kicked: list
    ) -> tuple:
        """
        Kick players 
        from the game based on hitboxes.
    
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
                pig.draw.rect(screen, (255, 0, 0), _OOOOOO0OOOOOO000O0OOOOOOO0O0OO=hitboxes[hitbox])
                if pig.mouse.get_pressed()[0]:
                    # Get the name of the player associated with the hitbox
                    OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = hitbox
                    print(players)
                    if player_name is not None:
                        # Remove the player from the players dictionary
                        for player in players:
                            if player.OOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 == player_name:
                                players.remove(player)
                                break
                        for player in points:
                            if OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOO == player_name:
                                points.pop(player)
                                kicked.append(player)
                                break
    
        # Kick the socket associated with the player
    
        # print("Player", player_name, "kicked.")
        # print(players, points, kicked)
        return players, points, kicked
    
    
    # Define nametag class
    class OOOOO0OOOO0OOOOOO0O0OO000OOOOOO0OOO0O0OOOO0OOOOOO0OOOOOO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, player: player.Player):
            """
            Initialize a Nametag instance.
    
            Args:
                player (player.Player): The player associated with the nametag.
            """
            self.player: player.OOO0OOOOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOO = player
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen: pig.Surface) -> None:
            """
            Draw the nametag on the screen.
    
            Args:
                screen (pig.Surface): The game screen surface.
    
            Returns:
                None
            """
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pig.font.Font(None, 20)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(self.player.name, True, (255, 255, 255))
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=(self.player.x, self.player.y - 15))
            screen.blit(text, text_rect)    
            import math
    
    
    def OOO00OOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOOOO0OOOOO000OOO0OOOOOO0OO000O000OOOOOO0O000OOOOOO0O0OO00000OOOO0O0OO00(colors, x, y, playerX, playerY, TimeOfDay):
        OOOOOOO0OOOOOOO0OOO0O0O0OOO0OOOO0OO000O0O0OO0OO0 = [(TimeOfDay * 25), TimeOfDay*10]
        OOOOOOOOOOO000OO0OO000O000O0OOOO0OOOOO0OOOO0OOOO0OO000O0O0OO0OO0 = [x, y]
        _OOOOO00OO0OOOOO00OOOOOO0OOOOO0O0OOOOOO0OOO0O0O0 = round(math.dist(blockPos, SunPos))
        _OOOOO00OO0OOOOO00OOOOOO0OOOOO0O0OOOOOO0OOO0O0O0 = Darken * TimeOfDay
        OOO0O0O0OOOOOOO0O0O0OO00 = 100
        OOO0O0O0OOOOOOO0O0O0OO00 = 139
        OOO0O0O0OOOOOOO0O0O0OO00 = 69
        OOO0O0O0OOOOOOO0O0O0OO00 = 19
        OOO0O0O0OOOOOOO0O0O0OO00 = 115
        OOO0O0O0OOOOOOO0O0O0OO00 = 85
        OOO0O0O0OOOOOOO0O0O0OO00 = 34
        OOO0O0O0OOOOOOO0O0O0OO00 = 0
        OOO0O0O0OOOOOOO0O0O0OO00 = 128
        OOO0O0O0OOOOOOO0O0O0OO00 = 211
        OOO0O0O0OOOOOOO0O0O0OO00 = 255
        OOO0O0O0OOOOOOO0O0O0OO00 = 223
        OOO0O0O0OOOOOOO0O0O0OO00 = 135
        OOO0O0O0OOOOOOO0O0O0OO00 = 206
        OOO0O0O0OOOOOOO0O0O0OO00 = 235
        if num1 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num2 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num3 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num4 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num5 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num6 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num7 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num8 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num9 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num10 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num11 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num12 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num13 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num14 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        if num15 - Darken < 0:
            OOO0O0O0OOOOOOO0O0O0OO00 = Darken
        _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOOO0OO0OO0OOO000OO0O000OOOO0OO0OO0OOO0O0OO = [
            (num1 - Darken, num1 - Darken, num1 - Darken),
            (num2 - Darken, num3 - Darken, num4 - Darken),
            (num2 - Darken, num5 - Darken, num6 - Darken),
            (num7 - Darken, num2 - Darken, num7 - Darken),
            (num8 - Darken, num9 - Darken, num8 - Darken),
            (num10 - Darken, num10 - Darken, num10 - Darken),
            (num11 - Darken, num12 - Darken, num8 - Darken),
            (num9 - Darken, num9 - Darken, num9 - Darken),
            (num13 - Darken, num14 - Darken, num15 - Darken),
            (num11 - Darken, num11 - Darken, num11 - Darken),
        ]
        return colorslist    
        import pygame
    
    
    def OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOO0O0OO00OOOOOOO0O0OO0OO00O000OOO00O0OOOO(file_path, OOO000OO0OO000O00OO000O0OOOOO0OOO0OO0OO0=0, O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OO=0, O00OOOOOOO0OOOOOO0OOO0OO0OOOOOO0O0OO0OOOO0O0OO00O0OO0OO0=0, _O0OOOO00000OOOOO0OOOOOOOO0O0O0OOO0O0O00OOOOOO0OOO000OO=0, O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=1):
        """
        Play a music file using Pygame's mixer module.
    
        This function initializes the Pygame mixer module if not already initialized
        and plays a music file specified by `file_path` on the specified audio `channel`.
        You can control various playback parameters, including the number of `loops`,
        the `start` position in milliseconds, and `fade_ms` for fading in and out.
        Additionally, you can set the `volume` of the audio channel.
    
        Args:
            file_path (str): The path to the music file to be played.
            loops (int, optional): Number of times the music should loop (0 for no looping, default).
            start (int, optional): Start playback at the specified position in milliseconds (default is 0).
            fade_ms (int, optional): Time in milliseconds for fading in/out (default is 0, no fade).
            channel (int, optional): The audio channel to use for playback (default is 0).
            volume (float, optional): The volume level for the audio channel (default is 1).
    
        Returns:
            None
    
        Note:
            - Ensure that Pygame and the mixer module are properly initialized before calling this function.
            - Make sure to handle any exceptions related to file loading or Pygame initialization.
    
        Example:
            # Play a music file with looping for 3 times, starting at 5000 milliseconds,
            # and fading in/out over 2000 milliseconds with reduced volume.
            play_music("background_music.mp3", OOO000OO0OO000O00OO000O0OOOOO0OOO0OO0OO0=3, O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OO=5000, O00OOOOOOO0OOOOOO0OOO0OO0OOOOOO0O0OO0OOOO0O0OO00O0OO0OO0=2000, O0O000OO0OO000O0OOO000OOOOOOOOO0O0O0OO000OOOOOO0=0.5)
        """
        pygame.mixer.init()
        pygame.mixer.Channel(channel).set_volume(volume)
        pygame.mixer.Channel(channel).play(
            pygame.mixer.Sound(file_path), loops, start, fade_ms
        )    
    import pygame as pg
    
    import random
    
    
    class _OO0OO00OOOOOO000OOOOOO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0OOOOOO0O0OOOOOO0OOO0O0O00OOOOOO000OOOOOOOO0OOOOOOOO0O0OO0OO000O000OOOOOO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, width, height, OOOOO0OO0OO000O0O0OO0OO0O0OO0OOOO00OO000=0, OOOOO0OO0OO000O0O0OO0OO0O0OO0OOOOOOO0OOO=0):
            self.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = width
            self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = height
            self.OOOOO0OO0OO000O0O0OO0OO0O0OO0OOOO00OO000 = pos_x
            self.OOOOO0OO0OO000O0O0OO0OO0O0OO0OOOOOOO0OOO = pos_y
            self.OOO0O0OO0OOOOOO000OOOOOO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0 = []
            self._O0OOOO0OO000O0OOO000OOOOO000OO0O000OOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0 = []
            self._O0OOOOOO0OOOOOO0O0OO000OOOOOO000OOOOOOOO0OOOOOO0OO0OOOO00OO000 = 0
            self._O0OOOOOO0OOOOOO0O0OO000OOOOOO000OOOOOOOO0OOOOOO0OO0OOOOOOO0OOO = 0
            self.OOOOO0OO00OOOOOO0OO000O0O0OOOOOO00OOOOOO0OOOOOO0O0OO0OO0O0OO0OO0 = 0  # Initialize progress to 0
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOOOOOO0OO00OOOOOO0OO000O0O0OOOOOO00OOOOOO0OOOOOO0O0OO0OO0O0OO0OO0O0OO0OOOOOOOOOOOOO0OOOOO00OOOOOO(self, screen, progress):
            OOOOOOOOOO0OOOOO00OOOOOOO0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = progress / 3000
            OOOOOOOOOO0OOOOO00OOOOOOO0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 20
            OOOOOOOOOO0OOOOO00OOOOOOO0OO0OOOO00OO000 = 20
            OOOOOOOOOO0OOOOO00OOOOOOO0OO0OOOOOOO0OOO = self.height - 30
            # OOOOO0OO00OOOOOO0OO000O0O0OOOOOO00OOOOOO0OOOOOO0O0OO0OO0O0OO0OO0O0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = int(bar_width * progress)
            pg.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, bar_width, bar_height))
    
        def O0OOOOOO0OOOOOO0OOO0O0O00OOOOOO000OOOOOOOO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O0OO0OOOOOO000OOOOOO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0(self, screen):
            """
            Generates a random terrain for a 2D game world.
    
            This method generates terrain consisting of ground, sky, trees, ore deposits,
            and clouds. It populates the `self.terrain` 2D array with numeric values
            representing different terrain elements.
    
            The generated terrain includes the following elements:
            - Ground, which can be stone or dirt (0 or 1).
            - Sky (8).
            - Trees, made of wood (2) and leaves (3).
            - Ore deposits, including coal (4), iron (5), gold (6), or diamond (7).
            - Clouds in the sky (9).
    
            This method uses randomization to create a varied and interesting terrain.
    
            Note: This method assumes that the necessary attributes like `self.width`,
            `self.height`, and `self.terrain` are properly initialized in the class.
    
            Args:
                None
    
            Returns:
                None
            """
            self.OOO0O0OO0OOOOOO000OOOOOO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0 = [[0 for _ in range(self.width[1])] for _ in range(self.height)]
            _OOOOOO0 = 0
            # Generate random ground
            O0OOOOOO00OOOOOO0OO000O0OOOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO000OO0OOOOOO0O0O000OO0OOOOOO0OOO000OOO0OO0OO0 = [self.height // 2] * self.width[1]
            for x in range(self.width[0], self.width[1]):
                ground_levels[x] = ground_levels[x - 1] + random.randint(-2, 2)
                ground_levels[x] = max(0, min(self.height - 1, ground_levels[x]))
                e += 1
            screen.fill((0, 0, 0))
            self.draw_progress_bar(screen, e)
            pg.display.flip()
    
            for x in range(self.width[0], self.width[1]):
                for y in range(ground_levels[x], self.height):
                    self.terrain[y][x] = random.choice([0, 1])  # Stone or Dirt
                    e += 1
            screen.fill((0, 0, 0))
            self.draw_progress_bar(screen, e)
            pg.display.flip()
    
            # Set sky blocks
            for x in range(self.width[0], self.width[1]):
                for y in range(ground_levels[x]):
                    self.terrain[y][x] = 8  # Sky
                    e += 1
            screen.fill((0, 0, 0))
            self.draw_progress_bar(screen, e)
            pg.display.flip()
    
            # Generate trees
            OOO0O0OO00OOOOOO0OOOOOO00OOOOOO0O0OO0OOO00O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = self.width[1] // 10
            for _ in range(tree_count):
                OOO0O0OO00OOOOOO0OOOOOO00OOOOOO0O0OO0OOOO00OO000 = random.randint(0, self.width[1] - 1)
                OOO0O0OO00OOOOOO0OOOOOO00OOOOOO0OOOO0OOOOOOOO0OOOO0OOOOO00OOOOOOOOO0O0OO0OO000O0OOO0O0O00OOOOOO0 = random.randint(5, 10)
                OOO0O0OO00OOOOOO0OOOOOO00OOOOOO0O0OO0OOOOOOO0OOO = ground_levels[tree_x] - treeypartone
                # OO0OOOO00O000OOOOOO0O0O0O0OOO0OO0OO000O0OO0OOOO0O0OO0OO0O0OOO0OO0O000OOOO0O0OO000OOOOOO0OOO0O0O0 = pg.display.get_window_size()[1]
                OOO0O0OO00OOOOOO0OOOOOO00OOOOOO0O0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = treeypartone  # random.randint(3, 6)
                for y in range(tree_y, tree_y + tree_height):
                    self.terrain[y][tree_x] = 2  # Wood
                    e += 1
    
                # Generate tree leaves
                OOO000OO0OOOOOO0OO0OOOOOO00OOOOOO0OO0OOO00OOOOOOOO0OOOOOO0OOO0OO0O000OOOOOOOOOO0O0OO0OO0 = random.randint(2, 4)
                for dx in range(-leaf_radius, leaf_radius + 1):
                    for dy in range(-leaf_radius, leaf_radius + 1):
                        if (
                            0 <= tree_x + dx < self.width[1]
                            and 0 <= tree_y + dy < self.height
                        ):
                            if abs(dx) + abs(dy) <= leaf_radius:
                                self.terrain[tree_y + dy][tree_x + dx] = 3  # Leaves
                        e += 1
            screen.fill((0, 0, 0))
            self.draw_progress_bar(screen, e)
            pg.display.flip()
    
            # Generate ore deposits
            _OO000O000OOOOOO0OOOOOO0O0OO0OOO00O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = self.width[1] // 100
            for _ in range(ore_count):
                _OO000O000OOOOOO0OOOOOO0O0OO0OOOOOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 = random.choice([4, 5, 6, 7])  # Coal, Iron, Gold, Diamond
                _OO000O000OOOOOO0OOOOOO0O0OO0OOOO00OO000 = random.randint(0, self.width[1] - 1)
                O0O000OOOO0OOOOOOOO000OO0O000OOOO0OOO0OOOOO0O0O0OOOOOOO0 = False
                while not validnu:
                    try:
                        _OO000O000OOOOOO0OOOOOO0O0OO0OOOOOOO0OOO = random.randint(ground_levels[ore_x] + 1, self.height - 1)
                        e += 1
                    except ValueError:
                        O0O000OOOO0OOOOOOOO000OO0O000OOOO0OOO0OOOOO0O0O0OOOOOOO0 = False
                    else:
                        O0O000OOOO0OOOOOOOO000OO0O000OOOO0OOO0OOOOO0O0O0OOOOOOO0 = True
                _OO000O000OOOOOO0OOOOOO0O0OO0OOO00OOOOOOOO0OOOOOO0OOO0OO0O000OOOOOOOOOO0O0OO0OO0 = random.randint(1, 4)
                for dx in range(-ore_radius, ore_radius + 1):
                    for dy in range(-ore_radius, ore_radius + 1):
                        if (
                            0 <= ore_x + dx < self.width[1]
                            and 0 <= ore_y + dy < self.height
                        ):
                            if abs(dx) + abs(dy) <= ore_radius:
                                self.terrain[ore_y + dy][ore_x + dx] = ore_type
                        e += 1
                screen.fill((0, 0, 0))
                self.draw_progress_bar(screen, e)
                pg.display.flip()
    
            _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOO00O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = random.randint(1, 10)  # Adjust the cloud count as needed
            for _ in range(cloud_count):
                _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = random.randint(12, 25)  # Adjust cloud size as needed
                _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = random.randint(5, 10)  # Adjust cloud size as needed
                _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOOO00OO000 = random.randint(0, self.width[1] - cloud_width)
                _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOOOOOO0OOOO0OO0OOOOOOOOOOO0OOOOOO0O00OOOOO0OO000O000OOOOOO0OOOOOO0OOO0OOOOOOOOO0OO0OOOOOO000OOOOOOOO0OOOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0 = tree_height - 20  # Adjust cloud height as needed
                # if cloud_y_beforeOperation <= 0:
                #    print("hi")
                # else:
                #    print('yay')
                # try:
    
                _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOOOOOO0OOO = random.randint(
                    0, abs(int(tree_height - 5))
                )  # Adjust cloud height as needed
                # except:
                #   continue
                for x in range(cloud_x, cloud_x + cloud_width):
                    for y in range(cloud_y, cloud_y + cloud_height):
                        if 0 <= x < self.width[1] and 0 <= y < self.height:
                            if self.terrain[y][x] == 8:  # sky
                                self.terrain[y][x] = 9  # Set cloud blocks
                        e += 1
            screen.fill((0, 0, 0))
            self.draw_progress_bar(screen, e)
            pg.display.flip()
    
            # # Generate colliders based on terrain
            # for x in range(len(self.terrain[0])):
            #    for y in range(len(self.terrain)):
            #        if self.terrain[y][x] != 0:
            #            _O0OOOO0OO000O0OOO000OOOOO000OO0O000OOOO0OOO0OO0OOOOOO000OOOOOO = c.Collider(x, y, 32, 32)
            #            self.colliders.append(collider)
            return e
    
        def _OOOOOOOOOOOOO0OOO0O0O0(self, screen):
            _O0OOOOOOO000OO0OO000O000O0OOOO0OOOOO0O = pg.time.Clock()
    
            self.generate_terrain()
    
            O0O000OOO00OO000 = 0
            O0O000OOOOOO0OOO = 0
    
            # _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
            # while running:
            #    for event in pg.event.get():
            #        if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pg.QUIT:
            #            _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
            #        elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pg.KEYDOWN:
            #            if event._OOOOO0O0OOOOOO0OOOO0OOO == pg.K_UP or event._OOOOO0O0OOOOOO0OOOO0OOO == ord('w'):
            #                O0O000OOOOOO0OOO = -1
            #            elif event._OOOOO0O0OOOOOO0OOOO0OOO == pg.K_DOWN or event._OOOOO0O0OOOOOO0OOOO0OOO == ord('s'):
            #                O0O000OOOOOO0OOO = 1
            #            elif event._OOOOO0O0OOOOOO0OOOO0OOO == pg.K_LEFT or event._OOOOO0O0OOOOOO0OOOO0OOO == ord('a'):
            #                O0O000OOO00OO000 = -1
            #            elif event._OOOOO0O0OOOOOO0OOOO0OOO == pg.K_RIGHT or event._OOOOO0O0OOOOOO0OOOO0OOO == ord('d'):
            #                O0O000OOO00OO000 = 1
            #    self.camera_x += vx
            #    self.camera_y += vy
            #    vx,O0O000OOOOOO0OOO=.5,0
            # if vx >= 0:
            #    O0O000OOO00OO000 = 0
            # if vy >= 0:
            #    O0O000OOOOOO0OOO = 0
            # if vx <= 0:
            #    O0O000OOO00OO000 = 0
            # if vy <= 0:
            #    O0O000OOOOOO0OOO = 0
    
            screen.fill((0, 0, 0))
            pg.display.flip()
            clock.tick(60)
    
    
    def O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OO():
        pg.init()
        infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pg.display.Info()
        screen: pg.OOOOOOO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = pg.display.set_mode(
            (infoObject.current_w, infoObject.current_h)
        )
        # pg.display.toggle_fullscreen()
        pg.display.set_caption("Square Pixel")
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_CROSSHAIR)
        OOO0O0OO0OOOOOO000OOOOOO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0O0OO0OOOO0OOOOOO0OOOOOO0OOO0O0O00OOOOOO000OOOOOOOO0OOOOOOOO0O0OO0OO000O000OOOOOO = TerrainGenerator((0, 10000), infoObject.current_h // 10)
        # terrain_generator.run(screen)
        _OOOOOO0 = terrain_generator.generate_terrain(screen)
        print(e)
    
    
    if __name__ == "__main__":
        start()    
        import pygame
    
    import sys
    
    import tkinter as tk
    from tkinter import filedialog
    
    import os
    
    # Get the current working directory
    OOOOO0OOOO0OOOOOOOO0O0OO00000OOO = os.getcwd()
    
    # Initialize Pygame
    pygame.init()
    
    # Initialize the screen with transparency
    _O000OOOOOO0O0O0O00OOOOO0OO000O0OOO0OOOOOOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.display.Info()
    WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = 800, 600  # infoObject.current_w, infoObject.current_h
    OOOO00OO000O00OOOO0O0O0O00OO0OO0OO0O0OOO = (255, 255, 255)
    _OO0OO0OOOO0OO0OOOOO0OOOOOOO0OOOOOOOOO0OOO0OOOOOOOOO0OOOOOO0OO0OO0O0OOOOOOOO0OO00OO0OO0 = (0, 0, 0, 0)
    OO0OOOOO000O00OOOOOOO0OOOOOO0OO0OOOOO0OOOO0OOOOO00OO0OO0OO0O0OOOOOOO0OO0O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (50, 150, 200)
    
    # Character properties
    _OOO0OOOOOO0OO0OOOOOO0OOO0OOO0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = 50
    OOOOOOOO0OO000O0O0OOO0OOOOOO0OOOO0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 100
    
    # Shapes
    O0OO0OO000000OOOOO0OOOOOOOOOO0OO0OOOOOO0O0OO0OO0 = []
    OOO0O0OO00OOOOOOOO0OOOOO0O000OOOOOO000OOO0OO0OO0 = True
    
    # Create a tkinter root window for file dialogs
    _OOOOOO0OO000O00OO000O0OOO0O0OO = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    
    # Pygame screen
    O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    pygame.display.set_caption("Character Customization")
    OOOOO0OOOOOO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOO00O0OOOO0OO000O0OOO0O0O0 = pygame.image.load(
        r"Recources\program recources\Screenshot 2023-09-21 181742.png"
    )
    pygame.display.set_icon(pygame_icon)
    OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0OO0OOOOOO00OOOOOO0OO000O0OOOOOOO0OOO0O0O0O0OOO0OO = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 36)
    
    # List of character paths
    _O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOOO0OO0OOOOOO000OO0O000OOOO0OO0OO0OOO0O0OO = [
        r"Recources\characters\thumbnails\blue.gif",
        r"Recources\characters\thumbnails\red.gif",
        # Add more character paths here
    ]
    
    # Load pre-made character thumbnails
    _O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOOO0OO0OOOOOO0O0OO00000OOOOOOOOOO0O0O0OO00OOOOOOOOOOO0O0O0OO0OOOOO0O000OOOOOO000OOO0OO0OO0 = []
    for character_path in character_list:
        _O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOOO0OO0OOOOOO0O0OO00000OOOOOOOOOO0O0O0OO00OOOOOOOOOOO0O0O0OO0OOOOO0O000OOOOOO000OO = pygame.image.load(character_path)
        _O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOOO0OO0OOOOOO0O0OO00000OOOOOOOOOO0O0O0OO00OOOOOOOOOOO0O0O0OO0OOOOO0O000OOOOOO000OO = pygame.transform.scale(character_thumbnail, (100, 100))
        character_thumbnails.append(character_thumbnail)
    
    # Sidebar position and size
    O0OO0OO00O000OOOO0OOO0OO0OOOOOO0OOOOOOOOOO0OOOOO00OOOOOOO0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = 150
    O0OO0OO00O000OOOO0OOO0OO0OOOOOO0OOOOOOOOOO0OOOOO00OOOOOOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect(
        infoObject.current_w - (sidebar_width + 20), 0, sidebar_width, infoObject.current_h
    )
    
    # Button position and size
    OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 100
    OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OOOO0OO0OO0OOOOO0OOOO0OOOOO00O0OOOO0O000OOOOOO0O0O0O0OOOOOO = 10
    OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OOO0OO0OO0 = [
        pygame.Rect(
            infoObject.current_w - sidebar_width - 7,
            10 + (button_height + button_spacing) * idx,
            sidebar_width - 20,
            button_height,
        )
        for idx in range(len(character_thumbnails))
    ]
    
    
    def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOO0OO0OO00O000OOOO0OOO0OO0OOOOOO0OOOOOOOOOO0OOOOO00OOOOOO(buttoncount):
        """
        Draw the sidebar with character thumbnails as buttons.
    
        Args:
            buttoncount (int): Index of the currently selected character thumbnail.
    
        Returns:
            None
        """
        _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = [(100, 100, 100), (150, 150, 150)]
        # Fill the sidebar background
        pygame.draw.rect(background, (50, 50, 50), sidebar_rect)
    
        # Draw character thumbnails as buttons
        for idx, thumbnail in enumerate(character_thumbnails):
            _O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = 0
            OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = button_rects[idx]
            for button in buttoncount:
                if OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == idx:
                    _O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = 1
            pygame.draw.rect(background, (color[count]), button_rect)
            background.blit(thumbnail, (button_rect.x + 10, button_rect.y + 10))
    
    
    def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOO00O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOO():
        """
        Draw the character's head, body, and legs on the background.
    
        Returns:
            None
        """
        # Draw head
        pygame.draw.circle(background, CHARACTER_COLOR, (WIDTH // 2, 150), head_size)
    
        # Draw body
        pygame.draw.rect(
            background, CHARACTER_COLOR, (WIDTH // 2 - 20, 200, 40, body_height)
        )
    
        # Draw legs
        pygame.draw.line(
            background, CHARACTER_COLOR, (WIDTH // 2, 300), (WIDTH // 2 - 30, 400), 10
        )
        pygame.draw.line(
            background, CHARACTER_COLOR, (WIDTH // 2, 300), (WIDTH // 2 + 30, 400), 10
        )
    
    
    def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOO0OO0OO000000OOOOO0OOOOOOOOOO0OO0OOOOOO0O0OO0OO0():
        """
        Draw shapes and buttons on the background.
    
        Returns:
            None
        """
        for shape in shapes:
            pygame.draw.rect(background, shape["color"], shape["rect"])
    
        # Draw buttons
        for button in buttons:
            pygame.draw.rect(
                background, (100, 100, 100), button["rect"]
            )  # Button background color
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = font.render(
                button["text"], True, (255, 255, 255)
            )  # Button text color
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text_surface.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=button["rect"].center)
            background.blit(text_surface, text_rect)
    
    
    def OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOO0OO0OO000000OOOOO0OOOOOOOOOO0OO0OOOOOO0(x, y, width, height, color):
        """
        Add a shape to the list of shapes.
    
        Args:
            x (int): X-coordinate of the shape's top-left corner.
            y (int): Y-coordinate of the shape's top-left corner.
            width (int): Width of the shape.
            height (int): Height of the shape.
            color (tuple): RGB color of the shape.
    
        Returns:
            None
        """
        O0OO0OO000000OOOOO0OOOOOOOOOO0OO0OOOOOO0 = {
            "rect": pygame.Rect(x, y, width, height),
            "color": color,
            "dragging": False,
        }
        shapes.append(shape)
    
    
    def O0O0OO00OO0OOOOO0O000OOOOOO0O0O0():
        """
        Main game loop for character customization.
    
        Returns:
            None
        """
        global head_size, body_height, trails
        _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
        OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O000O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = 0
        _OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
        O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO000O0OOOO00000OOOOO0OOOOO00OOOOOO = (False, 0)
        while running:
            if trails:
                screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O000O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = 0
                _OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
                for precharacter in button_rects:
                    if precharacter.collidepoint(
                        pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                    ):
                        hoveredbuttons.append(buttoncount)
                        if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN:
                            O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO000O0OOOO00000OOOOO0OOOOO00OOOOOO = (True, buttoncount)
                    buttoncount += 1
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN:
                    # Check for button clicks
                    for button in buttons:
                        if button["rect"].collidepoint(event.pos):
                            if button["text"] == "Finish":
                                _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
                                return button["callback"]()
                            else:
                                button["callback"]()
    
                    # Check for shape dragging
                    for shape in shapes:
                        if shape["rect"].collidepoint(event.pos):
                            shape["dragging"] = True
                            shape["offset_x"] = shape["rect"].x - event.pos[0]
                            shape["offset_y"] = shape["rect"].y - event.pos[1]
    
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONUP:
                    for shape in shapes:
                        shape["dragging"] = False
    
            # Clear the screen with transparency
            background.fill(TRANSPARENT)
    
            if drawchar[0]:
                _O0OOOO00000OOOOO0OOOOO00OOOOOO = character_thumbnails[drawchar[1]]
                _O0OOOO00000OOOOO0OOOOO00OOOOOO = pygame.transform.scale(char, (550, 550))
                screen.blit(
                    char,
                    (
                        infoObject.current_w // 20,
                        infoObject.current_h / 200,
                        40,
                        body_height,
                    ),
                )
            # Draw the character
            if not drawchar[0]:
                draw_character()
    
            # Draw the sidebar
            draw_sidebar(hoveredbuttons)
    
            # Draw shapes
            draw_shapes()
    
            # Update shape positions while dragging
            for shape in shapes:
                if shape["dragging"]:
                    shape["rect"].O00OO000 = pygame.mouse.get_pos()[0] + shape["offset_x"]
                    shape["rect"].OOOO0OOO = pygame.mouse.get_pos()[1] + shape["offset_y"]
    
            # Update the display
            screen.blit(background, (0, 0))
            pygame.display.update()
    
    
    # Create buttons
    OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = [
        {
            "rect": pygame.Rect(600, 50, 150, 50),
            "text": "Increase Head Size",
            "callback": lambda: increase_size("head"),
        },
        {
            "rect": pygame.Rect(600, 110, 150, 50),
            "text": "Decrease Head Size",
            "callback": lambda: decrease_size("head"),
        },
        {
            "rect": pygame.Rect(600, 170, 150, 50),
            "text": "Increase Body Height",
            "callback": lambda: increase_size("body"),
        },
        {
            "rect": pygame.Rect(600, 230, 150, 50),
            "text": "Decrease Body Height",
            "callback": lambda: decrease_size("body"),
        },
        {
            "rect": pygame.Rect(600, 290, 150, 50),
            "text": "Add Square",
            "callback": lambda: add_square(),
        },
        {
            "rect": pygame.Rect(600, 350, 150, 50),
            "text": "Finish",
            "callback": lambda: finish(),
        },
        {
            "rect": pygame.Rect(600, 410, 150, 50),
            "text": "Reset",
            "callback": lambda: reset_character(),
        },
        {
            "rect": pygame.Rect(600, 470, 150, 50),
            "text": "Toggle Trails",
            "callback": lambda: toggle_trails(),
        },
        {
            "rect": pygame.Rect(600, 530, 150, 50),
            "text": "Export Character",
            "callback": lambda: save_character_dialog(),
        },
        {
            "rect": pygame.Rect(600, 590, 150, 50),
            "text": "Load Character",
            "callback": lambda: load_character_dialog(),
        },
    ]
    
    
    def _O000OOOOOO0O0O000O0OOOO00OOOOOO0OOOOOO0OO0OOOOOO0OO0OO00OOOOOO0O0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0(part):
        """
        Increase the size of the character's head or body.
    
        Args:
            part (str): Either 'head' or 'body' to specify which part to increase.
    
        Returns:
            None
        """
        global head_size, body_height
        if OOOOO0OOOO0OOOOO00OOOOOOOOO0O0OO == "head":
            head_size += 5
        elif OOOOO0OOOO0OOOOO00OOOOOOOOO0O0OO == "body":
            body_height += 10
    
    
    def O0OOO0OO0OOOOOO000O0OOOO00OOOOOO0OOOOOO0OO0OOOOOO0OO0OO00OOOOOO0O0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0(part):
        """
        Decrease the size of the character's head or body.
    
        Args:
            part (str): Either 'head' or 'body' to specify which part to decrease.
    
        Returns:
            None
        """
        global head_size, body_height
        if OOOOO0OOOO0OOOOO00OOOOOOOOO0O0OO == "head":
            head_size -= 5
        elif OOOOO0OOOO0OOOOO00OOOOOOOOO0O0OO == "body":
            body_height -= 10
    
    
    def OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOO0OO0OO0OOO0OOOOOOOOOOO0OO0OOOOO00OOOOOO0OOOOOO0():
        """
        Add a square shape to the character.
    
        Returns:
            None
        """
        x, y, width, height, _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = 50, 400, 50, 50, (255, 0, 0)
        add_shape(x, y, width, height, color)
    
    
    def O00OOOOO0O000OOOOOO0O0O00O000OOOO0OO0OO000000OOO():
        """
        Finish character customization and export the character.
    
        Returns:
            str: Path to the exported character image.
    
        """
        global character_sprite, shapes_sprites, head_size, body_height, leg_length
    
        pygame.draw.rect(background, (0, 0, 0, 0), pygame.Rect(500, 50, 400, 1000))
        pygame.draw.rect(background, (0, 0, 0, 0), sidebar_rect)
    
        # Divide the character sizes by 4
        # head_size //= 8
        # body_height //= 4
        # leg_length //= 4
        # draw_character()
        # _O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOOO0OO0OOOO0OO0OO0OOOOO0OO00OOOOOO0O000OOOOOO0O0OO0OOOOOO0 = pygame.sprite.GroupSingle()
        # character_sprite.add(pygame.sprite.Sprite())
        # character_sprite.sprite._O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = background.copy()
        # shapes.clear()
        export_character(path + r"\\Recources\\characters\\current.png")
        return path + r"\\Recources\\characters\\current.png"
    
    
    def _OOOOOO0OOOOOO0O0OO0OO00OOOOOO0OOO0O0OOO0OO0OOO00O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOO():
        """
        Reset the character's head size, body height, and clear all shapes.
    
        Returns:
            None
        """
        global head_size, body_height, shapes
        _OOO0OOOOOO0OO0OOOOOO0OOO0OOO0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = 50
        OOOOOOOO0OO000O0O0OOO0OOOOOO0OOOO0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 100
        O0OO0OO000000OOOOO0OOOOOOOOOO0OO0OOOOOO0O0OO0OO0 = []
        background.fill(TRANSPARENT)
    
    
    def OOO0O0OO0OO000O0O0OOOOOOO0OOOOOOOOO000OO0OOOOOO0O0OO0OOOOOO0O0OO00OOOOOOOO0OOOOO0O000OOOOOO000OOO0OO0OO0():
        """
        Toggle the trails effect.
    
        Returns:
            None
        """
        global trails
        OOO0O0OO00OOOOOOOO0OOOOO0O000OOOOOO000OOO0OO0OO0 = not trails
    
    
    def O0OO0OO0OO0OOOOOO0O000OO0OOOOOO0O0OO0OOO00O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOOO0OO0OOOO0OOO0OO0O000OOOOO0OOOOOOOO000OO0OO000O0O0OOOOOO():
        """
        Open a file dialog for saving the character image.
    
        Returns:
            None
        """
        O00OOOOO0O000OOOOOO000OO0OOOOOO0OOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = filedialog.asksaveasfilename(
            O0OOO0OO0OOOOOO0O00OOOOOOO0OOOOOOOOOOOO0OOO000OOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO0OOOOOO0OOO0O0O0O0OO0OO00O000OOO0OO000O0OOO0O0O0=".png",
            O00OOOOO0O000OOOOOO000OO0OOOOOO0OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0O0OO0OO0=[("PNG files", "*.png")],
            _O000OOOOOO0O0O00O000OOOOOO0O0OO0O000OOOOO0OOOOOOOO000OOO0OOO0OO0O000OOO00OOOOOO=path + r"\\Recources\\characters\\",
        )
        if filename:
            export_character(filename)
    
    
    def OOO000OO0OO000O0OO0OOOOOO0OOO0OOO0OO0OOO00O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOOO0OO0OOOO0OOO0OO0O000OOOOO0OOOOOOOO000OO0OO000O0O0OOOOOO():
        """
        Open a file dialog for loading a character image.
    
        Returns:
            None
        """
        O00OOOOO0O000OOOOOO000OO0OOOOOO0OOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = filedialog.askopenfilename(
            O00OOOOO0O000OOOOOO000OO0OOOOOO0OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0O0OO0OO0=[("PNG files", "*.png")],
            _O000OOOOOO0O0O00O000OOOOOO0O0OO0O000OOOOO0OOOOOOOO000OOO0OOO0OO0O000OOO00OOOOOO=path + r"\\Recources\\characters\\",
        )
        if filename:
            load_character(filename)
    
    
    def _OOOOOO0O00OO000OOOOO0OO0OO000O000OOOOOOOOO0O0OOO0OO0OOO00O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOO(filename):
        """
        Export the character image to the specified file.
    
        Args:
            filename (str): The path where the character image will be saved.
    
        Returns:
            None
        """
        pygame.draw.rect(background, (0, 0, 0, 0), pygame.Rect(500, 50, 400, 1000))
        pygame.image.save(background, filename)
    
    
    def OOO000OO0OO000O0OO0OOOOOO0OOO0OOO0OO0OOO00O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOO(filename):
        """
        Load a character image 
            from the specified file and display it.
    
        Args:
            filename (str): The path of the character image to load.
    
        Returns:
            None
        """
        OOO000OO0OO000O0OO0OOOOOO0OOO0OO0OOOOOO0O0OOO0OOO0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = pygame.image.load(filename)
        screen.blit(loaded_image, (0, 0), (WIDTH, HEIGHT))
        pygame.display.update()
    
    
    if __name__ == "__main__":
        main()
    
    
    # import pygame
    # import sys
    #
    ## Initialize pygame
    # pygame.init()
    #
    ## Constants
    # WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = 800, 600
    # _OO0OO0OO0O0O0OOOO00OOOOO0O0OOOO0OO0OOOOOOOOOO0OO0O0O0OOOOO0000OO0O0OOO = 32
    # GRID_WIDTH, OOOOOO0OOOOO0OO0OO0O0O0O0OOOOO00O0OO0OOO000O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE
    # OOOO00OO000O00OOOO0O0O0O00OO0OO0OO0O0OOO = (255, 255, 255)
    # _O00OOOOOOO00OOOOOOOO0OOOO0OOOOOO0OOOO0O = (0, 0, 0)
    #
    ## Create the screen
    # O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pygame.display.set_mode((WIDTH, HEIGHT))
    # pygame.display.set_caption("Tile Map Editor")
    #
    ## Create a 2D array to represent the grid
    # O0OOOOOO00OOOOOO0O000OOOO0OOO0OO = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    #
    ## Define a function to draw the grid
    # def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOO0OOOOOO00OOOOOO0O000OOOO0OOO0OO():
    #    for row in range(GRID_HEIGHT):
    #        for col in range(GRID_WIDTH):
    #            if grid[row][col] == 1:
    #                pygame.draw.rect(screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    #
    ## Game loop
    # _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
    # O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO00O000OOOOOO0O0O0O0OOOOOO = False  # Indicates whether the user is drawing tiles
    # _OOOOOO000OOOOOOOO0OOOOOO0OO0OO00O000OOOOOO0O0O0O0OOOOOO = False  # Indicates whether the user is erasing tiles
    #
    # while running:
    #    for event in pygame.event.get():
    #        if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
    #            _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
    #        elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN:
    #            if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:  # Left mouse button
    #                O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO00O000OOOOOO0O0O0O0OOOOOO = True
    #            elif event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 3:  # Right mouse button
    #                _OOOOOO000OOOOOOOO0OOOOOO0OO0OO00O000OOOOOO0O0O0O0OOOOOO = True
    #        elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONUP:
    #            O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO00O000OOOOOO0O0O0O0OOOOOO = False
    #            _OOOOOO000OOOOOOOO0OOOOOO0OO0OO00O000OOOOOO0O0O0O0OOOOOO = False
    #        elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN:
    #            if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_s:  # Save the grid to a file when 's' key is pressed
    #                with open("grid.txt", "w") as file:
    #                    for row in grid:
    #                        file.write(" ".join(map(str, row)) + "\n")
    #
    #    # Get the mouse position
    #    mouse_x, O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0O0OO0OOOOOOO0OOO = pygame.mouse.get_pos()
    #
    #    # Convert mouse position to grid coordinates
    #    _O0OOOO0OO000O0OOO000OO = mouse_x // TILE_SIZE
    #    _OOOOOO0OO000O0OO0OOOO0 = mouse_y // TILE_SIZE
    #
    #    # Draw or erase tiles based on mouse input
    #    if drawing:
    #        if 0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT:
    #            grid[row][col] = 1
    #    elif erasing:
    #        if 0 <= col < GRID_WIDTH and 0 <= row < GRID_HEIGHT:
    #            grid[row][col] = 0
    #
    #    # Fill the screen with white
    #    screen.fill(WHITE)
    #
    #    # Draw the grid
    #    draw_grid()
    #
    #    # Update the display
    #    pygame.display.flip()
    #
    ## Quit pygame
    # pygame.quit()
    # sys.exit()
    #    import pygame
    from pygame import RESIZABLE
    
    import socket
    
    import threading
    
    import ipaddress
    
    import SquarePixels.multiplayer.client as client
    
    OOOOOOO0OO0O0OOOOOOO0OO0O0OOO0OOOO0O0OOOOOOO0OO0O0OO0OOOOOO0OOOOOOO0OOOOOOOO0OO000OO0OO0 = 12345
    _OO0OO0OO0O0O0OOOOO00OOOO0O0OOOOOO0OOOO0O0OOO0O00OO0OO0 = 1.0  # Timeout value for socket operations
    OOOOOOO0OO0OOOOOOOOOO0OOOOOOO0OOO0OO0OOO00OO0OO0OO0O0O0OOOOO00OOOO0O0OOOOOO0OOOO0O0OOO0O00OO0OO0 = 2.0  # Timeout value for server scanning
    OOOOOOO0OO0OOOOOOOOOO0OOOOOOO0OOO0OO0OOO00OO0OO0000O00OOOOOO0OO0OO0O0OOOOOOOO0OO0OOOOO00OOOOOOO0 = 50  # Number of threads for concurrent scanning
    pygame.init()
    infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.display.Info()
    WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = infoObject.current_w, infoObject.current_h
    _O00OOOOOOOOO0OOOO0OOOOOO0OOOO0OOOOOOO0OOOOO0OO0OOO0OOOO0O0OOO0OOOOOO0OO0OOOOO00O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (255, 255, 255)
    _OO0OO0OO0O0OOOOOOO0OOO00OO0OO0O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (0, 0, 0)
    _O000OOOOOOOO0OO = ""
    pygame.init()
    O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
    pygame.display.set_caption("Server Finder")
    _O0OOOOOOO000OO0OO000O000O0OOOO0OOOOO0O = pygame.time.Clock()
    O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.SysFont(None, 24)
    
    _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
    O0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OO0 = []
    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOO = None
    _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = "Name"
    O0OO0OO00OOOOOO0OOO0O0OOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OO0 = True
    
    
    def _O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0OO0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOO(server_ip):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(TIMEOUT)
                _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = sock.connect_ex((server_ip, SERVER_PORT))
                if _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO == 0 and server_ip not in servers:
                    servers.append(server_ip)
        except:
            pass
    
    
    def O0OO0OO000O0OOOOOO0OOOOOOOO0O0O0O0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OO0(ip_range):
        OOO0O0O00OOOOOO0OOO0O0OOOO0OOOO00OO000O000OOOOOO0OOOOO0O = ipaddress.ip_network(ip_range)
        for ip_address in network.hosts():
            O0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OOO0O000OOOOOOOO0OO = str(ip_address)
            threading.Thread(OOO0O0OOOO0OOOOO00OOOOOOO0OOOOOO0OOOOOO0OOO0O0OO=check_server, OO0OOOOO00OOOOOOO0OOOOOOO0OO0OO0=(server_ip,)).start()
    
    
    def O00OOOOO0O000OOOOOO0O0O0O0OOO0OOO0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OO0():
        global running
        if running:
            _OOO0OO000O0O0OO0OO0OOO0O0OOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = socket.gethostname()
            _O000OOOOOOOO0OOO0OO0OOOOO0OOOOOO0OOO0OOO0OOO0OO00OOOOOO0OOOOOO0O0OO0OO0O0OO0OO0 = socket.gethostbyname(hostname)
            OOO0O0O00OOOOOO0OOO0O0OOOO0OOOO00OO000O000OOOOOO0OOOOO0O = ipaddress.ip_network(ip_address, O0OO0OO0OOO0O0OO00OOOOOO0O000OOO00O0OOOOOOO0O0OO=False)
            _O000OOOOOOOO0OOO0OO0OOO00OOOOOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0 = f"{network.network_address}/{network.prefixlen}"
    
            print("Automatically selected IP range:", ip_range)
            print("Scanning for servers...")
            scan_servers(ip_range)
    
            threading.Timer(SCAN_TIMEOUT, find_servers).start()
    
    
    def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO(text, x, y):
        OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = font.render(text, True, TEXT_COLOR)
        OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text_surface.get_rect()
        text_rect.OOO0O0OO0OO000O0OOOOO0OOOOO000OO0OOOOOO0O00OOOOOOOO0O0OO = (x, y)
        screen.blit(text_surface, text_rect)
    
    
    def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OOO00O0OOOOOOO000OO0O000OOO00O0OOOO0OOOOO0O(selected_server):
        if selected_server is not None:
            # Perform actions based on the selected server
            print("Clicked on server:", selected_server)
            _O000OOOOOOOO0OO = selected_server
            # client.main(selected_server)
            handle_server_options(ip)
    
    
    def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OOO0OO000O0OOOOO0OOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OO0(ip) -> None:
        global player_name, character_image, input_text, settings
    
        _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect(10, 400, 200, 30)
        _O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect(220, 400, 100, 100)
        _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
    
        while settings:
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN:
                    if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                        if input_rect.collidepoint(event.pos):
                            _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                        else:
                            _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN:
                    if input_active:
                        if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_RETURN:
                            # Save the player name and character image
                            O0OO0OO00OOOOOO0OOO0O0OOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OO0 = False
                            client.main(ip, input_text)
                            OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = input_text
                            # _O0OOOO00000OOOOO0OOOOO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OO0OOOOOO000OOOOOOO0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = ...  # Save the selected character image
                            print("Player Name:", player_name)
                            print("Character Image:", character_image)
                            pygame.quit()
                            return
                        elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_BACKSPACE:
                            _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = input_text[:-1]
                        else:
                            input_text += event.unicode
    
            screen.fill(BACKGROUND_COLOR)
            pygame.draw.rect(screen, (200, 200, 200), input_rect, 2)
    
            if input_active:
                pygame.draw.rect(screen, (200, 200, 200), input_rect, 0)
    
            _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = font.render(input_text, True, TEXT_COLOR)
            screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))
    
            pygame.draw.rect(screen, (200, 200, 200), character_rect, 2)
            # Draw the selected character image in the character_rect
    
            pygame.display.flip()
            clock.tick(60)
    
    
    def O0O0OO00OO0OOOOO0O000OOOOOO0O0O0():
        global running
        while running:
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
                    quit()
    
            screen.fill(BACKGROUND_COLOR)
            draw_text("Found Servers:", 10, 10)
    
            for i, server in enumerate(servers):
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = f"Server {i+1}: {server}"
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = font.render(text, True, TEXT_COLOR)
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text_surface.get_rect()
                text_rect.OOO0O0OO0OO000O0OOOOO0OOOOO000OO0OOOOOO0O00OOOOOOOO0O0OO = (10, 40 + i * 30)
                if text_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.draw.rect(screen, (200, 200, 200), text_rect)
                    if pygame.mouse.get_pressed()[0]:
                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOO = server
                        _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
                        handle_server_click(selected_server)
                screen.blit(text_surface, text_rect)
    
            pygame.display.flip()
            clock.tick(60)
    
        pygame.quit()
    
    
    if __name__ == "__main__":
        find_servers()
        main()    
        import pygame as pig
    from playfab import PlayFabSettings, PlayFabErrors, PlayFabHTTP
    
    import json
    
    import requests
    from SquarePixels.uimanagement.MainMen import SignInScreen, em, p
    
    
    def _OOOOO000OO000O0OOO0OOOO0OO000O0O0OO0OO0OOO0O0OO(
        urlPath, request, authKey, authVal, callback, _O0OOOOOOOOOOO0O0OO0OO0OOO0O0OO0OO000O0O0O0OO000OOOOO00OO0OOOOOOOO0O0OOOO0OOOOO=None, _OOOOOO0O00OO000OOO0O0OO00OOOOOOOO0OOOOO000O00OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0=None
    ):
        """
        Note this is a blocking call and will always run synchronously
        the return type is a dictionary that should contain a valid dictionary that
        should reflect the expected JSON response
        if the call fails, there will be a returned PlayFabError
        """
    
        OOOOOOO000OOOOOOOOO000OO = PlayFabSettings.GetURL(
            urlPath, PlayFabSettings._internalSettings.RequestGetParams
        )
    
        try:
            O0OOOO0O = json.dumps(request)
        except Exception as e:
            raise PlayFabErrors.PlayFabException(
                "The given request is not json serializable. {}".format(e)
            )
    
        _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO000O00OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0 = {}
    
        if extraHeaders:
            requestHeaders.update(extraHeaders)
    
        requestHeaders["Content-Type"] = "application/json"
        requestHeaders["X-PlayFabSDK"] = PlayFabSettings._internalSettings.SdkVersionString
        requestHeaders[
            "X-ReportErrorAsSuccess"
        ] = "true"  # Makes processing PlayFab errors a little easier
    
        if authKey and authVal:
            requestHeaders[authKey] = authVal
    
        _OOOOOO0O0OOOOO0O0OOOOOOO0OOOOOO0OO00OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0 = requests.post(url, O0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO=j, _OOO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0=requestHeaders)
        print(httpResponse)
    
        _OOOOOO000OOOOOO00OOOOOO0OO000O000OOOOOO = _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0 = None
    
        if httpResponse.status_code != 200:
            # Failed to contact PlayFab Case
            _OOOOOO000OOOOOO00OOOOOO0OO000O000OOOOOO = PlayFabErrors.PlayFabError()
    
            error._O00OOOOO0O0OOOOO0O0OOOOOOO0OOOO0OOOOO0OO000O0O0OOO0OO0OOOOOO0 = httpResponse.status_code
            error._O00OOOOO0O0OOOOO0O0OOOOOOO0OOOOOOOOO0OOO0O0OOOO0OOOOOOOO0O0OOOOOOOOO0O0OO0OO0 = httpResponse.reason
        else:
            # Contacted playfab
            _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0OOOO00OO00OOOOOOOO0OOOOOOOOOO0OOOOOOO0OO0OOOOOO000OOOOOO = json.loads(httpResponse.content.decode("utf-8"))
            # print(responseWrapper)
            if responseWrapper["code"] != 200:
                # contacted PlayFab, but response indicated failure
                _OOOOOO000OOOOOO00OOOOOO0OO000O000OOOOOO = responseWrapper
                return None
            else:
                # successful call to PlayFab
                _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0 = responseWrapper["data"]
                return response
    
        if error and callback:
            callGlobalErrorHandler(error)
    
            try:
                # Notify the caller about an API Call failure
                callback(None, error)
            except Exception as e:
                # Global notification about exception in caller's callback
                PlayFabSettings.GlobalExceptionLogger(e)
        elif (response or _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0 == {}) and callback:
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
                _OOOOOO0O0O0OO00OOOOO0OOOOO0O0OOOOOO0OOOOOOO0OO00OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0OO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOO = PlayFabErrors.PlayFabError()
                emptyResponseError.OO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOO = "Empty Response Recieved"
                emptyResponseError.OO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOOOOOO00OO0OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0 = "PlayFabHTTP Recieved an empty response"
                emptyResponseError.OO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOOOO0OOOOO0OO000O0O0OOO0OO0OOOOOO0 = PlayFabErrors.PlayFabErrorCode.Unknown
                callback(None, emptyResponseError)
            except Exception as e:
                # Global notification about exception in caller's callback
                PlayFabSettings.GlobalExceptionLogger(e)
    
    
    def _O0OOOOOO0OOOOOOOO000OOOOO000OOOOOOOO0OOOO000OO0OO000O0OOOOOOOOOO0OOOOOOOO000OOOO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOO000O00OOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO000OOOOOO(error):
        if PlayFabSettings.GlobalErrorHandler:
            try:
                # Global notification about an API Call failure
                PlayFabSettings.GlobalErrorHandler(error)
            except Exception as e:
                # Global notification about exception in caller's callback
                PlayFabSettings.GlobalExceptionLogger(e)
    
    
    def OOOOOO0O0OOOOOO0OOO0O0OOOOO0OOOOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOOOOOOOO0OOO0O0OOOO0OOOOOOOO0O0OO0O000OOOO0OO0OO0OOO0O0OO0O000OOO00O0OOOOO0OO0OO0(request, callback, _O0OOOOOOOOOOO0O0OO0OO0OOO0O0OO0OO000O0O0O0OO000OOOOO00OO0OOOOOOOO0O0OOOO0OOOOO=None, _OOOOOO0O00OO000OOO0O0OO00OOOOOOOO0OOOOO000O00OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0=None):
        """
        Retrieves the indicated statistics (current version and values for all statistics, if none are specified), for the local
        player.
        https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getplayerstatistics
        """
        if not PlayFabSettings._internalSettings.ClientSessionTicket:
            raise PlayFabErrors.PlayFabException("Must be logged in to call this method")
    
        def OO0OOOO000OOOOOOOO0OOOOOOOOOO0OOOOOOO0OO0OOOOOO0O0OOO0OOOO0OOOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(playFabResult, error):
            if callback:
                callback(playFabResult, error)
    
        return DoPost(
            "/Client/GetPlayerStatistics",
            request,
            "X-Authorization",
            PlayFabSettings._internalSettings.ClientSessionTicket,
            wrappedCallback,
            customData,
            extraHeaders,
        )
    
    
    def _O0OOO0OOOOOO0OOO0OOO0OOOO0OOOOOOOO0O0OO0OOOOOO0OOO0OOOOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOOOOOOOO0OOO0O0OOOO0OOOOOOOO0O0OO0O000OOOO0OO0OO0OOO0O0OO0O000OOO00O0OOOOO0OO0OO0(request, callback, _O0OOOOOOOOOOO0O0OO0OO0OOO0O0OO0OO000O0O0O0OO000OOOOO00OO0OOOOOOOO0O0OOOO0OOOOO=None, _OOOOOO0O00OO000OOO0O0OO00OOOOOOOO0OOOOO000O00OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0=None):
        """
        Updates the values of the specified title-specific statistics for the user. By default, clients are not permitted to
        update statistics. Developers may override this setting in the Game Manager > Settings > API Features.
        https://docs.microsoft.com/rest/api/playfab/client/player-data-management/updateplayerstatistics
        """
        if not PlayFabSettings._internalSettings.ClientSessionTicket:
            raise PlayFabErrors.PlayFabException("Must be logged in to call this method")
    
        def OO0OOOO000OOOOOOOO0OOOOOOOOOO0OOOOOOO0OO0OOOOOO0O0OOO0OOOO0OOOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(playFabResult, error):
            if callback:
                callback(playFabResult, error)
    
        PlayFabHTTP.DoPost(
            "/Client/UpdatePlayerStatistics",
            request,
            "X-Authorization",
            PlayFabSettings._internalSettings.ClientSessionTicket,
            wrappedCallback,
            customData,
            extraHeaders,
        )
    
    
    def O0OOO0OO0OO000O0O0OO0OOOOOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OOO0OO0OOOOOOOOOO0OOOOO0OOO0OOO0OOOO0OOOOOOOO0O0OO0OOOOOO0O0OO0OO0(xp, width, height, death_text, screen):
        # Function to display a message on the screen
        SignInScreen.sign_in_with_email(None, em, p)
    
        def O0OOO0OO0O000OOOO0OO0OO0OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0(message, _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO=(255, 0, 0)):
            global current_message
            _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0 = message
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = death_text.render(message, True, color)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text_surface.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=(width // 2, height // 3))
            screen.blit(text_surface, text_rect)
    
        def _O0OOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(success, failure):
            if success:
                print("success")  # OOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = success.data.Leaderboard
            # O0OOOOOO0OO000O00OO000O0O0OOO0OO = True
            # display_message("Account created and signed in.", (0, 255, 0))
            else:
                print("failed to fetch leaderboard position")
                display_message("failed to fetch leaderboard position")
                if failure:
                    display_message("Here's some debug information:")
                    display_message(str(failure) + "leader board position")
                    print("Here's some debug information:")
                    print(str(failure) + "leader board")
    
        _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"StatisticNames": "XP"}
        _O0OOOOO00OO000OOOOO0OO = GetPlayerStatistics(
            request, callback
        )  # example output {"Statistics": [{"StatisticName": "XP", "Value": 900, "Version": 0}]}
        if cxp:
            O0O000OO0OOOOOO000OOOOOOO0OO0OO00O000OOO0OO000O0OOO0O0O0 = cxp["Statistics"][0]["Version"]
            _O0OOOOO00OO000OOOOO0OO = cxp["Statistics"][0]["Value"]
            print(cxp)
            if cxp:
                if cxp < xp:
                    print("hello")
                    _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {
                        "Statistics": [
                            {"StatisticName": "XP", "Value": xp, "Version": version}
                        ]
                    }
                    UpdatePlayerStatistics(request, callback)
            else:
                _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"StatisticName": "XP", "Value": xp}
                UpdatePlayerStatistics(request, callback)
        else:
            _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"StatisticName": "XP", "Value": xp}
            UpdatePlayerStatistics(request, callback)
    
    
    def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOO0OOO0OO0OOOOOO0OO0OOOOOOOO0O0OO00000OOOO0OO0OOOO0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0(screen, width, height, xp):
        clock: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pig.time.Clock()
        O0OOO0OO0OOOOOO0OO0OOOOOOOO0O0OO00000OOOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = pig.font.Font("Recources\Fonts\PixelifySans-Regular.ttf", 50)
        O0OOO0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = death_text.render("You Died", True, (255, 255, 255))
        O00OO000OOOOO0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = death_text.render(f"Your Score: {xp}", True, (255, 255, 255))
        O0OOO0OO0OOOOOO0OO0OOOOOOOO0O0OO00000OOOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = d_text.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=(width // 2, height // 3))
        O00OO000OOOOO0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = xp_text.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=(width // 2, height // 3 + 50))
        # Define buttons
        _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = pig.Rect(width // 4, height // 2, 200, 50)
        O0O0OO000OOOOOO0OOO0O0O0OOOOOOO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = pig.Rect(3 * width // 4, height // 2, 200, 50)
        try:
            do_leaderboard_updates(xp, width, height, death_text, screen)
        except Exception as e:
            print(e)
        while True:
            for event in pig.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.QUIT:
                    pig.quit()
                    quit()
            screen.fill((0, 0, 0))
            screen.blit(d_text, death_text_rect)
            screen.blit(xp_text, xp_text_rect)
            # Check if the mouse is hovering over the buttons
            if respawn_button.collidepoint(pig.mouse.get_pos()):
                pig.draw.rect(screen, (150, 150, 150), respawn_button)
                _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = death_text.render("Respawn", True, (0, 0, 0))
                _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = respawn_text.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=respawn_button.center)
                screen.blit(respawn_text, respawn_text_rect)
                if pig.mouse.get_pressed()[0]:
                    return True
            else:
                pig.draw.rect(screen, (255, 255, 255), respawn_button)
                _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = death_text.render("Respawn", True, (0, 0, 0))
                _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OOOO0OOOOOOO0OOOO0OOO0O0O0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = respawn_text.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=respawn_button.center)
                screen.blit(respawn_text, respawn_text_rect)
    
            if menu_button.collidepoint(pig.mouse.get_pos()):
                pig.draw.rect(screen, (150, 150, 150), menu_button)
                O0O0OO000OOOOOO0OOO0O0O0OOOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = death_text.render("Main Menu", True, (0, 0, 0))
                O0O0OO000OOOOOO0OOO0O0O0OOOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = menu_text.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=menu_button.center)
                screen.blit(menu_text, menu_text_rect)
                if pig.mouse.get_pressed()[0]:
                    return False
            else:
                pig.draw.rect(screen, (255, 255, 255), menu_button)
                O0O0OO000OOOOOO0OOO0O0O0OOOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = death_text.render("Main Menu", True, (0, 0, 0))
                O0O0OO000OOOOOO0OOO0O0O0OOOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = menu_text.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=menu_button.center)
                screen.blit(menu_text, menu_text_rect)
            pig.display.flip()
            clock.tick(60)    
            import random
    
    import pygame as pig
    
    pig.init()
    
    _O000OOOOOO0O0O0O00OOOOO0OO000O0OOO0OOOOOOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pig.display.Info()
    O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pig.display.set_mode((infoObject.current_w, infoObject.current_h))
    
    # Create item surfaces
    _O000OOOOOO0O0OO0OOOOOO0O0O0OO00O0OO0OO0 = [pig.Surface((50, 50), pig.SRCALPHA) for x in range(4)]
    OO0OOOO00OO000O00OO000O0O0OOO0OO = pig.image.load(r"Recources\Textures\wood.png")
    O0OO0OO0OOO0O0OO0OO000O0OOO0O0O00OOOOOO0 = pig.image.load(r"Recources\Textures\stone.jpg")
    O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0 = (25, 25)
    OO0OOOO00OO000O00OO000O0O0OOO0OO = pig.transform.scale(wood, scale)
    O0OO0OO0OOO0O0OO0OO000O0OOO0O0O00OOOOOO0 = pig.transform.scale(stone, scale)
    items[0].blit(wood, (15, 15, 100, 100))
    items[1].blit(stone, (15, 15, 100, 100))
    # Create a green sword item
    pig.draw.circle(items[2], (0, 255, 0), (25, 25), 25)
    # Create a blue circle item
    pig.draw.circle(items[3], (0, 0, 255), (25, 25), 25)
    
    O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pig.font.Font(pig.font.match_font("calibri"), 26)
    
    
    class OO0O0O0OOOO0O0OO0OOOOOO0O0O0OO00:
        """
        Represents an item with an associated image and ID.
    
        Args:
            id (int): The ID of the item.
    
        Attributes:
            id (int): The ID of the item.
            surface (pygame.Surface): The image representing the item.
        """
    
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, id):
            self._O000OOOO0OOO0OO = id
            self.O0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = items[id]
    
        def _OOOOOO0OOOOOO0O0OO0OO00O000OOO0OOOOOOO0OOOOOO0(self, size):
            """
            Resize the item's image.
    
            Args:
                size (int): The size to resize the image to.
    
            Returns:
                pygame.Surface: The resized image.
            """
            return pig.transform.scale(self.surface, (size, size))
    
    
    class OO0O0O0OOOO0O0O0O0O000OO0OOOOOO0OOO0O0O0OOO0O0OO0OO000O000OOOOOOOOOO0OOO:
        """
        Represents an inventory for managing items.
    
        Args:
            rows (int): The number of rows in the inventory grid.
            col (int): The number of columns in the inventory grid.
            box_size (int): The size of each inventory slot.
            x (int): The x-coordinate of the top-left corner of the inventory grid.
            y (int): The y-coordinate of the top-left corner of the inventory grid.
            border (int): The border size around each inventory slot.
        """
    
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(
            self, _OOOOOO0OO000O0OO0OOOO0O0OO0OO0=9, _O0OOOO0OO000O0OOO000OO=27, OOOOOOOO0OO000O0O00OO000O0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0=infoObject.current_w // 30, O00OO000=50, OOOO0OOO=50, OOOOOOOO0OO000O000OOOOOOO0OOO0OO0OOOOOO000OOOOOO=3
        ):
            self._OOOOOO0OO000O0OO0OOOO0O0OO0OO0 = rows
            self._O0OOOO0OO000O0OOO000OO = col
            self._O000OOOOOO0O0OO0OOOOOO0O0O0OO00O0OO0OO0 = [[None for _ in range(self.rows)] for _ in range(self.col)]
            self.OOOOOOOO0OO000O0O00OO000O0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = box_size
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.OOOOOOOO0OO000O000OOOOOOO0OOO0OO0OOOOOO000OOOOOO = border
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, ychange):
            """
            Draw the inventory grid on the screen.
    
            Args:
                ychange (list): A list containing a boolean value indicating if the y-position should change,
                               and the new y-position.
            """
            OOO0O0OO0OOOOOO0O0O0OO00OOOOO0OO = self.y
            if ychange[0]:
                self.OOOO0OOO = ychange[1]
            pig.draw.rect(
                screen,
                (100, 100, 100),
                (
                    self.x,
                    self.y,
                    (self.box_size + self.border) * self.col + self.border,
                    (self.box_size + self.border) * self.rows + self.border,
                ),
            )
            for x in range(self.col):
                for y in range(self.rows):
                    _OOOOOO0OOOOOO000O0OOOOOOO0O0OO = (
                        self.x + (self.box_size + self.border) * x + self.border,
                        self.y + (self.box_size + self.border) * y + self.border,
                        self.box_size,
                        self.box_size,
                    )
                    pig.draw.rect(screen, (180, 180, 180), rect)
                    if self.items[x][y]:
                        screen.blit(self.items[x][y][0].resize(self.box_size), rect)
                        _OO000O0OOOOOOOOO0OOOO0O = font.render(str(self.items[x][y][1]), True, (0, 0, 0))
                        screen.blit(
                            obj,
                            (rect[0] + self.box_size // 2, rect[1] + self.box_size // 2),
                        )
            # self.OOOO0OOO = temp
    
        def OOOOOO0O0OOOOOO0OOO0O0OOO0OO0OOOOOOOO0OO0OO000O0O0OO0OO0(self):
            """
            Get the position in the inventory grid where the mouse cursor is located.
    
            Returns:
                tuple: A tuple containing the x and y coordinates of the grid position.
            """
            O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0 = pig.mouse.get_pos()
            O00OO000 = mouse[0] - self.x
            OOOO0OOO = mouse[1] - self.y
            O00OO000 = x // (self.box_size + self.border)
            OOOO0OOO = y // (self.box_size + self.border)
            return (int(x), int(y))
    
        def OOOOO0OOO0OOO0OOO0OOO0OO(self, Item, xy):
            """
            Add an item to the inventory grid at the specified position.
    
            Args:
                Item (Item): The item to add.
                xy (tuple): A tuple containing the x and y coordinates of the position.
            """
            x, OOOO0OOO = xy
            if self.items[x][y]:
                if self.items[x][y][0]._O000OOOO0OOO0OO == Item[0].id:
                    self.items[x][y][1] += Item[1]
                else:
                    OOO0O0OO0OOOOOO0O0O0OO00OOOOO0OO = self.items[x][y]
                    self.items[x][y] = Item
                    return temp
            else:
                self.items[x][y] = Item
    
        def OO0O0O0OOOO0O0O0O0OO0OOOO0OOOOOO00OOOOOO0O000OOOO0OOO0OO(self, x, y):
            """
            Check if the specified coordinates are within the inventory grid.
    
            Args:
                x (int): The x-coordinate to check.
                y (int): The y-coordinate to check.
    
            Returns:
                bool: True if the coordinates are within the grid, False otherwise.
            """
            # print(
            #    f"x: {x} y: {y} {self.x} {self.y} {self.x+self.col +1*self.box_size} {self.y+self.rows*self.box_size}"
            # )
            if (
                x >= self.x
                and x <= self.x + ((self.col + 1) * self.box_size)
                and y >= self.y
                and y <= self.y + (self.rows * self.box_size)
            ):
                return True
            else:
                return False
    
        def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOO0O000OOOOOO0O0OO0OOOOOO0O0O0OO00(self, itemId):
            """
            Get an item with the specified item ID and add it to the inventory.
    
            Args:
                itemId (int): The ID of the item to retrieve.
            """
            OOO000OO0OO000O00OO000O00OOOOO0O0O000OOOOOO0O0O0O0OOOOOOO00OOOOO0OO000O000OOOOOOO0OO0OO0OOOOO0OO0OO000O0OOO0O0OO = True
            if itemId is not None:
                _O000OOOOOO0O0OO0OOOOOO0O0O0OO00 = Item(itemId)
                O00OO000 = 0
                OOOO0OOO = 0
                while lookingforspot:
                    if self.items[x][y]:
                        if self.items[x][y][0]._O000OOOO0OOO0OO == itemId:
                            OOO000OO0OO000O00OO000O00OOOOO0O0O000OOOOOO0O0O0O0OOOOOOO00OOOOO0OO000O000OOOOOOO0OO0OO0OOOOO0OO0OO000O0OOO0O0OO = False
                        else:
                            self.items[x][y] = item
                            OOO000OO0OO000O00OO000O00OOOOO0O0O000OOOOOO0O0O0O0OOOOOOO00OOOOO0OO000O000OOOOOOO0OO0OO0OOOOO0OO0OO000O0OOO0O0OO = False
                    else:
                        self.items[x][y] = item
                        OOO000OO0OO000O00OO000O00OOOOO0O0O000OOOOOO0O0O0O0OOOOOOO00OOOOO0OO000O000OOOOOOO0OO0OO0OOOOO0OO0OO000O0OOO0O0OO = False
    
        def OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO0O0OO0OOO0O000OOOOOO0O0OO0OOOOOO0O0O0OO00O0OO0OOO0O000OOOOOO0O0O0O0OO0OOO00O0OOOO00OOOOOOOO0OOOOOO00OOOOOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO0OOOOOO00OOOOOO0O000OOOO0OOO0OO(self, item, x, y):
            """
            Place an item in the crafting grid at the specified position.
    
            Args:
                item (Item): The item to place in the grid.
                x (int): The x-coordinate of the grid position.
                y (int): The y-coordinate of the grid position.
            """
            crafting_grid[y][x] = item
    
        def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOO0O000OOOOOO0O0OO0OOOOOO0O0O0OO00O0OO0OOOO00OOOOO00OOOOOO0OO000O0O0O0OO00O0OO0OOO00O0OOOO00OOOOOOOO0OOOOOO00OOOOOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO0OOOOOO00OOOOOO0O000OOOO0OOO0OO(self, x, y):
            """
            Get the item 
            from the crafting grid at the specified position.
    
            Args:
                x (int): The x-coordinate of the grid position.
                y (int): The y-coordinate of the grid position.
    
            Returns:
                Item: The item in the grid position, or None if no item is present.
            """
            return crafting_grid[y][x]
    
        def _O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OOO0OO0OOO0O000OOOOOO0O0OO0OOOOOO0O0O0OO00(self, item_id, inventory):
            """
            Count the number of items with the specified item ID in the inventory.
    
            Args:
                item_id (int): The ID of the item to count.
                inventory (Inventory): The inventory to search.
    
            Returns:
                int: The count of items with the specified ID.
            """
            _O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = 0
            for x in range(inventory.col):
                for y in range(inventory.rows):
                    if inventory.items[x][y] and inventory.items[x][y][0]._O000OOOO0OOO0OO == item_id:
                        count += inventory.items[x][y][1]
            return count
    
        def _OOOOOO0OOOOOO0O0O0OO000OO000O0O0O000OO0OOOOOO0O0OO0OOO0O000OOOOOO0O0OO0OOOOOO0O0O0OO00(self, item_id, count, inventory):
            """
            Remove a specified count of items with the given item ID 
                from the inventory.
    
            Args:
                item_id (int): The ID of the item to remove.
                count (int): The count of items to remove.
                inventory (Inventory): The inventory to remove items from.
            """
            for x in range(inventory.col):
                for y in range(inventory.rows):
                    if inventory.items[x][y] and inventory.items[x][y][0]._O000OOOO0OOO0OO == item_id:
                        if inventory.items[x][y][1] >= count:
                            inventory.items[x][y][1] -= count
                            if inventory.items[x][y][1] == 0:
                                inventory.items[x][y] = None
    
    
    OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOO0O000OOOOOO0O0O0O0O000OO0OOOOOO0OOO0O0O0OOO0O0OO0OO000O000OOOOOOOOOO0OOO = Inventory()
    _O000OOOOOO0O0OO0OOOOOO0O0O0OO00O0OO0OOOOOOOOOOOOO0OOOOO00OOOOOO = Inventory(1, 5, O00OO000=infoObject.current_w // 2.5, OOOO0OOO=infoObject.current_h / 1.2)
    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = None
    
    # Crafting Grid
    _O0OOOO00OOOOOOOO0OOOOOO00OOOOOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO0OOOOOO00OOOOOO0O000OOOO0OOO0OO = Inventory(
        _OOOOOO0OO000O0OO0OOOO0O0OO0OO0=3, _O0OOOO0OO000O0OOO000OO=3, OOOOOOOO0OO000O0O00OO000O0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0=50, O00OO000=50, OOOO0OOO=infoObject.current_h / 1.2, OOOOOOOO0OO000O000OOOOOOO0OOO0OO0OOOOOO000OOOOOO=3
    )
    
    
    _O0OOOO00OOOOOOOO0OOOOOO00OOOOOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOO00OOOOOO0OOOOOO000O0OOOO0O000OOOOOOOO0OO0OOOOOO0O0OO0OO0 = [
        {
            "pattern": [[(0, 1), None, (0, 1)], [None, (1, 1), None], [None, (1, 1), None]],
            "output": (2, 1),  # Green sword
        },
        # Add more recipes as needed
    ]
    
    
    if __name__ == "__main__":
        _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
        while running:
            for event in pig.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.QUIT:
                    _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.MOUSEBUTTONDOWN:
                    if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 3:
                        # Right-click to get a random item
                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = [Item(random.randint(0, 3)), 1]
                    elif event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                        try:
                            OOOOO0OO0OO000O0O0OO0OO0 = pig.mouse.get_pos()
                            O0OOOOOO00OOOOOO0O000OOOO0OOO0OOOOOOO0OO0OO000O0O0OO0OO0 = player_inventory.Get_pos()
                            if player_inventory.In_grid(pos[0], pos[1]):
                                if selected:
                                    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = player_inventory.Add(selected, gridpos)
                                elif player_inventory.items[gridpos[0]][gridpos[1]]:
                                    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = player_inventory.items[gridpos[0]][
                                        gridpos[1]
                                    ]
                                    player_inventory.items[gridpos[0]][gridpos[1]] = None
                            O0OOOOOO00OOOOOO0O000OOOO0OOO0OOOOOOO0OO0OO000O0O0OO0OO0 = crafting_grid.Get_pos()
                            if crafting_grid.In_grid(pos[0], pos[1]):
                                if selected:
                                    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = crafting_grid.Add(selected, gridpos)
                                elif crafting_grid.items[gridpos[0]][gridpos[1]]:
                                    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = crafting_grid.items[gridpos[0]][gridpos[1]]
                                    crafting_grid.items[gridpos[0]][gridpos[1]] = None
                            O0OOOOOO00OOOOOO0O000OOOO0OOO0OOOOOOO0OO0OO000O0O0OO0OO0 = item_bar.Get_pos()
                            if item_bar.In_grid(pos[0], pos[1]):
                                if selected:
                                    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = item_bar.Add(selected, gridpos)
                                elif item_bar.items[gridpos[0]][gridpos[1]]:
                                    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO = item_bar.items[gridpos[0]][gridpos[1]]
                                    item_bar.items[gridpos[0]][gridpos[1]] = None
                        except:
                            None  # Handle errors gracefully
    
            screen.fill((255, 255, 255, 100))
            player_inventory.draw([False, 0])
            crafting_grid.draw([False, 0])
            item_bar.draw([False, 0])
    
            if selected:
                mousex, O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0OOOO0OOO = pig.mouse.get_pos()
                screen.blit(selected[0].resize(30), (mousex, mousey))
                _OO000O0OOOOOOOOO0OOOO0O = font.render(str(selected[1]), True, (0, 0, 0))
                screen.blit(obj, (mousex + 15, mousey + 15))
    
            pig.display.update()    
            import pygame as pig
    
    import os
    from moviepy.editor import VideoFileClip
    
    import moviepy.editor
    
    import glob
    
    import numpy as np
    
    
    def _OOOOOO0O00OO000OOO0O0OO00OOOOOOOO0OOOOO00O0OOOOOOO0O0OOO0OO0OOOO00OOOOO00OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OO0(video_file: str, image_folder: str) -> None:
        if not os.path.isfile(image_folder + "/frame%04d.png"):
            _O0OOOOOOO000OO0O000OOOOOOOO0OO = VideoFileClip(video_file)
            # _O0OOOOOOO000OO0O000OOOOOOOO0OO = clip.reader.read_frame()
            # _O0OOOOOOO000OO0O000OOOOOOOO0OO = np.array(clip)
            # assert clip.OOO0O0O0O0OOO0OO0O000OOOO0O0OO00 == 3
            # print(clip.shape)
            # for xx in range(clip.shape[0]):
            #    for yy in range(clip.shape[1]):
            #        for zz in range(clip.shape[2]):
            #
            # _O0OOOOOOO000OO0O000OOOOOOOO0OO = moviepy.editor.ImageClip(clip)
            clip.write_images_sequence(image_folder + "/frame%04d.png")
            clip.audio.write_audiofile(image_folder + "/audio.wav")
    
    
    def OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOO0O000OOOOOO0O0O0OOO0O0OO00OOOOOO0OO000O0O0OO0OOOO0O000OO0O000OOOO0OOO0OO0OOOOOO00OO000O0(image_folder, not_skipped, screen, intro):
        clock: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pig.time.Clock()
    
        # Load the images from the specified folder
        if _O000OOOOOO0O0O0OOO0O0OO00OOOOOO0OO000O0 == 1:
            image_files: O0OO0OO0OOO0O0OO00OOOOOO = sorted(glob.glob(image_folder + "/*.jpg"))
        else:
            image_files: O0OO0OO0OOO0O0OO00OOOOOO = sorted(glob.glob(image_folder + "/frame*.png"))
        # Load the audio file
        audio_file: O0OO0OO0OOO0O0OO00OOOOOO = image_folder + "/audio.wav"
        pig.mixer.music.load(audio_file)
    
        # Start playing the audio
        pig.mixer.music.play()
    
        # Load each image and display it on the screen
        _O0OOOO00OOOOOO0OOOOOO0O0OOO0OO0O000OOOOOO0O0OOO0OO0OO0O0OO0OOOO00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pig.font.Font(
            "Recources\Fonts\PixelifySans-Regular.ttf", 50
        )
        for image_file in image_files:
            if OOO0O0O00OO000O0OOO0O0OOO0OO0OOOO0OO0OO00OOOOO0O0O000OOOOOOOO0OOOOOOO0OO0OOOOOO0O0OOO0OO == True:
                _O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = pig.image.load(image_file).convert()
                infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pig.display.Info()
                _O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = pig.transform.scale(
                    image, (infoObject.current_w, infoObject.current_h)
                )
                screen.blit(image, (0, 0))
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = credits_font.render(
                    "press anything to skip", True, (200, 200, 200)
                )
                screen.blit(
                    text_surface,
                    (
                        infoObject.current_w // 4 - text_surface.get_width() // 2,
                        infoObject.current_h - 60,
                    ),
                )
                pig.display.flip()
                clock.tick(60)  # Adjust the frame rate as needed
                for event in pig.event.get():
                    if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.VIDEORESIZE:
                        O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pig.display.set_mode((event.w, event.h), pig.RESIZABLE)
                    if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.QUIT:
                        pig.quit()
                        quit()
                    if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pig.KEYDOWN:
                        OOO0O0O00OO000O0OOO0O0OOO0OO0OOOO0OO0OO00OOOOO0O0O000OOOOOOOO0OOOOOOO0OO0OOOOOO0O0OOO0OO = False
    
        # Stop the audio playback
        pig.mixer.music.stop()    
        import os
    
    import PIL
    
    import pygame
    
    import sys
    
    import SquarePixels.eastereggs.credits_Easteregg as egg
    from SquarePixels.soundmanagement.music import play_music
    
    import random
    
    import playfab
    from playfab import PlayFabSettings
    from captcha.image import ImageCaptcha
    from playfab.PlayFabClientAPI import IsClientLoggedIn
    from playfab.PlayFabClientAPI import (
        LoginWithEmailAddress,
        RegisterPlayFabUser,
        LoginWithGoogleAccount,
    )
    from PIL import Image
    
    import tkinter as tk
    from tkinter import filedialog
    
    import hashlib
    from SquarePixels.uimanagement.easy_ui_maker import start
    
    import http.client
    from SquarePixels.uimanagement.get_user_avatar import get_user_avatar
    from SquarePixels.uimanagement.Image import ImageElement
    
    
    # from account_mannagement.authentication import SignInScreen, SignUpScreen
    from SquarePixels.uimanagement.leaderboard import (
        display_leaderboard,
        update_leaderboard,
        get_leaderboard,
        next_leadeboard_page,
        previous_leadeboard_page,
        search_input_callback_l,
    )
    from SquarePixels.uimanagement.input_feild import InputField
    from SquarePixels.uimanagement.button import Button
    from SquarePixels.uimanagement.clouds import Cloud
    from SquarePixels.uimanagement.friends import instance
    
    # Initialize Pygame
    pygame.init()
    # Add the signed_in flag
    O0OO0OO00O000OOOO0OOOOOOOOO0O0O00OOOOOO0O0OOO0OOO0OO0OOO0O000OOOOOO0O0O0 = IsClientLoggedIn()
    _OOOOOO0O0O0OO00 = ""
    OOOOO0OO = ""
    _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0 = ""
    # Constants
    infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.display.Info()
    WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = infoObject.current_w, infoObject.current_h
    _O00OOOOOOOOO0OOOO0OOOOOO0OOOO0OOOOOOO0OOOOO0OO0OOO0OOOO0O0OOO0OOOOOO0OO0OOOOO00O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (0, 0, 0)
    OOO0O0OOOOO0OOOOOOOOOOO0 = 60
    O0OOOOOO0OO000O00OO000O0O0OOO0OO = False
    OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O00OOOOOO0OO000O0OOOOOOO0OOO0O0O0O0OOO0OO = pygame.transform.scale(
        pygame.image.load(r"Recources\ui\mainmen\backround\cover.png"),
        (infoObject.current_w + 20, infoObject.current_h + 20),
    )
    # Initialize the screen
    O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Square Pixel")
    OOOOO0OOOOOO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOO00O0OOOO0OO000O0OOO0O0O0 = pygame.image.load(
        r"Recources\program recources\Screenshot 2023-09-21 181742.png"
    )
    pygame.display.set_icon(pygame_icon)
    
    OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO00OOOOOOO0OOOOOOOOOOOOOO0OO0OO00OOOOOO0OOO0O0OOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OO0 = PlayFabSettings
    playfabsettings._OO0OO00O000OOOOOO0O0OOOOO000OO0OOOOOO0OO0O0O0OO0OOO0OO = "4AAA9"
    # Define fonts
    O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 36)
    
    # Define colors
    OOOO00OO000O00OOOO0O0O0O00OO0OO0OO0O0OOO = (255, 255, 255)
    _O00OOOO0O0OOO0O00OO0OO000OO0OO0OOO0OOOOOOOOO0OOO0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (50, 50, 50)
    _O00OOOO0O0OOO0O00OO0OO000OO0OO0OOO0OOOOOOOOO0OOO0OO0OOO000O00OOOOO0OOOOO0OOO0OOOO0O0OOOOOOO0OO0O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (100, 100, 100)
    
    OO0OOOO000000OOO0O000OOOOOO0O0OO0OOOOOO0 = (255, 255, 255)
    
    
    # Load cloud images
    _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0O0OO0OO0 = [
        pygame.transform.scale(
            pygame.image.load(r"Recources\ui\mainmen\backround\clouds1.png"),
            (infoObject.current_w / 4, infoObject.current_h / 4),
        ),
        pygame.transform.scale(
            pygame.image.load(r"Recources\ui\mainmen\backround\clouds2.png"),
            (infoObject.current_w / 4, infoObject.current_h / 4),
        ),
    ]
    
    # Create a list to hold cloud objects
    _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OO0 = []
    # Game state
    play_music(r"Recources\sounds\music\Menu.mp3")
    O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0OO0OOOOOO0 = "menu"  # Initial state is the main menu
    O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = False  # Flag to control visibility of play buttons
    O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOO0O0OO00OOOOOOO0OOO000OOOOO0O0OO0O000OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOO0OO000O0OOOOO0OOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OO0 = False  # Flag to control visibility of multiplayer options
    
    # Create a screen for the sign-up process
    class OOOOOOO00O000OOOO0OOOOOOOOO0O0O00O0OOO0OOOOOO0OOOOOOOOO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self):
            self.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
            self.OOOOOOO0O0OO0OO00OOOOOO000OOOOOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OO = InputField(
                WIDTH // 2 - 100, HEIGHT // 2 - 100, 400, 40, "Username"
            )
            self._OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OO = InputField(
                WIDTH // 2 - 100, HEIGHT // 2 - 50, 400, 40, "Email"
            )
            self.OOOOO0OOOO0OOOOOO0OO0OO0O0OO0OO0OO0OOOO00OO000O000OOOOOOO0OOO0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OO = InputField(
                WIDTH // 2 - 100, HEIGHT // 2, 400, 40, "Password"
            )
            self.OOOOO0OO00OOOOOO0OO000O0O00OOOOO0O000OOOOOO000OO0OOOOOO0O0OO0OOOOOOOO0OO0O000OOO00O0OOOOOOO0O0OOOOOOOOO000OOOOOO0OOOOOO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Upload Profile Picture",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 50,
                200,
                50,
                self.upload_profile_picture,
            )
            self._O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOO0OOOOO00O0OOOO00O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Create Account",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 100,
                200,
                50,
                self.create_account,
            )
            self.O0OOOOOO0OO000O00OO000O0O0OOOOOOOOO000OO0OOOOOO0O0OO0OOOOOO000OO0OO000O0O0OOOOOO0O000OOOOOO0O0O0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Google Login",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 150,
                200,
                50,
                self.google_login,
            )
            self.OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0OO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Back",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 200,
                200,
                50,
                self.back,
            )
            self.buttons.extend(
                [
                    self.username_input,
                    self.email_input,
                    self.password_input,
                    self.profile_picture_button,
                    self.create_account_button,
                    self.google_login_button,
                    self.back_button,
                ]
            )
            self.OOOOO0OO00OOOOOO0OO000O0O00OOOOO0O000OOOOOO000OO0OOOOOO0O0OO0OOOOOOOO0OO0O000OOO00O0OOOOOOO0O0OOOOOOOOO000OOOOOO0OOOOOO0 = None
    
        def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOO(self):
            for button in self.buttons:
                button.draw(screen)
            if self.profile_picture:
                self.profile_picture.draw(screen)
    
        def OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(self):
            global current_page, main_page
            _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOOOO0OOOO0OOOOOO0OOOOOO0OOOOOO0 = main_page
    
        def O0OOOOOO0OO000O00OO000O0O0OOOOOOOOO000OO0OOOOOO0O0OO0OOOOOO000OO0OO000O0O0OOOOOO0O000OOOOOO0O0O0(self):
            _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"CreateAccount": True}
            request["TitleId"] = playfabsettings.TitleId
            request[
                "ServerAuthCode"
            ] = "95487563442-ta5a931frpcrsm78js4q5eb2sjvi927m.apps.googleusercontent.com"
    
            def _O0OOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(success, failure):
                if success:
                    display_message("Account created and signed in.", (0, 255, 0))
                else:
                    display_message("Account creation failed.")
                    if failure:
                        display_message("Here's some debug information:")
                        display_message(str(failure))
    
            _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = LoginWithGoogleAccount(request, callback)
    
        # Function to create an account with an email address
        def _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOO0OOOOO00O0OOOO00O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO(self):
            global signed_in
            _OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OO = self.email_input.text
            OOOOO0OOOO0OOOOOO0OO0OO0O0OO0OO0OO0OOOO00OO000O000OOOOOOO0OOO0OO = self.password_input.text
            OOOOOOO0O0OO0OO00OOOOOO000OOOOOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = self.username_input.text
    
            def _O0OOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(success, failure):
                if success:
                    display_message("Account created and signed in.", (0, 255, 0))
                else:
                    display_message("Account creation failed.")
                    if failure:
                        display_message("Here's some debug information:")
                        display_message(str(failure))
    
            try:
                _O0OOOO0OO000O0OOO0O0O0OOO0O0O0 = http.client.HTTPSConnection("api.eva.pingutil.com")
                OOOOO0OOOO0OOOOOOOOO0OOOOOO000OO0OO000O0OO0OOOOOO0OOO0OO = ''
                _OOO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0 = {}
                conn.request("GET", f"/email?_OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OO={email}", payload, headers)
                _OOOOOO0OOOOOO0O0OO0OO0 = conn.getresponse()
                O0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = res.read()
                #https://www.loginradius.com/blog/engineering/email-verification-api/
                _OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = data.decode("utf-8")
                if email_data["status"] == "success":
                    _OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = email_data["data"]
                    if email_data["disposible"] == False:
                        if email_data["valid_syntax"] == True:
                            if email_data["deliverable"] == True:
                                _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"CreateAccount": True}
                                request["TitleId"] = playfabsettings.TitleId
                                request["Email"] = email
                                request["Password"] = password
                                request["Username"] = username
    
                                # Upload the profile picture if it has been selected
                                if self.profile_picture:
                                    request["ProfilePicture"] = self.profile_picture
    
                                _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = RegisterPlayFabUser(request, callback)
    
                                if result is not None and "SessionTicket" in result:
                                    O0OO0OO00O000OOOO0OOOOOOOOO0O0O00OOOOOO0O0OOO0OOO0OO0OOO0O000OOOOOO0O0O0 = True
                                    display_message("Account created and signed in.", (0, 255, 0))
                                else:
                                    None
                            else:
                                display_message("Invalid Email.", (0, 255, 0))
                        else:
                            display_message("Invalid Email Syntax.", (0, 255, 0))
                    else:
                        display_message("Don't use a disposible email.", (0, 255, 0))
                else:
                    display_message("Couldn't check for email validness.", (0, 255, 0))
            except Exception as e:
                display_message(f"Account creation failed: {e}")
    
        # Function to upload a profile picture
        def OOOOOOO0OOOOO0OOOOO000OO0OO000O0OO0OOOOOO0OOO0OOO0OO0OOOOOOOO0OO00OOOOOO0OO000O0O00OOOOO0O000OOOOOO000OO0OOOOOO0O0OO0OOOOOOOO0OO0O000OOO00O0OOOOOOO0O0OOOOOOOOO000OOOOOO0OOOOOO0(self) -> None:
            """Uploads a selected profile picture
            Args:
                self: The class _O000OOOOOO0O0O0O0OO0OO0OOO0O0OOOO0OOOOOOOO0O0O000O0OOOO0OOOOOO0
            Returns: 
                None: No value is returned
            - Opens a file dialog window to select a profile picture file
            - Gets the file path of the selected picture
            - Checks if a file was selected before closing the dialog
            """
            # Open a file dialog to select a profile picture
            _OOOOOO0OO000O00OO000O0OOO0O0OO = tk.Tk()
            root.withdraw()  # Hide the main window
            O00OOOOO0O000OOOOOO000OO0OOOOOO0O0OO0OOOOOOOO0OOOO0OOOOOOOO0O0OO00000OOO = filedialog.askopenfilename(OOO0O0OO0O000OOOOOO0O0OOOOO000OO0OOOOOO0="Select a Profile Picture")
            root.destroy()  # Close the hidden root window
    
            if file_path:
                self.OOOOO0OO00OOOOOO0OO000O0O00OOOOO0O000OOOOOO000OO0OOOOOO0O0OO0OOOOOOOO0OO0O000OOO00O0OOOOOOO0O0OOOOOOOOO000OOOOOO0OOOOOO0 = Image.open(file_path, "r")
                self.OOOOO0OO00OOOOOO0OO000O0O00OOOOO0O000OOOOOO000OO0OOOOOO0O0OO0OOOOOOOO0OO0O000OOO00O0OOOOOOO0O0OOOOOOOOO000OOOOOO0OOOOOO0 = self.profile_picture.resize([HEIGHT // 2 + 50, HEIGHT // 2 + 50])
                self.OOOOO0OO00OOOOOO0OO000O0O00OOOOO0O000OOOOOO000OO0OOOOOO0O0OO0OOOOOOOO0OO0O000OOO00O0OOOOOOO0O0OOOOOOOOO000OOOOOO0OOOOOO0 = ImageElement((WIDTH - 25)-self.profile_picture.width, 25,self.profile_picture,"Circle")
    
    
    # Create a screen for the sign-in process
    class OOOOOOO00O000OOOO0OOOOOOOOO0O0O0OO0O0O0OOOO0O0O0OOOOOOO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self):
            self.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
            self._OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OO = InputField(
                WIDTH // 2 - 100, HEIGHT // 2 - 50, 400, 40, "Email"
            )
            self.OOOOO0OOOO0OOOOOO0OO0OO0O0OO0OO0OO0OOOO00OO000O000OOOOOOO0OOO0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OO = InputField(
                WIDTH // 2 - 100, HEIGHT // 2, 400, 40, "Password"
            )
            self.O0OO0OO00O000OOOO0OOOOOOOOO0O0O0O0OO0OOO0O000OOOOOO0O0O0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Sign In",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 50,
                200,
                50,
                self.sign_in_with_email,
            )
            self.OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0OO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Back",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 100,
                200,
                50,
                self.back,
            )
            self.buttons.extend(
                [
                    self.email_input,
                    self.password_input,
                    self.sign_in_button,
                    self.back_button,
                ]
            )
            self._OOOOOO0OOOOOO0O0O0OO000OOOOOO0O0O0OO00OOOOOOOO0OOOOOO000OOOOOOO0OO0OOOO0O0OO000OOOOOO0 = True
    
        def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOO(self):
            for button in self.buttons:
                button.draw(screen)
    
        # Function to sign in with an email address
    
        def O0OO0OO00O000OOOO0OOOOOOOOO0O0O0O0OO0OOO0O000OOOOOO0O0O0O0OO0OOOOO0OOOO00O000OOOOOO0O0OO00000OOOO0OO0OOO0OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OO(self, _OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OO=None, OOOOO0OOOO0OOOOOO0OO0OO0O0OO0OO0OO0OOOO00OO000O000OOOOOOO0OOO0OO=None):
            global signed_in, good, em, p  # , user
            if _OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OO == None and OOOOO0OOOO0OOOOOO0OO0OO0O0OO0OO0OO0OOOO00OO000O000OOOOOOO0OOO0OO == None:
                _OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OO = self.email_input.text
                OOOOO0OOOO0OOOOOO0OO0OO0O0OO0OO0OO0OOOO00OO000O000OOOOOOO0OOO0OO = self.password_input.text
            # print(email + "\n" + password)
    
            def _O0OOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(success, failure):
                global good
                if success:
                    O0OOOOOO0OO000O00OO000O0O0OOO0OO = True
                    display_message("Account created and signed in.", (0, 255, 0))
                else:
                    display_message("Account creation failed.")
                    if failure:
                        display_message("Here's some debug information:")
                        display_message(str(failure))
    
            try:
                _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {}
                request["TitleId"] = playfabsettings.TitleId
                request["Email"] = email
                request["Password"] = password
                _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = LoginWithEmailAddress(request, callback)
                print(good)
                if good:
                    O0OO0OO00O000OOOO0OOOOOOOOO0O0O00OOOOOO0O0OOO0OOO0OO0OOO0O000OOOOOO0O0O0 = True
                    _OOOOOO0O0O0OO00 = request["Email"]
                    OOOOO0OO = request["Password"]
                    # TODO #24 make keep logged in more secure
                    if self.remember_me:  # TODO #26 #25 add remember me checkbox
                        # with open("h.h", "x") as x:
                        # Create peekaboo.py and add var1 and var2
                        with open("SquarePixels/eastereggs/peekaboo.py", "w") as peekaboo_file:
                            peekaboo_file.write(f"O0O000OOOO0OOOOO00OOOOOO = {em}\n")
                            peekaboo_file.write(f"O0O000OOOO0OOOOO00OOOOOO = {p}\n")
                    #
                    ## Compile peekaboo.py to peekaboo.pyc
                    # import py_compile
                    #
                    # py_compile.compile("peekaboo.py")
                    # import peekaboo
                    #
                    # os.remove("peekaboo.py")
                    #
                    ## Create remember.cfg with the value True
                    # with open("remember.py", "w") as cfg_file:
                    #    cfg_file.write("OOO0O0OO = True\n")
                    #
                    ## playfab.PlayFabClientAPI.GetPlayerProfile
                    # OOOOOOO0O0OO0OO00OOOOOO000OOOOOO = {""}
                    display_message("Signed in.", (0, 255, 0))
                    return
                else:
                    print("signed in failed")
                    display_message("Sign-in failed.")
            except Exception as e:
                display_message(f"Sign-in failed: {e}")
    
        # Function to toggle the "Remember Me" checkbox
        def OOO0O0OO0OO000O0O0OOOOOOO0OOOOOOOOO000OO0OOOOOO0O0OO0OOO00OOOOOO0OOOOOO0O0O0OO000OOOOOO0O0O0OO00OOOOOOOO0OOOOOO000OOOOOOO0OO0OOOO0O0OO000OOOOOO0(self):
            self._OOOOOO0OOOOOO0O0O0OO000OOOOOO0O0O0OO00OOOOOOOO0OOOOOO000OOOOOOO0OO0OOOO0O0OO000OOOOOO0 = not self.remember_me
    
        # Function to send a verification code to the provided email
        def O0OO0OO00OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOO0O000OO0OOOOOO000OOOOOO0O000OOOO00OOOOO0O000OOO00O0OOOOOO0OOOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOO00O0OOOO0OO000O0O0OOO0OO0OOOOOO0(self):
            _OOOOOO0O0O0OO00OO0OOOOO0O000OOOOOO000OO = self.email_input.text
    
        def OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(self):
            global current_page, main_page
            _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOOOO0OOOO0OOOOOO0OOOOOO0OOOOOO0 = main_page
    
        # Add code to send a verification code to the email
        # You would typically use an email service or other means to send the code
    
    
    # Main Menu
    def O0O0OO00OO0OOOOO0O000OOOOOO0O0O0O0OO0OOOO0O0OO000OOOOOO0OOO0O0O0OOOOOOO0(
        host_button,
        join_button,
        leaderboard_data,
        leaderboard_page,
        next_button,
        previous_button,
        search_input,
        search_button,
    ):
        """
        Display the main menu and handle user interactions.
    
        Args:
            host_button (Button): The button for hosting a multiplayer game.
            join_button (Button): The button for joining a multiplayer game.
        """
        O0O0OO00OOOOOOO0OOO000OOOOO0O0OO0O000OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Multiplayer",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 50,
            200,
            50,
            toggle_multiplayer_options,
        )
        O0OO0OO00O000OOOOOO0O0O0O0OOOOOOOOO000OO0OOOOOO0OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Singleplayer",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 100,
            200,
            50,
            start_singleplayer_game,
        )
        _O0OOO0OOO0O0O0OO0O0OO00OO0OOOOO0OOOOO0O0OOOOOO000OOOOOO = Button(
            "Make UI (for testing purposes only) <unless future mod system...>",
            684,
            800,
            822,
            50,
            start,
        )
        UImaker.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = 20
        OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0OO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button("Back", WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50, back)
        OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Play", WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, toggle_play_buttons
        )
        O0OO0OO00OOOOOO0OOO0O0OOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Settings", WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, open_settings
        )
        _O0OOOO00OOOOOO0OOOOOO0O0OOO0OO0O000OOOOOO0O0OOO0OO0OO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Credits", WIDTH // 2 - 100, HEIGHT // 4 + 50, 200, 50, egg.start
        )
        OOO0OOOOOOOOOOO00O000OOOOOO0O0OOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Quit", WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50, quit_game
        )
    
        while running:
            global clouds
            if len(clouds) <= 6:
                if random.randint(0, 100) < 2:
                    _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = random.choice(cloud_images)
                    _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOOO00OO000 = random.randint(0, infoObject.current_w)
                    _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOOOOOO0OOO = random.randint(0, 200)
                    _O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OOO0OO0OOOO0OO0OO0OOOOO0OO0OOOOOO00OOOOOO0O0OOO0OO = random.uniform(0.1, 20)  # Random speed between 1 and 4
                    OOO0O0O00OOOOOO0OO0OOOO0O0OO0OOO00O0OOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OO = Cloud(cloud_x, cloud_y, cloud_image, cloud_speed)
                    clouds.append(new_cloud)
    
            # Remove clouds that are off-screen
            for cloud in clouds:
                if cloud._O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 == cloud_images[1]:
                    if cloud.x <= -300:
                        clouds.remove(cloud)
                else:
                    if cloud.x <= -500:
                        clouds.remove(cloud)
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
                # Handle events for buttons
                for button in instance.activebuttons:
                    button.handle_event(event)
                play_button.handle_event(event)
                settings_button.handle_event(event)
                quit_button.handle_event(event)
                credits_button.handle_event(event)
                UImaker.handle_event(event)
                update_leaderboard(
                    event, search_input, next_button, search_button, previous_button
                )
                if show_play_buttons:
                    singleplayer_button.handle_event(event)
                    multiplayer_button.handle_event(event)
                    back_button.handle_event(event)
                if show_multiplayer_options:
                    host_button.handle_event(event)
                    join_button.handle_event(event)
    
            # Clear the screen
            screen.fill(BACKGROUND_COLOR)
    
            # Draw buttons
            screen.blit(
                backround, (0, 0, infoObject.current_w / 20, infoObject.current_h / 20)
            )
            # Move and draw clouds
            for cloud in clouds:
                cloud.move()
                cloud.draw(screen)
            if not show_play_buttons:
                credits_button.draw(screen)
                play_button.draw(screen)
                settings_button.draw(screen)
                quit_button.draw(screen)
                UImaker.draw(screen)
            # Render the friends ui
            instance.render()
            # render the leaderboard
            display_leaderboard(
                leaderboard_data,
                "",
                next_button,
                previous_button,
                search_input,
                search_button,
                screen,
                WIDTH,
                WHITE,
            )
            if show_play_buttons:
                singleplayer_button.draw(screen)
                multiplayer_button.draw(screen)
                back_button.draw(screen)
    
            if show_multiplayer_options:
                host_button.draw(screen)
                join_button.draw(screen)
    
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)
    
    
    # Multiplayer Game
    def O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0():
        """
        Start the multiplayer game.
        """
        global game_state, show_play_buttons
        O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0OO0OOOOOO0 = "multiplayer"
        O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = False
    
    
    # Singleplayer Game
    def O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOO0OO0OO00O000OOOOOO0O0O0O0OOOOOOOOO000OO0OOOOOO0OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0():
        """
        Start the singleplayer game.
        """
        global running
        pygame.mixer.music.fadeout(2)
        _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
    
    
    # Host Multiplayer Game
    def _OOO0OO000O0O0OO0OO0OOO0O0OOO0OO0OOOO0O0OO00OOOOOOO0OOO000OOOOO0O0OO0O000OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0():
        """
        Host a multiplayer game.
        """
        
        import SquarePixels.uimanagement.server_ui as server_ui
    
        server_ui.load_servers()
        server_ui.load_mplayers()
        server_ui.game_loop()
    
    
    # Join Multiplayer Game
    def O0OOOO0O0OO000O00O000OOOOOO0O0O0O0OO0OOOO0O0OO00OOOOOOO0OOO000OOOOO0O0OO0O000OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0():
        """
        Join a multiplayer game.
        """
        
        import SquarePixels.uimanagement.client_ui as client_ui
    
        client_ui.find_servers()
        client_ui.main()
    
    
    # Toggle the visibility of play buttons
    def OOO0O0OO0OO000O0O0OOOOOOO0OOOOOOOOO000OO0OOOOOO0O0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0():
        """
        Toggle the visibility of play buttons.
        """
        global show_play_buttons
        O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = not show_play_buttons
    
    
    # Toggle the visibility of multiplayer options
    def OOO0O0OO0OO000O0O0OOOOOOO0OOOOOOOOO000OO0OOOOOO0O0OO0OOOO0O0OO00OOOOOOO0OOO000OOOOO0O0OO0O000OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOO0OO000O0OOOOO0OOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OO0():
        """
        Toggle the visibility of multiplayer options.
        """
        global show_multiplayer_options
        O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOO0O0OO00OOOOOOO0OOO000OOOOO0O0OO0O000OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OOO0OO000O0OOOOO0OOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OO0 = not show_multiplayer_options
    
    
    # Open the settings menu
    def _OO000O0OOOOO0OO0OOOOOO0OOO0O0O0O0OO0OOOO0OO0OO00OOOOOO0OOO0O0OOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OO0():
        """
        Open the settings menu.
        """
        global game_state
        O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0OO0OOOOOO0 = "settings"
    
    
    # Function to display a message on the screen
    def O0OOO0OO0O000OOOO0OO0OO0OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0(message, _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO=(255, 0, 0)):
        global current_message
        _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0 = message
        OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = font.render(message, True, color)
        OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text_surface.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=(WIDTH // 2, HEIGHT // 3))
        screen.blit(text_surface, text_rect)
    
    
    # Create a "Not a Robot" button
    # OOO0O0O00OO000O0OOO0O0OOO0OO0OOOOO0OOOOOO0OO0OOO00OOOOOO0OO000O0OOOOOOOO0OO000O0OOO0O0OOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button("Not a Robot", 100, 350, 200, 50)
    
    
    # Create pages for different states
    class OOO0OOOOOO0OOOOOO0OOOOOO0OOOOOO0:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self):
            """Initializes registration form fields and buttons
            Args: 
                self: {The class _O000OOOOOO0O0O0O0OO0OO0OOO0O0OOOO0OOOOOOOO0O0O000O0OOOO0OOOOOO0}: Initializes registration form fields and buttons
            Returns:
                None: Does not return anything, initializes form fields and buttons
            {Processing Logic}:
                - Initializes InputField objects for username, email, password
                - Initializes Button objects for profile picture upload, account creation, Google login, back 
                - Adds all InputField and Button objects to a buttons list
                - Sets initial profile picture to None"""
            self.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
    
        def OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0(self, button):
            self.buttons.append(button)
    
        def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOO(self):
            for button in self.buttons:
                button.draw(screen)
    
    
    # Create a page for email input and verification
    O0O0OO00OO0OOOOO0O000OOOOOO0O0O0O0OO0OOOOOOOO0OOOO0OOOOOO0OOOOOO0OOOOOO0 = Page()
    
    # Initialize the current page to the email verification page
    _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOOOO0OOOO0OOOOOO0OOOOOO0OOOOOO0 = main_page
    
    
    # Define a function to switch the current page to the sign-up screen
    def O0OO0OO0OO0OOOO00O000OOOOOO0O0OO00O0OOOO00000OOOO0OO0OOOOOO0O0OO0OO000O0O0OO0OOOO0OO0OO00O000OOOO0OOOOOOOOO0O0O0O0OO0OOOOOOOOOO0OOOOO0OO():
        global current_page
        screen.fill(WHITE)
        _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOOOO0OOOO0OOOOOO0OOOOOO0OOOOOO0 = SignUpScreen()
    
    
    # Define a function to switch the current page to the sign-in screen
    def O0OO0OO0OO0OOOO00O000OOOOOO0O0OO00O0OOOO00000OOOO0OO0OOOOOO0O0OO0OO000O0O0OO0OOOO0OO0OO00O000OOOO0OOOOOOOOO0O0O0O0OO0OOO0O000OOOOOO0O0O0():
        global current_page
        screen.fill(WHITE)
        _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOOOO0OOOO0OOOOOO0OOOOOO0OOOOOO0 = SignInScreen()
    
    
    def O0OOOOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO():
        global signed_in
        O0OO0OO00O000OOOO0OOOOOOOOO0O0O00OOOOOO0O0OOO0OOO0OO0OOO0O000OOOOOO0O0O0 = "Guest"
    
    
    # Add a function to show the sign-in or guest popup
    def O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOO0OO0OO00O000OOOO0OOOOOOOOO0O0O00O000OOOOOO0O0O0O0OO0OOOOOOOO0OO0OO000O0OOOOO0OOOOOOOOO0OOOOO0OO(leaderboard_page):
        global WIDTH, HEIGHT, screen, BACKGROUND_COLOR, signed_in, current_message
        ########################DEVELOPMENTAL TESTING ONLY##############################
        O0OO0OO00O000OOOO0OOOOOOOOO0O0O00O000OOOOOO0O0O0O0OO0OOOOO0OOOOOO0OO0OO0O0OO0OOOOOO0O0OO0OOOOOO0O0OO0OO0OOO0O0OOO0OO0OOOOOOOOOO0O0OO0OO00OOOOOO000OOOOOO = Button(
            "signin_as_test_user",
            WIDTH // 2 - 100,
            HEIGHT // 2 - 325,
            200,
            50,
            SignInScreen.sign_in_with_email,
            [None, "testuser@gmail.com", "test123"],
        )
        ########################DEVELOPMENTAL TESTING ONLY##############################
        _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOO0OOOOO00O0OOOO00O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OO = Button(
            "Create Acount", WIDTH // 2 - 100, HEIGHT // 2 - 225, 200, 50, switch_to_sign_up
        )
        OOOOO0OO0OO000O0OOOOO0OOOOOOOOO0OOOOO0OOO0OO0OOOO00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 24)
        OOOOO0OO0OO000O0OOOOO0OOOOOOOOO0OOOOO0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = "Please sign in to play the game and save your progress."
        OOOOO0OO0OO000O0OOOOO0OOOOOOOOO0OOOOO0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = "If you choose to play as a guest, your progress will reset daily because we won't be able to verify your ownership of the game."
        O0OO0OO00O000OOOO0OOOOOOOOO0O0O0O0OO0OOO0O000OOOOOO0O0O0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Sign In", WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, switch_to_sign_in
        )
        O0OOOOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Play as Guest",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 50,
            200,
            50,
            guest,  # play_as_guest
        )
    
        while True:
            screen.blit(
                backround, (0, 0, infoObject.current_w / 20, infoObject.current_h / 20)
            )
            display_message(current_message)
            OOOOO0OO0OO000O0OOOOO0OOOOOOOOO0OOOOO0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOO = popup_font.render(popup_text, True, WHITE)
            OOOOO0OO0OO000O0OOOOO0OOOOOOOOO0OOOOO0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOO = popup_font.render(popup_text2, True, WHITE)
            if _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOOOO0OOOO0OOOOOO0OOOOOO0OOOOOO0 == main_page:
                screen.blit(
                    popup_text_render,
                    (WIDTH // 2 - popup_text_render.get_width() // 2, HEIGHT // 2 - 100),
                )
                screen.blit(
                    popup_text2_render,
                    (WIDTH // 2 - popup_text2_render.get_width() // 2, HEIGHT // 2),
                )
                sign_in_button.draw(screen)
                guest_button.draw(screen)
                create_account.draw(screen)
                ########################DEVELOPMENTAL TESTING ONLY##############################
                signin_as_test_user.draw(screen)
                ########################DEVELOPMENTAL TESTING ONLY##############################
            current_page.render()
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.VIDEORESIZE:
                    WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = event.w, event.h
                    O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    
                # Handle button events based on the current page
                if current_page != main_page:
                    for button in current_page.buttons:
                        button.handle_event(event)
                else:
                    sign_in_button.handle_event(event)
                    guest_button.handle_event(event)
                    create_account.handle_event(event)
                    ########################DEVELOPMENTAL TESTING ONLY##############################
                    signin_as_test_user.handle_event(event)
                    ########################DEVELOPMENTAL TESTING ONLY##############################
            if signed_in != False:
                OOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = get_leaderboard(leaderboard_page, display_message)
                return leaderboard_data
    
            pygame.display.update()
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)
    
    
    def OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O():
        """
        Go back to the previous menu.
        """
        global show_play_buttons, game_state
        O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = not show_play_buttons
        O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0OO0OOOOOO0 = "menu"
    
    
    # Quit the game
    def OOO0OOOOOOOOOOO00O000OOOOOO0O0OOO0OO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0():
        """
        Quit the game.
        """
        pygame.quit()
        sys.exit()
    
    
    def O0O0OO00OO0OOOOO0O000OOOOOO0O0O0O00OOOOOOOOOOOO0OOO0O0O000O0OOOO():
        """
        Main function to run the game.
        """
        global running, current_leader_page
        # Add these constants to control pagination
        OO0O0OOOOOOOO0OO00OO0OO0OOOO0OO0OO0O0O0OOO0O0OOOOOOOOOO0O0OO0OOOOOO0OOOOOO0O0OOOOOOO0OO0O0OO0OOOOOO0OOOOOOOOO0OOOOOOOO0OOO0O0OOO = 10
        _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OOOOOOOO0OOOO0OOOOOO0OOOOOO0OOOOOO0 = 1
        OOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = get_leaderboard(current_leader_page, display_message)
        # Initialize multiplayer and singleplayer buttons
        _OOO0OO000O0O0OO0OO0OOO0O0OOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Host", WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, host_multiplayer_game
        )
        O0OOOO0O0OO000O00O000OOOOOO0O0O0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Join", WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50, join_multiplayer_game
        )
        # Add buttons for next and previous page
        OOO0O0O00OOOOOO0O00OO000OOO0O0OOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Next Page",
            WIDTH - 120,
            HEIGHT - 40,
            100,
            30,
            next_leadeboard_page,
            [current_leader_page, leaderboard_data, display_message],
        )
        OOOOO0OO00OOOOOO0OOOOOO0O0O000OO0O000OOO0OO000O0OOOOOOO0O0OO0OO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            "Previous Page",
            WIDTH - 500,
            HEIGHT - 40,
            120,
            30,
            previous_leadeboard_page,
            [current_leader_page, leaderboard_data, display_message],
        )
        # Add the search button in the display_leaderboard function
        O0OO0OO00OOOOOO0OO0OOOOO00OOOOOO00O0OOOO00000OOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button("Search", WIDTH - 320, 20, 80, 30, search_input_callback_l)
        # Add the search bar for filtering leaderboard entries
        O0OO0OO00OOOOOO0OO0OOOOO00OOOOOO00O0OOOO00000OOOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OO = InputField(WIDTH - 500, 20, 200, 30, "Search by Player Name")
        _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
        O00OOOOO0OOOOOO0OOO0O0OO00O0OOOO00000OOOO0OO0OOOOOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OO = False
        # Main game loop
        while running:
            # Generate a random cloud
            if (
                O0OO0OO00O000OOOO0OOOOOOOOO0O0O00OOOOOO0O0OOO0OOO0OO0OOO0O000OOOOOO0O0O0 == False
            ):  # DO NOT CHANGE TO "IF NOT SIGNED_IN: because singed_in can also be a string"
                try:
                    with open("h.h", "r") as a:
                        OOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = SignInScreen.sign_in_with_email(
                            SignInScreen(), a.readline(0), a.readline(1)
                        )
                except:
                    OOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = show_signin_popup(current_leader_page)
    
            if O0OO0OO00O000OOOO0OOOOOOOOO0O0O00OOOOOO0O0OOO0OOO0OO0OOO0O000OOOOOO0O0O0 == True:
                if not fetch_leaderboard:
                    OOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = get_leaderboard(current_leader_page, display_message)
                    # print(leaderboard_data)
                    O00OOOOO0OOOOOO0OOO0O0OO00O0OOOO00000OOOO0OO0OOOOOO000OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOOOOOOOOO0OO000O0OO0OOOOO00OOOOOOO0OOO0OO = True
                    #get_user_avatar(SignInScreen)
    
    
            if O0OO0OO00O000OOOO0OOOOOOOOO0O0O00OOOOOO0O0OOO0OOO0OO0OOO0O000OOOOOO0O0O0 == "Guest":
                pass  # TODO:implement #22 guest logic in future
            # TODO #23 add function checking acount variable for having bought this game
            if O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0OO0OOOOOO0 == "menu":
                main_menu(
                    host_button,
                    join_button,
                    leaderboard_data,
                    current_leader_page,
                    next_button,
                    previous_button,
                    search_input,
                    search_button,
                )
            elif O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0OO0OOOOOO0 == "multiplayer":
                if show_multiplayer_options:
                    host_button.draw(screen)
                    join_button.draw(screen)
            elif O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0OO0OOOOOO0 == "singleplayer":
                
                import SquarePixel
    
                SquarePixel.main()
            elif O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOOOOO0O0OO0OOOOOO0 == "settings":
                # Implement the settings menu here
                pass
    
            # Add other game states as needed
            pygame.display.update()
            pygame.time.Clock().tick(FPS)
    
    
    # Get a player's friends list
    def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0O0OO0OOOOOO000OO0O000OOOO0OO0OO0OOO0O0OO():
        _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {}
        _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = playfab.PlayFabClientAPI.GetFriendsList(request)
        if result is not None:
            O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0 = result.data.Friends
            # Process and display friends list in your game's UI
    
    
    # Add a friend
    def OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OO(player_id):
        _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"FriendPlayFabId": player_id}
        playfab.PlayFabClientAPI.AddFriend(request)
    
    
    # Handle friend requests, accept or decline
    def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOO00OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO(friend_playfab_id, accept):
        if accept:
            _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"FriendPlayFabId": friend_playfab_id}
            playfab.PlayFabClientAPI.AddFriend(request)
        else:
            _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"FriendPlayFabId": friend_playfab_id}
            playfab.PlayFabClientAPI.RemoveFriend(request)
    
    
    if __name__ == "__main__":
        mainfunc()    
        import pygame
    
    import sys
    
    import SquarePixels.multiplayer.server as server
    
    # Initialize Pygame
    pygame.init()
    
    # Define colors
    OOOO00OO000O00OOOO0O0O0O00OO0OO0OO0O0OOO = (255, 255, 255)
    _O00OOOOOOO00OOOOOOOO0OOOO0OOOOOO0OOOO0O = (0, 0, 0)
    OOOOOO0OOOOO0OO0OOOOO0OOOO0OO0OO = (128, 128, 128)
    
    # Constants
    infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.display.Info()
    SCREEN_WIDTH, OOOOOOO0OO0OOOOOOOOO0OO0OO0O0OOOOO0O0OOOOOOOO0OOO0OO0OOO000O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = infoObject.current_w, infoObject.current_h
    _O00OOOOOOOOO0OOOO0OOOOOO0OOOO0OOOOOOO0OOOOO0OO0OOO0OOOO0O0OOO0OOOOOO0OO0OOOOO00O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (0, 0, 0)
    OOO0O0OOOOO0OOOOOOOOOOO0 = 60
    
    # Define font
    OOO0O0OOOOO0OOOOOOOOO0OO00OO0OO0O0OO0OOOOOOOOOO0OO0O0O0OOOOO0000OO0O0OOO = 20
    OOO0O0OOOOO0OOOOOOOOO0OO00OO0OO0 = pygame.font.Font(None, FONT_SIZE)
    
    # Define server configuration variables
    _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOO = None
    O0O0OO00OO0OOOOOO00OO000O0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OO0 = "max players"
    O0O0OO00OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOOO0OOOOOOOO000OOOOO000OO = []
    
    # Create a list to store created servers
    O0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OO0 = []
    
    # Create a list to store delete buttons
    O0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
    
    # File to save the servers
    OOOOOOO0OO0O0OOOOOOO0OO0O0OOO0OOOO0O0OOOOOOO0OO0OOOOOOO0O0OO0OOOOOO0O0OOOO0O0O0OOOO00OOOOO0O0OOO = "servers.txt"
    OOOO00OOOOO0OOOOOOO00OOOOOOOO0OOOO0OO0OOOO0O0OOOOOOO0OO0OOOOOOO0O0OO0OOOOOO0O0OOOO0O0O0OOOO00OOOOO0O0OOO = "mplayers.txt"
    
    
    # Load servers from file
    def OOO000OO0OO000O0OO0OOOOOO0OOO0OOO0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OO0():
        try:
            with open(SERVERS_FILE, "r") as file:
                for line in file:
                    O0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOO = line.strip()
                    servers.append(server)
        except FileNotFoundError:
            pass
    
    
    # Load max_players values from file
    def OOO000OO0OO000O0OO0OOOOOO0OOO0OOO0OO0OOOO0O0OO00OOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OO0() -> None:
        try:
            with open(MPLAYERS_FILE, "r") as file:
                for line in file:
                    O0O0OO00OOOOO0OO = int(line.strip())
                    mplayall.append(mp)
        except FileNotFoundError:
            pass
    
    
    # Save servers to file
    def O0OO0OO0OO0OOOOOO0O000OO0OOOOOO0O0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OO0():
        with open(SERVERS_FILE, "w") as file:
            for server in servers:
                file.write(server + "\n")
        with open(MPLAYERS_FILE, "w") as file:
            for mpla in mplayall:
                file.write(str(mpla) + "\n")
    
    
    # Create a Pygame screen
    O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Server Manager")
    
    
    # Function to draw the sidebar
    def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOO0OO0OO00O000OOOO0OOO0OO0OOOOOO0OOOOOOOOOO0OOOOO00OOOOOO():
        pygame.draw.rect(screen, GRAY, (0, 0, 200, SCREEN_HEIGHT))
    
        OOOO0OOO = 50
        server_buttons.clear()  # Clear the server buttons list
        for i, server in enumerate(servers):
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = FONT.render(server, True, BLACK)
            screen.blit(text, (10, y))
    
            # Draw the delete button for each server
            O0OOO0OO0OOOOOO0OOO000OO0OOOOOO0OOO0O0OO0OOOOOO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect(180, y - 15, 15, 15)
            pygame.draw.rect(screen, BLACK, delete_button_rect)
            server_buttons.append(delete_button_rect)  # Add the button rect to the list
    
            y += 30
    
    
    # Function to draw the server configuration area
    def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOOO0OO0OOO00O0OOOO0OO000O0OOO0O0O0O00OOOOO0O000OOOO0OOOOOOOOOOOOO000OOOOOOOO0OOOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0():
        pygame.draw.rect(screen, WHITE, (220, 50, SCREEN_WIDTH - 240, SCREEN_HEIGHT - 100))
    
        if current_server:
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = FONT.render("Server: " + current_server, True, BLACK)
            screen.blit(text, (230, 60))
    
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = FONT.render("Max Players: " + str(max_players), True, BLACK)
            screen.blit(text, (230, 90))
    
            pygame.draw.rect(screen, BLACK, (230, 130, 120, 30))
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = FONT.render("Save Server", True, WHITE)
            screen.blit(text, (250, 135))
    
            pygame.draw.rect(screen, BLACK, (230, 160, 120, 30))
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = FONT.render("Run Server", True, WHITE)
            screen.blit(text, (250, 165))
    
    
    # Function to start the server
    def O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOO():
        if current_server:
            print("Starting server:", current_server)
            server.main(5, current_server)
    
    
    # Function to delete a server
    def O0OOO0OO0OOOOOO0OOO000OO0OOOOOO0OOO0O0OO0OOOOOO0O0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOO(index):
        if index >= 0 and index < len(servers):
            del servers[index]
            del mplayall[index]
            save_servers()
    
    
    # Main game loop
    def O0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOOOOO000OO0OO000O00OO000O0OOOOO0OO():
        # Create the input box
        global max_players, current_server
        OOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = False
        OOO0O0O0OOOOOOO0O0O0OO00OOOOOOOO0OOOOOO000OOOOOOO0OO0OO0 = False
        _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOOOOOOO0OO000O0O00OO000 = pygame.Rect(SCREEN_WIDTH - 230, SCREEN_HEIGHT - 40, 150, 20)
        OOO0O0O0OOOOOOO0O0O0OO00OOOOOOOO0OOOOOO000OOOOOOO0OO0OOOOOOOOOOO0OO000O0O00OO000 = pygame.Rect(SCREEN_WIDTH - 340, SCREEN_HEIGHT - 40, 100, 20)
        _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = "server Name"
    
        while True:
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN:
                    if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_DOWN:
                        # Scroll down event
                        pass
                    elif event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_BACKSPACE:
                        # Handle backspace in the input box
                        _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = input_text[:-1]
                        O0O0OO00OO0OOOOOO00OO000O0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OO0 = max_players[:-1]
                    else:
                        if event.unicode.isdigit():
                            max_players += event.unicode
                        else:
                            # Add typed characters to the input box
                            input_text += event.unicode
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN:
                    if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                        O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0O0OO0OOOOOOOO0OO0OO000O0O0OO0OO0 = pygame.mouse.get_pos()
                        if mouse_pos[0] < 200:
                            # Clicked on sidebar
                            O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0O000OOOOOO0O0O0O0OOO0OO0OOOOOO0O00OO000 = (mouse_pos[1] - 50) // 30
                            if selected_index >= 0 and selected_index < len(servers):
                                _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOO = servers[selected_index]
                                O0O0OO00OO0OOOOOO00OO000O0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OO0 = mplayall[selected_index]
                        elif (
                            mouse_pos[0] >= 230
                            and mouse_pos[1] >= 130
                            and mouse_pos[1] <= 160
                        ):
                            # Clicked on Save Server button
                            if current_server and max_players > 0:
                                servers.append(current_server)
                                _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0OO0OO00OOOOOO000OOOOOOO0O000OO0OOOOOO000OOOOOO = None
                                mplayall.append(max_players)
                                save_servers()
                        elif input_box.collidepoint(mouse_pos):
                            # Clicked inside the input box
                            OOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = True
                            pass
                        else:
                            OOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = False
    
                        if number_box.collidepoint(mouse_pos):
                            # Clicked inside the input box
                            OOO0O0O0OOOOOOO0O0O0OO00OOOOOOOO0OOOOOO000OOOOOOO0OO0OO0 = True
                            pass
                        else:
                            OOO0O0O0OOOOOOO0O0O0OO00OOOOOOOO0OOOOOO000OOOOOOO0OO0OO0 = False
    
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
                                    O0O0OO00OO0OOOOOO00OO000O0OO0OOOOOOOO0OOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOO0OO0OO0 = int(max_players)
                                except ValueError:
                                    print("not a valid number for max players")
                                    break
                                servers.append(input_text)
                                mplayall.append(max_players)
                                _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = ""
                                save_servers()
    
            screen.fill(WHITE)
    
            draw_sidebar()
            draw_server_configuration()
    
            # Draw the input box
            pygame.draw.rect(screen, BLACK, input_box, 2)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = FONT.render(input_text, True, BLACK)
            screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
    
            # draw the number box
            pygame.draw.rect(screen, BLACK, number_box, 2)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = FONT.render(str(max_players), True, BLACK)
            screen.blit(text_surface, (number_box.x + 5, number_box.y + 5))
    
            # Draw the create server button
            pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - 40, SCREEN_HEIGHT - 40, 30, 30))
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = FONT.render("+", True, WHITE)
            screen.blit(text, (SCREEN_WIDTH - 35, SCREEN_HEIGHT - 35))
    
            pygame.display.flip()
    
    
    # Load servers from file
    load_servers()
    load_mplayers()
    
    # Start the game loop
    game_loop()    
    import pygame
    
    
    if __name__ == "__main__":
        # Constants
        infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.display.Info()
        WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = infoObject.current_w, infoObject.current_h
        _O00OOOOOOOOO0OOOO0OOOOOO0OOOO0OOOOOOO0OOOOO0OO0OOO0OOOO0O0OOO0OOOOOO0OO0OOOOO00O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (0, 0, 0)
    O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font("Recources\Fonts\PixelifySans-Regular.ttf", 36)
    # Define colors
    OOOO00OO000O00OOOO0O0O0O00OO0OO0OO0O0OOO = (255, 255, 255)
    _O00OOOO0O0OOO0O00OO0OO000OO0OO0OOO0OOOOOOOOO0OOO0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (50, 50, 50)
    _O00OOOO0O0OOO0O00OO0OO000OO0OO0OOO0OOOOOOOOO0OOO0OO0OOO000O00OOOOO0OOOOO0OOO0OOOO0O0OOOOOOO0OO0O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (100, 100, 100)
    OO0OOOO000000OOO0O000OOOOOO0O0OO0OOOOOO0 = (255, 255, 255)
    
    
    class _O00OOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0:
        """Button class O00OOOOO0OO000O000OOOOOO creating interactive buttons in the game."""
    
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(
            self,
            text,
            x,
            y,
            width,
            height,
            command,
            additional_data: OOO000OO0O000OOOO0OO0OO0OOO0O0OO = None,
            _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO=(255, 255, 255),
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
            self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = text
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = width
            self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = height
            self._O0OOOO0OO000O0O0O0OO00O0O0OO00OO0OOOOOOOO0O0O0O0OOO0OO = command
            self.OO0OOOOOO0OOO0OOO0OOO0OO0O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0OO0OOOOOOOO000OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO = additional_data
            self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = False
            self.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = 36
            self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
            self.OOOOOOOO0OO000O0OOO000OOO0OOO0OO = False
            self._O000OOOOOO0O0OOOO0OOOOOOOO000OO0O000OOO00O0OOOOO0OO0OO0 = False
            self.OOOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOOOO000OO0O000OOOOOO0O0O00OOOOOO0O0OOO0OO = False
            self.O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = "Recources\Fonts\PixelifySans-Regular.ttf"
            self._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = color
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen):
            """Draw the button on the screen."""
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(self.font_name, self.size)
            font.set_bold(self.bold)
            font.set_italic(self.italics)
            font.set_underline(self.underlined)
            _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = BUTTON_HOVER_COLOR if self.hovered else BUTTON_COLOR
            pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(self.text, True, self.color)
            screen.blit(
                text,
                (
                    self.x + self.width // 2 - text.get_width() // 2,
                    self.y + self.height // 2 - text.get_height() // 2,
                ),
            )
    
        def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOO0OOOOOO0O0O000OO0OOOOOO0OOO0O0O0OOO0O0OO(self, event):
            """
            Handle events related to the button.
    
            Args:
                event: The Pygame event to be processed.
            """
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEMOTION:
                self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = (
                    self.x < event.pos[0] < self.x + self.width
                    and self.y < event.pos[1] < self.y + self.height
                )
            elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                if self.hovered:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                    if self.additional_data != None:
                        self.command(*self.additional_data)
                    else:
                        self.command()
                else:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
    
        def O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OO(self):
            self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = True
    
        def _O0OOOO00000OOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO(self, event):
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEMOTION:
                self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = (
                    self.x < event.pos[0] < self.x + self.width
                    and self.y < event.pos[1] < self.y + self.height
                )
            elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                if self.hovered:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                else:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN and self.active:
                if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_BACKSPACE:
                    self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = self.text[:-1]
                else:
                    self.text += event.unicode    
                    import pygame
    
    if __name__ == "__main__":
        # Constants
        infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.display.Info()
        WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = infoObject.current_w, infoObject.current_h
        _O00OOOOOOOOO0OOOO0OOOOOO0OOOO0OOOOOOO0OOOOO0OO0OOO0OOOO0O0OOO0OOOOOO0OO0OOOOO00O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (0, 0, 0)
    O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 36)
    # Define colors
    OOOO00OO000O00OOOO0O0O0O00OO0OO0OO0O0OOO = (255, 255, 255)
    _O00OOOO0O0OOO0O00OO0OO000OO0OO0OOO0OOOOOOOOO0OOO0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (50, 50, 50)
    _O00OOOO0O0OOO0O00OO0OO000OO0OO0OOO0OOOOOOOOO0OOO0OO0OOO000O00OOOOO0OOOOO0OOO0OOOO0O0OOOOOOO0OO0O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (100, 100, 100)
    
    OO0OOOO000000OOO0O000OOOOOO0O0OO0OOOOOO0 = (255, 255, 255)
    
    
    # Create an InputField class O00OOOOO0OO000O000OOOOOO text input
    class OO0O0O0OOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOOOO0O0OO0O000OOO0OOOOOO0OOO000OOO0OOO0OO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x, y, width, height, placeholder, _O0OOOO0OO000O0O0O0OO00O0O0OO00OO0OOOOOOOO0O0O0O0OOO0OO=None, OOOOO0OOOO0OOOOO00OOOOOOOO0OOOOOO0O0OO000OOOOOO0OOO0O0OO0OOOOOO000OOOOOOO0OO0OO0=None):
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
                - Sets the x, y, width and height attributes 
            from the arguments
                - Sets the placeholder text
                - Initializes other attributes like text, active state etc
                - Sets the command and parameters if provided
            """
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = width
            self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = height
            self.OOOOO0OOOOO000OOOO0OOOOO00O0OOOO0OOOOOO000000OOO0OO000O0OOO000OOO0OOO0OO0OOOOOO000OOOOOO = placeholder
            self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = ""
            self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
            self.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = 36
            self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = False
            self.O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = "Recources\Fonts\PixelifySans-Regular.ttf"
            self.OOOOOOOO0OO000O0OOO000OOO0OOO0OO = False
            self._O000OOOOOO0O0OOOO0OOOOOOOO000OO0O000OOO00O0OOOOO0OO0OO0 = False
            self.OOOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOOOO000OO0O000OOOOOO0O0O00OOOOOO0O0OOO0OO = False
            self._O0OOOO0OO000O0O0O0OO00O0O0OO00OO0OOOOOOOO0O0O0O0OOO0OO = command
            self.OOOOO0OOOO0OOOOO00OOOOOOOO0OOOOOO0O0OO000OOOOOO0OOO0O0OO0OOOOOO000OOOOOOO0OO0OO0 = parameters
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen):
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
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(self.font_name, self.size)
            font.set_bold(self.bold)
            font.set_italic(self.italics)
            font.set_underline(self.underlined)
            _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = BUTTON_COLOR if not self.active else BUTTON_HOVER_COLOR
            pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOO00O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (0, 0, 0) if not self.active else (255, 255, 255)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(
                self.text if self.text else self.placeholder, True, font_color
            )
            screen.blit(text, (self.x + 10, self.y + 10))
    
        def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOO0OOOOOO0O0O000OO0OOOOOO0OOO0O0O0OOO0O0OO(self, event):
            """Handle mouse and keyboard events for a button
            Args:
                event: The pygame event to handle
            Returns:
                self.active: Whether the button is currently pressed
            - Check if mouse button 1 was pressed within button bounds and set self.active
            - Check if a key was pressed and button is active
            """
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = (
                    self.x < event.pos[0] < self.x + self.width
                    and self.y < event.pos[1] < self.y + self.height
                )
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN and self.active:
                if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_BACKSPACE:
                    self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = self.text[:-1]
                else:
                    self.text += event.unicode
                if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_RETURN:
                    if self.command:
                        if self.parameters:
                            self.command(*self.parameters)
                        else:
                            self.command()
    
        def _O0OOOO00000OOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO(self, event):
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
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEMOTION:
                self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = (
                    self.x < event.pos[0] < self.x + self.width
                    and self.y < event.pos[1] < self.y + self.height
                )
            elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                if self.hovered:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                else:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN and self.active:
                if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_BACKSPACE:
                    self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = self.text[:-1]
                else:
                    self.text += event.unicode
    
        def _O0OOOOOOO000OO0OOOOOO0OO0OOOOO00OOOOOO(self):
            """Clears the text in the object
            Args:
                self: The object whose text needs to be cleared
            Returns:
                None: Does not return anything
            - Sets the text attribute of the object to an empty string ""
            - This empties out any existing text in the object"""
            self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = ""    # Cloud class
    class OO0OOOOOOOO000OO0OO000O0OOOOOOO0O0OOO0OO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x, y, image, speed):
            self.O00OO000 = x
            self.OOOO0OOO = y
            self._O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = image
            self.O0OO0OO0OOOOO0OO0OOOOOO00OOOOOO0O0OOO0OO = speed
            self.OO0OOOOOOOO000OOOOOOO0OO00000OOOOO0OOOOO = 0
    
        def O0O0OO000OO000O0O0O000OO0OOOOOO0(self):
            self.x -= self.speed
            self.alpha += 1
            if self.alpha >= 255:
                self.OO0OOOOOOOO000OOOOOOO0OO00000OOOOO0OOOOO = 255
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen):
            self.image.set_alpha(self.alpha)
            screen.blit(self.image, (self.x, self.y))    
            import pygame
    from playfab.PlayFabClientAPI import (
        GetFriendLeaderboard,
        AddFriend,
        RemoveFriend,
        CreateSharedGroup,
        SetFriendTags,
    )
    
    import playfab.PlayFabErrors as PlayFabErrors
    
    import playfab.PlayFabSettings as PlayFabSettings
    
    import requests
    
    import json
    
    pygame.init()
    
    from SquarePixels.uimanagement.button import Button
    from SquarePixels.uimanagement.input_feild import InputField
    
    
    infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.display.Info()
    screen: pygame.OOOOOOO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = pygame.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    OOOOO0OOOOOO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOO00O0OOOO0OO000O0OOO0O0O0 = pygame.image.load(
        r"Recources\program recources\Screenshot 2023-09-21 181742.png"
    )
    pygame.display.set_icon(pygame_icon)
    # pygame.display.toggle_fullscreen()
    
    pygame.display.set_caption("Square Pixel")
    O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font("Recources\Fonts\PixelifySans-Regular.ttf", 36)
    
    WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = infoObject.current_w, infoObject.current_h
    
    
    # Function to display a message on the screen
    def O0OOO0OO0O000OOOO0OO0OO0OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0(message, _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO=(255, 0, 0)):
        global current_message
        _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0 = message
        OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = font.render(message, True, color)
        OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text_surface.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=(WIDTH // 2, HEIGHT // 3))
        screen.blit(text_surface, text_rect)
    
    
    class OOO0O0OO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self):
            self.O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = None  # You should initialize this appropriately
            self._O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0 = ""
            self.O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0 = []
    
        def _OOOOO000OO000O0OOO0OOOO0OO000O0O0OO0OO0OOO0O0OO(
            self,
            urlPath,
            request,
            authKey,
            authVal,
            callback,
            _O0OOOOOOOOOOO0O0OO0OO0OOO0O0OO0OO000O0O0O0OO000OOOOO00OO0OOOOOOOO0O0OOOO0OOOOO=None,
            _OOOOOO0O00OO000OOO0O0OO00OOOOOOOO0OOOOO000O00OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0=None,
        ):
            """
            Note this is a blocking call and will always run synchronously
            the return type is a dictionary that should contain a valid dictionary that
            should reflect the expected JSON response
            if the call fails, there will be a returned PlayFabError
            """
    
            OOOOOOO000OOOOOOOOO000OO = PlayFabSettings.GetURL(
                urlPath, PlayFabSettings._internalSettings.RequestGetParams
            )
    
            try:
                O0OOOO0O = json.dumps(request)
            except Exception as e:
                raise PlayFabErrors.PlayFabException(
                    "The given request is not json serializable. {}".format(e)
                )
    
            _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO000O00OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0 = {}
    
            if extraHeaders:
                requestHeaders.update(extraHeaders)
    
            requestHeaders["Content-Type"] = "application/json"
            requestHeaders[
                "X-PlayFabSDK"
            ] = PlayFabSettings._internalSettings.SdkVersionString
            requestHeaders[
                "X-ReportErrorAsSuccess"
            ] = "true"  # Makes processing PlayFab errors a little easier
    
            if authKey and authVal:
                requestHeaders[authKey] = authVal
    
            _OOOOOO0O0OOOOO0O0OOOOOOO0OOOOOO0OO00OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0 = requests.post(url, O0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO=j, _OOO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0=requestHeaders)
            # print(httpResponse)
    
            _OOOOOO000OOOOOO00OOOOOO0OO000O000OOOOOO = _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0 = None
    
            if httpResponse.status_code != 200:
                # Failed to contact PlayFab Case
                _OOOOOO000OOOOOO00OOOOOO0OO000O000OOOOOO = PlayFabErrors.PlayFabError()
    
                error._O00OOOOO0O0OOOOO0O0OOOOOOO0OOOO0OOOOO0OO000O0O0OOO0OO0OOOOOO0 = httpResponse.status_code
                error._O00OOOOO0O0OOOOO0O0OOOOOOO0OOOOOOOOO0OOO0O0OOOO0OOOOOOOO0O0OOOOOOOOO0O0OO0OO0 = httpResponse.reason
            else:
                # Contacted playfab
                _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0OOOO00OO00OOOOOOOO0OOOOOOOOOO0OOOOOOO0OO0OOOOOO000OOOOOO = json.loads(httpResponse.content.decode("utf-8"))
                # print(responseWrapper)
                if responseWrapper["code"] != 200:
                    # contacted PlayFab, but response indicated failure
                    _OOOOOO000OOOOOO00OOOOOO0OO000O000OOOOOO = responseWrapper
                    return None
                else:
                    # successful call to PlayFab
                    _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0 = responseWrapper["data"]
                    return response
    
            if error and callback:
                self.callGlobalErrorHandler(error)
    
                try:
                    # Notify the caller about an API Call failure
                    callback(None, error)
                except Exception as e:
                    # Global notification about exception in caller's callback
                    PlayFabSettings.GlobalExceptionLogger(e)
            elif (response or _OOOOOO0OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0 == {}) and callback:
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
                    _OOOOOO0O0O0OO00OOOOO0OOOOO0O0OOOOOO0OOOOOOO0OO00OOOOOO0O0OO0OO0OOOOO0OO0OO000O0OOO0O0O0O0OO0OO00OOOOOO0OO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOO = PlayFabErrors.PlayFabError()
                    emptyResponseError.OO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOO = "Empty Response Recieved"
                    emptyResponseError.OO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOOOOOO00OO0OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0 = (
                        "PlayFabHTTP Recieved an empty response"
                    )
                    emptyResponseError.OO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOOOO0OOOOO0OO000O0O0OOO0OO0OOOOOO0 = PlayFabErrors.PlayFabErrorCode.Unknown
                    callback(None, emptyResponseError)
                except Exception as e:
                    # Global notification about exception in caller's callback
                    PlayFabSettings.GlobalExceptionLogger(e)
    
            # Your existing DoPost function with "self" references
    
        def _O0OOOOOO0OOOOOOOO000OOOOO000OOOOOOOO0OOOO000OO0OO000O0OOOOOOOOOO0OOOOOOOO000OOOO0O0OOO00OOOOOO00OOOOOO0OO000O000OOOOOO000O00OOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO000OOOOOO(self, error):
            if PlayFabSettings.GlobalErrorHandler:
                try:
                    # Global notification about an API Call failure
                    PlayFabSettings.GlobalErrorHandler(error)
                except Exception as e:
                    # Global notification about exception in caller's callback
                    PlayFabSettings.GlobalExceptionLogger(e)
    
        def O0OOO0OO0O000OOOO0OO0OO0OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0(self, message, _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO=(255, 0, 0)):
            self._O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOO0O0OO000OOOOOO0O0OO0OO0O0OO0OO0OO0OOOOOO0OOOOOO0OOOOOO0 = message
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = self.font.render(message, True, color)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text_surface.get_rect(_O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO=(WIDTH // 2, HEIGHT // 3))
            self.screen.blit(text_surface, text_rect)
    
        def OOOOOO0O0OOOOOO0OOO0O0OOOOO0O0OO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0OOO00OOO0O000OOOO0OO0OO0OOO0O0OOO0OO0OOO00000OOOOOO0O0OOOOO0O0OOOOOOO0OO(
            self, request, callback, _O0OOOOOOOOOOO0O0OO0OO0OOO0O0OO0OO000O0O0O0OO000OOOOO00OO0OOOOOOOO0O0OOOO0OOOOO=None, _OOOOOO0O00OO000OOO0O0OO00OOOOOOOO0OOOOO000O00OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0=None
        ):
            """
            Retrieves the current friend list for the local user, constrained to users who have PlayFab accounts. Friends from
            linked accounts (Facebook, Steam) are also included. You may optionally exclude some linked services' friends.
            https://docs.microsoft.com/rest/api/playfab/client/friend-list-management/getfriendslist
            """
            if not PlayFabSettings._internalSettings.ClientSessionTicket:
                raise PlayFabErrors.PlayFabException(
                    "Must be logged in to call this method"
                )
    
            def OO0OOOO000OOOOOOOO0OOOOOOOOOO0OOOOOOO0OO0OOOOOO0O0OOO0OOOO0OOOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(playFabResult, error):
                if callback:
                    callback(playFabResult, error)
    
            return self.DoPost(
                "/Client/GetFriendsList",
                request,
                "X-Authorization",
                PlayFabSettings._internalSettings.ClientSessionTicket,
                wrappedCallback,
                customData,
                extraHeaders,
            )
    
        def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0(self):
            _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {}
    
            def _O0OOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(success, failure):
                if success:
                    print("success")
                    self.display_message("success")
                else:
                    self.display_message("failed")
                    print("failed")
                    if failure:
                        self.display_message("Here's some debug information:")
                        self.display_message(str(failure) + "leader board")
    
            try:
                _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = self.GetFriendsList_http(request, callback)
            except:
                _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = None
            if result is not None:
                print(result)
                return result
            else:
                return []
    
        def O0OOO0OO0O000OOOO0OO0OO0OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0(self, friends):
            OOOO0OOO = 100
            for friend in friends:
                O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = self.font.render(friend.username, True, (255, 255, 255))
                self.screen.blit(friend_text, (50, y))
                y += 50
    
        def OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0(self, friend_identifier):
            if "@" in friend_identifier:
                # If the friend_identifier contains "@" symbol, it's an email
                _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"FriendEmail": friend_identifier}
            else:
                # Otherwise, it's a username
                _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"FriendUsername": friend_identifier}
    
            def _O0OOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(success, failure):
                if success:
                    print("success")
                    self.display_message("success")
                else:
                    self.display_message("failed")
                    print("failed")
                    if failure:
                        self.display_message("Here's some debug information:")
                        self.display_message(str(failure) + "leader board")
    
            # Call the AddFriend method
            try:
                _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = AddFriend(request, callback)
            except:
                print("error")
    
    
    class OOO0O0OO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOOOOOOOO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self):
            self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
            self.O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO000OO0O000OOOO0OO0OO0OOO0O0OO = [
                "Friends will appear here"
            ]  # Initialize a list to store friend names
            self.OOOOO0OO0OOOOOO0OOO0O0O0O0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO000OO0O000OOOO0OO0OO0OOO0O0OO = []  # List to store pending friend requests
            self.O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO000OO0O000OOOO0OO0OO0OOO0O0OOO0OO0OOO0OO000O0O00OOOOOO00OOOOOO0OO0OO00OOOOOO0OOO0O0OO = 0  # Offset for displaying friends
            self.O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOOOOOO0OO0OOOOOO0OOO0O0O0O0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0 = (
                False  # To toggle between "Friends" and "Pending Friends" tabs
            )
            self.O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOO = "Friends"  # Initialize the selected tab
            self.O0OO0OO00OOOOOO0OO0OOOOO00OOOOOO00O0OOOO00000OOOO0OO0OOOOOOOOOOOOO0OOOOO00OOOOOO = InputField(50, 50, 400, 40, "Search Players")
            self.search_bar.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = 30
            self.OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OO = InputField(50, 220, 400, 40, "Enter Username/Email")
            self.O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0O0OO0OOO0O000OOOOOO0O0O0O0OO0OO0OOO0O0OOOO0OOOOOOOO0O0O000O0OOOO0OOOOOO0 = Friends()
            self.OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOO = Button(
                "Add Friend",
                50,
                150,
                200,
                50,
                self.show_add_friends,
            )
            self.OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Send Friend Request",
                150,
                270,
                200,
                50,
                self.add_friend,
            )
            self._OOOOOO0OOOOOO0O00OOOOO00OOOOOO0OOOOOO0O0OO0OO000000OOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Refresh",
                50,
                100,
                200,
                50,
                self.refresh_friends,
            )
            self.O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0O0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Friends",
                270,
                95,
                200,
                50,
                self.show_friends,
            )
            self.OOOOO0OO0OOOOOO0OOO0O0O0O0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0O0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
                "Pending Friends",
                300,
                150,
                200,
                50,
                self.show_pending_friends_list,
            )
            # self.OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0OO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            #    "Back",
            #    50,
            #    HEIGHT - 100,
            #    200,
            #    50,
            #    self.back,
            # )
            self.activebuttons.extend(
                [
                    self.search_bar,
                    self.refresh_button,
                    self.friends_tab_button,
                    self.add_friend_tab,
                    self.pending_friends_tab_button,
                ]
            )
    
        def _OOOOOO0OOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOO(self):
            # Background for the friend list
            # Highlight the selected tab
            OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O00OOOOOO0OO000O0OOOOOOO0OOO0O0O0O0OOO0OO = pygame.Surface(
                (525, pygame.display.Info().current_h), pygame.SRCALPHA
            )
    
            pygame.draw.rect(
                backround,
                (0, 0, 0, 100),
                (0, 0, 525, pygame.display.Info().current_h),
            )
            screen.blit(
                backround,
                (
                    0,
                    0,
                ),
            )
            if self.O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOO == "Friends":
                self.friends_tab_button.selected()
                # Display the list of friends
                self.display_friends()
    
                self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
                self.activebuttons.extend(
                    [
                        self.search_bar,
                        self.refresh_button,
                        self.friends_tab_button,
                        self.add_friend_tab,
                        self.pending_friends_tab_button,
                    ]
                )
    
            elif self.O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOO == "Pending Friends":
                # Display the list of pending friends
                self.display_pending_friends()
                self.pending_friends_tab_button.selected()
    
            elif self.O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOO == "Add Friends":
                self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
                self.activebuttons.extend(
                    [
                        self.search_bar,
                        self.refresh_button,
                        self.friends_tab_button,
                        self.add_friend_tab,
                        self.pending_friends_tab_button,
                        self.add_friend_input,
                        self.add_friend_button,
                    ]
                )
    
            for button in self.activebuttons:
                button.draw(screen)
    
        def _OOOOOO0OOOOOO0O00OOOOO00OOOOOO0OOOOOO0O0OO0OO000000OOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0(self):
            # Call a method to refresh the friend list
            self.O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO000OO0O000OOOO0OO0OO0OOO0O0OO = self.friends_instance.get_friends()
            # Also, update the pending friend list if needed
    
        def O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0(self):
            self.O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOOOOOO0OO0OOOOOO0OOO0O0O0O0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0 = False
            self.O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOO = "Friends"
    
        def O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOOOOOO0OO0OOOOOO0OOO0O0O0O0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0O0OO0OOOOOO000OO0O000OOOO0OO0OO0OOO0O0OO(self):
            # Call a method to get pending friend requests
            self.O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOO = "Pending Friends"
            self.OOOOO0OO0OOOOOO0OOO0O0O0O0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO000OO0O000OOOO0OO0OO0OOO0O0OO = self.friends_instance.get_pending_friend_requests()
            self.O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOOOOOO0OO0OOOOOO0OOO0O0O0O0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0 = True
    
        def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0(self):
            self.O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0 = self.friends_instance.get_friends()
    
        def O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOOOO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0(self):
            self.O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0OOOO0OOOOOOOOOOOOO = "Add Friends"
    
        # Function to add a friend
        def OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OO(self):
            O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = self.add_friend_input.text
            if friend_name:
                self.friend_list.append(friend_name)
                self.friends_instance.add_friends(friend_name)
                # Send a request to the server to add the friend
                self.add_friend_input.clear()
    
        # Function to display the list of friends
        def O0OOO0OO0O000OOOO0OO0OO0OOOOO0OOOOO000OOOO0OOOOOOOOO0OOOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0(self):
            # Filter friends based on the search bar input
            O0OO0OO00OOOOOO0OO0OOOOO00OOOOOO00O0OOOO00000OOOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = self.search_bar.text.lower()
            O00OOOOO0O000OOOOOO000OOOOO0O0OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OOO0OO0OOOO00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OO0 = [
                friend for friend in self.friend_list if search_text in friend.lower()
            ]
    
            # Display a portion of the filtered friend list (e.g., 10 friends at a time)
            OOOO0OOO = 200
            for friend in filtered_friends[
                self.friend_list_offset : self.friend_list_offset + 10
            ]:
                O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(friend, True, (255, 255, 255))
                screen.blit(friend_text, (50, y))
                y += 50
    
        # Function to go back to the main menu
        def OOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(self):
            global current_page, main_page
            _O0OOOOOOOOOOO000OOOOOO00OOOOOO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OOOOOOOO0OOOO0OOOOOO0OOOOOO0OOOOOO0 = main_page
    
    
    # Usage Example:
    _O000OOOOOO0O0O0O0OO0OO0OOO0O0OOOO0OOOOOOOO0O0O000O0OOOO0OOOOOO0 = FriendScreen()
    
    
    if __name__ == "__main__":
        # instance.O00OOOOO00OOOOOO0O000OOO0OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO000OO0O000OOOO0OO0OO0OOO0O0OO = instance.get_friends()
    
        # Game loop
        _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
        while running:
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
    
                # Handle user input events
                for button in instance.activebuttons:
                    button.handle_event(event)
    
            # Update your friend list or other game logic as needed
            # friend_screen.update()
    
            # Clear the screen
            screen.fill((255, 255, 255))
    
            instance.render()
            # Update the display
            pygame.display.flip()
    
        # Quit Pygame
        pygame.quit()    
        import pygame
    
    
    class _OO0OO00OOOOOO0O00OO000OOO0O0OOOO0O0OOOOOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x, y, text, font_size):
            """
            Initialize a button object
            Args:
                x: x-coordinate of the button
                y: y-coordinate of the button 
                text: Text to display on the button
                font_size: Font size of the text
            Returns: 
                self: Button object
            - Sets the x and y coordinates
            - Sets the text and font size
            - Sets default color, size and other attributes
            - Initializes other properties like hover, width, height etc.
            """
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = text
            self.O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = font_size
            self._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (255, 255, 255)  # Default text color
            self.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = font_size
            self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = False
            self.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = 50
            self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 25
            self.OOOOOOOO0OO000O0OOO000OOO0OOO0OO = False
            self._O000OOOOOO0O0OOOO0OOOOOOOO000OO0O000OOO00O0OOOOO0OO0OO0 = False
            self.OOOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOOOO000OO0O000OOOOOO0O0O00OOOOOO0O0OOO0OO = False
            self.O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = None
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen):
            """
            Renders text on a screen surface.
            Args:
                screen: The screen surface to render text on
            Returns: 
                None: Does not return anything
            - Loads the font based on properties of the Text object
            - Renders the text surface using the font and text properties  
            - Blits/draws the text surface onto the screen surface at the x,y position"""
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(self.font_name, self.size)
            font.set_bold(self.bold)
            font.set_italic(self.italics)
            font.set_underline(self.underlined)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = font.render(self.text, True, self.color)
            screen.blit(text_surface, (self.x, self.y))
    
        def _O0OOOO00000OOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO(self, event):
            """
            Change text on mouse events
            Args: 
                event: pygame event object
            Returns: 
                None
            Processing Logic:
            - Check if mouse is hovering over button on MOUSEMOTION
            - Set button to active if mouse is pressed on button on MOUSEBUTTONDOWN 
            - Change text if a key is pressed while button is active on KEYDOWN
            """
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEMOTION:
                self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = (
                    self.x < event.pos[0] < self.x + self.width
                    and self.y < event.pos[1] < self.y + self.height
                )
            elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                if self.hovered:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                else:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN and self.active:
                if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_BACKSPACE:
                    self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = self.text[:-1]
                else:
                    self.text += event.unicode    
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
    _O00OOOO0O0OOO0O00OO0OO000OO0OO0OOO0OOOOOOOOO0OOO0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (50, 50, 50)
    _O00OOOO0O0OOO0O00OO0OO000OO0OO0OOO0OOOOOOOOO0OOO0OO0OOO000O00OOOOO0OOOOO0OOO0OOOO0O0OOOOOOO0OO0O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (100, 100, 100)
    OOOO00OO000O00OOOO0O0O0O00OO0OO0OO0O0OOO = (255, 255, 255)
    
    
    # Set the screen size
    infoObject: _OO000O0OOOOOOOOO0OOOO0O0OOOOOO000O0OOOOOOO0O0OO = pygame.display.Info()
    screen_width, O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0O0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = infoObject.current_w, infoObject.current_h
    screen: pygame.OOOOOOO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = pygame.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    OOOOO0OOOOOO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOO00O0OOOO0OO000O0OOO0O0O0 = pygame.image.load(
        r"Recources\program recources\Screenshot 2023-09-21 181742.png"
    )
    pygame.display.set_icon(pygame_icon)  # pygame.display.toggle_fullscreen()
    pygame.display.set_caption("Square Pixel")
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    
    OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
    _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OOO0OO0OO0 = []
    O0OO0OO00O000OOOO0OOO0OO0OOOOOO0OOOOOOOOOO0OOOOO00OOOOOOO0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OO0 = []
    OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OOO0OO0OO0 = []
    _O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0OOOOOOOOO0OO000O0O00OO0000OOOOOO0O0OO0OO0 = []
    O0OO0OO000O0OOOO00OOOOOO0O000OOOOOOOO0OOOOO0O0OOO0OO0OO0 = []
    _O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0O0OO0OO0 = []
    
    
    # Element that is currently being moved or scaled
    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = None
    O0OO0OO000O0OOOOOO0OOOOOOOO000OO0O000OOOOOO0O0O0O0OOOOOO = False
    O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOO00OO000 = 0
    O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOOOOO0OOO = 0
    O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = 0
    O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 0
    
    # UI panel properties
    OOOOOOO00O000OOOO0OO0OOOOOOOO0OOOO0OOOOOOOO0O0O00OOOOOO0OOO000OOO0OO0OOOO00OO000 = screen_width - 200
    OOOOOOO00O000OOOO0OO0OOOOOOOO0OOOO0OOOOOOOO0O0O00OOOOOO0OOO000OOO0OO0OOOOOOO0OOO = 0
    OOOOOOO00O000OOOO0OO0OOOOOOOO0OOOO0OOOOOOOO0O0O00OOOOOO0OOO000OOO0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = 200
    OOOOOOO00O000OOOO0OO0OOOOOOOO0OOOO0OOOOOOOO0O0O00OOOOOO0OOO000OOO0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = screen_height
    
    # Create a font for displaying instructions
    _O000OOOOOO0O0O0O0OO0OO0OOO0O0OO00OOOOOOOOOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOOO00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 13)
    # Add instructions for updating the selected element
    _O000OOOOOO0O0O0O0OO0OO0OOO0O0OO00OOOOOOOOOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = "Click and drag to move, right-click to resize element and scroll to change font size. "
    instruction_text += "Edit properties in the UI panel, then press Enter to apply changes to the selected element. "
    instruction_text += "To use color wheel hold mouse button down and then move it around the inner circle. "
    instruction_text += "The bar on the right of the wheel controls brightness. "
    instruction_text += (
        "Once you find the color you want then just click the element you want to recolor. "
    )
    
    
    # Function for updating font size when scrolling
    def OOOOOOO0OOOOO0OOO0OOO0OOOO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOO00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0(selected_element, scroll_direction):
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
    
    
    def _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0(text, x, y, width, height, command, OO0OOOOOO0OOO0OOO0OOO0OO0O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0OO0OOOOOOOO000OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO=None):
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
    
    
    def _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OO(x, y, width, height, placeholder):
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
    
    
    def _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OOO0OO000O0OOO0O0O0O0OO0OOOO0OO0OO00O000OOOO0OOO0OO0OOOOOO0OOOOOOOOOO0OOOOO00OOOOOO(text, y, create_function, _OOOOOO0O00OO000OOO0O0OO00OOOOOOOO0OOOOO=None):
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
        OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = 120
        OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 40
        OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0O0OO0OOOO00OO000 = 10
        OOO0O0O00OOOOOO0OO0OOOO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button(
            text,
            button_x,
            y,
            button_width,
            button_height,
            create_function,
            OO0OOOOOO0OOO0OOO0OOO0OO0O000OOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0OO0OOOOOOOO000OOO0OO0OOOO0OOO0OOOO0OOOOOOOO0O0OOOO0OOOOO=extra,
        )
        sidebar_buttons.append(new_button)
    
    
    def OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0(_O0OOOO0O000OOO00OOOOOO00O0OOOOOOO000OO0OOOOOO0=None):
        """
        Add an image to the canvas
        Args:
            circle: The circle object to add the image to
        Returns:
            None: Does not return anything
        - Opens a file dialog to select an image file
        - Checks if a file was selected
        - If file selected, adds the image to the canvas"""
        _OOOOOO0OO000O00OO000O0OOO0O0OO = tk.Tk()
        root.withdraw()  # Hide the main tkinter window
    
        O00OOOOO0O000OOOOOO000OO0OOOOOO0O0OO0OOOOOOOO0OOOO0OOOOOOOO0O0OO00000OOO = filedialog.askopenfilename(
            O00OOOOO0O000OOOOOO000OO0OOOOOO0OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0O0OO0OO0=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
    
        if file_path:
            # Load the selected image using PIL
            _O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = Image.open(file_path)
    
            # Create an ImageElement object and add it to your list of elements
            if circle:
                _O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0O0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = ImageElement(200, 400, image, "Circle")
            else:
                _O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0O0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = ImageElement(200, 400, image)
            images.append(image_element)
    
    
    # Function for creating a new button
    def _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O0O00OOOOOO0OO0OOOO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0():
        """Creates a new button and adds it to the buttons list
    
        Args:
            None
        Returns:
            None: No value is returned
    
        - A new button object is created with the label "Button", positioned at (200,200) with dimensions of 100x50 pixels
        - The new button is appended to the global buttons list
        - No value is returned as the button is added directly to the buttons list"""
        OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = create_button("Button", 200, 200, 100, 50, None)
        buttons.append(button)
    
    
    # Function for creating a new text element
    def _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O0O00OOOOOO0OO0OOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO():
        """
        Creates and adds a new text element to the list
        Args:
            None
        Returns:
            None: No value is returned
        - Creates a new TextElement object with default values
        - Adds the new TextElement to the text_elements list
        - No value is returned, only side effect is adding to list"""
        OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = TextElement(200, 300, "Text", 24)
        text_elements.append(text_element)
    
    
    def O0OOO0OO0OOOOOO0OOO000OO0OOOOOO0OOO0O0OO0OOOOOO0O0OO0OOOO0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO():
        """Deletes currently selected element
        Args:
            None
        Returns:
            None: Selected element is deleted 
        from list
        - Check if a selected element exists
        - If it does, remove it 
            from the global list storing all elements
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
    
            O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = None
    
    
    def _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOO0OOO0OO0OOOOOO0OOO000OO0OOOOOO0OOO0O0OO0OOOOOO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0(OOOO0OOO=280):
        """
        Create and add a delete button to the sidebar
        Args:
            y: Position of the button 
            from the top of the sidebar in pixels
        Returns:
            None: No value is returned
        - Create a Button object with text "Delete", x position 10, y position from argument, width 120 and height 40
        - Assign the delete_selected_element function to the button's command
        - Append the button object to the sidebar_buttons list"""
        O0OOO0OO0OOOOOO0OOO000OO0OOOOOO0OOO0O0OO0OOOOOO0O0OO0OOOOOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 = Button("Delete", 10, y, 120, 40, delete_selected_element)
        sidebar_buttons.append(delete_button)
    
    
    def _OOOOOO0O00OO000OOOOO0OO0OO000O000OOOOOOOOO0O0OOO0OO0OOOOOOOOOO00O000OOOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OOO0OO0OO0():
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
        _O0OOOO0OO000O0O0OOO0OO0OOOOOO0 = [
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
        _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = "\n".join(code)
        pyperclip.copy(result)
        screen.fill((0, 0, 0))
        while True:
            for event in pygame.event.get():
                if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Display the generated code on the screen
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 15)
            for index, t in enumerate(code):
                if _O000OOOOOO0O0O0O0OOO0OO0OOOOOO0O00OO000 == len(code) - 1:
                    index += 5
                    O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 25)
                _O0OOOO0OO000O0O0OOO0OO0OOOOOO0O0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = font.render(t, True, (255, 255, 255))
                screen.blit(
                    code_surface, (10, 60 + (15 * index))
                )  # Adjust position as needed
                pygame.display.flip()
    
    
    # Function for creating a new input field
    def _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O0O00OOOOOO0OO0OOOO0O0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OO():
        """
        Creates and adds a new input field to the list of input fields
        Args:
            None: No arguments are passed to this function
        Returns:
            None: This function does not return anything
        - Creates a new input field object using the create_input_field function and default parameters
        - Appends the newly created input field object to the list of existing input fields
        - This allows adding multiple input fields dynamically to the UI"""
        _O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OO = create_input_field(300, 300, 200, 30, "Enter text")
        input_fields.append(input_field)
    
    
    def _O0OOOO00OOOOOO0OOOOOO0OO0OOOOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O0O00OOOOOO0OO0OOOO0O0OO0OOO00O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0OOOOOOOOO0OO000O0O00OO000():
        """Creates a new checkbox object and appends it to the checkboxes list
    
        Args:
            None
        Returns:
            None: No value is returned
        - A CheckBox object is instantiated with coordinates (380, 40) and label "Label"
        - The new CheckBox object is appended to the checkboxes list
        - This allows the checkbox to be drawn and interacted with through the checkboxes list
        """
        _O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0OOOOOOOOO0OO000O0O00OO000 = CheckBox(380, 40, "Label")
        checkboxes.append(checkbox)
    
    
    create_button_on_sidebar("New Button", 10, create_new_button)
    create_button_on_sidebar("New Input", 60, create_new_input_field)
    create_button_on_sidebar("New Text", 110, create_new_text_element)
    create_button_on_sidebar("Checkbox", 170, create_new_checkbox)
    create_button_on_sidebar("Add Image", 230, add_image)
    create_button_on_sidebar("Add Circle Image", 290, add_image, [True])  # circle
    create_button_on_sidebar("Save UI", 350, export_ui_elements)
    create_delete_button(410)
    
    
    class OOOOO0OO0OO000O0O0OOO0OO0OOOOOO0:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, node_type, x, y, node_id):
            self.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 = node_type
            self.O00OO000 = x
            self.OOOO0OOO = y
            self._O000OOOO0OOO0OO = node_id
            self.OOO000OO0OO000O0O0OOOOOO0O000OOO00O0OOOO = lambda: None  # Default logic for the node
    
    
    # Text input field for customizing text
    class _OO0OO00OOOOOO0O00OO000OOO0O0OOOO0O0O0OOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOOOO0O0OO0O000OOO0OOOOOO0OOO000OOO0OOO0OO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x, y, width, height, label, default_text):
            """
            Initialize a graph object
            Args:
                None: No arguments required
            Returns:
                None: Does not return anything
            - Initialize an empty list to store nodes
            - Initialize an empty list to store connections between nodes"""
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = width
            self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = height
            self.OOO000OOOO0OOOOOOOOOOOOO0OOOOOO0OOO000OO = label
            self.O0OOO0OO0OOOOOO0O00OOOOOOO0OOOOOOOOOOOO0OOO000OOOOO0O0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = default_text
            self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = default_text
            self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen):
            """Draws a rectangle on the screen.
            Args:
                screen: The screen surface to draw on.
            Returns:
                None: Does not return anything.
            - Draws a filled rectangle on the screen surface using the object's position, size and background color attributes.
            - Loops through the object's elements list and draws each element."""
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 36)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(self.label, True, (0, 0, 0))
            screen.blit(text, (self.x, self.y))
            pygame.draw.rect(
                screen, (255, 255, 255), (self.x, self.y + 30, self.width, self.height), 2
            )
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(self.text, True, (0, 0, 0))
            screen.blit(text, (self.x + 5, self.y + 35))
    
        def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOO0OOOOOO0O0O000OO0OOOOOO0OOO0O0O0OOO0O0OO(self, event):
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = (
                    self.x < event.pos[0] < self.x + self.width
                    and self.y + 30 < event.pos[1] < self.y + 30 + self.height
                )
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN and self.active:
                if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_BACKSPACE:
                    self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = self.text[:-1]
                else:
                    self.text += event.unicode
    
    
    # Create UI panel
    OOOOOOO00O000OOOO0OO0OOOOOOOO0OOOO0OOOOOOOO0O0O00OOOOOO0OOO000OO = UIPanel(ui_panel_x, ui_panel_y, ui_panel_width, ui_panel_height)
    
    # Create input fields for customization
    OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OO = TextInputField(
        ui_panel_x + 10, 30, ui_panel_width - 20, 30, "Text:", ""
    )
    OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0O0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OO = NumericInputField(
        ui_panel_x + 10, 100, ui_panel_width - 20, 30, "Text Size:", 0
    )
    OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OO = NumericInputField(
        ui_panel_x + 10, 170, ui_panel_width - 20, 30, "Width:", 0
    )
    _OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OO = NumericInputField(
        ui_panel_x + 10, 250, ui_panel_width - 20, 30, "Height:", 0
    )
    
    O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OO = TextInputField(
        ui_panel_x + 10, 330, ui_panel_width - 20, 30, "Font Name:", "Arial"
    )
    OOOOOOOO0OO000O0OOO000OOO0OOO0OOO0OO0OOO00O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0OOOOOOOOO0OO000O0O00OO000 = CheckBox(ui_panel_x + 10, 450, "Bold", False, _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO=(0, 0, 0))
    _O000OOOOOO0O0OOOO0OOOOOOOO000OO0O000OOO00O0OOOOO0OO0OOO00O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0OOOOOOOOO0OO000O0O00OO000 = CheckBox(ui_panel_x + 10, 500, "Italic", False, _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO=(0, 0, 0))
    OOOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOOOO000OO0O000OOOOOO0O0O00OOOOOO0O0OO0OOO00O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0OOOOOOOOO0OO000O0O00OO000 = CheckBox(ui_panel_x + 10, 550, "Underline", False, _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO=(0, 0, 0))
    # Create color picker input field for customizing color
    _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOOO0OO0OOOOOOOO0OO0O000OOO00O0OOOO0OOOOO0O0OOOOOO000OOOOOOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOO00OOOOO0O000OOO0OOOOOO0OOO000OOO0OOO0OO = ColorPickerInputField(
        ui_panel_x + 10, 630, ui_panel_width - 20, 40, "Color:", (255, 0, 0)
    )
    
    ui_panel._OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OOO0OO0OO0 = [
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
        el.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = 20
    
    
    def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOO0OOOOOO0O0O000OO0OOOOOO0OOO0O0O0OOO0O0OOO0OO0OO0():
        global selected_element, scaling, scale_start_x, scale_start_y, scale_start_width, scale_start_height
        for event in pygame.event.get():
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
            elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                if scaling:
                    O0OO0OO000O0OOOOOO0OOOOOOOO000OO0O000OOOOOO0O0O0O0OOOOOO = False
                for button in buttons:
                    if (
                        button.x < event.pos[0] < button.x + button.width
                        and button.y < event.pos[1] < button.y + button.height
                    ):
                        button.selected()
                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = button
                for input_field in input_fields:
                    if (
                        input_field.x < event.pos[0] < input_field.x + input_field.width
                        and input_field.y
                        < event.pos[1]
                        < input_field.y + input_field.height
                    ):
                        input_field.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = input_field
                for text in text_elements:
                    if text.x < event.pos[0] < text.x + (
                        text.width + text.size
                    ) and text.y < event.pos[1] < text.y + (text.height + text.size):
                        text.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = text
                for check in checkboxes:
                    if check.x < event.pos[0] < check.x + (
                        check.width + check.size
                    ) and check.y < event.pos[1] < check.y + (check.height + check.size):
                        check.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = check
                for image in images:
                    if (
                        image.x < event.pos[0] < image.x + image.width
                        and image.y < event.pos[1] < image.y + image.height
                    ):
                        image.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = image
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
                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOO0OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO = None
            elif (
                event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN
                and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 3
                and selected_element
            ):
                O0OO0OO000O0OOOOOO0OOOOOOOO000OO0O000OOOOOO0O0O0O0OOOOOO = True
                O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOO00OO000 = event.pos[0]
                O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOOOOO0OOO = event.pos[1]
                O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = selected_element.width
                O0OO0OO000O0OOOOOO0OOOOOOOO000OO0OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = selected_element.height
    
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
                text_input_field.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = selected_element.text
                text_size_input_field.O0O000OOOO0OOOOOOOO000OOOOOOOOO00OOOOOO0 = selected_element.size
                width_input_field.O0O000OOOO0OOOOOOOO000OOOOOOOOO00OOOOOO0 = selected_element.width
                height_input_field.O0O000OOOO0OOOOOOOO000OOOOOOOOO00OOOOOO0 = selected_element.height
                font_name_input_field.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = selected_element.font_name
                bold_checkbox._O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO = selected_element.bold
                italic_checkbox._O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO = selected_element.italics
                underline_checkbox._O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO = selected_element.underlined
    
                if scaling and event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEMOTION:
                    selected_element.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = scale_start_width + (
                        event.pos[0] - scale_start_x
                    )
                    selected_element._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = scale_start_height - (
                        scale_start_y - event.pos[1]
                    )
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEMOTION:
                    if pygame.mouse.get_pressed()[0]:  # Left mouse button is held
                        selected_element.x += event.rel[0]
                        selected_element.y += event.rel[1]
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 4:
                    selected_element.size += 1
                elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 5:
                    selected_element.size -= 1
            for inspect in ui_panel.elements:
                if isinstance(inspect, ColorPickerInputField):
                    inspect.handle_event(event)
                else:
                    inspect.handle_event(event)
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN and event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_RETURN:
                # Update the selected element's properties with the UI panel values
                if selected_element:
                    selected_element.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = text_input_field.text
                    selected_element.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = text_size_input_field.value
                    selected_element.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = width_input_field.value
                    selected_element._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = height_input_field.value
                    selected_element.O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = font_name_input_field.text
                    selected_element.OOOOOOOO0OO000O0OOO000OOO0OOO0OO = bold_checkbox.checked
                    selected_element._O000OOOOOO0O0OOOO0OOOOOOOO000OO0O000OOO00O0OOOOO0OO0OO0 = italic_checkbox.checked
                    selected_element.OOOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOOOO000OO0O000OOOOOO0O0O00OOOOOO0O0OOO0OO = underline_checkbox.checked
            # Update the selected element's color based on the color picker value
            if selected_element:
                selected_element._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = color_picker_input_field.color
    
    
    def O0O0OO00OO0OOOOO0O000OOOOOO0O0O0():
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
            _O000OOOOOO0O0O0O0OO0OO0OOO0O0OO00OOOOOOOOOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OOOO0OO0OO0OOOOOOO000OOOOOOO00OOOOOOO0OOOOO00O0OOOO0OOOOOO0 = instruction_font.render(
                instruction_text, True, (255, 255, 255)
            )
            screen.blit(instruction_surface, (10, screen_height - 30))
            # Draw the UI panel
            ui_panel.draw(screen)
    
            pygame.display.flip()
    
    
    def O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OO():
        for bu in sidebar_buttons:
            bu.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = 20
        main()
    
    
    if __name__ == "__main__":
        start()    
        import pygame
    
    
    class OO0OOOOO00000OOO0OOOOOO000O0OOOO0OOOOO0O0O00OOOO0OO000O0O00OO000:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(
            self, x, y, text, _O000OOOO0OO0OO0O0OO0OOO00O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO=False, O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0=20, _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO=(255, 255, 255)
        ):
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = text
            self._O000OOOO0OO0OO0O0OO0OOO00O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO = is_checked
            self.OOOOOOOO0OO000O0OOO000OOO0OOO0OO = False
            self._O000OOOOOO0O0OOOO0OOOOOOOO000OO0O000OOO00O0OOOOO0OO0OO0 = False
            self.OOOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOOOO000OO0O000OOOOOO0O0O00OOOOOO0O0OOO0OO = False
            self.O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = None
            self.O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOO0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = font_size
            self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
            self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = False
            self.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = 20
            self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 20
            self.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = font_size
            self._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = color
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen):
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(self.font_name, self.size)
            font.set_bold(self.bold)
            font.set_italic(self.italics)
            font.set_underline(self.underlined)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(self.text, True, self.color)
            screen.blit(text, (self.x, self.y))
    
            # Draw the checkbox
            _O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0OOOOOOOOO0OO000O0O00OO000O0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect(self.x + 100, self.y, self.width, self.height)
            pygame.draw.rect(screen, self.color, checkbox_rect, 2)
            if self.is_checked:
                pygame.draw.line(
                    screen,
                    self.color,
                    (self.x + 105, self.y + 10),
                    (self.x + 115, self.y + 20),
                    5,
                )
                pygame.draw.line(
                    screen,
                    self.color,
                    (self.x + 115, self.y + 20),
                    (self.x + 135, self.y + 5),
                    5,
                )
    
        def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOO0OOOOOO0O0O000OO0OOOOOO0OOO0O0O0OOO0O0OO(self, event):
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                if (
                    self.x + 100 < event.pos[0] < self.x + 120
                    and self.y < event.pos[1] < self.y + 20
                ):
                    self._O000OOOO0OO0OO0O0OO0OOO00O0OOOO00000OOO0OOOOOO000O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO = not self.is_checked
    
        def _O0OOOO00000OOOOO0OOOOOOOO0O0O0O0OOOOOO0OOOOOO0O0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO(self, event):
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEMOTION:
                self._OOO0OO000O0O0O000OO0OOOOOO000OOOOOO0OOOOOO0O0OOO0OO = (
                    self.x < event.pos[0] < self.x + self.width
                    and self.y < event.pos[1] < self.y + self.height
                )
            elif event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                if self.hovered:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                else:
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.KEYDOWN and self.active:
                if event._OOOOO0O0OOOOOO0OOOO0OOO == pygame.K_BACKSPACE:
                    self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = self.text[:-1]
                else:
                    self.text += event.unicode    
    
    import pygame
    from PIL import Image, ImageDraw, ImageOps
    
    
    class OO0O0O0OO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0OO0O0OOOOOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x, y, image, _O0OOOO00OOOOOO0OO000O0OOOOO0OOO0OO0OOOO0O0OO000OO000O0O0OOO0OO0OOOOOO0="None"):
            self.O00OO000 = x
            self.OOOO0OOO = y
            self._O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = image
            self._O0OOOO00OOOOOO0OO000O0OOOOO0OOO0OO0OOOO0O0OO000OO000O0O0OOO0OO0OOOOOO0 = crop_mode  # "None" or "Circle"
            self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
            self.width, self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = self.image.size
            self.widtho, self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO0OO000O0 = self.image.size
            self.OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = ""
            self.OOOOOOOO0OO000O0OOO000OOO0OOO0OO = False
            self._O000OOOOOO0O0OOOO0OOOOOOOO000OO0O000OOO00O0OOOOO0OO0OO0 = False
            self.OOOOOOO0OOO0O0O0O0OOO0OO0OOOOOO000OOOOOOOOO000OO0O000OOOOOO0O0O00OOOOOO0O0OOO0OO = False
            self.O00OOOOO0OO000O0OOO0O0O0OOO0O0OOO0OO0OOOOOO0O0O0OO0OOOOOO0O0OO000OOOOOO0 = "Recources\Fonts\PixelifySans-Regular.ttf"
            self._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = (0, 0, 0)
            self.O0OO0OO00O000OOO0OOOOOOO0OOOOOO0 = self.width * self.height
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen):
            # Optionally apply cropping based on the selected cropping mode
            if self._O0OOOO00OOOOOO0OO000O0OOOOO0OOO0OO0OOOO0O0OO000OO000O0O0OOO0OO0OOOOOO0 == "Circle":
                # Crop the image to a circle using PIL
                O0O0OO00OO0OOOOOO0OO0OO00OOOOO0O = Image.new("L", (self.widtho, self.heighto), 0)
                O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0 = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, self.widtho, self.heighto), O00OOOOO0O000OOOOOO000OOOOO000OO=255)
                self.image.putalpha(mask)
    
            # Draw the image on the screen
            OOOOO0OOOOOO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = pygame.image.fromstring(
                self.image.tobytes(), self.image.size, self.image.mode
            )
            OOOOO0OOOOOO0OOOO0OOOOOOOO0OOOOOO0O0OO000OOOOOO0O0OO0OOO0O000OOOO0O0OO00OO0OOOOOO0OOOOOO0OOOOOO0 = pygame.transform.scale(pygame_image, (self.width, self.height))
            screen.blit(pygame_image, (self.x, self.y))    
            import pygame
    
    import sys
    
    # Initialize Pygame
    pygame.init()
    
    # Constants
    WIDTH, _O00OOOO0O0OOOOO0O0O0OOOOOOO0O000O00OO00OO0OO0 = 800, 600
    OOOOO0OOOOO0OOOO0OOOOO00OO0O0OOOO0OO0OOOOOOO0OO0OOOOO0OO0OOOOO00OO0O0O0O0O0OOO0OOOOOOOO0 = 20
    OOOOO0OOOOO0OOOO0OOOOO00OO0O0OOOO0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (100, 100, 100)
    OOO00OOOOO0O0O0OOOOOO0OOOO0O0OOOO0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (255, 255, 255)
    OO0OOOOOOOO0OOOOOOOOO0OOOOOOO0OOOO0O0OOOOO0OOOOO00OO0OO0OO0O0O0OOOO0OOOOOOOOO0OOO0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (255, 255, 0)
    OO0OOOOOOOO0OOOOOOOOO0OOOOOOO0OOOO0O0OOOOO0OOOOO00OO0OO0OO0O0O0OOOO0OOOOOOOOO0OOO0OO0OOOOOOO00OOOO0O0O0O0OOOOO0000OO0OO0000O00OO = 2
    _OO0OO0OO0O0OOOOOOO0OOO00OO0OO0O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (0, 0, 255)  # Blue for node labels
    
    # Node types and their labels
    OOO0O0O00OO000O0O0OOO0OO0OOOOOO0O0OO0OOOOOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0O0OO0OO0 = [
        {"label": "Remove Object", "action": "remove"},
        {"label": "Add Object", "action": "add"},
        {"label": "Reveal Object", "action": "reveal"},
        {"label": "Hide Object", "action": "hide"},
        {"label": "Move Object", "action": "move"},
        {"label": "Function", "action": "Script"},
        {"label": "If", "action": "if"},
        {"label": "is_clicked", "action": "clicked"},
    ]
    
    # Create a Pygame screen
    O0OO0OO000O0OOOO00OOOOOO0OOOOOO00OOOOOO0OOO0O0O0 = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Node Editor")
    
    # List to store nodes and connections
    OOO0O0O00OO000O0O0OOO0OO0OOOOOO0O0OO0OO0 = []
    _O0OOOO0OO000O0OOO0O0O0OOO0O0O00OOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OO0 = []
    O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = {"type": "Start", "label": "Start", "position": (50, HEIGHT // 2)}
    _OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = {"label": "End", "type": "End", "position": (WIDTH - 50, HEIGHT // 2)}
    nodes.append(start_node)
    nodes.append(end_node)
    
    # Constants for the inspector tab
    OO0O0O0OOOOOO0OOOOOOOOO0OOO0OOOOOO0O0OOOOO0OOOOO00OO0OO0OOO0OOOOOOOO0OO0O0OO0OOOOOOO00OOOO0O0O0O0OOOOO0000OO0OO0000O00OO = 200
    OO0O0O0OOOOOO0OOOOOOOOO0OOO0OOOOOO0O0OOOOO0OOOOO00OO0OO0OOO0OOOOOOOO0OO0O0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (50, 50, 50)
    
    # Create an Inspector rect
    _O000OOOOOO0O0O0O0OO0OO0OOOOO0OO0OOOOOO000O0OOOOOOO0O0OO0OO000O000OOOOOOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect(WIDTH - INSPECTOR_WIDTH, 0, INSPECTOR_WIDTH, HEIGHT)
    
    # Create a text input area
    OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect(
        WIDTH - INSPECTOR_WIDTH + 10, 50, INSPECTOR_WIDTH - 20, 100
    )
    OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = ""
    O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 36)
    OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
    
    
    # Function to add a new node to the canvas
    def OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0(node_type, position):
        nodes.append(
            {
                "type": node_type["label"],
                "position": position,
                "rect": pygame.Rect(20, 20, 20, 20),
            }
        )
    
    
    # Function to create a connection between two nodes
    def OO0OOOOOO0OOO0OOO0OOO0OOO0OO0OOO00O0OOOO0OO000O0OOO0O0O0OOO0O0O00OOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0(start_node, end_node):
        """
        Adds a connection between two nodes
        Args:
            start_node: The starting node of the connection 
            end_node: The ending node of the connection
        Returns: 
            None: Does not return anything
        - Appends a tuple containing the start and end nodes to the connections list
        - This records the connection between the two nodes passed as arguments
        - No value is returned as the connection is added by side effect of appending to the list
        - Only the connection between the two nodes is recorded, no checking is done on the nodes"""
        connections.append((start_node, end_node))
    
    
    # Function to draw the inspector tab
    def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0O0OO0OOO0O000OOOOOO0O0O0O0OO0OO0OOOOO0OO0OOOOOO000O0OOOOOOO0O0OO0OO000O000OOOOOO():
        """Draws the inspector rectangle on screen
        Args: 
            screen: The screen surface to draw on
        Returns:
            None: Does not return anything
        - Draws a rectangle on the screen surface using pygame's draw.rect method  
        - The rectangle is drawn with the color INSPECTOR_COLOR
        - The rectangle is drawn using the inspector_rect object which defines its position and size
        - No value is returned as the rectangle is drawn directly to the screen surface"""
        """Draws the inspector rectangle on screen
        Args:
            screen: The screen surface to draw on
        Returns: 
            None: Does not return anything
        - Draws a rectangle on the screen surface using pygame's draw.rect method
        - The rectangle is drawn with the color INSPECTOR_COLOR
        - The rectangle is drawn using the inspector_rect object which defines its position and size
        - No value is returned as the rectangle is drawn directly to the screen surface"""
        pygame.draw.rect(screen, INSPECTOR_COLOR, inspector_rect)
    
    
    # Function to display details about the selected node in the inspector tab
    def O0OO0OO000000OOO0OO000O0OO0OOOO0O0OO0OOO0O000OOOOOO0O0O0O0OO0OO0OOOOO0OO0OOOOOO000O0OOOOOOO0O0OO0OO000O000OOOOOO(node):
        """
        Display inspector details of a node
        Args:
            node: The node to display inspector details for
        Returns: 
            None: Does not return anything
        - Check if the passed node is not None
        - If node is valid, display its inspector details
        - No return value as function just displays details"""
        if node is not None:
            # Create a text input box for details
            pygame.draw.rect(screen, (255, 255, 255), text_input_rect)
            pygame.draw.rect(screen, (0, 0, 0), text_input_rect, 2)
    
            # Display details about the selected node
            if "type" in node:
                O0OOO0OO0OOOOOO0OOO0O0OOOO0OOOOO0O000OOOOOO000OOO0OO0OO0 = "Node Type: " + node["type"]
                O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 28)
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(details, True, (0, 0, 0))
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text.get_rect()
                text_rect.OOO0O0OO0OO000O0OOOOO0OOOOO000OO0OOOOOO0O00OOOOOOOO0O0OO = (text_input_rect.x + 10, text_input_rect.y + 10)
                screen.blit(text, text_rect)
            else:
                OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOOO0O0OO0OOOOOO0O00OO000OOO0O0OO = ""
    
    
    # Main loop
    _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = True
    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
    OO0OOOOOO0OOO0OOO0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
    O0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
    O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0O0OO0OOOO0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO = False
    _O0OOOO0OO000O0OOO0O0O0OOO0O0O00OOOOOO000O0OOOOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
    O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO00O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO000OO0O000OOOOOO0O0O00OOOOOO0 = False
    OOO000OO0O000OOOOOO0O0O00OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OO = None
    OOO0O0O00OO000O0O0OOO0OO0OOOOOO0O0OO0OOOO0O0OO000OO000O0O0O000OO0O000OOOOOO0O0O0O0OOOOOO = False
    O0OOO0OO0O000OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO0O000OOO0OO000O0OOO0O0O0O0OO0OO0 = {}
    
    while running:
        for event in pygame.event.get():
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.QUIT:
                _OOOOOOOOOOOOO0OOO0O0O0OOO0O0O00O000OOOOOO0O0O0O0OOOOOO = False
    
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN:
                if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                    OOOOO0OO0OO000O0O0OO0OO0 = pygame.mouse.get_pos()
                    if adding_node is not None:
                        add_node(adding_node, pos)
                        OO0OOOOOO0OOO0OOO0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
    
                    # Check if a node is clicked and make it the selected node
                    for node in nodes:
                        if node["rect"].collidepoint(pos):
                            O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = node
                            O0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = node
    
                    for idx, node_type in enumerate(node_types):
                        OOO0O0O00OO000O0O0OOO0OO0OOOOOO0O0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect(10, 10 + idx * 30, 200, 20)
                        if node_rect.collidepoint(pos):
                            OO0OOOOOO0OOO0OOO0OOO0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = node_type
    
                    for node in nodes:
                        if node["rect"].collidepoint(pos):
                            _O0OOOO0OO000O0OOO0O0O0OOO0O0O00OOOOOO000O0OOOOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = node
                            O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO00O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO000OO0O000OOOOOO0O0O00OOOOOO0 = True
                            OOO000OO0O000OOOOOO0O0O00OOOOOO0O0OO0OOOO0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OO = connecting_node["position"]
    
                elif event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 2:
                    OOOOO0OO0OO000O0O0OO0OO0 = pygame.mouse.get_pos()
                    for node in nodes:
                        if node["rect"].collidepoint(pos):
                            O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = node
                            O0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = node
                            O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0O0OO0OOOO0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO = True
                    OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO0O000OOOOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOO0OO0OOOOO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = text_input_rect.collidepoint(pos)
    
                if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 3:
                    OOOOO0OO0OO000O0O0OO0OO0 = pygame.mouse.get_pos()
                    for node in nodes:
                        if node["rect"].collidepoint(pos):
                            O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = node
                            OOO0O0O00OO000O0O0OOO0OO0OOOOOO0O0OO0OOOO0O0OO000OO000O0O0O000OO0O000OOOOOO0O0O0O0OOOOOO = True
                            break
    
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONUP:
                if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                    if drawing_line:
                        OOOOO0OO0OO000O0O0OO0OO0 = pygame.mouse.get_pos()
                        for node in nodes:
                            if node["rect"].collidepoint(pos) and node != connecting_node:
                                add_connection(connecting_node, node)
                        O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO00O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO000OO0O000OOOOOO0O0O00OOOOOO0 = False
                    _O0OOOO0OO000O0OOO0O0O0OOO0O0O00OOOOOO000O0OOOOOOO0O0OO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
    
                if event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                    if dragging_node and selected_node:
                        O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
                        O0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
    
                elif event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 2:
                    O0OO0OO00OOOOOO0OOO000OO0OOOOOO000O0OOOOOOO0O0OO0OOOOOO0O0OOO0OOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
                    O0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOOO0OO0OOOOOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = None
                    O0O0OO000OO000O0OOOOOOO0O0OO0OO00OOOOOO0O0OO0OOOO0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO = False
    
        screen.fill((0, 0, 0))
    
        for connection in connections:
            O0OO0OO0OOO0O0OOOO0OOOOO00OOOOOOOOO0O0OOO0OO0OOOOOOOO0OO0OO000O0O0OO0OO0 = connection[0]["position"]
            _OOOOOO0OOO0O0O0O0OOO0OOO0OO0OOOOOOOO0OO0OO000O0O0OO0OO0 = connection[1]["position"]
            pygame.draw.line(screen, LINE_COLOR, start_pos, end_pos, CONNECTION_WIDTH)
    
        for node in [start_node, end_node]:
            node["rect"] = pygame.draw.circle(
                screen, NODE_COLOR, node["position"], NODE_RADIUS
            )
            if OOO0O0O00OO000O0O0OOO0OO0OOOOOO0 == selected_node:
                pygame.draw.circle(screen, (0, 255, 0), node["position"], NODE_RADIUS)
            pygame.draw.circle(screen, LINE_COLOR, node["position"], NODE_RADIUS, 2)
    
        for idx, node_type in enumerate(node_types):
            OOO0O0O00OO000O0O0OOO0OO0OOOOOO0 = node_type["label"]
            OOO0O0O00OO000O0O0OOO0OO0OOOOOO0O0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = pygame.Rect(10, 10 + idx * 30, 200, 20)
            pygame.draw.rect(screen, NODE_COLOR, node_rect)
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 36)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(node, True, (255, 255, 255))
            screen.blit(text, (20, 20 + idx * 30))
    
        for node in nodes:
            node["rect"] = pygame.draw.circle(
                screen, NODE_COLOR, node["position"], NODE_RADIUS
            )
            if OOO0O0O00OO000O0O0OOO0OO0OOOOOO0 == selected_node:
                pygame.draw.circle(screen, (0, 255, 0), node["position"], NODE_RADIUS)
            pygame.draw.circle(screen, LINE_COLOR, node["position"], NODE_RADIUS, 2)
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 24)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(node["type"], True, TEXT_COLOR)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OOO0OO0OOO00OOOOOO0OOOOOO000O0OOOOOOO0O0OO = text.get_rect()
            text_rect._O0OOOO0OOOOOO0OOO0O0O0OOO0O0OO0OOOOOO000OOOOOO = (node["position"][0], node["position"][1] - NODE_RADIUS - 10)
            screen.blit(text, text_rect)
    
        if drawing_line:
            pygame.draw.line(
                screen,
                CONNECTION_COLOR,
                line_start,
                pygame.mouse.get_pos(),
                CONNECTION_WIDTH,
            )
    
        # Draw the inspector tab
        draw_inspector()
    
        # Show options for the selected node in the inspector tab
        show_inspector(selected_node)
    
        pygame.display.flip()
    
    # Quit Pygame
    pygame.quit()
    sys.exit()    # UI panel for editing properties
    
    import pygame
    
    # UI panel background color
    _O0OOO0OOO0O0O0OO0OO0OOOOOO0OOOOOOOOO0OOOOOOO0OOOO0O0OOOOOO00OOOO0OO0OOOOO0OOOOOOOO0OOOOOOO00OOOOOO0OOOOOOOO0OO0 = (200, 200, 200)
    
    
    class _O0OOO0OOO0O0O0OOOO0OOOOOO0OOOOOOOO0O0O00OOOOOO0OOO000OO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x, y, width, height):
            """
            Initialize a UI panel object
            Args:
                x: X coordinate of panel
                y: Y coordinate of panel
                width: Width of panel
                height: Height of panel
            Returns:
                None: Does not return anything
            - Sets x, y, width and height attributes of panel 
from arguments
            - Sets default background color
            - Initializes empty elements list to add UI elements later"""
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = width
            self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = height
            self.OOOOOOOOO0OOOOOOO0OO0OOO00O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = UI_PANEL_COLOR
            self._OOOOOO0OOO000OO0OOOOOO0O0O0OO000OOOOOO0OOO0O0O0OOO0O0OOO0OO0OO0 = []
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen):
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
                import playfab
    from SquarePixels.uimanagement.leaderboard import DoPost
    from playfab import PlayFabSettings, PlayFabErrors
    
    
    def OOOOOO0O0OOOOOO0OOO0O0OOOOOOO0OO00O0OOOO00O0OOOO0OO000O0OOOOOOO0OOO0O0O0OOO0O0OOOO0O0O0OOOO0O0O0O00OOOOO0OO000O0(request, callback, _O0OOOOOOOOOOO0O0OO0OO0OOO0O0OO0OO000O0O0O0OO000OOOOO00OO0OOOOOOOO0O0OOOO0OOOOO = None, _OOOOOO0O00OO000OOO0O0OO00OOOOOOOO0OOOOO000O00OO0OOOOOO0OO0OOOOOO0OOO0OO0OOOOOO000OOOOOOO0OO0OO0 = None):
        """
        Retrieves the user's PlayFab account details
        https://docs.microsoft.com/rest/api/playfab/client/account-management/getaccountinfo
        """
        if not PlayFabSettings._internalSettings.ClientSessionTicket:
            raise PlayFabErrors.PlayFabException("Must be logged in to call this method")
    
        def OO0OOOO000OOOOOOOO0OOOOOOOOOO0OOOOOOO0OO0OOOOOO0O0OOO0OOOO0OOOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(playFabResult, error):
            if callback:
                callback(playFabResult, error)
    
        return DoPost("/Client/GetAccountInfo", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)
    
    
    class OOO0OOOOOOO000OOOO0OOOOOOOOO0OOO0OOOOOO000OOOOOOOOO0OOOO00OOOOOO0OO000O0O00OOOOO0O000OOOOOO000OO0OOOOOO0O0OOO0OO0O000OOO0OOOOOO0OO0OOOO0OO0OOOOO0OO000O0OOO0O0O0O0OO0OO0OOO0O0OO00OOOOOOOO0OOOOO0O000OOOOOO0O0O0OOO0O0OOO0OO0OO0:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, OOOOOOO000000OOO0OO000O0OO0OOOO0OOOOO0OOO0O000OOOO0OOOOOOOO0O0OOOO0OOOOO00OOOOOO0O0OOO0O00OOOOOOOOO000OO=False):
            self.OOOOOOO000000OOO0OO000O0OO0OOOO0OOOOO0OOO0O000OOOO0OOOOOOOO0O0OOOO0OOOOO00OOOOOO0O0OOO0O00OOOOOOOOO000OO = ShowAvatarUrl
            
    def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOOOOOOOOO0O0OO0OO00OOOOOO000OOOOOOO0OO0OOOOO0OOOOOO0O000OOOO0OOOOOOOO0O0OOOO0OOOOO00OOOOOO(email):
        _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"Email":email}
        def _O0OOOOOO0OOOOOOOO000OOOOO000OOOOOOOOOOOO0OOOOO00O0OOOO0OOOOO0O(success, failure):
                if success:
                    print("Retrieved account details.")
                else:
                    print("failed to retrieve account details.")
                    if failure:
                        print("Here's some debug information:")
                        print(str(failure))
                        
        _OOOOOO0OOOOOO0O0OO0OO0OOOOOOO0OOO000OOOOO0O0OO = playfab.PlayFabClientAPI.GetAccountInfo(request, callback)
        print(result)
        _OOOOOO0OOOOOO0OOO0OOOOOOOOOOO00OOOOOO0O0OO0OO0OOO0O0OO = {"ProfileConstraints":PlayerProfileViewConstraints(True),"PlayFabId":result}
        playfab.PlayFabClientAPI.GetPlayerProfile()    # Color picker input field for customizing color
    
    import math
    
    import pygame
    
    
    class OO0OOOOO0OO000O0OOO000OO0OO000O000OOOOOOOOO0OOOO0O000OOO00O0OOOO0OOOOO0O0OOOOOO000OOOOOOOO0O0O0OOOO0O0O0OOOOO0OOOOOOOOO0OOO0O0OOOOO0O0OO0O000OOO0OOOOOO0OOO000OOO0OOO0OO:
        def O0OO0OOOO0OO0OOO0O000OOOOOO0O0O00O000OOOOOO0O0OOO0OO0OOOO0OO0OOO(self, x, y, width, height, label, default_color):
            self.O00OO000 = x
            self.OOOO0OOO = y
            self.OO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = width
            self._OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = height
            self.OOO000OOOO0OOOOOOOOOOOOO0OOOOOO0OOO000OO = label
            self._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = default_color
            self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
            self._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOOO0OO0OOOO0OOO0OO0O000OOOOO0OOOOOOOO000OO0OO000O0O0OOOOOOO0OO0OOO00OOOOOOOO0OOOOOO0OOO0OO0O000OOOOOOOOOO0O0OO0OO0 = 50  # Radius of the circular color picker
            self.OOOOOOOO00OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOO0O0O00OOOOOO0O0OO0OO0O0OO0OO0O0OO0OOO00O0OOOO0OO000O0OOO0O0O0OOO0O0OO00OOOOOO0OO000O0OOO000OOO0OO0OOOO00OO000 = self.x + 130
            self.OOOOOOOO00OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOO0O0O00OOOOOO0O0OO0OO0O0OO0OO0O0OO0OOO00O0OOOO0OO000O0OOO0O0O0OOO0O0OO00OOOOOO0OO000O0OOO000OOO0OO0OOOOOOO0OOO = self.y
            self.OOOOOOOO00OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOO0O0O00OOOOOO0O0OO0OO0O0OO0OO0O0OO0OOO00O0OOOO0OO000O0OOO0O0O0OOO0O0OO00OOOOOO0OO000O0OOO000OOO0OO0OOOOO0OOOO00O000OOOO0OOO0OOOOO0O0OO00000OOO = 15
            self.OOOOOOOO00OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOO0O0O00OOOOOO0O0OO0OO0O0OO0OO0O0OO0OOO00O0OOOO0OO000O0OOO0O0O0OOO0O0OO00OOOOOO0OO000O0OOO000OOO0OO0OOO00000OOO0OOOOOO00O000OOOO0OOOOOO00000OOOOOO0O0OO = 120
            self.OOOOOOOO00OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOO0O0O00OOOOOO0O0OO0OO0O0OO0OO0 = 50  # Default brightness
            self.OOOOOOOO00OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOO0O0O00OOOOOO0O0OO0OO0O0OO0OO0O0OO0OOO00O0OOOO0OO000O0OOO0O0O0OOO0O0OO00OOOOOO0OO000O0OOO000OOO0OO0OOOO0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO = False
    
        def O0OOO0OO00OOOOOOOO0OOOOOOO0OOOO0(self, screen):
            O00OOOOO0OO000O0OOO0O0O0OOO0O0OO = pygame.font.Font(None, 36)
            OOO0O0OO0OOOOOO0O00OO000OOO0O0OO = font.render(self.label, True, (0, 0, 0))
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
                _OOOOOOOO0OOOOOO0OOO0OO0O000OOOOO0OOOOOOOO0O0O0O0OO0OO0 = math.radians(angle)
                _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = pygame.Color(255, 0, 0)  # Initialize with red
                color._OOOO0OO0OO0OOO000OOOO0OOOOO = (angle, 100, self.brightness, 100)
                O00OO000 = int(self.x + 60 + self.color_dialog_radius * math.cos(radians))
                OOOO0OOO = int(self.y + 60 + self.color_dialog_radius * math.sin(radians))
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
    
        def _OOOOO0OOOOOOOO0O0O0O0OOO0OOOOO000OO0OOOOOO0O0OO0OOO0OOOOOO0O0O000OO0OOOOOO0OOO0O0O0OOO0O0OO(self, event):
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONDOWN and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                if self.is_color_picker_clicked(event.pos):
                    self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = True
                if (
                    self.brightness_control_x
                    <= event.pos[0]
                    <= self.brightness_control_x + self.brightness_control_width
                    and self.brightness_control_y
                    <= event.pos[1]
                    <= self.brightness_control_y + self.brightness_control_height
                ):
                    self.OOOOOOOO00OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOO0O0O00OOOOOO0O0OO0OO0O0OO0OO0O0OO0OOO00O0OOOO0OO000O0OOO0O0O0OOO0O0OO00OOOOOO0OO000O0OOO000OOO0OO0OOOO0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO = True
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEMOTION:
                if self.active:
                    if self.is_color_picker_clicked(event.pos):
                        self._O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = self.get_color_at(event.pos)
                if self.brightness_control_dragging:
                    # Move the brightness control up and down
                    OOO0O0O00OOOOOO0OO0OOOO0O0OO0OOOOOOO0OOO = event.pos[1] - 7.5
                    OOO0O0O00OOOOOO0OO0OOOO0O0OO0OOOOOOO0OOO = max(self.brightness_control_y, new_y)
                    OOO0O0O00OOOOOO0OO0OOOO0O0OO0OOOOOOO0OOO = min(
                        self.brightness_control_y + self.brightness_control_height - 15,
                        new_y,
                    )
                    self.OOOOOOOO00OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOO0O0O00OOOOOO0O0OO0OO0O0OO0OO0 = (
                        100
                        - (
                            (new_y - self.brightness_control_y)
                            / (self.brightness_control_height - 15)
                        )
                        * 100
                    )
            if event.OOO0O0OOOOOO0OOOOOOOO0OO0OOOOOO0 == pygame.MOUSEBUTTONUP and event.OOOOOOOOOOOOOOO0OOO0O0OOOOO0O0OO0OO000O0OOO0O0O0 == 1:
                self.OO0OOOOO00O0OOOOOOO0O0OO0O000OOOO0O000OO0OOOOOO0 = False
                self.OOOOOOOO00OOOOOO0O000OOOO0OOOOOO00000OOOOOO0O0OOOOO0O0O00OOOOOO0O0OO0OO0O0OO0OO0O0OO0OOO00O0OOOO0OO000O0OOO0O0O0OOO0O0OO00OOOOOO0OO000O0OOO000OOO0OO0OOOO0OOO0OO00OOOOOOOO0OOOOOO0OOOOOOO0OOOOOO0O000OOOOOO0O0O0O0OOOOOO = False
    
        def _O000OOOO0OO0OO0O0OO0OOO00O0OOOO0OO000O0OOO000OO0OO000O000OOOOOOO0OO0OOOOOOOO0OO0O000OOO00O0OOOO0OOOOO0O0OOOOOO000OOOOOOO0OO0OOO00O0OOOOOOO000OO0O000OOO00O0OOOO0OOOOO0O0OOOOOO0O0OOO0OO(self, pos):
            return (
                math.hypot(pos[0] - (self.x + 60), pos[1] - (self.y + 60))
                <= self.color_dialog_radius
            )
    
        def O0OOOOOO0OOOOOO0OOO0O0OOO0OO0OOO00O0OOOO0OO000O0OOO000OO0OO000O000OOOOOOO0OO0OOOOO0OOOOOOOO0O0OO(self, pos):
            OO0OOOOOOOO0O0O0O0OOOOOOOOO000OO0OOOOOO0 = math.degrees(math.atan2(pos[1] - (self.y + 60), pos[0] - (self.x + 60)))
            if angle < 0:
                angle += 360
            _O0OOOO0OO000O0OOO000OO0OO000O000OOOOOO = pygame.Color(255, 0, 0)
            color._OOOO0OO0OO0OOO000OOOO0OOOOO = (angle, 100, self.brightness, 100)
            return color