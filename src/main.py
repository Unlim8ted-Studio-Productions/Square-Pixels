import pygame as pig
import glob
from moviepy.editor import VideoFileClip
import os
import pygame as pig
from moviepy.editor import VideoFileClip
import terrain_gen as tgen
import render
import typing as tp

def extract_frames(video_file:str, image_folder:str) -> None:
    if not os.path.isfile(image_folder + "/frame%04d.png"):
        clip = VideoFileClip(video_file)
        clip.write_images_sequence(image_folder + "/frame%04d.png")
        clip.audio.write_audiofile(image_folder + "/audio.wav")


def play_intro_video(image_folder, not_skipped, screen):
    clock:object = pig.time.Clock()

    # Load the images from the specified folder
    image_files:str = sorted(glob.glob(image_folder + "/frame*.png"))

    # Load the audio file
    audio_file:str = image_folder + "/audio.wav"
    pig.mixer.music.load(audio_file)

    # Start playing the audio
    pig.mixer.music.play()

    # Load each image and display it on the screen
    
    for image_file in image_files:
        if not_skipped == True:
            image = pig.image.load(image_file).convert()
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


if __name__ == "__main__":
    pig.init()

    not_skipped:bool = True
    # Path to your video file
    video_file:str = r"terraria_styled_game\\Company Animated Logo.mov"
    infoObject:object = pig.display.Info()
    screen:pig.Surface = pig.display.set_mode((infoObject.current_w, infoObject.current_h))
    pig.display.toggle_fullscreen()
    pig.display.set_caption("terraria styledgame")
    pig.mouse.set_cursor(pig.SYSTEM_CURSOR_CROSSHAIR)

    # Path to the folder to save the extracted frames
    image_folder = r"terraria_styled_game\\frames"

    # Extract frames from the video
    # extract_frames(video_file, image_folder)

    # Call the function to play the video
    play_intro_video(image_folder, not_skipped, screen)

    # Rest of game code goes here...
    world:object = tgen.generate()
    for square in world.tiles:
        render.draw(screen, square)
    
