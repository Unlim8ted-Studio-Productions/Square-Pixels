import pygame as pg
import random
import collision as c


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

    def generate_terrain(self):
        self.terrain = [[0 for _ in range(self.width[1])] for _ in range(self.height)]
        ground_levels = [int(self.height / 1.5)] * self.width[1]  
        # Set sky blocks
        for x in range(self.width[0], self.width[1]):
            for y in range(ground_levels[x]):
                self.terrain[y][x] = 8  # Sky
                
        # Generate natural water features in dips (lakes)
        for x in range(self.width[0], self.width[1]):
            dip_chance = random.randint(0, 100)
            if dip_chance < 5:  # Adjust the chance as needed for less frequent lakes
                lake_width = random.randint(10, 30)  # Random width of the lake
                lake_depth = random.randint(5, 15)   # Random depth of the lake
                lake_start_y = ground_levels[x]  # Start the lake at the ground level
                for y in range(lake_start_y, lake_start_y + lake_depth):
                    for dx in range(-lake_width // 2, lake_width // 2 + 1):
                        if 0 <= x + dx < self.width[1] and 0 <= y < self.height:
                            self.terrain[y][x + dx] = 10  # Water
            
        # Generate random ground
        ground_levels = [int(self.height / 1.5)] * self.width[1]
        for x in range(self.width[0], self.width[1]):
            ground_levels[x] = ground_levels[x - 1] + random.randint(-2, 2)
            ground_levels[x] = max(0, min(self.height - 1, ground_levels[x]))

        for x in range(self.width[0], self.width[1]):
            for y in range(ground_levels[x], self.height):
                self.terrain[y][x] = random.choice([0, 1])  # Stone or Dirt

        # sand
        for x in range(self.width[0], self.width[1]):
            for y in range(ground_levels[x], self.height):
                if self.terrain[y - 1][x] == 10:
                    self.terrain[y][x] = 11  # Replace empty space with dirt

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
                             

        # Generate ore deposits
        ore_count = self.width[1] // 100
        for _ in range(ore_count):
            ore_type = random.choice([4, 5, 6, 7])  # Coal, Iron, Gold, Diamond
            ore_x = random.randint(0, self.width[1] - 1)
            validnu = False
            while not validnu:
                try:
                    ore_y = random.randint(ground_levels[ore_x] + 1, self.height - 1)
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

        # # Generate colliders based on terrain
        # for x in range(len(self.terrain[0])):
        #    for y in range(len(self.terrain)):
        #        if self.terrain[y][x] != 0:
        #            collider = c.Collider(x, y, 32, 32)
        #            self.colliders.append(collider)

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
    pg.display.set_caption("terraria styledgame")
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_CROSSHAIR)
    terrain_generator = TerrainGenerator(800, infoObject.current_h // 10)
    terrain_generator.run(screen)
