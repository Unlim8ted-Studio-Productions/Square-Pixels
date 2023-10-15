import random
import pygame as pig

pig.init()

infoObject = pig.display.Info()
screen = pig.display.set_mode((infoObject.current_w, infoObject.current_h))

# Create item surfaces
items = [pig.Surface((50, 50), pig.SRCALPHA) for x in range(4)]
wood = pig.image.load(r"terraria_styled_game\Textures\wood.png")
stone = pig.image.load(r"terraria_styled_game\Textures\stone.jpg")
scale = (25, 25)
wood = pig.transform.scale(wood, scale)
stone = pig.transform.scale(stone, scale)
items[0].blit(wood, (15, 15, 100, 100))
items[1].blit(stone, (15, 15, 100, 100))
# Create a green sword item
pig.draw.circle(items[2], (0, 255, 0), (25, 25), 25)
# Create a blue circle item
pig.draw.circle(items[3], (0, 0, 255), (25, 25), 25)

font = pig.font.Font(pig.font.match_font("calibri"), 26)


class Item:
    """
    Represents an item with an associated image and ID.

    Args:
        id (int): The ID of the item.

    Attributes:
        id (int): The ID of the item.
        surface (pygame.Surface): The image representing the item.
    """

    def __init__(self, id):
        self.id = id
        self.surface = items[id]

    def resize(self, size):
        """
        Resize the item's image.

        Args:
            size (int): The size to resize the image to.

        Returns:
            pygame.Surface: The resized image.
        """
        return pig.transform.scale(self.surface, (size, size))


class Inventory:
    """
    Represents an inventory for managing items.

    Args:
        rows (int): The number of rows in the inventory grid.
        col (int): The number of columns in the inventory grid.
        box_size (int): The size of each inventory slot.
        x (int): The x-coordinate of the top-left corner of the inventory grid.
        y (int): The y-coordinate of the top-left corner of the inventory grid.
        border (int): The border size around each inventory slot.
    """

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

    def draw(self, ychange):
        """
        Draw the inventory grid on the screen.

        Args:
            ychange (list): A list containing a boolean value indicating if the y-position should change,
                           and the new y-position.
        """
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
        # self.y = temp

    def Get_pos(self):
        """
        Get the position in the inventory grid where the mouse cursor is located.

        Returns:
            tuple: A tuple containing the x and y coordinates of the grid position.
        """
        mouse = pig.mouse.get_pos()
        x = mouse[0] - self.x
        y = mouse[1] - self.y
        x = x // (self.box_size + self.border)
        y = y // (self.box_size + self.border)
        return (int(x), int(y))

    def Add(self, Item, xy):
        """
        Add an item to the inventory grid at the specified position.

        Args:
            Item (Item): The item to add.
            xy (tuple): A tuple containing the x and y coordinates of the position.
        """
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

    def In_grid(self, x, y):
        """
        Check if the specified coordinates are within the inventory grid.

        Args:
            x (int): The x-coordinate to check.
            y (int): The y-coordinate to check.

        Returns:
            bool: True if the coordinates are within the grid, False otherwise.
        """
        # print(
        #    f"x: {x} y: {y} {self.x} {self.y} {self.x+self.col +1*self.box_size} {self.y+self.rows*self.box_size}"
        # )
        if (
            x >= self.x
            and x <= self.x + ((self.col + 1) * self.box_size)
            and y >= self.y
            and y <= self.y + (self.rows * self.box_size)
        ):
            return True
        else:
            return False

    def get_item(self, itemId):
        """
        Get an item with the specified item ID and add it to the inventory.

        Args:
            itemId (int): The ID of the item to retrieve.
        """
        lookingforspot = True
        if itemId is not None:
            item = Item(itemId)
            x = 0
            y = 0
            while lookingforspot:
                if self.items[x][y]:
                    if self.items[x][y][0].id == itemId:
                        lookingforspot = False
                    else:
                        self.items[x][y] = item
                        lookingforspot = False
                else:
                    self.items[x][y] = item
                    lookingforspot = False

    def place_item_in_crafting_grid(self, item, x, y):
        """
        Place an item in the crafting grid at the specified position.

        Args:
            item (Item): The item to place in the grid.
            x (int): The x-coordinate of the grid position.
            y (int): The y-coordinate of the grid position.
        """
        crafting_grid[y][x] = item

    def get_item_from_crafting_grid(self, x, y):
        """
        Get the item from the crafting grid at the specified position.

        Args:
            x (int): The x-coordinate of the grid position.
            y (int): The y-coordinate of the grid position.

        Returns:
            Item: The item in the grid position, or None if no item is present.
        """
        return crafting_grid[y][x]

    def count_item(self, item_id, inventory):
        """
        Count the number of items with the specified item ID in the inventory.

        Args:
            item_id (int): The ID of the item to count.
            inventory (Inventory): The inventory to search.

        Returns:
            int: The count of items with the specified ID.
        """
        count = 0
        for x in range(inventory.col):
            for y in range(inventory.rows):
                if inventory.items[x][y] and inventory.items[x][y][0].id == item_id:
                    count += inventory.items[x][y][1]
        return count

    def remove_item(self, item_id, count, inventory):
        """
        Remove a specified count of items with the given item ID from the inventory.

        Args:
            item_id (int): The ID of the item to remove.
            count (int): The count of items to remove.
            inventory (Inventory): The inventory to remove items from.
        """
        for x in range(inventory.col):
            for y in range(inventory.rows):
                if inventory.items[x][y] and inventory.items[x][y][0].id == item_id:
                    if inventory.items[x][y][1] >= count:
                        inventory.items[x][y][1] -= count
                        if inventory.items[x][y][1] == 0:
                            inventory.items[x][y] = None


