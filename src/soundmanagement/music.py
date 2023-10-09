import pygame


def play_music(file_path, loops=0, start=0, fade_ms=0, channel=0, volume=1):
    pygame.mixer.init()
    pygame.mixer.Channel(channel).set_volume(volume)
    pygame.mixer.Channel(channel).play(
        pygame.mixer.Sound(file_path), loops, start, fade_ms
    )
