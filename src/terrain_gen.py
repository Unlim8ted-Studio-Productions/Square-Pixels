import pygame as pg
import random

class TerrainGenerator:
    def __init__(self, width, height, pos_x=0, pos_y=0):
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.terrain = []
        self.camera_x = 0
        self.camera_y = 0

    def generate_terrain(self):
        self.terrain = [[0 for _ in range(self.width)] for _ in range(self.height)]

        # Generate random ground
        ground_levels = [self.height // 2] * self.width
        for x in range(1, self.width):
            ground_levels[x] = ground_levels[x - 1] + random.randint(-2, 2)
            ground_levels[x] = max(0, min(self.height - 1, ground_levels[x]))

        for x in range(self.width):
            for y in range(ground_levels[x], self.height):
                self.terrain[y][x] = random.choice([0, 1])  # Stone or Dirt

        # Set sky blocks
        for x in range(self.width):
            for y in range(ground_levels[x]):
                self.terrain[y][x] = 8  # Sky

        # Generate trees
        tree_count = self.width // 10
        for _ in range(tree_count):
            tree_x = random.randint(0, self.width - 1)
            treeypartone = random.randint(5, 10)
            tree_y = ground_levels[tree_x] - treeypartone
            #windowsdimen = pg.display.get_window_size()[1]
            tree_height = treeypartone  # random.randint(3, 6)
            for y in range(tree_y, tree_y + tree_height):
                self.terrain[y][tree_x] = 2  # Wood

            # Generate tree leaves
            leaf_radius = random.randint(2, 4)
            for dx in range(-leaf_radius, leaf_radius + 1):
                for dy in range(-leaf_radius, leaf_radius + 1):
                    if 0 <= tree_x + dx < self.width and 0 <= tree_y + dy < self.height:
                        if abs(dx) + abs(dy) <= leaf_radius:
                            self.terrain[tree_y + dy][tree_x + dx] = 3  # Leaves

        # Generate ore deposits
        ore_count = self.width // 100
        for _ in range(ore_count):
            ore_type = random.choice([4, 5, 6, 7])  # Coal, Iron, Gold, Diamond
            ore_x = random.randint(0, self.width - 1)
            ore_y = random.randint(ground_levels[ore_x] + 1, self.height - 1)
            ore_radius = random.randint(1, 4)
            for dx in range(-ore_radius, ore_radius + 1):
                for dy in range(-ore_radius, ore_radius + 1):
                    if 0 <= ore_x + dx < self.width and 0 <= ore_y + dy < self.height:
                        if abs(dx) + abs(dy) <= ore_radius:
                            self.terrain[ore_y + dy][ore_x + dx] = ore_type

    def render_terrain(self, screen):
        tile_size = 10
        colors = [
            (100, 100, 100),  # Stone
            (139, 69, 19),    # Dirt
            (139, 115, 85),   # Wood
            (34, 139, 34),    # Leaves
            (0, 128, 0),      # Coal
            (211, 211, 211),  # Iron
            (255, 223, 0),    # Gold
            (128, 128, 128),  # Diamond
            (135, 206, 235),  # Sky (Blue)
        ]  # Color palette for blocks

        for x in range(self.width):
            for y in range(self.height):
                block_type = self.terrain[y][x]
                color = colors[block_type]
                pg.draw.rect(
                    screen,
                    color,
                    (
                        (x + self.pos_x - self.camera_x) * tile_size,
                        (y + self.pos_y - self.camera_y) * tile_size,
                        tile_size,
                        tile_size,
                    ),
                )

    def run(self, screen):
        clock = pg.time.Clock()

        self.generate_terrain()

        vx = 0
        vy = 0
        
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_UP or event.key == ord('w'):
                        vy = -1
                    elif event.key == pg.K_DOWN or event.key == ord('s'):
                        vy = 1
                    elif event.key == pg.K_LEFT or event.key == ord('a'):
                        vx = -1
                    elif event.key == pg.K_RIGHT or event.key == ord('d'):
                        vx = 1
            self.camera_x += vx
            self.camera_y += vy
            vx,vy=.5,0
            #if vx >= 0:
            #    vx = 0
            #if vy >= 0:
            #    vy = 0
            #if vx <= 0:
            #    vx = 0
            #if vy <= 0:
            #    vy = 0
            
            screen.fill((0, 0, 0))
            self.render_terrain(screen)
            pg.display.flip()
            clock.tick(60)

        pg.quit()


def start():
    pg.init()
    infoObject:object = pg.display.Info()
    screen:pg.Surface = pg.display.set_mode((infoObject.current_w, infoObject.current_h))
    #pg.display.toggle_fullscreen()
    pg.display.set_caption("terraria styledgame")
    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_CROSSHAIR)
    terrain_generator = TerrainGenerator(800, infoObject.current_h//10)
    terrain_generator.run(screen)
