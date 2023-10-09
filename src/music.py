import pygame


def play_music(file_path, loops=0, start=0, fade_ms=0):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops, start, fade_ms)
