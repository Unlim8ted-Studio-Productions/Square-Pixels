import pygame

if __name__ == "__main__":
    # Constants
    infoObject: object = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    BACKGROUND_COLOR = (0, 0, 0)
font = pygame.font.Font(None, 36)
# Define colors
WHITE = (255, 255, 255)
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)

white = (255, 255, 255)


# Create an InputField class for text input
class InputField:
    def __init__(self, x, y, width, height, placeholder):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.placeholder = placeholder
        self.text = ""
        self.active = False
        self.size = 36
        self.hovered = False
        self.font_name = "terraria_styled_game\Fonts\PixelifySans-Regular.ttf"

    def draw(self, screen):
        font = pygame.font.Font(self.font_name, self.size)
        color = BUTTON_COLOR if not self.active else BUTTON_HOVER_COLOR
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        font_color = (0, 0, 0) if not self.active else (255, 255, 255)
        text = font.render(
            self.text if self.text else self.placeholder, True, font_color
        )
        screen.blit(text, (self.x + 10, self.y + 10))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def change_text(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = (
                self.x < event.pos[0] < self.x + self.width
                and self.y < event.pos[1] < self.y + self.height
            )
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered:
                self.active = True
            else:
                self.active = False
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
