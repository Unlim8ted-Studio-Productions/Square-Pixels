import pygame as pig
import random
import math


class enemy:
    def __init__(
        self,
        enemyy=random.randint(0, pig.display.get_window_size()[1]),
        enemyx=random.randint(0, pig.display.get_window_size()[0]),
        health=random.randint(3, 7),
        damaged=False,
        defence=random.randint(1, 4),
        passive=False,
        damageamount=random.randint(2, 5),
        attackstrength=random.randint(2, 5),
    ):
        self.enemyy = enemyy
        self.enemyx = enemyx
        self.health = health
        self.damaged = damaged
        self.defence = defence
        self.passive = passive
        self.attackstrength = attackstrength
        self.damageamount = damageamount
        self.direction = False  # left
        self.spit = False
        self.left = pig.transform(
            pig.image.load(
                r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(1)(5).gif"
            ),
            25,
            25,
        )
        self.right = pig.transform(
            pig.image.load(
                r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(1)(1).gif"
            ),
            25,
            25,
        )
        self.spitattack = pig.transform(
            pig.image.load(
                r"terraria_styled_game\creatures\enemies\Little Demon\wall climbing\Little demon(1)(5).gif"
            ),
            25,
            25,
        )

    def roundtoblock(self, x, base=15):
        return base * round(x / base)

    def update(self, x, y, colliders, sky, player):
        self.move(x, colliders, sky)
        # Calculate the distance from the player to the enemy
        distance = math.sqrt((self.enemyx - x) ** 2 + (self.enemyy - y) ** 2)
        if distance <= 30:  # two blocks
            self.attack(player)
        if self.damaged:
            self.attacked()

    def attacked(self):
        pass

    def attack(self, player):
        player.get_damage(random.randint(3, 7))
        self.spit = True
        self.draw()

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
            screen.blit()
            # right
        else:
            screen.blit()
        if self.spit:
            screen.blit()

        pig.draw.rect(screen, (200, 0, 0), (self.enemyx - 10, self.enemyy - 15, 20, 20))
