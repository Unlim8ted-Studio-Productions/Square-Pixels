import cv2
import pygame as pig


def play_intro_video(frame):
    # Load the video
    while success:
        clock.tick(60)
        success, img = frame.read()
        for event in pig.event.get():
            if event.type == pig.QUIT:
                success = False
        screen.blit(pig.image.frombuffer(img.tobytes(), shape, "BGR"), (0, 0))
        pig.display.update()
        for event in pig.event.get():
            if event.type == pig.QUIT:
                pig.quit()
                quit()

    pig.quit()


if __name__ == "__main__":
    pig.init()

    video = cv2.VideoCapture(r"terraria_styled_game\\Company Animated Logo.mov")
    success, img = video.read()
    shape = img.shape[1::-1]
    clock = pig.time.Clock()
    screen = pig.display.set_mode((600, 600))
    pig.display.toggle_fullscreen()
    pig.display.set_caption("terraria styledgame")
    # Path to your video file

    # Call the function to play the video
    play_intro_video(img)

    # Rest of your game code goes here...
