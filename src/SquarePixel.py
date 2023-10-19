if __name__ == "__main__":
    import pygame as pig
    import terraingen.terrain_gen as tgen
    import uimanagement.logo as logo
    import player.player as pl
    from uimanagement.Character_creation import main
    from game.game import game
    import uimanagement.MainMen as MainMen
    from soundmanagement.music import play_music

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
    play_music(r"terraria_styled_game\sounds\music\Menu.mp3")
    MainMen.mainfunc()
    # Rest of game code goes here...
    terrain_gen = tgen.TerrainGenerator(
        width=(0, infoObject.current_w // 10), height=infoObject.current_h // 15
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
