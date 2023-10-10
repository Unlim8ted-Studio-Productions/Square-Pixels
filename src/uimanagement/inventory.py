import pygame as pig


pig.init()

infoObject: object = pig.display.Info()
screen: pig.Surface = pig.display.set_mode((infoObject.current_w, infoObject.current_h))

# these are the images that get shown as items, different color circle for each item
items = [pig.Surface((50, 50), pig.SRCALPHA) for x in range(4)]
wood = pig.image.load(r"terraria_styled_game\Textures\wood.png")
scale = (25, 25)
wood = pig.transform.scale(wood, scale)
items[0].blit(wood, (15, 15, 100, 100))
stone = pig.image.load(r"terraria_styled_game\Textures\stone.jpg")
stone = pig.transform.scale(stone, scale)
items[1].blit(stone, (15, 15, 100, 100))
pig.draw.circle(items[2], (255, 255, 0), (25, 25), 25)
pig.draw.circle(items[3], (0, 0, 255), (25, 25), 25)

font = pig.font.Font(pig.font.match_font("calibri"), 26)


# class for a item, just holds the surface and can resize it
class Item:
    def __init__(self, id):
        self.id = id
        self.surface = items[id]

    def resize(self, size):
        return pig.transform.scale(self.surface, (size, size))


# the inventory system
class Inventory:
    def __init__(
        self, rows=9, col=27, box_size=infoObject.current_w // 30, x=50, y=50, border=3
    ):
        self.rows = rows
        self.col = col
        self.items = [[None for _ in range(self.rows)] for _ in range(self.col)]
        self.box_size = box_size
        self.x = x
        self.y = y
        self.border = border

    # draw everything
    def draw(self, ychange):
        # draw background
        temp = self.y
        if ychange[0]:
            self.y = ychange[1]
        pig.draw.rect(
            screen,
            (100, 100, 100),
            (
                self.x,
                self.y,
                (self.box_size + self.border) * self.col + self.border,
                (self.box_size + self.border) * self.rows + self.border,
            ),
        )
        for x in range(self.col):
            for y in range(self.rows):
                rect = (
                    self.x + (self.box_size + self.border) * x + self.border,
                    self.y + (self.box_size + self.border) * y + self.border,
                    self.box_size,
                    self.box_size,
                )
                pig.draw.rect(screen, (180, 180, 180), rect)
                if self.items[x][y]:
                    screen.blit(self.items[x][y][0].resize(self.box_size), rect)
                    obj = font.render(str(self.items[x][y][1]), True, (0, 0, 0))
                    screen.blit(
                        obj,
                        (rect[0] + self.box_size // 2, rect[1] + self.box_size // 2),
                    )
        self.y = temp

    # get the square that the mouse is over
    def Get_pos(self):
        mouse = pig.mouse.get_pos()

        x = mouse[0] - self.x
        y = mouse[1] - self.y
        x = x // (self.box_size + self.border)
        y = y // (self.box_size + self.border)
        return (x, y)

    # add an item/s
    def Add(self, Item, xy):
        x, y = xy
        if self.items[x][y]:
            if self.items[x][y][0].id == Item[0].id:
                self.items[x][y][1] += Item[1]
            else:
                temp = self.items[x][y]
                self.items[x][y] = Item
                return temp
        else:
            self.items[x][y] = Item

    # check whether the mouse in in the grid
    def In_grid(self, x, y):
        if 0 > x > self.col - 1:
            return False
        if 0 > y > self.rows - 1:
            return False
        return True

    def get_item(self, itemId: int):
        lookingforspot = True
        if itemId != None:
            item = Item(itemId)
            # 0=wood 1=stone
            x = 0
            y = 0
            while lookingforspot:
                if self.items[x][y]:
                    if self.items[x][y].id == itemId:
                        # self.items[x][y] += 1
                        lookingforspot = False
                    else:
                        self.items[x][y] = item
                        lookingforspot = False
                else:
                    self.items[x][y] = item
                    lookingforspot = False


player_inventory = Inventory()
item_bar = Inventory(1, 5, x=infoObject.current_w // 2.5, y=infoObject.current_h / 1.2)

# what the player is holding
selected = None


def inventory(e, truescreen):
    global selected, player_inventory
    inven = True
    while inven:
        mousex, mousey = pig.mouse.get_pos()
        # draw the screen
        screen.fill((255, 255, 255, 100))
        backround = pig.Surface([640, 480], pig.SRCALPHA)
        #
        truescreen.blit(backround, (0, 0))
        player_inventory.draw()

        # if holding something, draw it next to mouse
        if selected:
            truescreen.blit(selected[0].resize(30), (mousex, mousey))
            obj = font.render(str(selected[1]), True, (0, 0, 0))
            truescreen.blit(obj, (mousex + 15, mousey + 15))

        pig.display.update()
        if e.type == pig.K_ESCAPE:
            inven = False

            # if e.type == pig.MOUSEBUTTONDOWN:
            # if right clicked, get a random item
            # if e.button == 3:
            #    selected = [Item(random.randint(0, 3)), 1]

            if e.button == 1:
                pos = player_inventory.Get_pos()
                if player_inventory.In_grid(pos[0], pos[1]):
                    if selected:
                        selected = player_inventory.Add(selected, pos)
                    elif player_inventory.items[pos[0]][pos[1]]:
                        selected = player_inventory.items[pos[0]][pos[1]]
                        player_inventory.items[pos[0]][pos[1]] = None
