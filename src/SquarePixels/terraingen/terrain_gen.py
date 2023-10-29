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
