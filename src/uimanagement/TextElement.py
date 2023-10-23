import pygame


class TextElement:
    def __init__(self, x, y, text, font_size):
        self.x = x
        self.y = y
        self.text = text
        self.font_size = font_size
        self.color = (255, 255, 255)  # Default text color
        self.size = font_size
        self.hovered = False
        self.width = 50
        self.height = 25
        self.bold = False
        self.italics = False
        self.underlined = False
        self.font_name = None

    def draw(self, screen):
        font = pygame.font.Font(self.font_name, self.size)
        font.set_bold(self.bold)
        font.set_italic(self.italics)
        font.set_underline(self.underlined)
        text_surface = font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.x, self.y))

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
