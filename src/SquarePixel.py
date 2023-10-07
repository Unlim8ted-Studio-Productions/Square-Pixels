if __name__ == "__main__":
    import pygame as pig
    import terrain_gen as tgen
    import logo
    import player as pl
    from Character_creation import main
    from game import game

    tile = [-1, 0]

    pig.init()
    clock: object = pig.time.Clock()
    not_skipped: bool = True
    reset_terrain: bool = False
    clicked: bool = False
    # Path to your video file
    video_file: str = r"terraria_styled_game\\Company Animated Logo.mov"
    infoObject: object = pig.display.Info()
    screen: pig.Surface = pig.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    pygame_icon = pig.image.load(
        r"terraria_styled_game\program recources\Screenshot 2023-09-21 181742.png"
    )
    pig.display.set_icon(pygame_icon)
    # pig.display.toggle_fullscreen()
    pig.display.set_caption("Square Pixel")
    pig.mouse.set_cursor(pig.SYSTEM_CURSOR_CROSSHAIR)
    # Path to the folder to save the extracted frames
    image_folder: str = r"terraria_styled_game\\frames"
    colliders: list = []
    # Extract frames from the video
    # logo.extract_frames(video_file, image_folder)
    vx, vy = 0, 0  # infoObject.current_w/2, 0#infoObject.current_h /2
    # Call the function to play the video
    logo.play_intro_video(image_folder, not_skipped, screen, 0)
    image_folder: str = r"terraria_styled_game\\NewHorizonsFrames"
    logo.play_intro_video(image_folder, not_skipped, screen, 1)
    import MainMen

    MainMen.mainfunc()
    # Rest of game code goes here...
    terrain_gen = tgen.TerrainGenerator(
        width=(0, infoObject.current_w // 10), height=infoObject.current_h // 15
    )
    terrain_gen.run(screen)
    player_sprite = main()
    player = pl.Player(vx, vy)
    DayTime = 0
    Morning = 0

    # world:object = tgen.generate()
    # for square in world.tiles:
    #    render.draw(screen, square)
    # print(terrain_gen.terrain)
    # quit()
    # rect=pig.Rect((0,0),(infoObject.current_w,infoObject.current_h))
    running = True
    game(
        screen,
        running,
        terrain_gen,
        player,
        infoObject,
        player_sprite,
        clock,
        vx,
        vy,
        reset_terrain,
        Morning,
        DayTime,
        tile,
    )
