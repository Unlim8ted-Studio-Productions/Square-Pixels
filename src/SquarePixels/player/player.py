import numpy as np
import pygame as pig
import typing
import colorsys
import math
import random
from SquarePixels.uimanagement.inventory import Item, player_inventory, item_bar, crafting_grid, crafting_recipes
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
        self.name = "Gus"
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
        self.state = f"falling{0}"

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
        Fire an arrow from the player character.

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
                    self.player_jump()
                elif event.key == pig.K_LEFT or event.key == ord("a"):
                    self.player_move_left()
                elif event.key == pig.K_RIGHT or event.key == ord("d"):
                    self.player_move_right()
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
        Delete a tile from the terrain.

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

    def player_move_left(self):
        self.velocity_x -= self.speed
        music.play_music(
            r"Recources\sounds\player\running.mp3",
            1,
            channel=2,
            volume=15,
        )

    def player_move_right(self):
        self.velocity_x += self.speed
        music.play_music(
            r"Recources\sounds\player\running.mp3",
            1,
            channel=2,
            volume=15,
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
                    print(crafting_grid.items)
                if event.type == pig.MOUSEBUTTONDOWN:
                    # if right clicked, get a random item
                    if event.button == 3:
                        selected = [Item(random.randint(0, 5)), 1]
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
            #craftitems = crafting_grid.items
            #for it in craftitems:
            #    for ite in it:
            #        if ite:
            #            ite[0] = ite[0].id
            #[[(<SquarePixels.uimanagement.inventory.Item object at 0x000001B1CF881F50>, 1), <SquarePixels.uimanagement.inventory.Item object at 0x000001B1CF881F90>, <SquarePixels.uimanagement.inventory.Item object at 0x000001B1CF881F50>], 
            # [None, (<SquarePixels.uimanagement.inventory.Item object at 0x000001B1CF881F10>, 1), None], 
            # [None, (<SquarePixels.uimanagemen0001B1CF881F10>, 1),0001B1CF881F10>, 1), None],

           #craftitems=[[[craftitems[0][0][0], craftitems[0][0][1]], [craftitems[0][1][0], craftitems[0][1][1]],[craftitems[0][2][0], craftitems[0][2][1]]],
           #            [[craftitems[1][0][0], craftitems[1][0][1]], [craftitems[1][1][0], craftitems[1][1][1]],[craftitems[1][2][0], craftitems[1][2][1]],
           #            [[craftitems[2][0][0], craftitems[2][0][1]], [craftitems[2][1][0], craftitems[2][1][1]],[craftitems[2][2][0], craftitems[2][2][1]]]]]
           # Convert the list of lists to a NumPy array
            grid_np = np.array(crafting_grid.items)
            
            # Transpose the array
            rotated_grid = np.rot90(grid_np, k=-1).tolist()
            print("items")
            print(rotated_grid)
            print("recipe")
            print(crafting_recipes[0]["pattern"])
            for recipe in crafting_recipes:
                if rotated_grid == recipe["pattern"]:
                    #output=recipe["output"]
                    #for re in output:
                    #    for rec in re:
                    #        if rec:
                    #            rec[0] = Item(rec[0])
                    crafting_grid.items = recipe["output"]
                    print("crafted")
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
        self.trail = []  # Clear the trail
