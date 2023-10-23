import pygame


class CheckBox:
    def __init__(self, x, y, label, is_checked=False, font_size=20):
        self.x = x
        self.y = y
        self.label = label
        self.is_checked = is_checked
        self.bold = False
        self.italics = False
        self.underlined = False
        self.font_name = None
        self.font_size = font_size

    def draw(self, screen):
        font = pygame.font.Font(self.font_name, 24)
        font.set_bold(self.bold)
        font.set_italic(self.italics)
        font.set_underline(self.underlined)
        text = font.render(self.label, True, (255, 255, 255))
        screen.blit(text, (self.x, self.y))

        # Draw the checkbox
        checkbox_rect = pygame.Rect(self.x + 100, self.y, 20, 20)
        pygame.draw.rect(screen, (255, 255, 255), checkbox_rect, 2)
        if self.is_checked:
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (self.x + 105, self.y + 10),
                (self.x + 115, self.y + 20),
                2,
            )
            pygame.draw.line(
                screen,
                (255, 255, 255),
                (self.x + 115, self.y + 20),
                (self.x + 135, self.y + 5),
                2,
            )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (
                self.x + 100 < event.pos[0] < self.x + 120
                and self.y < event.pos[1] < self.y + 20
            ):
                self.is_checked = not self.is_checked
