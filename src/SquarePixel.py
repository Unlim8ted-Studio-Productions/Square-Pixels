if __name__ == "__main__":
    import pygame as pig
    from SquarePixels.terraingen import terrain_gen as tgen
    from SquarePixels.uimanagement import logo, MainMen
    from SquarePixels.uimanagement.window import start
    from SquarePixels.player import player as pl
    from SquarePixels.uimanagement.Character_creation import main
    from SquarePixels.game.game import game
    from SquarePixels.soundmanagement.music import play_music

    tile = [-1, 0]

    pig.init()
    clock: object = pig.time.Clock()
    not_skipped: bool = True
    reset_terrain: bool = False
    clicked: bool = False
    # Path to your video file
    video_file: str = r"Recources\\Company Animated Logo.mov"
    infoObject: object = pig.display.Info()
    screen: pig.Surface = pig.display.set_mode(
        (infoObject.current_w, infoObject.current_h - 32), pig.RESIZABLE
    )

    pygame_icon = pig.image.load(
        r"Recources\program recources\Screenshot 2023-09-21 181742.png"
    )
    pig.display.set_icon(pygame_icon)  # pig.display.toggle_fullscreen()

    pig.display.set_caption("Square Pixel")
    pig.mouse.set_cursor(pig.SYSTEM_CURSOR_CROSSHAIR)
    # Path to the folder to save the extracted frames
    image_folder: str = r"Recources\\frames"
    colliders: list = []
    # Extract frames from the video
    # logo.extract_frames(video_file, image_folder)
    vx, vy = 0, 0  # infoObject.current_w/2, 0#infoObject.current_h /2
    # Call the function to play the video
    logo.play_intro_video(image_folder, not_skipped, screen, 0)
    # start()
    screen: pig.Surface = pig.display.set_mode(
        (infoObject.current_w, infoObject.current_h - 32), pig.RESIZABLE
    )
    image_folder: str = r"Recources\\NewHorizonsFrames"
    logo.play_intro_video(image_folder, not_skipped, screen, 1)
    play_music(r"Recources\sounds\music\Menu.mp3")
    with open(r"Recources\data\first.txt", "r") as first:
        bool_value = first.readlines()
        if bool(bool_value[0]):
            import SquarePixels.uimanagement.EllipsesWarning

            # with open(r"Recources\data\first.txt", "w") as first:3423434234234
            #    None564523454324324
            #    first.write("False") disabled for developmental purposes423423423423

    MainMen.mainfunc()
    # Rest of game code goes here...
    terrain_gen = tgen.TerrainGenerator(
        width=(-100, infoObject.current_w // 15), height=infoObject.current_h // 15
    )
    player_sprite = main()
    terrain_gen.generate_terrain(screen)
    player = pl.Player(vx, vy, infoObject.current_w - 40, 0)
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
