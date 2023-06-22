import pygame as pig
import terrain_gen as tgen
import render
import typing as tp
import logo


if __name__ == "__main__":
    pig.init()
    clock: object = pig.time.Clock()
    not_skipped: bool = True
    # Path to your video file
    video_file: str = r"terraria_styled_game\\Company Animated Logo.mov"
    infoObject: object = pig.display.Info()
    screen: pig.Surface = pig.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    # pig.display.toggle_fullscreen()
    pig.display.set_caption("terraria styledgame")
    pig.mouse.set_cursor(pig.SYSTEM_CURSOR_CROSSHAIR)

    # Path to the folder to save the extracted frames
    image_folder = r"terraria_styled_game\\frames"

    # Extract frames from the video
    # logo.extract_frames(video_file, image_folder)

    # Call the function to play the video
    logo.play_intro_video(image_folder, not_skipped, screen)

    # Rest of game code goes here...
    terrain_gen = tgen.TerrainGenerator(800, infoObject.current_h // 10)
    terrain_gen.run(screen)

    # world:object = tgen.generate()
    # for square in world.tiles:
    #    render.draw(screen, square)
    vx, vy = 0, 0
    running = True
    while running:
        for event in pig.event.get():
            if event.type == pig.QUIT:
                running = False
            elif event.type == pig.KEYDOWN:
                if event.key == pig.K_UP or event.key == ord("w"):
                    vy = -1
                elif event.key == pig.K_DOWN or event.key == ord("s"):
                    vy = 1
                elif event.key == pig.K_LEFT or event.key == ord("a"):
                    vx = -1
                elif event.key == pig.K_RIGHT or event.key == ord("d"):
                    vx = 1
        terrain_gen.camera_x += vx
        terrain_gen.camera_y += vy
        screen.fill((0, 0, 0))
        render.render_terrain(
            screen,
            terrain_gen.width,
            terrain_gen.height,
            terrain_gen.terrain,
            terrain_gen.pos_x,
            terrain_gen.pos_y,
            terrain_gen.camera_x,
            terrain_gen.camera_y,
        )
        pig.display.flip()
        clock.tick(60)
