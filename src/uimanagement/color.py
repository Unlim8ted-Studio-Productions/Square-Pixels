# Color picker input field for customizing color
import math
import pygame


class ColorPickerInputField:
    def __init__(self, x, y, width, height, label, default_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.color = default_color
        self.active = False
        self.color_dialog_radius = 50  # Radius of the circular color picker
        self.brightness_control_x = self.x + 130
        self.brightness_control_y = self.y
        self.brightness_control_width = 15
        self.brightness_control_height = 120
        self.brightness = 50  # Default brightness
        self.brightness_control_dragging = False

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(self.label, True, (0, 0, 0))
        screen.blit(text, (self.x, self.y - 40))

        # Draw circular color picker dialog
        pygame.draw.circle(
            screen,
            (
                255 - self.brightness * 2,
                255 - self.brightness * 2,
                255 - self.brightness * 2,
            ),
            (self.x + 60, self.y + 60),
            self.color_dialog_radius + 10,
        )

        for angle in range(360):
            radians = math.radians(angle)
            color = pygame.Color(255, 0, 0)  # Initialize with red
            color.hsla = (angle, 100, self.brightness, 100)
            x = int(self.x + 60 + self.color_dialog_radius * math.cos(radians))
            y = int(self.y + 60 + self.color_dialog_radius * math.sin(radians))
            pygame.draw.circle(screen, color, (x, y), 5)

        # Draw selected color
        pygame.draw.circle(screen, self.color, (self.x + 60, self.y + 60), 30)

        # Draw gray background for brightness control
        pygame.draw.rect(
            screen,
            (200, 0, 200),
            (
                self.brightness_control_x,
                self.brightness_control_y,
                self.brightness_control_width,
                self.brightness_control_height,
            ),
        )

        # Draw the brightness control
        pygame.draw.rect(
            screen,
            (0, 0, 0),
            (
                self.brightness_control_x,
                self.brightness_control_y
                + int(
                    (self.brightness_control_height - 15) * (1 - self.brightness / 100)
                ),
                self.brightness_control_width,
                15,
            ),
        )

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_color_picker_clicked(event.pos):
                self.active = True
            if (
                self.brightness_control_x
                <= event.pos[0]
                <= self.brightness_control_x + self.brightness_control_width
                and self.brightness_control_y
                <= event.pos[1]
                <= self.brightness_control_y + self.brightness_control_height
            ):
                self.brightness_control_dragging = True
        if event.type == pygame.MOUSEMOTION:
            if self.active:
                if self.is_color_picker_clicked(event.pos):
                    self.color = self.get_color_at(event.pos)
            if self.brightness_control_dragging:
                # Move the brightness control up and down
                new_y = event.pos[1] - 7.5
                new_y = max(self.brightness_control_y, new_y)
                new_y = min(
                    self.brightness_control_y + self.brightness_control_height - 15,
                    new_y,
                )
                self.brightness = (
                    100
                    - (
                        (new_y - self.brightness_control_y)
                        / (self.brightness_control_height - 15)
                    )
                    * 100
                )
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.active = False
            self.brightness_control_dragging = False

    def is_color_picker_clicked(self, pos):
        return (
            math.hypot(pos[0] - (self.x + 60), pos[1] - (self.y + 60))
            <= self.color_dialog_radius
        )

    def get_color_at(self, pos):
        angle = math.degrees(math.atan2(pos[1] - (self.y + 60), pos[0] - (self.x + 60)))
        if angle < 0:
            angle += 360
        color = pygame.Color(255, 0, 0)
        color.hsla = (angle, 100, self.brightness, 100)
        return color
