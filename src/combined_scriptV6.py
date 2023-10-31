if __name__ == '__main__':
    if __name__ == "__main__":
        
        import pygame as pig
        from SquarePixels.terraingen import terrain_gen as tgen
        from SquarePixels.uimanagement import logo, MainMen
        from SquarePixels.player import player as pl
        from SquarePixels.uimanagement.Character_creation import main
        from SquarePixels.game.game import game
        from SquarePixels.soundmanagement.music import play_music
    
        tile = [-1, 0]
    
        pig.init()
        clock: object = pig.time.Clock()
        not_skipped: bool = True
        reset_terrain: bool = False
        clicked: bool = False
        # Path to your video file
        video_file: str = r"Recources\\Company Animated Logo.mov"
        infoObject: object = pig.display.Info()
        screen: pig.Surface = pig.display.set_mode(
            (infoObject.current_w, infoObject.current_h)
        )
        pygame_icon = pig.image.load(
            r"Recources\program recources\Screenshot 2023-09-21 181742.png"
        )
        pig.display.set_icon(pygame_icon)  # pig.display.toggle_fullscreen()
    
        pig.display.set_caption("Square Pixel")
        pig.mouse.set_cursor(pig.SYSTEM_CURSOR_CROSSHAIR)
        # Path to the folder to save the extracted frames
        image_folder: str = r"Recources\\frames"
        colliders: list = []
        # Extract frames from the video
        # logo.extract_frames(video_file, image_folder)
        vx, vy = 0, 0  # infoObject.current_w/2, 0#infoObject.current_h /2
        # Call the function to play the video
        logo.play_intro_video(image_folder, not_skipped, screen, 0)
        image_folder: str = r"Recources\\NewHorizonsFrames"
        logo.play_intro_video(image_folder, not_skipped, screen, 1)
        play_music(r"Recources\sounds\music\Menu.mp3")
        MainMen.mainfunc()
        # Rest of game code goes here...
        terrain_gen = tgen.TerrainGenerator(
            width=(0, infoObject.current_w // 10), height=infoObject.current_h // 15
        )
        player_sprite = main()
        terrain_gen.generate_terrain(screen)
        player = pl.Player(vx, vy, infoObject.current_w - 40, 0)
        DayTime = 0
        Morning = 0
        # world:object = tgen.generate()
        # for square in world.tiles:
        #    render.draw(screen, square)
        # print(terrain_gen.terrain)
        # quit()
        # rect=pig.Rect((0,0),(infoObject.current_w,infoObject.current_h))
        running = True
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
    def generate_maze(WIDTH, CELL_SIZE, HEIGHT):
        maze = [
            ["#" for _ in range(WIDTH // CELL_SIZE)] for _ in range(HEIGHT // CELL_SIZE)
        ]
        visited = set()
    
        def can_visit(x, y):
            return (
                0 < x < WIDTH // CELL_SIZE - 1
                and 0 < y < HEIGHT // CELL_SIZE - 1
                and maze[y][x] == "#"
            )
    
        def carve_path(x, y):
            maze[y][x] = " "
            visited.add((x, y))
    
            directions = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
            random.shuffle(directions)
    
            for nx, ny in directions:
                if (nx, ny) not in visited and can_visit(nx, ny):
                    maze[(y + ny) // 2][(x + nx) // 2] = " "
                    carve_path(nx, ny)
    
        start_x, start_y = (
            random.randint(1, WIDTH // (2 * CELL_SIZE)) * 2 - 1,
            random.randint(1, HEIGHT // (2 * CELL_SIZE)) * 2 - 1,
        )
        carve_path(start_x, start_y)
    
        return maze
    
    
    # Breadth-First Search (BFS) Pathfinding
    def bfs(maze, start, goal):
        queue = deque([(start, [])])
        visited = set()
    
        while queue:
            current, path = queue.popleft()
    
            if current == goal:
                return path
    
            if current in visited:
                continue
    
            visited.add(current)
    
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if (
                    0 <= neighbor[0] < len(maze[0])
                    and 0 <= neighbor[1] < len(maze)
                    and maze[neighbor[1]][neighbor[0]] != "#"
                ):
                    queue.append((neighbor, path + [neighbor]))
    
        return None
    
    
    def start():
        # Initialize Pygame
        pygame.init()
        infoObject: object = pygame.display.Info()
        screen: pygame.Surface = pygame.display.set_mode(
            (infoObject.current_w, infoObject.current_h)
        )
        pygame_icon = pygame.image.load(
            r"Recources\program recources\Screenshot 2023-09-21 181742.png"
        )
        pygame.display.set_icon(pygame_icon)
    
        # Constants
        WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
        WHITE = (0, 0, 0)
        RED = (255, 0, 0)
        CELL_SIZE = 40
    
        # Create the screen
    
        # pygame.display.toggle_fullscreen()
        pygame.display.set_caption("Square Pixel")
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
    
        # Player
        player = pygame.Rect(40, 40, CELL_SIZE // 2, CELL_SIZE // 2)
    
        # Goal
        goal = pygame.Rect(680, 440, CELL_SIZE, CELL_SIZE)
        maze = generate_maze(WIDTH, CELL_SIZE, HEIGHT)
    
        # Game loop
        running = True
        won = False
        credits_font = pygame.font.Font(
            "Recources\Fonts\PixelifySans-Regular.ttf", 50
        )
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    return None
    
            # Get the current mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
    
            # Calculate the path from player to mouse using BFS algorithm
            start_pos = (player.centerx // CELL_SIZE, player.centery // CELL_SIZE)
            goal_pos = (mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)
            path = bfs(maze, start_pos, goal_pos)
    
            if path:
                # Move player towards the next position in the path
                next_pos = path[1] if len(path) >= 2 else path[0]
                dx = (next_pos[0] * CELL_SIZE + CELL_SIZE / 2) - player.centerx
                dy = (next_pos[1] * CELL_SIZE + CELL_SIZE / 2) - player.centery
                length = max(1, (dx**2 + dy**2) ** 0.5)
                dx /= length
                dy /= length
                player.x += dx
                player.y += dy
    
            # Check if player reaches the goal
            if player.colliderect(goal):
                won = True
    
            # Clear the screen
            screen.fill(WHITE)
    
            # Draw maze, player, and goal
            if not won:
                for y, row in enumerate(maze):
                    for x, cell in enumerate(row):
                        if cell == "#":
                            pygame.draw.rect(
                                screen,
                                RED,
                                (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                            )
    
            pygame.draw.rect(screen, (200, 231, 193), player)
            pygame.draw.rect(screen, (123, 143, 233), goal)
            text_surface = credits_font.render(
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
                text_surface = credits_font.render(
                    "press anything to skip", True, (100, 100, 100)
                )
                screen.blit(
                    text_surface,
                    (
                        WIDTH // 4 - text_surface.get_width() // 2,
                        HEIGHT - 50,
                    ),
                )
                credits_y = HEIGHT
                credits_text = [
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
                credits_font = pygame.font.Font(
                    r"Recources\Fonts\PixelifySans-Regular.ttf", 36
                )
                asciiartfont = pygame.font.SysFont("monospace", 20)
    
                while credits_y >= -len(credits_text) * 40 and won:
                    screen.fill(WHITE)
                    for i, text in enumerate(credits_text):
                        if i <= 42:
                            text_surface = credits_font.render(text, True, RED)
                            screen.blit(
                                text_surface,
                                (
                                    WIDTH // 2 - text_surface.get_width() // 2,
                                    credits_y + i * 40,
                                ),
                            )
                        else:
                            text_surface = asciiartfont.render(text, True, (100, 255, 100))
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
                        if event.type == pygame.QUIT:
                            running = False
                            won = False
                            pygame.quit()
                            sys.exit()
                        if event.type == pygame.KEYDOWN:
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
    
    active_chunks = [(int, int)]
    creatures = []
    spawned = False
    placey = int
    placex = int
    
    
    class Enemy_manager:
        def __init__(self, active_chunks=[(int, int)], creatures=[]) -> None:
            """
            Initializes an Enemy_manager object.
    
            Parameters:
            - active_chunks (list of tuples): List of active chunks represented as tuples of two integers.
            - creatures (list): List to store Enemy objects.
    
            Returns:
            None
            """
            self.active_chunks = active_chunks
            self.creatures = creatures
    
        def spawn(self, air, objectinfo):
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
                    spawned = False
                    while not spawned:
                        placey = rand(0, objectinfo.current_h)
                        placex = rand(i[0], i[1])
                        if any(a.collidepoint(placex, placey) for a in air):
                            self.creatures.append(enemy.Enemy(placey, placex))
                            spawned = True
    
        def update(self, x, y, air, objectinfo, colliders, screen, player, day):
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
            if len(self.creatures) <= rand(1, 2):  # and day == 1:
                self.spawn(air, objectinfo)
    
            # if day == 0 and len(self.creatures) > 0:
            #    self.creatures.pop(rand(0, len(self.creatures)))
            for creature in self.creatures:
                creature.update(x, y, colliders, air, player, screen)    
                import pygame as pig
    
    import random
    
    import math
    from PIL import Image, ImageSequence
    
    
    def load_gif_animation(gif_path):
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
        frames = load_gif_animation("example.gif")
        for frame_surface in frames:
            # Display or manipulate each frame_surface as needed
            # (e.g., blit it onto a Pygame display)
        """
        # Load the GIF image using Pillow
        gif_image = Image.open(gif_path)
    
        # Convert the GIF frames to pig surfaces
        frames = []
        for frame in ImageSequence.Iterator(gif_image):
            frame_surface = pig.image.fromstring(frame.tobytes(), frame.size, frame.mode)
            frames.append(frame_surface)
        frames.pop(0)
        return frames
    
    
    class Enemy:
        def __init__(
            self,
            enemyy=random.randint(0, pig.display.get_window_size()[1]),
            enemyx=random.randint(0, pig.display.get_window_size()[0]),
            health=random.randint(3, 7),
            defence=random.randint(1, 4),
            passive=False,
            damageamount=random.randint(2, 5),
            attackstrength=random.randint(2, 5),
        ):
            self.enemyy = enemyy
            self.enemyx = enemyx
            self.health = health
            self.defence = defence
            self.passive = passive
            self.attackstrength = attackstrength
            self.damageamount = damageamount
            self.direction = False  # left
            self.spit = False
            self.left = load_gif_animation(
                r"Recources\creatures\enemies\Little Demon\wall climbing\Little demon(1)(1)(1).gif"
            )
            self.right = load_gif_animation(
                r"Recources\creatures\enemies\Little Demon\wall climbing\Little demon(2)(1).gif"
            )
            self.rspitattack = load_gif_animation(
                r"Recources\creatures\enemies\Little Demon\attack\Little demon(1)(1).gif"
            )
            self.lspitattack = load_gif_animation(
                r"Recources\creatures\enemies\Little Demon\attack\Little demon(1).gif"
            )
    
        def roundtoblock(self, x, base=15):
            """
            Rounds a number 'x' to the nearest multiple of 'base'.
    
            Parameters:
            - x (float): The number to be rounded.
            - base (float, optional): The multiple to which 'x' should be rounded. Default is 15 which is the block size in the world.
    
            Returns:
            float: The rounded value of 'x' to the nearest multiple of 'base'.
            """
            return base * round(x / base)
    
        def update(self, x, y, colliders, sky, player, screen):
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
            distance = math.sqrt((self.enemyx - x) ** 2 + (self.enemyy - y) ** 2)
            if distance <= 30:  # two blocks
                self.attack(player)
            self.draw(screen)
            self.spit = False
    
        def attacked(self):
            pass
    
        def attack(self, player):
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
            self.spit = True
    
        def move(self, x, colliders, sky):
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
                            self.direction = True
                        else:
                            self.direction = False
                            self.enemyx -= 1
                    else:
                        self.enemyx = self.roundtoblock(self.enemyx)
                        if self.enemyx <= x:
                            self.enemyx -= 1
                        else:
                            self.enemyx += 1
                if any(air.collidepoint(self.enemyx, self.enemyy + 3) for air in sky):
                    self.enemyy += 5
            else:
                # implement passive logic
                pass
    
        def draw(self, screen: pig.display):
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
                    self.right = load_gif_animation(
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
                        self.rspitattack = load_gif_animation(
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
                    self.left = load_gif_animation(
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
                        self.lspitattack = load_gif_animation(
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
    
    
    def game(
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
        music.play_music(r"Recources\sounds\music\ingame\music\Ingame1.mp3", volume=0.2)
        enemymanager = enemy_manager.Enemy_manager([(0, infoObject.current_w)])
        while running:
            clicked = False
            if reset_terrain:
                terrain_gen.run(screen)
            # pig.draw.rect(screen,(.100,.100,.100,50),rect)
            screen.fill((0.035, 206, 235))
    
            if Morning == 0:
                DayTime = DayTime + 0.005
            else:
                DayTime = DayTime - 0.005
                if DayTime <= 0:
                    Morning = 0
            sky, colliders = render.render_terrain(
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
    
    
    def main(ip, name):
        # Initialize the game
        pygame.init()
    
        # Set up the game window
        o_p_c: list = []
        screen_width: int = 800
        screen_height: int = 600
        screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height))
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
        # Game loop
        running: bool = True
        while running:
            clock.tick(FPS)
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and player.y == screen_height - 20:
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
                    elif event.key == pygame.K_p and typing == False:
                        if paint == False:
                            paint = True
                        else:
                            paint = False
                    elif event.key == pygame.K_g and typing == False:
                        if gravity == False:
                            gravity = True
                            player.gravityi = gravity
                        else:
                            gravity = False
                            player.gravityi = gravity
                    elif event.key == pygame.K_i and typing == False:
                        if player.inverse == False:
                            player.inverse = True
                        else:
                            player.inverse = False
                    elif event.key == pygame.K_r and typing == False:
                        if player.rainbow == False:
                            player.rainbow = True
                        else:
                            player.rainbow = False
                    elif event.key == pygame.K_0 and typing == False:
                        if ai == False:
                            print("AI activated")
                            ai = True
                        else:
                            print("AI deactivated")
                            ai = False
                    elif event.key == pygame.K_g and typing:
                        input_box += "g"
                    elif event.key == pygame.K_p and typing:
                        input_box += "p"
                    elif event.key == pygame.K_i and typing == True:
                        input_box += "i"
                    elif event.key == pygame.K_r and typing == True:
                        input_box += "r"
                    elif event.key <= 127 and typing:
                        input_box += chr(event.key)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        player.velocity_x = -0.9
                    if event.key == pygame.K_RIGHT:
                        player.velocity_x = 0.9
    
            # Update AI player if AI flag is True
            if ai:
                aiplayer.update(circle_x, circle_y)
    
            # Update player location
            player.update(screen_height, screen_width)
    
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
        import pygame
    
    import random
    
    # Initialize Pygame
    pygame.init()
    
    # Set up the screen
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bouncing Balls Animation")
    
    # Define colors
    WHITE = (255, 255, 255)
    
    
    # Define Ball class
    class Ball:
        def __init__(self, x, y, radius):
            self.radius = radius
            self.color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            self.x = x
            self.y = y
            self.dx = random.choice([-1, 1]) * random.randint(1, 3)
            self.dy = random.choice([-1, 1]) * random.randint(1, 3)
    
        def update(self):
            self.x += self.dx
            self.y += self.dy
    
            # Check for collisions with the screen edges
            if self.x - self.radius < 0 or self.x + self.radius > screen_width:
                self.dx *= -1
            if self.y - self.radius < 0 or self.y + self.radius > screen_height:
                self.dy *= -1
    
        def draw(self):
            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
    
        def eat(self, other_ball):
            if self.radius > other_ball.radius:
                self.radius += int(other_ball.radius * 0.2)  # Increase radius
                other_ball.reset()  # Reset the smaller ball
    
        def reset(self):
            self.x = random.randint(self.radius, screen_width - self.radius)
            self.y = random.randint(self.radius, screen_height - self.radius)
            self.radius = random.randint(10, 30)
            self.color = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            self.dx = random.choice([-1, 1]) * random.randint(1, 3)
            self.dy = random.choice([-1, 1]) * random.randint(1, 3)
    
    
    # Create a list to store the balls
    balls = []
    
    # Create some initial balls
    for _ in range(10):
        x = random.randint(30, screen_width - 30)
        y = random.randint(30, screen_height - 30)
        radius = random.randint(10, 30)
        ball = Ball(x, y, radius)
        balls.append(ball)
    
    # Game loop
    running = True
    clock = pygame.time.Clock()
    
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # Clear the screen
        screen.fill(WHITE)
    
        # Update and draw the balls
        for ball in balls:
            ball.update()
            ball.draw()
    
        # Check for collisions between balls
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                dx = balls[i].x - balls[j].x
                dy = balls[i].y - balls[j].y
                distance = ((dx**2) + (dy**2)) ** 0.5
    
                if distance < balls[i].radius + balls[j].radius:
                    if balls[i].radius > balls[j].radius:
                        balls[i].eat(balls[j])
                    else:
                        balls[j].eat(balls[i])
    
        # Remove balls that are too big
        balls = [ball for ball in balls if ball.radius < 500]
    
        # Spawn new balls
        while len(balls) < 10:
            x = random.randint(30, screen_width - 30)
            y = random.randint(30, screen_height - 30)
            radius = random.randint(10, 30)
            ball = Ball(x, y, radius)
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
    
    selected = None
    inven = False
    holdobject = [Item, 999999999999999999]
    unaturalblocks = []
    
    
    class Player:
        """
        Represents the player character in the game.
        """
    
        def __init__(self, x, y, health_bar_length, xp):
            """
            Initializes the Player object.
    
            Parameters:
            - x (int): The initial x-coordinate of the player.
            - y (int): The initial y-coordinate of the player.
            - health_bar_length (int): The length of the health bar displayed on the screen.
            """
            # Initialize player attributes
            self.x = x
            self.y = y
            self.xp = xp
            self.width = 5
            self.height = 5
            self.jump = False
            self.bash_power = 3
            self.bash_cooldown = 0
            self.aiming = False
            self.arrow_pos = pig.mouse.get_pos()
            self.arrow_end_pos = pig.mouse.get_pos()
            self.speed = 3
            self.digging = False
            self.gravityi = True
            self.gravity = 0.2
            self.velocity_x = 0
            self.velocity_y = 0
            self.trail = []
            self.inverse = False
            self.rainbow = True
            self.platform = False
            self.click = (0, 0)
            self.place = (0, 0)
            self.current_health = 200
            self.target_health = 500
            self.max_health = 1000
            self.health_bar_length = health_bar_length
            self.health_ratio = self.max_health / self.health_bar_length
            self.health_change_speed = 5
    
        def respawn(self, sky, infoObject, active_chunks=[(int, int)]):
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
            player_inventory.items = [
                [None for _ in range(player_inventory.rows)]
                for _ in range(player_inventory.col)
            ]
            # Reset player health and find a respawn location
            self.current_health = 200
            self.target_health = 500
            self.xp = 0
            respawned = False
            for i in active_chunks:
                while not respawned:
                    placey = random.randint(0, infoObject.current_h)
                    placex = random.randint(i[0], i[1])
                    if any(a.collidepoint(placex, placey) for a in sky):
                        respawned = True
                        self.x = placex
                        self.y = placey
                        return None
    
        def get_damage(self, amount):
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
                        channel=4,
                        volume=4,
                    )
            if self.target_health < 0:
                self.target_health = 0
                if not pig.mixer.Channel(4).get_busy():
                    music.play_music(
                        r"Recources\sounds\player\death.mp3",
                        0,
                        channel=4,
                        volume=1,
                    )
    
        def get_health(self, amount):
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
                self.target_health = self.max_health
    
        def advanced_health(self, screen):
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
            transition_width = 0
            transition_color = (255, 0, 0)
            if self.current_health < self.target_health:
                self.current_health += self.health_change_speed
                transition_width = int(
                    (self.target_health - self.current_health) / self.health_ratio
                )
                transition_color = (0, 255, 0)
            if self.current_health > self.target_health:
                self.current_health -= self.health_change_speed
                transition_width = int(
                    (self.target_health - self.current_health) / self.health_ratio
                )
                transition_color = (255, 255, 0)
            health_bar_width = int(self.current_health / self.health_ratio)
            health_bar = pig.Rect(30, 45, health_bar_width, 25)
            transition_bar = pig.Rect(health_bar.right, 45, transition_width, 25)
    
            pig.draw.rect(screen, (255, 0, 0), health_bar)
            pig.draw.rect(screen, transition_color, transition_bar)
            pig.draw.rect(screen, (255, 255, 255), (30, 45, self.health_bar_length, 25), 4)
    
        def is_colliding(self, collider) -> typing.Tuple[str, bool]:
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
    
        def bash(self, collider, screen):
            """
            Perform a bash ability on a collider.
    
            Parameters:
            - collider: The object to perform the bash on.
            - screen: Pygame display surface.
    
            Returns:
            None
            """
            if self.bash_power > 0 and self.bash_cooldown == 0:
                self.bash_power -= 1
                self.bash_cooldown = 60  # Cooldown for 60 frames (1 second)
                self.fire(collider, screen)
    
        def dig(self, collider, colliders: list):
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
    
        def draw(self, screen, character):
            """
            Draw the player character on the screen.
    
            Parameters:
            - screen: Pygame display surface.
            - character (str): The path to the character image to be drawn.
    
            Returns:
            None
            """
            chrect = pig.Rect(self.x, self.y, self.width, self.height)
            cim = pig.image.load(character)
            # scale = (float("."+f"{self.width}"), float("."+f"{self.height}"))
            scale = (540, 400)
            image = pig.transform.scale(cim, scale)
            # add custom character collisions here
            image.get_rect()
            screen.blit(image, (self.x - 100, self.y - 150))
            if self.aiming:
                pig.draw.line(screen, (0, 255, 0), self.arrow_pos, self.arrow_end_pos, 2)
    
        def fire(self, collider, screen):
            """
            Fire an arrow 
            from the player character.
    
            Parameters:
            - collider: The object to fire at.
            - screen: Pygame display surface.
    
            Returns:
            None
            """
            dir_vector = (
                self.arrow_end_pos[0] - self.arrow_pos[0],
                self.arrow_end_pos[1] - self.arrow_pos[1],
            )
            magnitude = math.sqrt(dir_vector[0] ** 2 + dir_vector[1] ** 2)
            if magnitude != 0:
                normalized_vector = (dir_vector[0] / magnitude, dir_vector[1] / magnitude)
                speed = 10
                dx = normalized_vector[0] * speed
                dy = normalized_vector[1] * speed
    
        def start_digging(self):
            """
            Start the digging action.
    
            Returns:
            None
            """
            self.digging = True
    
        def stop_digging(self):
            """
            Stop the digging action.
    
            Returns:
            None
            """
            self.digging = False
    
        def move(self, screen, infoObject, tile, terrain):
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
            mousex, mousey = pig.mouse.get_pos()
            Mainfont = pig.font.Font(pig.font.match_font("Impact"), 300)
    
            font = pig.font.Font(pig.font.match_font("calibri"), 26)
            item_bar.draw(ychange=(False, 0))
            if selected:
                self.render_selection(screen, mousex, mousey, font)
            looking = False
            if tile != [-1, 0]:
                self.get_item(tile)
    
            for event in pig.event.get():
                if event.type == pig.QUIT:
                    quit()
                elif event.type == pig.MOUSEBUTTONDOWN:
                    tmp = self.handle_item_bar(event, terrain, holdobject)
                    if tmp != None:
                        return tmp
                elif event.type == pig.KEYDOWN:
                    if event.key == pig.K_UP or event.key == pig.K_SPACE:
                        self.player_jump
                    elif event.key == pig.K_LEFT or event.key == ord("a"):
                        self.velocity_x = -self.speed
                        music.play_music(
                            r"Recources\sounds\player\running.mp3",
                            1,
                            channel=2,
                            volume=15,
                        )
                    elif event.key == pig.K_RIGHT or event.key == ord("d"):
                        self.velocity_x = self.speed
                        music.play_music(
                            r"Recources\sounds\player\running.mp3",
                            1,
                            channel=2,
                            volume=15,
                        )
                    elif event.key == pig.K_r:
                        return True, False
                    elif event.key == pig.K_e or event.key == ord("e"):
                        inven = True
                        self.open_inventory(screen, infoObject, Mainfont, font)
    
        def update(
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
            selfbounds = pig.Rect(self.x, self.y, self.width, self.width)
            self.advanced_health(screen)
            # Check for collisions with colliders
            self.gravityi = True  # Assume gravity is applied unless a collision is detected
    
            for collider in colliders:
                iscolliding = selfbounds.colliderect(collider)
                if iscolliding:
                    self.gravityi = False
                    # Adjust the player's position to be on top of the block
                    self.y = collider.y - self.height  # Place player on top of the block
                    self.platform = True
                    if self.jump and self.platform:
                        self.y -= 5
                        self.jump = False
                        self.platform = False
                    self.velocity_y = 1
    
            if self.gravityi:
                self.velocity_y += self.gravity
    
            self.x += self.velocity_x
            if self.gravityi:
                self.y += self.velocity_y
    
            if self.y > screen_height - 20:
                self.y = screen_height - 20
                self.velocity_y = 0
            if self.x <= 0:
                self.velocity_x = 1
            if self.x >= screen_width:
                self.velocity_x = -1
    
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
                #        gravity = 0
                #    #    self.bash(collider, screen)  # Perform bash ability on collision
    
            # Update arrow position if aiming
            if self.aiming:
                self.arrow_end_pos = pig.mouse.get_pos()
    
        def delete_tile(self, terrain, tile):
            """
            Delete a tile 
        from the terrain.
    
            Parameters:
            - terrain (list): The terrain map of the game.
            - tile: The tile to delete.
    
            Returns:
            object: The modified tile.
            """
            y = tile
            # Check if the provided coordinates are within the bounds of the terrain
            # if 0 <= self.click[1] < len(terrain) and 0 <= self.click[0] < len(terrain[self.click[1]]):
            # Set the value at the specified position to 8 (sky block/empty tile)
            try:
                a = terrain[self.click[1] // 15][self.click[0] // 15]
                b = terrain[(self.click[1] + 5) // 15][(self.click[0] - 5) // 15]
                c = terrain[(self.click[1] - 5) // 15][(self.click[0] + 5) // 15]
                d = terrain[(self.click[1] + 5) // 15][self.click[0] // 15]
                e = terrain[(self.click[1] - 5) // 15][self.click[0] // 15]
                f = terrain[self.click[1] // 15][(self.click[0] - 5) // 15]
                g = terrain[self.click[1] // 15][(self.click[0] + 5) // 15]
                h = [a, b, c, d, e, f, g]
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
                blocks = [a, b, c, d, e, f, g]
                for x in blocks:
                    if x == 2 and y[0] != 1:
                        y[0] = 0
                        y[1] += 1
                    if x == 0 and y[0] != 0:
                        y[0] = 1
                        y[1] += 1
                return y
            except:
                # print("tile does not exist")
                None
            # else:
            #   print("Invalid coordinates")
    
        def placeitem(self, object, terrain):
            """
            Place an item in the game world.
    
            Parameters:
            - object: The item to place.
            - terrain (list): The terrain map of the game.
    
            Returns:
            None
            """
            global unaturalblocks
            item_ids = {
                "0": 10,
                "1": 11,
            }
            if terrain[self.place[1] // 15][self.place[0] // 15] == 8:
                print("<_-.-_>")
                block = item_ids[f"{object[0].id}"]
                terrain[self.place[1] // 15][self.place[0] // 15] = block
                object[1] -= 1
                if object[1] == 0:
                    object = [Item, 999999999999999999]
                return terrain
    
        def breakunaturalblock():
            pass
    
        def handle_item_bar(self, event, terrain, holdobject):
            """
            Handle interactions with the item bar.
    
            Parameters:
            - event: The pygame event object.
            - terrain (list): The terrain map of the game.
            - holdobject: The object currently held by the player.
    
            Returns:
            Tuple[bool, bool, object]: A tuple containing game state information and the current held object.
            """
            if event.button == 1:
                self.click = pig.mouse.get_pos()
                pos = pig.mouse.get_pos()
                try:
                    gridpos = item_bar.Get_pos()
                    if item_bar.In_grid(pos[0], pos[1]):
                        if selected:
                            selected = item_bar.Add(selected, gridpos)
                        elif item_bar.items[gridpos[0]][gridpos[1]]:
                            selected = item_bar.items[gridpos[0]][gridpos[1]]
                            item_bar.items[gridpos[0]][gridpos[1]] = None
                except:
                    None
                    # clicked out of inventory
                return False, True, holdobject
            if event.button == 3 and holdobject != [Item, 999999999999999999]:
                self.place = pig.mouse.get_pos()
                return self.placeitem(holdobject, terrain)
    
        def draw_xp(self):
            pass
    
        def player_jump(self):
            """makes the player jump"""
            self.velocity_y -= 3
            self.jump = True
            music.play_music(
                r"Recources\sounds\player\jump.mp3",
                1,
                channel=3,
                volume=5,
            )
    
        def render_selection(self, screen, mousex, mousey, font):
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
            obj = font.render(str(selected[1]), True, (0, 0, 0))
            screen.blit(obj, (mousex + 15, mousey + 15))
    
        def get_item(self, tile):
            """
            Get an item and add it to the player's inventory.
    
            Parameters:
            - tile: The item to add to the inventory.
    
            Returns:
            None
            """
            looking = True
            x = 0
            y = 0
            itemscollected = [Item(tile[0]), tile[1]]
            while looking:
                if player_inventory.items[x][y]:
                    if player_inventory.items[x][y][0].id == itemscollected[0].id:
                        player_inventory.items[x][y][1] += itemscollected[1]
                        tile = [-1, 0]
                        looking = False
                    else:
                        if x <= 27:
                            x += 1
                        else:
                            y += 1
                            x = 0
                else:
                    player_inventory.Add(itemscollected, (x, y))
                    tile = [-1, 0]
                    looking = False
    
        def open_inventory(self, screen, infoObject, Mainfont, font):
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
                mousex, mousey = pig.mouse.get_pos()
                # draw the screen
                screen.fill((0, 0, 0, 50))
                backround = pig.Surface([640, 480], pig.SRCALPHA)
                text = Mainfont.render("Inventory", True, (255, 255, 255), (100, 100, 100))
                screen.blit(
                    text,
                    (
                        infoObject.current_w / 5,
                        infoObject.current_h - 350,
                    ),  # (infoObject.current_h - infoObject.current_h /1.5, infoObject.current_w / 2 - 150)
                )
                #
                screen.blit(backround, (0, 0))
                player_inventory.draw(ychange=(False, 0))
                item_bar.draw(ychange=(True, infoObject.current_h / 1.64))
                crafting_grid.draw(ychange=(False, 0))
                # if holding something, draw it next to mouse
                if selected:
                    screen.blit(selected[0].resize(30), (mousex, mousey))
                    obj = font.render(str(selected[1]), True, (0, 0, 0))
                    screen.blit(obj, (mousex + 15, mousey + 15))
                pig.display.update()
                for event in pig.event.get():
                    if event.type == pig.QUIT:
                        quit()
                    if event.type == pig.KEYDOWN:
                        inven = False
                    if event.type == pig.MOUSEBUTTONDOWN:
                        # if right clicked, get a random item
                        if event.button == 3:
                            selected = [Item(random.randint(0, 3)), 1]
                        elif event.button == 1:
                            try:
                                pos = pig.mouse.get_pos()
                                gridpos = player_inventory.Get_pos()
                                if player_inventory.In_grid(pos[0], pos[1]):
                                    if selected:
                                        selected = player_inventory.Add(selected, gridpos)
                                    elif player_inventory.items[gridpos[0]][gridpos[1]]:
                                        selected = player_inventory.items[gridpos[0]][
                                            gridpos[1]
                                        ]
                                        player_inventory.items[gridpos[0]][
                                            gridpos[1]
                                        ] = None
                                gridpos = crafting_grid.Get_pos()
                                if crafting_grid.In_grid(pos[0], pos[1]):
                                    if selected:
                                        selected = crafting_grid.Add(selected, gridpos)
                                    elif crafting_grid.items[gridpos[0]][gridpos[1]]:
                                        selected = crafting_grid.items[gridpos[0]][
                                            gridpos[1]
                                        ]
                                        crafting_grid.items[gridpos[0]][gridpos[1]] = None
                                gridpos = item_bar.Get_pos()
                                if item_bar.In_grid(pos[0], pos[1]):
                                    if selected:
                                        selected = item_bar.Add(selected, gridpos)
                                    elif item_bar.items[gridpos[0]][gridpos[1]]:
                                        selected = item_bar.items[gridpos[0]][gridpos[1]]
                                        item_bar.items[gridpos[0]][gridpos[1]] = None
                            except:
                                None  # Handle errors gracefully
            item_bar.y = infoObject.current_h / 1.2
    
        def draw_trail(self, screen: pig.Surface) -> None:
            """
            Draw the trail of the object on the specified Pygame screen.
    
            Args:
                screen (pygame.Surface): The Pygame surface on which to draw the trail.
    
            Returns:
                None
            """
            trail_s_num: int = 1
            trail_l_num: int = len(self.trail)
            add_tsize: int = 1
    
            if self.inverse:
                for position in self.trail:
                    pig.draw.circle(
                        screen, (255, 255, 255), position, (trail_l_num - trail_s_num)
                    )
                    trail_s_num += 1
            else:
                if self.rainbow:
                    hue_step = 360 / len(self.trail)
                    hue = 0
                    for position in self.trail:
                        rgb = colorsys.hsv_to_rgb(hue / 360, 1, 1)
                        r, g, b = [int(c * 255) for c in rgb]
                        pig.draw.circle(
                            screen, (r, g, b), position, (trail_s_num + add_tsize)
                        )
                        add_tsize += 0.5
                        hue += hue_step
                else:
                    r: int = 255
                    g: int = 255
                    b: int = 255
                    for position in self.trail:
                        pig.draw.circle(
                            screen, (r, g, b), position, (trail_s_num + add_tsize)
                        )
                        add_tsize += 0.5
    
        def clear_trail(self) -> None:
            """
            Clear the trail of the object.
    
            Returns:
                None
            """
            self.trail = []  # Clear the trail    import pygame as pig
    
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
            import math
    
    
    def LightAlgorithm(colors, x, y, playerX, playerY, TimeOfDay):
        SunPos = [(TimeOfDay * 25), TimeOfDay*10]
        blockPos = [x, y]
        Darken = round(math.dist(blockPos, SunPos))
        Darken = Darken * TimeOfDay
        num1 = 100
        num2 = 139
        num3 = 69
        num4 = 19
        num5 = 115
        num6 = 85
        num7 = 34
        num8 = 0
        num9 = 128
        num10 = 211
        num11 = 255
        num12 = 223
        num13 = 135
        num14 = 206
        num15 = 235
        if num1 - Darken < 0:
            num1 = Darken
        if num2 - Darken < 0:
            num2 = Darken
        if num3 - Darken < 0:
            num3 = Darken
        if num4 - Darken < 0:
            num4 = Darken
        if num5 - Darken < 0:
            num5 = Darken
        if num6 - Darken < 0:
            num6 = Darken
        if num7 - Darken < 0:
            num7 = Darken
        if num8 - Darken < 0:
            num8 = Darken
        if num9 - Darken < 0:
            num9 = Darken
        if num10 - Darken < 0:
            num10 = Darken
        if num11 - Darken < 0:
            num11 = Darken
        if num12 - Darken < 0:
            num12 = Darken
        if num13 - Darken < 0:
            num13 = Darken
        if num14 - Darken < 0:
            num14 = Darken
        if num15 - Darken < 0:
            num15 = Darken
        colorslist = [
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
    
    
    def play_music(file_path, loops=0, start=0, fade_ms=0, channel=0, volume=1):
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
            play_music("background_music.mp3", loops=3, start=5000, fade_ms=2000, volume=0.5)
        """
        pygame.mixer.init()
        pygame.mixer.Channel(channel).set_volume(volume)
        pygame.mixer.Channel(channel).play(
            pygame.mixer.Sound(file_path), loops, start, fade_ms
        )    
    import pygame as pg
    
    import random
    
    
    class TerrainGenerator:
        def __init__(self, width, height, pos_x=0, pos_y=0):
            self.width = width
            self.height = height
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.terrain = []
            self.colliders = []
            self.camera_x = 0
            self.camera_y = 0
            self.progress = 0  # Initialize progress to 0
    
        def draw_progress_bar(self, screen, progress):
            bar_width = progress / 3000
            bar_height = 20
            bar_x = 20
            bar_y = self.height - 30
            # progress_width = int(bar_width * progress)
            pg.draw.rect(screen, (0, 255, 0), (bar_x, bar_y, bar_width, bar_height))
    
        def generate_terrain(self, screen):
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
            self.terrain = [[0 for _ in range(self.width[1])] for _ in range(self.height)]
            e = 0
            # Generate random ground
            ground_levels = [self.height // 2] * self.width[1]
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
            tree_count = self.width[1] // 10
            for _ in range(tree_count):
                tree_x = random.randint(0, self.width[1] - 1)
                treeypartone = random.randint(5, 10)
                tree_y = ground_levels[tree_x] - treeypartone
                # windowsdimen = pg.display.get_window_size()[1]
                tree_height = treeypartone  # random.randint(3, 6)
                for y in range(tree_y, tree_y + tree_height):
                    self.terrain[y][tree_x] = 2  # Wood
                    e += 1
    
                # Generate tree leaves
                leaf_radius = random.randint(2, 4)
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
            ore_count = self.width[1] // 100
            for _ in range(ore_count):
                ore_type = random.choice([4, 5, 6, 7])  # Coal, Iron, Gold, Diamond
                ore_x = random.randint(0, self.width[1] - 1)
                validnu = False
                while not validnu:
                    try:
                        ore_y = random.randint(ground_levels[ore_x] + 1, self.height - 1)
                        e += 1
                    except ValueError:
                        validnu = False
                    else:
                        validnu = True
                ore_radius = random.randint(1, 4)
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
    
            cloud_count = random.randint(1, 10)  # Adjust the cloud count as needed
            for _ in range(cloud_count):
                cloud_width = random.randint(12, 25)  # Adjust cloud size as needed
                cloud_height = random.randint(5, 10)  # Adjust cloud size as needed
                cloud_x = random.randint(0, self.width[1] - cloud_width)
                cloud_y_beforeOperation = tree_height - 20  # Adjust cloud height as needed
                # if cloud_y_beforeOperation <= 0:
                #    print("hi")
                # else:
                #    print('yay')
                # try:
    
                cloud_y = random.randint(
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
            #            collider = c.Collider(x, y, 32, 32)
            #            self.colliders.append(collider)
            return e
    
        def run(self, screen):
            clock = pg.time.Clock()
    
            self.generate_terrain()
    
            vx = 0
            vy = 0
    
            # running = True
            # while running:
            #    for event in pg.event.get():
            #        if event.type == pg.QUIT:
            #            running = False
            #        elif event.type == pg.KEYDOWN:
            #            if event.key == pg.K_UP or event.key == ord('w'):
            #                vy = -1
            #            elif event.key == pg.K_DOWN or event.key == ord('s'):
            #                vy = 1
            #            elif event.key == pg.K_LEFT or event.key == ord('a'):
            #                vx = -1
            #            elif event.key == pg.K_RIGHT or event.key == ord('d'):
            #                vx = 1
            #    self.camera_x += vx
            #    self.camera_y += vy
            #    vx,vy=.5,0
            # if vx >= 0:
            #    vx = 0
            # if vy >= 0:
            #    vy = 0
            # if vx <= 0:
            #    vx = 0
            # if vy <= 0:
            #    vy = 0
    
            screen.fill((0, 0, 0))
            pg.display.flip()
            clock.tick(60)
    
    
    def start():
        pg.init()
        infoObject: object = pg.display.Info()
        screen: pg.Surface = pg.display.set_mode(
            (infoObject.current_w, infoObject.current_h)
        )
        # pg.display.toggle_fullscreen()
        pg.display.set_caption("Square Pixel")
        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_CROSSHAIR)
        terrain_generator = TerrainGenerator((0, 10000), infoObject.current_h // 10)
        # terrain_generator.run(screen)
        e = terrain_generator.generate_terrain(screen)
        print(e)
    
    
    if __name__ == "__main__":
        start()    
        import pygame
    
    import sys
    
    import tkinter as tk
    from tkinter import filedialog
    
    import os
    
    # Get the current working directory
    path = os.getcwd()
    
    # Initialize Pygame
    pygame.init()
    
    # Initialize the screen with transparency
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = 800, 600  # infoObject.current_w, infoObject.current_h
    WHITE = (255, 255, 255)
    TRANSPARENT = (0, 0, 0, 0)
    CHARACTER_COLOR = (50, 150, 200)
    
    # Character properties
    head_size = 50
    body_height = 100
    
    # Shapes
    shapes = []
    trails = True
    
    # Create a tkinter root window for file dialogs
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window
    
    # Pygame screen
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
    pygame.display.set_caption("Character Customization")
    pygame_icon = pygame.image.load(
        r"Recources\program recources\Screenshot 2023-09-21 181742.png"
    )
    pygame.display.set_icon(pygame_icon)
    background = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    font = pygame.font.Font(None, 36)
    
    # List of character paths
    character_list = [
        r"Recources\characters\thumbnails\blue.gif",
        r"Recources\characters\thumbnails\red.gif",
        # Add more character paths here
    ]
    
    # Load pre-made character thumbnails
    character_thumbnails = []
    for character_path in character_list:
        character_thumbnail = pygame.image.load(character_path)
        character_thumbnail = pygame.transform.scale(character_thumbnail, (100, 100))
        character_thumbnails.append(character_thumbnail)
    
    # Sidebar position and size
    sidebar_width = 150
    sidebar_rect = pygame.Rect(
        infoObject.current_w - (sidebar_width + 20), 0, sidebar_width, infoObject.current_h
    )
    
    # Button position and size
    button_height = 100
    button_spacing = 10
    button_rects = [
        pygame.Rect(
            infoObject.current_w - sidebar_width - 7,
            10 + (button_height + button_spacing) * idx,
            sidebar_width - 20,
            button_height,
        )
        for idx in range(len(character_thumbnails))
    ]
    
    
    def draw_sidebar(buttoncount):
        """
        Draw the sidebar with character thumbnails as buttons.
    
        Args:
            buttoncount (int): Index of the currently selected character thumbnail.
    
        Returns:
            None
        """
        color = [(100, 100, 100), (150, 150, 150)]
        # Fill the sidebar background
        pygame.draw.rect(background, (50, 50, 50), sidebar_rect)
    
        # Draw character thumbnails as buttons
        for idx, thumbnail in enumerate(character_thumbnails):
            count = 0
            button_rect = button_rects[idx]
            for button in buttoncount:
                if button == idx:
                    count = 1
            pygame.draw.rect(background, (color[count]), button_rect)
            background.blit(thumbnail, (button_rect.x + 10, button_rect.y + 10))
    
    
    def draw_character():
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
    
    
    def draw_shapes():
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
            text_surface = font.render(
                button["text"], True, (255, 255, 255)
            )  # Button text color
            text_rect = text_surface.get_rect(center=button["rect"].center)
            background.blit(text_surface, text_rect)
    
    
    def add_shape(x, y, width, height, color):
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
        shape = {
            "rect": pygame.Rect(x, y, width, height),
            "color": color,
            "dragging": False,
        }
        shapes.append(shape)
    
    
    def main():
        """
        Main game loop for character customization.
    
        Returns:
            None
        """
        global head_size, body_height, trails
        running = True
        buttoncount = 0
        hoveredbuttons = []
        drawchar = (False, 0)
        while running:
            if trails:
                screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                buttoncount = 0
                hoveredbuttons = []
                for precharacter in button_rects:
                    if precharacter.collidepoint(
                        pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]
                    ):
                        hoveredbuttons.append(buttoncount)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            drawchar = (True, buttoncount)
                    buttoncount += 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Check for button clicks
                    for button in buttons:
                        if button["rect"].collidepoint(event.pos):
                            if button["text"] == "Finish":
                                running = False
                                return button["callback"]()
                            else:
                                button["callback"]()
    
                    # Check for shape dragging
                    for shape in shapes:
                        if shape["rect"].collidepoint(event.pos):
                            shape["dragging"] = True
                            shape["offset_x"] = shape["rect"].x - event.pos[0]
                            shape["offset_y"] = shape["rect"].y - event.pos[1]
    
                elif event.type == pygame.MOUSEBUTTONUP:
                    for shape in shapes:
                        shape["dragging"] = False
    
            # Clear the screen with transparency
            background.fill(TRANSPARENT)
    
            if drawchar[0]:
                char = character_thumbnails[drawchar[1]]
                char = pygame.transform.scale(char, (550, 550))
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
                    shape["rect"].x = pygame.mouse.get_pos()[0] + shape["offset_x"]
                    shape["rect"].y = pygame.mouse.get_pos()[1] + shape["offset_y"]
    
            # Update the display
            screen.blit(background, (0, 0))
            pygame.display.update()
    
    
    # Create buttons
    buttons = [
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
    
    
    def increase_size(part):
        """
        Increase the size of the character's head or body.
    
        Args:
            part (str): Either 'head' or 'body' to specify which part to increase.
    
        Returns:
            None
        """
        global head_size, body_height
        if part == "head":
            head_size += 5
        elif part == "body":
            body_height += 10
    
    
    def decrease_size(part):
        """
        Decrease the size of the character's head or body.
    
        Args:
            part (str): Either 'head' or 'body' to specify which part to decrease.
    
        Returns:
            None
        """
        global head_size, body_height
        if part == "head":
            head_size -= 5
        elif part == "body":
            body_height -= 10
    
    
    def add_square():
        """
        Add a square shape to the character.
    
        Returns:
            None
        """
        x, y, width, height, color = 50, 400, 50, 50, (255, 0, 0)
        add_shape(x, y, width, height, color)
    
    
    def finish():
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
        # character_sprite = pygame.sprite.GroupSingle()
        # character_sprite.add(pygame.sprite.Sprite())
        # character_sprite.sprite.image = background.copy()
        # shapes.clear()
        export_character(path + r"\\Recources\\characters\\current.png")
        return path + r"\\Recources\\characters\\current.png"
    
    
    def reset_character():
        """
        Reset the character's head size, body height, and clear all shapes.
    
        Returns:
            None
        """
        global head_size, body_height, shapes
        head_size = 50
        body_height = 100
        shapes = []
        background.fill(TRANSPARENT)
    
    
    def toggle_trails():
        """
        Toggle the trails effect.
    
        Returns:
            None
        """
        global trails
        trails = not trails
    
    
    def save_character_dialog():
        """
        Open a file dialog for saving the character image.
    
        Returns:
            None
        """
        filename = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")],
            initialdir=path + r"\\Recources\\characters\\",
        )
        if filename:
            export_character(filename)
    
    
    def load_character_dialog():
        """
        Open a file dialog for loading a character image.
    
        Returns:
            None
        """
        filename = filedialog.askopenfilename(
            filetypes=[("PNG files", "*.png")],
            initialdir=path + r"\\Recources\\characters\\",
        )
        if filename:
            load_character(filename)
    
    
    def export_character(filename):
        """
        Export the character image to the specified file.
    
        Args:
            filename (str): The path where the character image will be saved.
    
        Returns:
            None
        """
        pygame.draw.rect(background, (0, 0, 0, 0), pygame.Rect(500, 50, 400, 1000))
        pygame.image.save(background, filename)
    
    
    def load_character(filename):
        """
        Load a character image 
            from the specified file and display it.
    
        Args:
            filename (str): The path of the character image to load.
    
        Returns:
            None
        """
        loaded_image = pygame.image.load(filename)
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
    # WIDTH, HEIGHT = 800, 600
    # TILE_SIZE = 32
    # GRID_WIDTH, GRID_HEIGHT = WIDTH // TILE_SIZE, HEIGHT // TILE_SIZE
    # WHITE = (255, 255, 255)
    # BLACK = (0, 0, 0)
    #
    ## Create the screen
    # screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # pygame.display.set_caption("Tile Map Editor")
    #
    ## Create a 2D array to represent the grid
    # grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    #
    ## Define a function to draw the grid
    # def draw_grid():
    #    for row in range(GRID_HEIGHT):
    #        for col in range(GRID_WIDTH):
    #            if grid[row][col] == 1:
    #                pygame.draw.rect(screen, BLACK, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
    #
    ## Game loop
    # running = True
    # drawing = False  # Indicates whether the user is drawing tiles
    # erasing = False  # Indicates whether the user is erasing tiles
    #
    # while running:
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            running = False
    #        elif event.type == pygame.MOUSEBUTTONDOWN:
    #            if event.button == 1:  # Left mouse button
    #                drawing = True
    #            elif event.button == 3:  # Right mouse button
    #                erasing = True
    #        elif event.type == pygame.MOUSEBUTTONUP:
    #            drawing = False
    #            erasing = False
    #        elif event.type == pygame.KEYDOWN:
    #            if event.key == pygame.K_s:  # Save the grid to a file when 's' key is pressed
    #                with open("grid.txt", "w") as file:
    #                    for row in grid:
    #                        file.write(" ".join(map(str, row)) + "\n")
    #
    #    # Get the mouse position
    #    mouse_x, mouse_y = pygame.mouse.get_pos()
    #
    #    # Convert mouse position to grid coordinates
    #    col = mouse_x // TILE_SIZE
    #    row = mouse_y // TILE_SIZE
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
        import pygame as pig
    from playfab import PlayFabSettings, PlayFabErrors, PlayFabHTTP
    
    import json
    
    import requests
    from SquarePixels.uimanagement.MainMen import SignInScreen, em, p
    
    
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
        print(httpResponse)
    
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
    
    
    def GetPlayerStatistics(request, callback, customData=None, extraHeaders=None):
        """
        Retrieves the indicated statistics (current version and values for all statistics, if none are specified), for the local
        player.
        https://docs.microsoft.com/rest/api/playfab/client/player-data-management/getplayerstatistics
        """
        if not PlayFabSettings._internalSettings.ClientSessionTicket:
            raise PlayFabErrors.PlayFabException("Must be logged in to call this method")
    
        def wrappedCallback(playFabResult, error):
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
    
    
    def UpdatePlayerStatistics(request, callback, customData=None, extraHeaders=None):
        """
        Updates the values of the specified title-specific statistics for the user. By default, clients are not permitted to
        update statistics. Developers may override this setting in the Game Manager > Settings > API Features.
        https://docs.microsoft.com/rest/api/playfab/client/player-data-management/updateplayerstatistics
        """
        if not PlayFabSettings._internalSettings.ClientSessionTicket:
            raise PlayFabErrors.PlayFabException("Must be logged in to call this method")
    
        def wrappedCallback(playFabResult, error):
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
    
    
    def do_leaderboard_updates(xp, width, height, death_text, screen):
        # Function to display a message on the screen
        SignInScreen.sign_in_with_email(None, em, p)
    
        def display_message(message, color=(255, 0, 0)):
            global current_message
            current_message = message
            text_surface = death_text.render(message, True, color)
            text_rect = text_surface.get_rect(center=(width // 2, height // 3))
            screen.blit(text_surface, text_rect)
    
        def callback(success, failure):
            if success:
                print("success")  # leaderboard_data = success.data.Leaderboard
            # good = True
            # display_message("Account created and signed in.", (0, 255, 0))
            else:
                print("failed to fetch leaderboard position")
                display_message("failed to fetch leaderboard position")
                if failure:
                    display_message("Here's some debug information:")
                    display_message(str(failure) + "leader board position")
                    print("Here's some debug information:")
                    print(str(failure) + "leader board")
    
        request = {"StatisticNames": "XP"}
        cxp = GetPlayerStatistics(
            request, callback
        )  # example output {"Statistics": [{"StatisticName": "XP", "Value": 900, "Version": 0}]}
        if cxp:
            version = cxp["Statistics"][0]["Version"]
            cxp = cxp["Statistics"][0]["Value"]
            print(cxp)
            if cxp:
                if cxp < xp:
                    print("hello")
                    request = {
                        "Statistics": [
                            {"StatisticName": "XP", "Value": xp, "Version": version}
                        ]
                    }
                    UpdatePlayerStatistics(request, callback)
            else:
                request = {"StatisticName": "XP", "Value": xp}
                UpdatePlayerStatistics(request, callback)
        else:
            request = {"StatisticName": "XP", "Value": xp}
            UpdatePlayerStatistics(request, callback)
    
    
    def draw_death_screen(screen, width, height, xp):
        clock: object = pig.time.Clock()
        death_text = pig.font.Font("Recources\Fonts\PixelifySans-Regular.ttf", 50)
        d_text = death_text.render("You Died", True, (255, 255, 255))
        xp_text = death_text.render(f"Your Score: {xp}", True, (255, 255, 255))
        death_text_rect = d_text.get_rect(center=(width // 2, height // 3))
        xp_text_rect = xp_text.get_rect(center=(width // 2, height // 3 + 50))
        # Define buttons
        respawn_button = pig.Rect(width // 4, height // 2, 200, 50)
        menu_button = pig.Rect(3 * width // 4, height // 2, 200, 50)
        try:
            do_leaderboard_updates(xp, width, height, death_text, screen)
        except Exception as e:
            print(e)
        while True:
            for event in pig.event.get():
                if event.type == pig.QUIT:
                    pig.quit()
                    quit()
            screen.fill((0, 0, 0))
            screen.blit(d_text, death_text_rect)
            screen.blit(xp_text, xp_text_rect)
            # Check if the mouse is hovering over the buttons
            if respawn_button.collidepoint(pig.mouse.get_pos()):
                pig.draw.rect(screen, (150, 150, 150), respawn_button)
                respawn_text = death_text.render("Respawn", True, (0, 0, 0))
                respawn_text_rect = respawn_text.get_rect(center=respawn_button.center)
                screen.blit(respawn_text, respawn_text_rect)
                if pig.mouse.get_pressed()[0]:
                    return True
            else:
                pig.draw.rect(screen, (255, 255, 255), respawn_button)
                respawn_text = death_text.render("Respawn", True, (0, 0, 0))
                respawn_text_rect = respawn_text.get_rect(center=respawn_button.center)
                screen.blit(respawn_text, respawn_text_rect)
    
            if menu_button.collidepoint(pig.mouse.get_pos()):
                pig.draw.rect(screen, (150, 150, 150), menu_button)
                menu_text = death_text.render("Main Menu", True, (0, 0, 0))
                menu_text_rect = menu_text.get_rect(center=menu_button.center)
                screen.blit(menu_text, menu_text_rect)
                if pig.mouse.get_pressed()[0]:
                    return False
            else:
                pig.draw.rect(screen, (255, 255, 255), menu_button)
                menu_text = death_text.render("Main Menu", True, (0, 0, 0))
                menu_text_rect = menu_text.get_rect(center=menu_button.center)
                screen.blit(menu_text, menu_text_rect)
            pig.display.flip()
            clock.tick(60)    
            import random
    
    import pygame as pig
    
    pig.init()
    
    infoObject = pig.display.Info()
    screen = pig.display.set_mode((infoObject.current_w, infoObject.current_h))
    
    # Create item surfaces
    items = [pig.Surface((50, 50), pig.SRCALPHA) for x in range(4)]
    wood = pig.image.load(r"Recources\Textures\wood.png")
    stone = pig.image.load(r"Recources\Textures\stone.jpg")
    scale = (25, 25)
    wood = pig.transform.scale(wood, scale)
    stone = pig.transform.scale(stone, scale)
    items[0].blit(wood, (15, 15, 100, 100))
    items[1].blit(stone, (15, 15, 100, 100))
    # Create a green sword item
    pig.draw.circle(items[2], (0, 255, 0), (25, 25), 25)
    # Create a blue circle item
    pig.draw.circle(items[3], (0, 0, 255), (25, 25), 25)
    
    font = pig.font.Font(pig.font.match_font("calibri"), 26)
    
    
    class Item:
        """
        Represents an item with an associated image and ID.
    
        Args:
            id (int): The ID of the item.
    
        Attributes:
            id (int): The ID of the item.
            surface (pygame.Surface): The image representing the item.
        """
    
        def __init__(self, id):
            self.id = id
            self.surface = items[id]
    
        def resize(self, size):
            """
            Resize the item's image.
    
            Args:
                size (int): The size to resize the image to.
    
            Returns:
                pygame.Surface: The resized image.
            """
            return pig.transform.scale(self.surface, (size, size))
    
    
    class Inventory:
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
    
        def __init__(
            self, rows=9, col=27, box_size=infoObject.current_w // 30, x=50, y=50, border=3
        ):
            self.rows = rows
            self.col = col
            self.items = [[None for _ in range(self.rows)] for _ in range(self.col)]
            self.box_size = box_size
            self.x = x
            self.y = y
            self.border = border
    
        def draw(self, ychange):
            """
            Draw the inventory grid on the screen.
    
            Args:
                ychange (list): A list containing a boolean value indicating if the y-position should change,
                               and the new y-position.
            """
            temp = self.y
            if ychange[0]:
                self.y = ychange[1]
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
                    rect = (
                        self.x + (self.box_size + self.border) * x + self.border,
                        self.y + (self.box_size + self.border) * y + self.border,
                        self.box_size,
                        self.box_size,
                    )
                    pig.draw.rect(screen, (180, 180, 180), rect)
                    if self.items[x][y]:
                        screen.blit(self.items[x][y][0].resize(self.box_size), rect)
                        obj = font.render(str(self.items[x][y][1]), True, (0, 0, 0))
                        screen.blit(
                            obj,
                            (rect[0] + self.box_size // 2, rect[1] + self.box_size // 2),
                        )
            # self.y = temp
    
        def Get_pos(self):
            """
            Get the position in the inventory grid where the mouse cursor is located.
    
            Returns:
                tuple: A tuple containing the x and y coordinates of the grid position.
            """
            mouse = pig.mouse.get_pos()
            x = mouse[0] - self.x
            y = mouse[1] - self.y
            x = x // (self.box_size + self.border)
            y = y // (self.box_size + self.border)
            return (int(x), int(y))
    
        def Add(self, Item, xy):
            """
            Add an item to the inventory grid at the specified position.
    
            Args:
                Item (Item): The item to add.
                xy (tuple): A tuple containing the x and y coordinates of the position.
            """
            x, y = xy
            if self.items[x][y]:
                if self.items[x][y][0].id == Item[0].id:
                    self.items[x][y][1] += Item[1]
                else:
                    temp = self.items[x][y]
                    self.items[x][y] = Item
                    return temp
            else:
                self.items[x][y] = Item
    
        def In_grid(self, x, y):
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
    
        def get_item(self, itemId):
            """
            Get an item with the specified item ID and add it to the inventory.
    
            Args:
                itemId (int): The ID of the item to retrieve.
            """
            lookingforspot = True
            if itemId is not None:
                item = Item(itemId)
                x = 0
                y = 0
                while lookingforspot:
                    if self.items[x][y]:
                        if self.items[x][y][0].id == itemId:
                            lookingforspot = False
                        else:
                            self.items[x][y] = item
                            lookingforspot = False
                    else:
                        self.items[x][y] = item
                        lookingforspot = False
    
        def place_item_in_crafting_grid(self, item, x, y):
            """
            Place an item in the crafting grid at the specified position.
    
            Args:
                item (Item): The item to place in the grid.
                x (int): The x-coordinate of the grid position.
                y (int): The y-coordinate of the grid position.
            """
            crafting_grid[y][x] = item
    
        def get_item_from_crafting_grid(self, x, y):
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
    
        def count_item(self, item_id, inventory):
            """
            Count the number of items with the specified item ID in the inventory.
    
            Args:
                item_id (int): The ID of the item to count.
                inventory (Inventory): The inventory to search.
    
            Returns:
                int: The count of items with the specified ID.
            """
            count = 0
            for x in range(inventory.col):
                for y in range(inventory.rows):
                    if inventory.items[x][y] and inventory.items[x][y][0].id == item_id:
                        count += inventory.items[x][y][1]
            return count
    
        def remove_item(self, item_id, count, inventory):
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
                    if inventory.items[x][y] and inventory.items[x][y][0].id == item_id:
                        if inventory.items[x][y][1] >= count:
                            inventory.items[x][y][1] -= count
                            if inventory.items[x][y][1] == 0:
                                inventory.items[x][y] = None
    
    
    player_inventory = Inventory()
    item_bar = Inventory(1, 5, x=infoObject.current_w // 2.5, y=infoObject.current_h / 1.2)
    selected = None
    
    # Crafting Grid
    crafting_grid = Inventory(
        rows=3, col=3, box_size=50, x=50, y=infoObject.current_h / 1.2, border=3
    )
    
    
    crafting_recipes = [
        {
            "pattern": [[(0, 1), None, (0, 1)], [None, (1, 1), None], [None, (1, 1), None]],
            "output": (2, 1),  # Green sword
        },
        # Add more recipes as needed
    ]
    
    
    if __name__ == "__main__":
        running = True
        while running:
            for event in pig.event.get():
                if event.type == pig.QUIT:
                    running = False
                if event.type == pig.MOUSEBUTTONDOWN:
                    if event.button == 3:
                        # Right-click to get a random item
                        selected = [Item(random.randint(0, 3)), 1]
                    elif event.button == 1:
                        try:
                            pos = pig.mouse.get_pos()
                            gridpos = player_inventory.Get_pos()
                            if player_inventory.In_grid(pos[0], pos[1]):
                                if selected:
                                    selected = player_inventory.Add(selected, gridpos)
                                elif player_inventory.items[gridpos[0]][gridpos[1]]:
                                    selected = player_inventory.items[gridpos[0]][
                                        gridpos[1]
                                    ]
                                    player_inventory.items[gridpos[0]][gridpos[1]] = None
                            gridpos = crafting_grid.Get_pos()
                            if crafting_grid.In_grid(pos[0], pos[1]):
                                if selected:
                                    selected = crafting_grid.Add(selected, gridpos)
                                elif crafting_grid.items[gridpos[0]][gridpos[1]]:
                                    selected = crafting_grid.items[gridpos[0]][gridpos[1]]
                                    crafting_grid.items[gridpos[0]][gridpos[1]] = None
                            gridpos = item_bar.Get_pos()
                            if item_bar.In_grid(pos[0], pos[1]):
                                if selected:
                                    selected = item_bar.Add(selected, gridpos)
                                elif item_bar.items[gridpos[0]][gridpos[1]]:
                                    selected = item_bar.items[gridpos[0]][gridpos[1]]
                                    item_bar.items[gridpos[0]][gridpos[1]] = None
                        except:
                            None  # Handle errors gracefully
    
            screen.fill((255, 255, 255, 100))
            player_inventory.draw([False, 0])
            crafting_grid.draw([False, 0])
            item_bar.draw([False, 0])
    
            if selected:
                mousex, mousey = pig.mouse.get_pos()
                screen.blit(selected[0].resize(30), (mousex, mousey))
                obj = font.render(str(selected[1]), True, (0, 0, 0))
                screen.blit(obj, (mousex + 15, mousey + 15))
    
            pig.display.update()    
            import pygame as pig
    
    import os
    from moviepy.editor import VideoFileClip
    
    import moviepy.editor
    
    import glob
    
    import numpy as np
    
    
    def extract_frames(video_file: str, image_folder: str) -> None:
        if not os.path.isfile(image_folder + "/frame%04d.png"):
            clip = VideoFileClip(video_file)
            # clip = clip.reader.read_frame()
            # clip = np.array(clip)
            # assert clip.ndim == 3
            # print(clip.shape)
            # for xx in range(clip.shape[0]):
            #    for yy in range(clip.shape[1]):
            #        for zz in range(clip.shape[2]):
            #
            # clip = moviepy.editor.ImageClip(clip)
            clip.write_images_sequence(image_folder + "/frame%04d.png")
            clip.audio.write_audiofile(image_folder + "/audio.wav")
    
    
    def play_intro_video(image_folder, not_skipped, screen, intro):
        clock: object = pig.time.Clock()
    
        # Load the images from the specified folder
        if intro == 1:
            image_files: str = sorted(glob.glob(image_folder + "/*.jpg"))
        else:
            image_files: str = sorted(glob.glob(image_folder + "/frame*.png"))
        # Load the audio file
        audio_file: str = image_folder + "/audio.wav"
        pig.mixer.music.load(audio_file)
    
        # Start playing the audio
        pig.mixer.music.play()
    
        # Load each image and display it on the screen
        credits_font = pig.font.Font(
            "Recources\Fonts\PixelifySans-Regular.ttf", 50
        )
        for image_file in image_files:
            if not_skipped == True:
                image = pig.image.load(image_file).convert()
                infoObject: object = pig.display.Info()
                image = pig.transform.scale(
                    image, (infoObject.current_w, infoObject.current_h)
                )
                screen.blit(image, (0, 0))
                text_surface = credits_font.render(
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
                    if event.type == pig.VIDEORESIZE:
                        screen = pig.display.set_mode((event.w, event.h), pig.RESIZABLE)
                    if event.type == pig.QUIT:
                        pig.quit()
                        quit()
                    if event.type == pig.KEYDOWN:
                        not_skipped = False
    
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
    signed_in = IsClientLoggedIn()
    em = ""
    p = ""
    current_message = ""
    # Constants
    infoObject: object = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    BACKGROUND_COLOR = (0, 0, 0)
    FPS = 60
    good = False
    backround = pygame.transform.scale(
        pygame.image.load(r"Recources\ui\mainmen\backround\cover.png"),
        (infoObject.current_w + 20, infoObject.current_h + 20),
    )
    # Initialize the screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Square Pixel")
    pygame_icon = pygame.image.load(
        r"Recources\program recources\Screenshot 2023-09-21 181742.png"
    )
    pygame.display.set_icon(pygame_icon)
    
    playfabsettings = PlayFabSettings
    playfabsettings.TitleId = "4AAA9"
    # Define fonts
    font = pygame.font.Font(None, 36)
    
    # Define colors
    WHITE = (255, 255, 255)
    BUTTON_COLOR = (50, 50, 50)
    BUTTON_HOVER_COLOR = (100, 100, 100)
    
    white = (255, 255, 255)
    
    
    # Load cloud images
    cloud_images = [
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
    clouds = []
    # Game state
    play_music(r"Recources\sounds\music\Menu.mp3")
    game_state = "menu"  # Initial state is the main menu
    show_play_buttons = False  # Flag to control visibility of play buttons
    show_multiplayer_options = False  # Flag to control visibility of multiplayer options
    
    # Create a screen for the sign-up process
    class SignUpScreen:
        def __init__(self):
            self.buttons = []
            self.username_input = InputField(
                WIDTH // 2 - 100, HEIGHT // 2 - 100, 400, 40, "Username"
            )
            self.email_input = InputField(
                WIDTH // 2 - 100, HEIGHT // 2 - 50, 400, 40, "Email"
            )
            self.password_input = InputField(
                WIDTH // 2 - 100, HEIGHT // 2, 400, 40, "Password"
            )
            self.profile_picture_button = Button(
                "Upload Profile Picture",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 50,
                200,
                50,
                self.upload_profile_picture,
            )
            self.create_account_button = Button(
                "Create Account",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 100,
                200,
                50,
                self.create_account,
            )
            self.google_login_button = Button(
                "Google Login",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 150,
                200,
                50,
                self.google_login,
            )
            self.back_button = Button(
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
            self.profile_picture = None
    
        def render(self):
            for button in self.buttons:
                button.draw(screen)
            if self.profile_picture:
                self.profile_picture.draw(screen)
    
        def back(self):
            global current_page, main_page
            current_page = main_page
    
        def google_login(self):
            request = {"CreateAccount": True}
            request["TitleId"] = playfabsettings.TitleId
            request[
                "ServerAuthCode"
            ] = "95487563442-ta5a931frpcrsm78js4q5eb2sjvi927m.apps.googleusercontent.com"
    
            def callback(success, failure):
                if success:
                    display_message("Account created and signed in.", (0, 255, 0))
                else:
                    display_message("Account creation failed.")
                    if failure:
                        display_message("Here's some debug information:")
                        display_message(str(failure))
    
            result = LoginWithGoogleAccount(request, callback)
    
        # Function to create an account with an email address
        def create_account(self):
            global signed_in
            email = self.email_input.text
            password = self.password_input.text
            username = self.username_input.text
    
            def callback(success, failure):
                if success:
                    display_message("Account created and signed in.", (0, 255, 0))
                else:
                    display_message("Account creation failed.")
                    if failure:
                        display_message("Here's some debug information:")
                        display_message(str(failure))
    
            try:
                conn = http.client.HTTPSConnection("api.eva.pingutil.com")
                payload = ''
                headers = {}
                conn.request("GET", f"/email?email={email}", payload, headers)
                res = conn.getresponse()
                data = res.read()
                #https://www.loginradius.com/blog/engineering/email-verification-api/
                email_data = data.decode("utf-8")
                if email_data["status"] == "success":
                    email_data = email_data["data"]
                    if email_data["disposible"] == False:
                        if email_data["valid_syntax"] == True:
                            if email_data["deliverable"] == True:
                                request = {"CreateAccount": True}
                                request["TitleId"] = playfabsettings.TitleId
                                request["Email"] = email
                                request["Password"] = password
                                request["Username"] = username
    
                                # Upload the profile picture if it has been selected
                                if self.profile_picture:
                                    request["ProfilePicture"] = self.profile_picture
    
                                result = RegisterPlayFabUser(request, callback)
    
                                if result is not None and "SessionTicket" in result:
                                    signed_in = True
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
        def upload_profile_picture(self) -> None:
            """Uploads a selected profile picture
            Args:
                self: The class instance
            Returns: 
                None: No value is returned
            - Opens a file dialog window to select a profile picture file
            - Gets the file path of the selected picture
            - Checks if a file was selected before closing the dialog
            """
            # Open a file dialog to select a profile picture
            root = tk.Tk()
            root.withdraw()  # Hide the main window
            file_path = filedialog.askopenfilename(title="Select a Profile Picture")
            root.destroy()  # Close the hidden root window
    
            if file_path:
                self.profile_picture = Image.open(file_path, "r")
                self.profile_picture = self.profile_picture.resize([HEIGHT // 2 + 50, HEIGHT // 2 + 50])
                self.profile_picture = ImageElement((WIDTH - 25)-self.profile_picture.width, 25,self.profile_picture,"Circle")
    
    
    # Create a screen for the sign-in process
    class SignInScreen:
        def __init__(self):
            self.buttons = []
            self.email_input = InputField(
                WIDTH // 2 - 100, HEIGHT // 2 - 50, 400, 40, "Email"
            )
            self.password_input = InputField(
                WIDTH // 2 - 100, HEIGHT // 2, 400, 40, "Password"
            )
            self.sign_in_button = Button(
                "Sign In",
                WIDTH // 2 - 100,
                HEIGHT // 2 + 50,
                200,
                50,
                self.sign_in_with_email,
            )
            self.back_button = Button(
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
            self.remember_me = True
    
        def render(self):
            for button in self.buttons:
                button.draw(screen)
    
        # Function to sign in with an email address
    
        def sign_in_with_email(self, email=None, password=None):
            global signed_in, good, em, p  # , user
            if email == None and password == None:
                email = self.email_input.text
                password = self.password_input.text
            # print(email + "\n" + password)
    
            def callback(success, failure):
                global good
                if success:
                    good = True
                    display_message("Account created and signed in.", (0, 255, 0))
                else:
                    display_message("Account creation failed.")
                    if failure:
                        display_message("Here's some debug information:")
                        display_message(str(failure))
    
            try:
                request = {}
                request["TitleId"] = playfabsettings.TitleId
                request["Email"] = email
                request["Password"] = password
                result = LoginWithEmailAddress(request, callback)
                print(good)
                if good:
                    signed_in = True
                    em = request["Email"]
                    p = request["Password"]
                    # TODO #24 make keep logged in more secure
                    if self.remember_me:  # TODO #26 #25 add remember me checkbox
                        # with open("h.h", "x") as x:
                        # Create peekaboo.py and add var1 and var2
                        with open("SquarePixels/eastereggs/peekaboo.py", "w") as peekaboo_file:
                            peekaboo_file.write(f"var1 = {em}\n")
                            peekaboo_file.write(f"var2 = {p}\n")
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
                    #    cfg_file.write("t = True\n")
                    #
                    ## playfab.PlayFabClientAPI.GetPlayerProfile
                    # user = {""}
                    display_message("Signed in.", (0, 255, 0))
                    return
                else:
                    print("signed in failed")
                    display_message("Sign-in failed.")
            except Exception as e:
                display_message(f"Sign-in failed: {e}")
    
        # Function to toggle the "Remember Me" checkbox
        def toggle_remember_me(self):
            self.remember_me = not self.remember_me
    
        # Function to send a verification code to the provided email
        def send_verification_code(self):
            email = self.email_input.text
    
        def back(self):
            global current_page, main_page
            current_page = main_page
    
        # Add code to send a verification code to the email
        # You would typically use an email service or other means to send the code
    
    
    # Main Menu
    def main_menu(
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
        multiplayer_button = Button(
            "Multiplayer",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 50,
            200,
            50,
            toggle_multiplayer_options,
        )
        singleplayer_button = Button(
            "Singleplayer",
            WIDTH // 2 - 100,
            HEIGHT // 2 + 100,
            200,
            50,
            start_singleplayer_game,
        )
        UImaker = Button(
            "Make UI (for testing purposes only) <unless future mod system...>",
            684,
            800,
            822,
            50,
            start,
        )
        UImaker.size = 20
        back_button = Button("Back", WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50, back)
        play_button = Button(
            "Play", WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, toggle_play_buttons
        )
        settings_button = Button(
            "Settings", WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, open_settings
        )
        credits_button = Button(
            "Credits", WIDTH // 2 - 100, HEIGHT // 4 + 50, 200, 50, egg.start
        )
        quit_button = Button(
            "Quit", WIDTH // 2 - 100, HEIGHT // 2 + 150, 200, 50, quit_game
        )
    
        while running:
            global clouds
            if len(clouds) <= 6:
                if random.randint(0, 100) < 2:
                    cloud_image = random.choice(cloud_images)
                    cloud_x = random.randint(0, infoObject.current_w)
                    cloud_y = random.randint(0, 200)
                    cloud_speed = random.uniform(0.1, 20)  # Random speed between 1 and 4
                    new_cloud = Cloud(cloud_x, cloud_y, cloud_image, cloud_speed)
                    clouds.append(new_cloud)
    
            # Remove clouds that are off-screen
            for cloud in clouds:
                if cloud.image == cloud_images[1]:
                    if cloud.x <= -300:
                        clouds.remove(cloud)
                else:
                    if cloud.x <= -500:
                        clouds.remove(cloud)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
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
    def start_game():
        """
        Start the multiplayer game.
        """
        global game_state, show_play_buttons
        game_state = "multiplayer"
        show_play_buttons = False
    
    
    # Singleplayer Game
    def start_singleplayer_game():
        """
        Start the singleplayer game.
        """
        global running
        pygame.mixer.music.fadeout(2)
        running = False
    
    
    # Host Multiplayer Game
    def host_multiplayer_game():
        """
        Host a multiplayer game.
        """
        
        import SquarePixels.uimanagement.server_ui as server_ui
    
        server_ui.load_servers()
        server_ui.load_mplayers()
        server_ui.game_loop()
    
    
    # Join Multiplayer Game
    def join_multiplayer_game():
        """
        Join a multiplayer game.
        """
        
        import SquarePixels.uimanagement.client_ui as client_ui
    
        client_ui.find_servers()
        client_ui.main()
    
    
    # Toggle the visibility of play buttons
    def toggle_play_buttons():
        """
        Toggle the visibility of play buttons.
        """
        global show_play_buttons
        show_play_buttons = not show_play_buttons
    
    
    # Toggle the visibility of multiplayer options
    def toggle_multiplayer_options():
        """
        Toggle the visibility of multiplayer options.
        """
        global show_multiplayer_options
        show_multiplayer_options = not show_multiplayer_options
    
    
    # Open the settings menu
    def open_settings():
        """
        Open the settings menu.
        """
        global game_state
        game_state = "settings"
    
    
    # Function to display a message on the screen
    def display_message(message, color=(255, 0, 0)):
        global current_message
        current_message = message
        text_surface = font.render(message, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(text_surface, text_rect)
    
    
    # Create a "Not a Robot" button
    # not_a_robot_button = Button("Not a Robot", 100, 350, 200, 50)
    
    
    # Create pages for different states
    class Page:
        def __init__(self):
            """Initializes registration form fields and buttons
            Args: 
                self: {The class instance}: Initializes registration form fields and buttons
            Returns:
                None: Does not return anything, initializes form fields and buttons
            {Processing Logic}:
                - Initializes InputField objects for username, email, password
                - Initializes Button objects for profile picture upload, account creation, Google login, back 
                - Adds all InputField and Button objects to a buttons list
                - Sets initial profile picture to None"""
            self.buttons = []
    
        def add_button(self, button):
            self.buttons.append(button)
    
        def render(self):
            for button in self.buttons:
                button.draw(screen)
    
    
    # Create a page for email input and verification
    main_page = Page()
    
    # Initialize the current page to the email verification page
    current_page = main_page
    
    
    # Define a function to switch the current page to the sign-up screen
    def switch_to_sign_up():
        global current_page
        screen.fill(WHITE)
        current_page = SignUpScreen()
    
    
    # Define a function to switch the current page to the sign-in screen
    def switch_to_sign_in():
        global current_page
        screen.fill(WHITE)
        current_page = SignInScreen()
    
    
    def guest():
        global signed_in
        signed_in = "Guest"
    
    
    # Add a function to show the sign-in or guest popup
    def show_signin_popup(leaderboard_page):
        global WIDTH, HEIGHT, screen, BACKGROUND_COLOR, signed_in, current_message
        ########################DEVELOPMENTAL TESTING ONLY##############################
        signin_as_test_user = Button(
            "signin_as_test_user",
            WIDTH // 2 - 100,
            HEIGHT // 2 - 325,
            200,
            50,
            SignInScreen.sign_in_with_email,
            [None, "testuser@gmail.com", "test123"],
        )
        ########################DEVELOPMENTAL TESTING ONLY##############################
        create_account = Button(
            "Create Acount", WIDTH // 2 - 100, HEIGHT // 2 - 225, 200, 50, switch_to_sign_up
        )
        popup_font = pygame.font.Font(None, 24)
        popup_text = "Please sign in to play the game and save your progress."
        popup_text2 = "If you choose to play as a guest, your progress will reset daily because we won't be able to verify your ownership of the game."
        sign_in_button = Button(
            "Sign In", WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, switch_to_sign_in
        )
        guest_button = Button(
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
            popup_text_render = popup_font.render(popup_text, True, WHITE)
            popup_text2_render = popup_font.render(popup_text2, True, WHITE)
            if current_page == main_page:
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.VIDEORESIZE:
                    WIDTH, HEIGHT = event.w, event.h
                    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    
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
                leaderboard_data = get_leaderboard(leaderboard_page, display_message)
                return leaderboard_data
    
            pygame.display.update()
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)
    
    
    def back():
        """
        Go back to the previous menu.
        """
        global show_play_buttons, game_state
        show_play_buttons = not show_play_buttons
        game_state = "menu"
    
    
    # Quit the game
    def quit_game():
        """
        Quit the game.
        """
        pygame.quit()
        sys.exit()
    
    
    def mainfunc():
        """
        Main function to run the game.
        """
        global running, current_leader_page
        # Add these constants to control pagination
        ENTRIES_PER_PAGE = 10
        current_leader_page = 1
        leaderboard_data = get_leaderboard(current_leader_page, display_message)
        # Initialize multiplayer and singleplayer buttons
        host_button = Button(
            "Host", WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, host_multiplayer_game
        )
        join_button = Button(
            "Join", WIDTH // 2 - 100, HEIGHT // 2 + 100, 200, 50, join_multiplayer_game
        )
        # Add buttons for next and previous page
        next_button = Button(
            "Next Page",
            WIDTH - 120,
            HEIGHT - 40,
            100,
            30,
            next_leadeboard_page,
            [current_leader_page, leaderboard_data, display_message],
        )
        previous_button = Button(
            "Previous Page",
            WIDTH - 500,
            HEIGHT - 40,
            120,
            30,
            previous_leadeboard_page,
            [current_leader_page, leaderboard_data, display_message],
        )
        # Add the search button in the display_leaderboard function
        search_button = Button("Search", WIDTH - 320, 20, 80, 30, search_input_callback_l)
        # Add the search bar for filtering leaderboard entries
        search_input = InputField(WIDTH - 500, 20, 200, 30, "Search by Player Name")
        running = True
        fetch_leaderboard = False
        # Main game loop
        while running:
            # Generate a random cloud
            if (
                signed_in == False
            ):  # DO NOT CHANGE TO "IF NOT SIGNED_IN: because singed_in can also be a string"
                try:
                    with open("h.h", "r") as a:
                        leaderboard_data = SignInScreen.sign_in_with_email(
                            SignInScreen(), a.readline(0), a.readline(1)
                        )
                except:
                    leaderboard_data = show_signin_popup(current_leader_page)
    
            if signed_in == True:
                if not fetch_leaderboard:
                    leaderboard_data = get_leaderboard(current_leader_page, display_message)
                    # print(leaderboard_data)
                    fetch_leaderboard = True
                    #get_user_avatar(SignInScreen)
    
    
            if signed_in == "Guest":
                pass  # TODO:implement #22 guest logic in future
            # TODO #23 add function checking acount variable for having bought this game
            if game_state == "menu":
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
            elif game_state == "multiplayer":
                if show_multiplayer_options:
                    host_button.draw(screen)
                    join_button.draw(screen)
            elif game_state == "singleplayer":
                
                import SquarePixel
    
                SquarePixel.main()
            elif game_state == "settings":
                # Implement the settings menu here
                pass
    
            # Add other game states as needed
            pygame.display.update()
            pygame.time.Clock().tick(FPS)
    
    
    # Get a player's friends list
    def get_friends_list():
        request = {}
        result = playfab.PlayFabClientAPI.GetFriendsList(request)
        if result is not None:
            friends = result.data.Friends
            # Process and display friends list in your game's UI
    
    
    # Add a friend
    def add_friend(player_id):
        request = {"FriendPlayFabId": player_id}
        playfab.PlayFabClientAPI.AddFriend(request)
    
    
    # Handle friend requests, accept or decline
    def handle_friend_request(friend_playfab_id, accept):
        if accept:
            request = {"FriendPlayFabId": friend_playfab_id}
            playfab.PlayFabClientAPI.AddFriend(request)
        else:
            request = {"FriendPlayFabId": friend_playfab_id}
            playfab.PlayFabClientAPI.RemoveFriend(request)
    
    
    if __name__ == "__main__":
        mainfunc()    
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
                - Sets the x, y, width and height attributes 
            from the arguments
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
            self.text = ""    # Cloud class
    class Cloud:
        def __init__(self, x, y, image, speed):
            self.x = x
            self.y = y
            self.image = image
            self.speed = speed
            self.alpha = 0
    
        def move(self):
            self.x -= self.speed
            self.alpha += 1
            if self.alpha >= 255:
                self.alpha = 255
    
        def draw(self, screen):
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
    
    
    infoObject: object = pygame.display.Info()
    screen: pygame.Surface = pygame.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    pygame_icon = pygame.image.load(
        r"Recources\program recources\Screenshot 2023-09-21 181742.png"
    )
    pygame.display.set_icon(pygame_icon)
    # pygame.display.toggle_fullscreen()
    
    pygame.display.set_caption("Square Pixel")
    font = pygame.font.Font("Recources\Fonts\PixelifySans-Regular.ttf", 36)
    
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    
    
    # Function to display a message on the screen
    def display_message(message, color=(255, 0, 0)):
        global current_message
        current_message = message
        text_surface = font.render(message, True, color)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
        screen.blit(text_surface, text_rect)
    
    
    class Friends:
        def __init__(self):
            self.font = None  # You should initialize this appropriately
            self.current_message = ""
            self.friends = []
    
        def DoPost(
            self,
            urlPath,
            request,
            authKey,
            authVal,
            callback,
            customData=None,
            extraHeaders=None,
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
            requestHeaders[
                "X-PlayFabSDK"
            ] = PlayFabSettings._internalSettings.SdkVersionString
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
                self.callGlobalErrorHandler(error)
    
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
                    emptyResponseError.ErrorMessage = (
                        "PlayFabHTTP Recieved an empty response"
                    )
                    emptyResponseError.ErrorCode = PlayFabErrors.PlayFabErrorCode.Unknown
                    callback(None, emptyResponseError)
                except Exception as e:
                    # Global notification about exception in caller's callback
                    PlayFabSettings.GlobalExceptionLogger(e)
    
            # Your existing DoPost function with "self" references
    
        def callGlobalErrorHandler(self, error):
            if PlayFabSettings.GlobalErrorHandler:
                try:
                    # Global notification about an API Call failure
                    PlayFabSettings.GlobalErrorHandler(error)
                except Exception as e:
                    # Global notification about exception in caller's callback
                    PlayFabSettings.GlobalExceptionLogger(e)
    
        def display_message(self, message, color=(255, 0, 0)):
            self.current_message = message
            text_surface = self.font.render(message, True, color)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
            self.screen.blit(text_surface, text_rect)
    
        def GetFriendsList_http(
            self, request, callback, customData=None, extraHeaders=None
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
    
            def wrappedCallback(playFabResult, error):
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
    
        def get_friends(self):
            request = {}
    
            def callback(success, failure):
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
                result = self.GetFriendsList_http(request, callback)
            except:
                result = None
            if result is not None:
                print(result)
                return result
            else:
                return []
    
        def display_friends(self, friends):
            y = 100
            for friend in friends:
                friend_text = self.font.render(friend.username, True, (255, 255, 255))
                self.screen.blit(friend_text, (50, y))
                y += 50
    
        def add_friends(self, friend_identifier):
            if "@" in friend_identifier:
                # If the friend_identifier contains "@" symbol, it's an email
                request = {"FriendEmail": friend_identifier}
            else:
                # Otherwise, it's a username
                request = {"FriendUsername": friend_identifier}
    
            def callback(success, failure):
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
                result = AddFriend(request, callback)
            except:
                print("error")
    
    
    class FriendScreen:
        def __init__(self):
            self.activebuttons = []
            self.friend_list = [
                "Friends will appear here"
            ]  # Initialize a list to store friend names
            self.pending_friend_list = []  # List to store pending friend requests
            self.friend_list_offset = 0  # Offset for displaying friends
            self.show_pending_friends = (
                False  # To toggle between "Friends" and "Pending Friends" tabs
            )
            self.selected_tab = "Friends"  # Initialize the selected tab
            self.search_bar = InputField(50, 50, 400, 40, "Search Players")
            self.search_bar.size = 30
            self.add_friend_input = InputField(50, 220, 400, 40, "Enter Username/Email")
            self.friends_instance = Friends()
            self.add_friend_tab = Button(
                "Add Friend",
                50,
                150,
                200,
                50,
                self.show_add_friends,
            )
            self.add_friend_button = Button(
                "Send Friend Request",
                150,
                270,
                200,
                50,
                self.add_friend,
            )
            self.refresh_button = Button(
                "Refresh",
                50,
                100,
                200,
                50,
                self.refresh_friends,
            )
            self.friends_tab_button = Button(
                "Friends",
                270,
                95,
                200,
                50,
                self.show_friends,
            )
            self.pending_friends_tab_button = Button(
                "Pending Friends",
                300,
                150,
                200,
                50,
                self.show_pending_friends_list,
            )
            # self.back_button = Button(
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
    
        def render(self):
            # Background for the friend list
            # Highlight the selected tab
            backround = pygame.Surface(
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
            if self.selected_tab == "Friends":
                self.friends_tab_button.selected()
                # Display the list of friends
                self.display_friends()
    
                self.activebuttons = []
                self.activebuttons.extend(
                    [
                        self.search_bar,
                        self.refresh_button,
                        self.friends_tab_button,
                        self.add_friend_tab,
                        self.pending_friends_tab_button,
                    ]
                )
    
            elif self.selected_tab == "Pending Friends":
                # Display the list of pending friends
                self.display_pending_friends()
                self.pending_friends_tab_button.selected()
    
            elif self.selected_tab == "Add Friends":
                self.activebuttons = []
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
    
        def refresh_friends(self):
            # Call a method to refresh the friend list
            self.friend_list = self.friends_instance.get_friends()
            # Also, update the pending friend list if needed
    
        def show_friends(self):
            self.show_pending_friends = False
            self.selected_tab = "Friends"
    
        def show_pending_friends_list(self):
            # Call a method to get pending friend requests
            self.selected_tab = "Pending Friends"
            self.pending_friend_list = self.friends_instance.get_pending_friend_requests()
            self.show_pending_friends = True
    
        def get_friends(self):
            self.friends = self.friends_instance.get_friends()
    
        def show_add_friends(self):
            self.selected_tab = "Add Friends"
    
        # Function to add a friend
        def add_friend(self):
            friend_name = self.add_friend_input.text
            if friend_name:
                self.friend_list.append(friend_name)
                self.friends_instance.add_friends(friend_name)
                # Send a request to the server to add the friend
                self.add_friend_input.clear()
    
        # Function to display the list of friends
        def display_friends(self):
            # Filter friends based on the search bar input
            search_text = self.search_bar.text.lower()
            filtered_friends = [
                friend for friend in self.friend_list if search_text in friend.lower()
            ]
    
            # Display a portion of the filtered friend list (e.g., 10 friends at a time)
            y = 200
            for friend in filtered_friends[
                self.friend_list_offset : self.friend_list_offset + 10
            ]:
                friend_text = font.render(friend, True, (255, 255, 255))
                screen.blit(friend_text, (50, y))
                y += 50
    
        # Function to go back to the main menu
        def back(self):
            global current_page, main_page
            current_page = main_page
    
    
    # Usage Example:
    instance = FriendScreen()
    
    
    if __name__ == "__main__":
        # instance.friend_list = instance.get_friends()
    
        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
    
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
    
    
    class TextElement:
        def __init__(self, x, y, text, font_size):
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
            self.x = x
            self.y = y
            self.text = text
            self.font_size = font_size
            self.color = (255, 255, 255)  # Default text color
            self.size = font_size
            self.hovered = False
            self.width = 50
            self.height = 25
            self.bold = False
            self.italics = False
            self.underlined = False
            self.font_name = None
    
        def draw(self, screen):
            """
            Renders text on a screen surface.
            Args:
                screen: The screen surface to render text on
            Returns: 
                None: Does not return anything
            - Loads the font based on properties of the Text object
            - Renders the text surface using the font and text properties  
            - Blits/draws the text surface onto the screen surface at the x,y position"""
            font = pygame.font.Font(self.font_name, self.size)
            font.set_bold(self.bold)
            font.set_italic(self.italics)
            font.set_underline(self.underlined)
            text_surface = font.render(self.text, True, self.color)
            screen.blit(text_surface, (self.x, self.y))
    
        def change_text(self, event):
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
    
            selected_element = None
    
    
    def create_delete_button(y=280):
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
    
    
    class CheckBox:
        def __init__(
            self, x, y, text, is_checked=False, font_size=20, color=(255, 255, 255)
        ):
            self.x = x
            self.y = y
            self.text = text
            self.is_checked = is_checked
            self.bold = False
            self.italics = False
            self.underlined = False
            self.font_name = None
            self.font_size = font_size
            self.active = False
            self.hovered = False
            self.width = 20
            self.height = 20
            self.size = font_size
            self.color = color
    
        def draw(self, screen):
            font = pygame.font.Font(self.font_name, self.size)
            font.set_bold(self.bold)
            font.set_italic(self.italics)
            font.set_underline(self.underlined)
            text = font.render(self.text, True, self.color)
            screen.blit(text, (self.x, self.y))
    
            # Draw the checkbox
            checkbox_rect = pygame.Rect(self.x + 100, self.y, self.width, self.height)
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
    
        def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if (
                    self.x + 100 < event.pos[0] < self.x + 120
                    and self.y < event.pos[1] < self.y + 20
                ):
                    self.is_checked = not self.is_checked
    
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
            import pygame
    
    import sys
    
    # Initialize Pygame
    pygame.init()
    
    # Constants
    WIDTH, HEIGHT = 800, 600
    NODE_RADIUS = 20
    NODE_COLOR = (100, 100, 100)
    LINE_COLOR = (255, 255, 255)
    CONNECTION_COLOR = (255, 255, 0)
    CONNECTION_WIDTH = 2
    TEXT_COLOR = (0, 0, 255)  # Blue for node labels
    
    # Node types and their labels
    node_types = [
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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Node Editor")
    
    # List to store nodes and connections
    nodes = []
    connections = []
    start_node = {"type": "Start", "label": "Start", "position": (50, HEIGHT // 2)}
    end_node = {"label": "End", "type": "End", "position": (WIDTH - 50, HEIGHT // 2)}
    nodes.append(start_node)
    nodes.append(end_node)
    
    # Constants for the inspector tab
    INSPECTOR_WIDTH = 200
    INSPECTOR_COLOR = (50, 50, 50)
    
    # Create an Inspector rect
    inspector_rect = pygame.Rect(WIDTH - INSPECTOR_WIDTH, 0, INSPECTOR_WIDTH, HEIGHT)
    
    # Create a text input area
    text_input_rect = pygame.Rect(
        WIDTH - INSPECTOR_WIDTH + 10, 50, INSPECTOR_WIDTH - 20, 100
    )
    text_input_text = ""
    font = pygame.font.Font(None, 36)
    text_input_active = False
    
    
    # Function to add a new node to the canvas
    def add_node(node_type, position):
        nodes.append(
            {
                "type": node_type["label"],
                "position": position,
                "rect": pygame.Rect(20, 20, 20, 20),
            }
        )
    
    
    # Function to create a connection between two nodes
    def add_connection(start_node, end_node):
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
    def draw_inspector():
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
    def show_inspector(node):
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
                details = "Node Type: " + node["type"]
                font = pygame.font.Font(None, 28)
                text = font.render(details, True, (0, 0, 0))
                text_rect = text.get_rect()
                text_rect.topleft = (text_input_rect.x + 10, text_input_rect.y + 10)
                screen.blit(text, text_rect)
            else:
                text_input_text = ""
    
    
    # Main loop
    running = True
    selected_node = None
    adding_node = None
    dragging_node = None
    mouse_dragging = False
    connecting_node = None
    drawing_line = False
    line_start = None
    node_moving = False
    directions = {}
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if adding_node is not None:
                        add_node(adding_node, pos)
                        adding_node = None
    
                    # Check if a node is clicked and make it the selected node
                    for node in nodes:
                        if node["rect"].collidepoint(pos):
                            selected_node = node
                            dragging_node = node
    
                    for idx, node_type in enumerate(node_types):
                        node_rect = pygame.Rect(10, 10 + idx * 30, 200, 20)
                        if node_rect.collidepoint(pos):
                            adding_node = node_type
    
                    for node in nodes:
                        if node["rect"].collidepoint(pos):
                            connecting_node = node
                            drawing_line = True
                            line_start = connecting_node["position"]
    
                elif event.button == 2:
                    pos = pygame.mouse.get_pos()
                    for node in nodes:
                        if node["rect"].collidepoint(pos):
                            selected_node = node
                            dragging_node = node
                            mouse_dragging = True
                    text_input_active = text_input_rect.collidepoint(pos)
    
                if event.button == 3:
                    pos = pygame.mouse.get_pos()
                    for node in nodes:
                        if node["rect"].collidepoint(pos):
                            selected_node = node
                            node_moving = True
                            break
    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if drawing_line:
                        pos = pygame.mouse.get_pos()
                        for node in nodes:
                            if node["rect"].collidepoint(pos) and node != connecting_node:
                                add_connection(connecting_node, node)
                        drawing_line = False
                    connecting_node = None
    
                if event.button == 1:
                    if dragging_node and selected_node:
                        selected_node = None
                        dragging_node = None
    
                elif event.button == 2:
                    selected_node = None
                    dragging_node = None
                    mouse_dragging = False
    
        screen.fill((0, 0, 0))
    
        for connection in connections:
            start_pos = connection[0]["position"]
            end_pos = connection[1]["position"]
            pygame.draw.line(screen, LINE_COLOR, start_pos, end_pos, CONNECTION_WIDTH)
    
        for node in [start_node, end_node]:
            node["rect"] = pygame.draw.circle(
                screen, NODE_COLOR, node["position"], NODE_RADIUS
            )
            if node == selected_node:
                pygame.draw.circle(screen, (0, 255, 0), node["position"], NODE_RADIUS)
            pygame.draw.circle(screen, LINE_COLOR, node["position"], NODE_RADIUS, 2)
    
        for idx, node_type in enumerate(node_types):
            node = node_type["label"]
            node_rect = pygame.Rect(10, 10 + idx * 30, 200, 20)
            pygame.draw.rect(screen, NODE_COLOR, node_rect)
            font = pygame.font.Font(None, 36)
            text = font.render(node, True, (255, 255, 255))
            screen.blit(text, (20, 20 + idx * 30))
    
        for node in nodes:
            node["rect"] = pygame.draw.circle(
                screen, NODE_COLOR, node["position"], NODE_RADIUS
            )
            if node == selected_node:
                pygame.draw.circle(screen, (0, 255, 0), node["position"], NODE_RADIUS)
            pygame.draw.circle(screen, LINE_COLOR, node["position"], NODE_RADIUS, 2)
            font = pygame.font.Font(None, 24)
            text = font.render(node["type"], True, TEXT_COLOR)
            text_rect = text.get_rect()
            text_rect.center = (node["position"][0], node["position"][1] - NODE_RADIUS - 10)
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
            - Sets x, y, width and height attributes of panel 
from arguments
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
                import playfab
    from SquarePixels.uimanagement.leaderboard import DoPost
    from playfab import PlayFabSettings, PlayFabErrors
    
    
    def GetAccountInfo(request, callback, customData = None, extraHeaders = None):
        """
        Retrieves the user's PlayFab account details
        https://docs.microsoft.com/rest/api/playfab/client/account-management/getaccountinfo
        """
        if not PlayFabSettings._internalSettings.ClientSessionTicket:
            raise PlayFabErrors.PlayFabException("Must be logged in to call this method")
    
        def wrappedCallback(playFabResult, error):
            if callback:
                callback(playFabResult, error)
    
        return DoPost("/Client/GetAccountInfo", request, "X-Authorization", PlayFabSettings._internalSettings.ClientSessionTicket, wrappedCallback, customData, extraHeaders)
    
    
    class PlayerProfileViewConstraints:
        def __init__(self, ShowAvatarUrl=False):
            self.ShowAvatarUrl = ShowAvatarUrl
            
    def get_user_avatar(email):
        request = {"Email":email}
        def callback(success, failure):
                if success:
                    print("Retrieved account details.")
                else:
                    print("failed to retrieve account details.")
                    if failure:
                        print("Here's some debug information:")
                        print(str(failure))
                        
        result = playfab.PlayFabClientAPI.GetAccountInfo(request, callback)
        print(result)
        request = {"ProfileConstraints":PlayerProfileViewConstraints(True),"PlayFabId":result}
        playfab.PlayFabClientAPI.GetPlayerProfile()    # Color picker input field for customizing color
    
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