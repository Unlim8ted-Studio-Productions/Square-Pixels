import pygame as pig
import typing
import colorsys


class Player:
    def __init__(self, x: int, y: int, name: str):
        self.x: int = x
        self.y: int = y
        self.velocity_y: float = 0
        self.velocity_x: float = 0
        self.speed: int = 2
        self.gravity: float = 0.02
        self.name: str = name
        self.gravityi: bool = True
        self.rainbow: bool = False
        self.inverse: bool = False
        self.trail: typing.List[
            typing.Tuple[int, int]
        ] = []  # Stores previous positions

    def update(self, screen_height: int, screen_width: int) -> None:
        if self.gravityi:
            self.velocity_y += self.gravity

        self.x += self.velocity_x
        self.y += self.velocity_y

        if self.y > screen_height - 20:
            self.y = screen_height - 20
            self.velocity_y = 0
        if self.x <= 0:
            self.velocity_x = 1
        if self.x >= screen_width:
            self.velocity_x = -1

        if self.velocity_x > 0:
            self.velocity_x -= 0.001
        if self.velocity_x < 0:
            self.velocity_x += 0.001

        self.trail.append((self.x, self.y))  # Add current position to trail

        if len(self.trail) > 20:  # Limit the trail length to 10
            self.trail.pop(0)  # Remove the oldest position

    def draw_trail(self, screen: pig.Surface) -> None:
        trail_s_num: int = 1
        trail_l_num: int = len(self.trail)
        add_tsize: int = 1

        if self.inverse:
            for position in self.trail:
                pig.draw.circle(
                    screen, (255, 255, 255), position, (trail_l_num - trail_s_num)
                )
                trail_s_num += 1
        else:
            if self.rainbow:
                hue_step = 360 / len(self.trail)
                hue = 0
                for position in self.trail:
                    rgb = colorsys.hsv_to_rgb(hue / 360, 1, 1)
                    r, g, b = [int(c * 255) for c in rgb]
                    pig.draw.circle(
                        screen, (r, g, b), position, (trail_s_num + add_tsize)
                    )
                    add_tsize += 0.5
                    hue += hue_step
            else:
                r: int = 255
                g: int = 255
                b: int = 255
                for position in self.trail:
                    pig.draw.circle(
                        screen, (r, g, b), position, (trail_s_num + add_tsize)
                    )
                    add_tsize += 0.5

    def clear_trail(self) -> None:
        self.trail = []  # Clear the trail
