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

    def roundtoblock(self, x, base=15):
        return base * round(x / base)

    def update(self, x, y, colliders, sky):
        self.move(x, colliders, sky)
        # Calculate the distance from the player to the enemy
        distance = math.sqrt((self.enemyx - x) ** 2 + (self.enemyy - y) ** 2)
        if distance <= 30:  # two blocks
            self.attack()
        if self.damaged:
            self.attacked()

    def attacked(self, damage, strength):
        pass

    def attack(self):
        pass

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
                    else:
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
        pig.draw.rect(screen, (200, 0, 0), (self.enemyx - 10, self.enemyy - 15, 20, 20))
