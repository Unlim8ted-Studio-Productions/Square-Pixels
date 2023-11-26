from SquarePixels.uimanagement.elements.button import Button
from SquarePixels.uimanagement.elements.input_feild import InputField
from SquarePixels.uimanagement.elements.TextElement import TextElement
from SquarePixels.uimanagement.elements.checkbox import CheckBox
from SquarePixels.uimanagement.elements.color import ColorPickerInputField
from SquarePixels.uimanagement.elements.Image import ImageElement
from SquarePixels.uimanagement.elements.slider import Slider
import pygame

# Set the screen size
infoObject: object = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
screen_width, screen_height = infoObject.current_w, infoObject.current_h
screen: pygame.Surface = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h)
)
pygame_icon = pygame.image.load(
    r"recources\program recources\Screenshot 2023-09-21 181742.png"
)
pygame.display.set_icon(pygame_icon)  # pygame.display.toggle_fullscreen()
pygame.display.set_caption("Square Pixel")
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)


button1 = Button(
    "Trails",
    WIDTH / 3.5164835164835164,
    HEIGHT / 4.302788844621514,
    WIDTH / 10.726256983240223,
    HEIGHT / 17.142857142857142,
    None,
)

button4 = Button(
    "Back",
    WIDTH / 2.4615384615384617,
    HEIGHT / 3.085714285714286,
    WIDTH / 13.81294964028777,
    HEIGHT / 22.97872340425532,
    None,
)
button5 = Button(
    "ariving soon",
    WIDTH / 2.2857142857142856,
    HEIGHT / 4.202334630350195,
    WIDTH / 11.851851851851851,
    HEIGHT / 20.37735849056604,
    None,
)

TextElement1 = TextElement(
    WIDTH / 2.5396825396825395, HEIGHT / 14.4, WIDTH / 38.4, HEIGHT / 43.2
)
TextElement2 = TextElement(
    WIDTH / 1.6040100250626566, HEIGHT / 6.428571428571429, WIDTH / 38.4, HEIGHT / 43.2
)
