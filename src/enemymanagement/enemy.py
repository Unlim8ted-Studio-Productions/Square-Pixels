import pygame as pig
import random
import math
from PIL import Image, ImageSequence


def load_gif_animation(gif_path):
    """
    Loads a GIF animation from a file and converts it into a list of Pygame surfaces.

    Parameters:
    - gif_path (str): The file path to the GIF image to be loaded.

    Returns:
    list: A list of Pygame surfaces, each representing a frame of the GIF animation.

    Note:
    - This function uses the Pillow library to load the GIF image.
    - The returned list contains Pygame surfaces representing each frame of the animation.
    - The first frame (static image) is removed from the list, as GIFs typically start from the second frame.

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
            r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(1)(1)(1).gif"
        )
        self.right = load_gif_animation(
            r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(2)(1).gif"
        )
        self.rspitattack = load_gif_animation(
            r"terraria_styled_game\creatures\enemies\Little Demon\attack\Little demon(1)(1).gif"
        )
        self.lspitattack = load_gif_animation(
            r"terraria_styled_game\creatures\enemies\Little Demon\attack\Little demon(1).gif"
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
                    r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(2)(1).gif"
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
                        r"terraria_styled_game\creatures\enemies\Little Demon\attack\Little demon(1)(1).gif"
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
                    r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(1)(1)(1).gif"
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
                        r"terraria_styled_game\creatures\enemies\Little Demon\attack\Little demon(1).gif"
                    )
                    screen.blit(
                        pig.transform.scale(self.lspitattack[0], (100, 80)),
                        (self.enemyx, self.enemyy - 15, 25, 25),
                    )
                    self.lspitattack.pop(0)
