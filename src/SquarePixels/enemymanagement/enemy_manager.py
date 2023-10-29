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
