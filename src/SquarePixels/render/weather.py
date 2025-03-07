import pygame as pig
import random
infoObject: object = pig.display.Info()

def draw_rain(screen, raindrops, wind):
    for drop in raindrops:
        # Update raindrop position based on wind
        drop[0] += wind + random.uniform(-.1,.1)
        drop[1] += 5  # Move down
        drop[2] -= 5  # Decrease opacity

        # Draw semi-transparent line for a blur effect
        pig.draw.aaline(screen, (random.randint(0,20), random.randint(0,220), random.randint(220,255), drop[2]), (drop[0], drop[1]), (drop[0], drop[1] + 5))

    # Remove raindrops that have moved out of the screen or faded completely
    raindrops[:] = [drop for drop in raindrops if drop[1] < infoObject.current_h and drop[2] > 0]


def draw_lightning(screen, lightning_pos, lightning_duration, frame_count):
    if frame_count < lightning_duration:
        # Draw lightning
        pig.draw.line(screen, (255, 255, 255), lightning_pos[0], lightning_pos[1], 2)

        # Simulate flash by adding a transparent white surface
        flash_surface = pig.Surface((infoObject.current_w, infoObject.current_h), pig.SRCALPHA)
        flash_surface.fill((255, 255, 255, min(100, frame_count * 10)))  # Adjust the transparency level
        screen.blit(flash_surface, (0, 0))

    else:
        # Fading out the lightning effect
        fade_out = min(255, max(0, 255 - (frame_count - lightning_duration) * 5))
        pig.draw.line(screen, (255, 255, 255, fade_out), lightning_pos[0], lightning_pos[1], 2)


def draw_clouds(screen, clouds):
    for cloud in clouds:
        pig.draw.ellipse(screen, (255, 255, 255), cloud)

def draw_leaves(screen, leaves):
    for leaf in leaves:
        pig.draw.ellipse(screen, (34, 139, 34), leaf)

def update_weather(weather, raindrops, lightning_pos, clouds, leaves):
    if weather == "rain":
        for i in range(10):
            # Initialize raindrop with random position and full opacity
            raindrops.append([random.randint(0, infoObject.current_w), random.randint(0, infoObject.current_h), 255])
    elif weather == "thunderstorm":
        if random.randint(0, 100) < 5:  # Probability of lightning occurring
            lightning_pos[0] = (random.randint(0, infoObject.current_w), 0)
            lightning_pos[1] = (random.randint(0, infoObject.current_w), infoObject.current_h)
            frame_count = 0  # Reset frame count for lightning duration
        for i in range(10):
            # Initialize raindrop with random position and full opacity
            raindrops.append([random.randint(0, infoObject.current_w), random.randint(0, infoObject.current_h), 255])

    elif weather == "cloudy":
        for i in range(5):
            cloud_size = random.randint(50, 100)
            cloud = pig.Rect(random.randint(0, infoObject.current_w), random.randint(0, infoObject.current_h), cloud_size, cloud_size)
            clouds.append(cloud)
    elif weather == "windy":
        for i in range(5):
            leaf_size = random.randint(5, 20)
            leaf = pig.Rect(random.randint(0, infoObject.current_w), random.randint(0, infoObject.current_h), leaf_size, leaf_size)
            leaves.append(leaf)
