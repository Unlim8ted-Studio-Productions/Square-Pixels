from ast import Tuple
import pygame as pig
import terrain_gen as tgen
import render
import typing as tp
import logo
import player as pl


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
    colliders = []
    # Extract frames from the video
    # logo.extract_frames(video_file, image_folder)
    vx, vy = 0,0#infoObject.current_w/2, 0#infoObject.current_h /2
    # Call the function to play the video
    logo.play_intro_video(image_folder, not_skipped, screen)

    # Rest of game code goes here...
    terrain_gen = tgen.TerrainGenerator( width = (0,infoObject.current_h // 5), height= infoObject.current_h // 10)
    terrain_gen.run(screen)
    player = pl.Player(vx,vy)
    # world:object = tgen.generate()
    # for square in world.tiles:
    #    render.draw(screen, square)
    #print(terrain_gen.terrain)
    #quit()
    running = True
    while running:
        for event in pig.event.get():
            if event.type == pig.QUIT:
                running = False
        screen.fill((0, 0, 0))
        colliders = render.render_terrain(
            screen,
            terrain_gen.width,
            terrain_gen.height,
            terrain_gen.terrain,
            terrain_gen.pos_x,
            terrain_gen.pos_y,
            terrain_gen.camera_x,
            terrain_gen.camera_y,
        )
        player.move(infoObject.current_h)
        player.delete_tile(terrain_gen.terrain)
        player.update(infoObject.current_h, infoObject.current_w, colliders)#terrain_gen.colliders)
        terrain_gen.camera_x += vx
        terrain_gen.camera_y += vy
        player.draw(screen)
        player.draw_trail(screen)
        pig.display.flip()
        clock.tick(60)
