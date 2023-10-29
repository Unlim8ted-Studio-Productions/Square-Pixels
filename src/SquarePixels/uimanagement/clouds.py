# Cloud class
class Cloud:
    def __init__(self, x, y, image, speed):
        self.x = x
        self.y = y
        self.image = image
        self.speed = speed
        self.alpha = 0

    def move(self):
        self.x -= self.speed
        self.alpha += 1
        if self.alpha >= 255:
            self.alpha = 255

    def draw(self, screen):
        self.image.set_alpha(self.alpha)
        screen.blit(self.image, (self.x, self.y))
