import pygame as pig
import random
from SquarePixels.render.weather import update_weather, draw_clouds, draw_leaves, draw_lightning, draw_rain

frame_count = 0  # Count frames for lightning duration
lightning_duration = 10  # Adjust the duration of the lightning effect


running = True
clock = pig.time.Clock()
raindrops = []
lightning_pos = [(0, 0), (0, 0)]
clouds = []
leaves = []
wind = 0
newwind = 0
weather = "clear"  # Initial weather
rain = False
def weather_manager():
    global weather, wind, newwind, rain, clouds, leaves, lightning_pos, frame_count, raindrops
    if not rain and random.randint(0,1000) <= 1:
        weather = "rain"
        rain = True
    if weather != "clear" and random.randint(0,1000) <= 1:
        weather = "clear"
        rain = False
    if random.randint(0, 100) < 5:  # Probability of wind direction change occurring
        newwind = random.randint(-3, 3)  # Introduce wind for raindrops
    if wind < newwind:
        wind += .01
    if wind > newwind:
        wind -= .01
    return weather
def draw_weather(screen):
    global weather, wind, newwind, rain, clouds, leaves, lightning_pos, frame_count, raindrops

    # Update and draw weather effects
    update_weather(weather, raindrops, lightning_pos, clouds, leaves)
    draw_rain(screen, raindrops, wind)
    draw_lightning(screen, lightning_pos, lightning_duration, frame_count)
    draw_clouds(screen, clouds)
    draw_leaves(screen, leaves)
