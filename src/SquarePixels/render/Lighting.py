import math


def LightAlgorithm(colors, x, y, playerX, playerY, TimeOfDay):
    SunPos = [(TimeOfDay * 25), TimeOfDay*10]
    blockPos = [x, y]
    Darken = round(math.dist(blockPos, SunPos))
    Darken = Darken * TimeOfDay
    num1 = 100
    num2 = 139
    num3 = 69
    num4 = 19
    num5 = 115
    num6 = 85
    num7 = 34
    num8 = 0
    num9 = 128
    num10 = 211
    num11 = 255
    num12 = 223
    num13 = 135
    num14 = 206
    num15 = 235
    if num1 - Darken < 0:
        num1 = Darken
    if num2 - Darken < 0:
        num2 = Darken
    if num3 - Darken < 0:
        num3 = Darken
    if num4 - Darken < 0:
        num4 = Darken
    if num5 - Darken < 0:
        num5 = Darken
    if num6 - Darken < 0:
        num6 = Darken
    if num7 - Darken < 0:
        num7 = Darken
    if num8 - Darken < 0:
        num8 = Darken
    if num9 - Darken < 0:
        num9 = Darken
    if num10 - Darken < 0:
        num10 = Darken
    if num11 - Darken < 0:
        num11 = Darken
    if num12 - Darken < 0:
        num12 = Darken
    if num13 - Darken < 0:
        num13 = Darken
    if num14 - Darken < 0:
        num14 = Darken
    if num15 - Darken < 0:
        num15 = Darken
    colorslist = [
        (num1 - Darken, num1 - Darken, num1 - Darken),
        (num2 - Darken, num3 - Darken, num4 - Darken),
        (num2 - Darken, num5 - Darken, num6 - Darken),
        (num7 - Darken, num2 - Darken, num7 - Darken),
        (num8 - Darken, num9 - Darken, num8 - Darken),
        (num10 - Darken, num10 - Darken, num10 - Darken),
        (num11 - Darken, num12 - Darken, num8 - Darken),
        (num9 - Darken, num9 - Darken, num9 - Darken),
        (num13 - Darken, num14 - Darken, num15 - Darken),
        (num11 - Darken, num11 - Darken, num11 - Darken),
    ]
    return colorslist