player_inventory = Inventory()
item_bar = Inventory(1, 5, x=infoObject.current_w // 2.5, y=infoObject.current_h / 1.2)
selected = None

# Crafting Grid
crafting_grid = Inventory(
    rows=3, col=3, box_size=50, x=50, y=infoObject.current_h / 1.2, border=3
)


crafting_recipes = [
    {
        "pattern": [[(0, 1), None, (0, 1)], [None, (1, 1), None], [None, (1, 1), None]],
        "output": (2, 1),  # Green sword
    },
    # Add more recipes as needed
]


if __name__ == "__main__":
    running = True
    while running:
        for event in pig.event.get():
            if event.type == pig.QUIT:
                running = False
            if event.type == pig.MOUSEBUTTONDOWN:
                if event.button == 3:
                    # Right-click to get a random item
                    selected = [Item(random.randint(0, 3)), 1]
                elif event.button == 1:
                    try:
                        pos = pig.mouse.get_pos()
                        gridpos = player_inventory.Get_pos()
                        if player_inventory.In_grid(pos[0], pos[1]):
                            if selected:
                                selected = player_inventory.Add(selected, gridpos)
                            elif player_inventory.items[gridpos[0]][gridpos[1]]:
                                selected = player_inventory.items[gridpos[0]][
                                    gridpos[1]
                                ]
                                player_inventory.items[gridpos[0]][gridpos[1]] = None
                        gridpos = crafting_grid.Get_pos()
                        if crafting_grid.In_grid(pos[0], pos[1]):
                            if selected:
                                selected = crafting_grid.Add(selected, gridpos)
                            elif crafting_grid.items[gridpos[0]][gridpos[1]]:
                                selected = crafting_grid.items[gridpos[0]][gridpos[1]]
                                crafting_grid.items[gridpos[0]][gridpos[1]] = None
                        gridpos = item_bar.Get_pos()
                        if item_bar.In_grid(pos[0], pos[1]):
                            if selected:
                                selected = item_bar.Add(selected, gridpos)
                            elif item_bar.items[gridpos[0]][gridpos[1]]:
                                selected = item_bar.items[gridpos[0]][gridpos[1]]
                                item_bar.items[gridpos[0]][gridpos[1]] = None
                    except:
                        None  # Handle errors gracefully

        screen.fill((255, 255, 255, 100))
        player_inventory.draw([False, 0])
        crafting_grid.draw([False, 0])
        item_bar.draw([False, 0])

        if selected:
            mousex, mousey = pig.mouse.get_pos()
            screen.blit(selected[0].resize(30), (mousex, mousey))
            obj = font.render(str(selected[1]), True, (0, 0, 0))
            screen.blit(obj, (mousex + 15, mousey + 15))

        pig.display.update()
