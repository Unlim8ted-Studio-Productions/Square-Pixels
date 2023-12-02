import SquarePixels.render.render as render
import pygame as pig
import SquarePixels.enemymanagement.enemy_manager as enemy_manager
from SquarePixels.uimanagement import death, MainMen
import SquarePixels.soundmanagement.music as music
import random

hidden_area = []


def game(
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
):
    music.play_music(r"Recources\sounds\music\ingame\music\Ingame1.mp3", volume=0.2)
    enemymanager = enemy_manager.Enemy_manager([(0, infoObject.current_w)])
    while running:
        clicked = False
        if reset_terrain:
            terrain_gen.run(screen)
            reset_terrain = False
        # pig.draw.rect(screen,(.100,.100,.100,50),rect)
        screen.fill((0.035, 206, 235))

        if Morning == 0:
            DayTime = DayTime + 0.005
        else:
            DayTime = DayTime - 0.005
            if DayTime <= 0:
                Morning = 0
        sky, colliders, hidden_area = render.render_terrain(
            screen,
            terrain_gen.width,
            terrain_gen.height,
            terrain_gen.terrain,
            terrain_gen.pos_x,
            terrain_gen.pos_y,
            terrain_gen.camera_x,
            terrain_gen.camera_y,
            player,
            DayTime,
            Morning,
        )

        if DayTime > 6.5:
            Morning = 1
        result = player.move(screen, infoObject, tile, terrain_gen.terrain)
        if result != None:
            if len(result) <= 5:
                reset_terrain = result[0]
                clicked = result[1]
                try:
                    objectheld = result[2]
                except:
                    pass
            else:
                terrain_gen.terrain = result
        tile = [-1, 0]
        if clicked:
            if random.randint(0, 1) == 1:
                music.play_music(
                    r"Recources\sounds\block break\block break.mp3",
                    0,
                    channel=1,
                    volume=5,
                )
            else:
                music.play_music(
                    r"Recources\sounds\block break\blockbreak1.mp3",
                    0,
                    channel=1,
                    volume=5,
                )
            tile = player.delete_tile(terrain_gen.terrain, tile)
        player.update(
            infoObject.current_h, infoObject.current_w, colliders, screen
        )  # terrain_gen.colliders)
        enemymanager.update(
            player.x, player.y, sky, infoObject, colliders, screen, player, Morning
        )
        if player.current_health <= 0:
            if death.draw_death_screen(
                screen, infoObject.current_w, infoObject.current_h, player.xp
            ):
                player.respawn(sky, infoObject, [(0, infoObject.current_w)])
            else:
                player.respawn(sky, infoObject, [(0, infoObject.current_w)])
                MainMen.mainfunc()
        terrain_gen.camera_x += vx
        terrain_gen.camera_y += vy
        player.draw(screen, player_sprite)
        # print(player.xp)
        # player.draw_trail(screen)
        pig.display.flip()
        clock.tick(60)
