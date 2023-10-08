import pygame as pig
import random
import math
from PIL import Image, ImageSequence


def load_gif_animation(gif_path):
    # Load the GIF image using Pillow
    gif_image = Image.open(gif_path)

    # Convert the GIF frames to pig surfaces
    frames = []
    for frame in ImageSequence.Iterator(gif_image):
        frame_surface = pig.image.fromstring(frame.tobytes(), frame.size, frame.mode)
        frames.append(frame_surface)
    return frames


class enemy:
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
            r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(1)(5).gif"
        )
        self.right = load_gif_animation(
            r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(1)(1).gif"
        )
        self.rspitattack = load_gif_animation(
            r"terraria_styled_game\creatures\enemies\Little Demon\attack\Little demon(1)(1).gif"
        )
        self.lspitattack = load_gif_animation(
            r"terraria_styled_game\creatures\enemies\Little Demon\attack\Little demon(1).gif"
        )

    def roundtoblock(self, x, base=15):
        return base * round(x / base)

    def update(self, x, y, colliders, sky, player, screen):
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
        player.get_damage(random.randint(3, 7))
        self.spit = True

    def move(self, x, colliders, sky):
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

    def draw(self, screen):
        if self.direction:
            if len(self.right) != 0:
                screen.blit(
                    pig.transform.scale(self.right[0], (40, 15)),
                    (self.enemyx, self.enemyy, 25, 25),
                )
                self.rspitattack.pop(0)
                self.right.pop(0)
                if self.spit:
                    if len(self.rspitattack) != 0:
                        screen.blit(
                            pig.transform.scale(self.rspitattack[0], (40, 15)),
                            (self.enemyx, self.enemyy, 25, 25),
                        )
                        self.rspitattack.pop(0)
                    else:
                        self.rspitattack = load_gif_animation(
                            r"terraria_styled_game\creatures\enemies\Little Demon\attack\Little demon(1)(1).gif"
                        )
            else:
                self.right = load_gif_animation(
                    r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(1)(1).gif"
                )
        else:
            if len(self.left) != 0:
                screen.blit(
                    pig.transform.scale(self.left[0], (40, 15)),
                    (self.enemyx, self.enemyy, 25, 25),
                )
                self.left.pop(0)
                if self.spit:
                    if len(self.lspitattack) != 0:
                        screen.blit(
                            pig.transform.scale(self.lspitattack[0], (40, 15)),
                            (self.enemyx, self.enemyy, 25, 25),
                        )
                        self.lspitattack.pop(0)
                    else:
                        self.lspitattack = load_gif_animation(
                            r"terraria_styled_game\creatures\enemies\Little Demon\attack\Little demon(1).gif"
                        )

            else:
                self.left = load_gif_animation(
                    r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(1)(5).gif"
                )
