import pygame


class CheckBox:
    def __init__(
        self, x, y, text, is_checked=False, font_size=20, color=(255, 255, 255)
    ):
        self.x = x
        self.y = y
        self.text = text
        self.is_checked = is_checked
        self.bold = False
        self.italics = False
        self.underlined = False
        self.font_name = None
        self.font_size = font_size
        self.active = False
        self.hovered = False
        self.width = 20
        self.height = 20
        self.size = font_size
        self.color = color

    def draw(self, screen):
        font = pygame.font.Font(self.font_name, self.size)
        font.set_bold(self.bold)
        font.set_italic(self.italics)
        font.set_underline(self.underlined)
        text = font.render(self.text, True, self.color)
        screen.blit(text, (self.x, self.y))

        # Draw the checkbox
        checkbox_rect = pygame.Rect(self.x + 100, self.y, self.width, self.height)
        pygame.draw.rect(screen, self.color, checkbox_rect, 2)
        if self.is_checked:
            pygame.draw.line(
                screen,
                self.color,
                (self.x + 105, self.y + 10),
                (self.x + 115, self.y + 20),
                5,
            )
            pygame.draw.line(
                screen,
                self.color,
                (self.x + 115, self.y + 20),
                (self.x + 135, self.y + 5),
                5,
            )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (
                self.x + 100 < event.pos[0] < self.x + 120
                and self.y < event.pos[1] < self.y + 20
            ):
                self.is_checked = not self.is_checked

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
