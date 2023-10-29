import pygame


def play_music(file_path, loops=0, start=0, fade_ms=0, channel=0, volume=1):
    """
    Play a music file using Pygame's mixer module.

    This function initializes the Pygame mixer module if not already initialized
    and plays a music file specified by `file_path` on the specified audio `channel`.
    You can control various playback parameters, including the number of `loops`,
    the `start` position in milliseconds, and `fade_ms` for fading in and out.
    Additionally, you can set the `volume` of the audio channel.

    Args:
        file_path (str): The path to the music file to be played.
        loops (int, optional): Number of times the music should loop (0 for no looping, default).
        start (int, optional): Start playback at the specified position in milliseconds (default is 0).
        fade_ms (int, optional): Time in milliseconds for fading in/out (default is 0, no fade).
        channel (int, optional): The audio channel to use for playback (default is 0).
        volume (float, optional): The volume level for the audio channel (default is 1).

    Returns:
        None

    Note:
        - Ensure that Pygame and the mixer module are properly initialized before calling this function.
        - Make sure to handle any exceptions related to file loading or Pygame initialization.

    Example:
        # Play a music file with looping for 3 times, starting at 5000 milliseconds,
        # and fading in/out over 2000 milliseconds with reduced volume.
        play_music("background_music.mp3", loops=3, start=5000, fade_ms=2000, volume=0.5)
    """
    pygame.mixer.init()
    pygame.mixer.Channel(channel).set_volume(volume)
    pygame.mixer.Channel(channel).play(
        pygame.mixer.Sound(file_path), loops, start, fade_ms
    )
