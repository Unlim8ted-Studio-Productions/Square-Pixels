import pygame as pig
import os
from moviepy.editor import VideoFileClip
import moviepy.editor
import glob
import numpy as np


def extract_frames(video_file: str, image_folder: str) -> None:
    if not os.path.isfile(image_folder + "/frame%04d.png"):
        clip = VideoFileClip(video_file)
        # clip = clip.reader.read_frame()
        # clip = np.array(clip)
        # assert clip.ndim == 3
        # print(clip.shape)
        # for xx in range(clip.shape[0]):
        #    for yy in range(clip.shape[1]):
        #        for zz in range(clip.shape[2]):
        #
        # clip = moviepy.editor.ImageClip(clip)
        clip.write_images_sequence(image_folder + "/frame%04d.png")
        clip.audio.write_audiofile(image_folder + "/audio.wav")


def play_intro_video(image_folder, not_skipped, screen):
    clock: object = pig.time.Clock()

    # Load the images from the specified folder
    image_files: str = sorted(glob.glob(image_folder + "/frame*.png"))

    # Load the audio file
    audio_file: str = image_folder + "/audio.wav"
    pig.mixer.music.load(audio_file)

    # Start playing the audio
    pig.mixer.music.play()

    # Load each image and display it on the screen

    for image_file in image_files:
        if not_skipped == True:
            image = pig.image.load(image_file).convert()
            infoObject: object = pig.display.Info()
            image = pig.transform.scale(
                image, (infoObject.current_w, infoObject.current_h)
            )
            screen.blit(image, (0, 0))
            pig.display.flip()
            clock.tick(60)  # Adjust the frame rate as needed
            for event in pig.event.get():
                if event.type == pig.VIDEORESIZE:
                    screen = pig.display.set_mode((event.w, event.h), pig.RESIZABLE)
                if event.type == pig.QUIT:
                    pig.quit()
                    quit()
                if event.type == pig.KEYDOWN:
                    not_skipped = False

    # Stop the audio playback
    pig.mixer.music.stop()
