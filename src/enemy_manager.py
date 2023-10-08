import enemy
from random import randint as rand

active_chunks = [(int, int)]
creatures = []
spawned = False
placey = int
placex = int


class enemy_manager:
    def __init__(self, active_chunks=[(int, int)], creatures=[]) -> None:
        self.active_chunks = active_chunks
        self.creatures = creatures

    def update(self, x, y, air, objectinfo, colliders, screen, player):
        for i in self.active_chunks:
            if len(self.creatures) <= rand(1, 2):
                spawned = False
                while not spawned:
                    placey = rand(0, objectinfo.current_h)
                    placex = rand(i[0], i[1])
                    if any(a.collidepoint(placex, placey) for a in air):
                        self.creatures.append(
                            enemy.enemy(placey, placex),
                        )
                        spawned = True
        for creature in self.creatures:
            creature.update(x, y, colliders, air, player, screen)
