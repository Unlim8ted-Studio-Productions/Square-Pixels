import render
import pygame as pig


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
    enemyx = 200
    enemyy = 500
    while running:
        clicked = False
        if reset_terrain:
            terrain_gen.run(screen)
        # pig.draw.rect(screen,(.100,.100,.100,50),rect)
        screen.fill((0.035, 206, 235))

        if Morning == 0:
            DayTime = DayTime + 0.005
        else:
            DayTime = DayTime - 0.005
            if DayTime <= 0:
                Morning = 0
        colliders = render.render_terrain(
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
            reset_terrain = result[0]
            clicked = result[1]
            try:
                objectheld = result[2]
            except:
                pass
        tile = [-1, 0]
        if clicked:
            tile = player.delete_tile(terrain_gen.terrain, tile)
        player.update(
            infoObject.current_h, infoObject.current_w, colliders
        )  # terrain_gen.colliders)
        for block in colliders:
            if enemyx < player.x:
                if not block.collidepoint(enemyx + 0.01, enemyy - 16):
                    enemyy += 0.01
                if not block.collidepoint(
                    (enemyx + 0.01, enemyy)
                ) and block.collidepoint((enemyx + 0.01, enemyy + 16)):
                    enemyx += 0.01
                else:
                    if not block.collidepoint((enemyx + 0.01, enemyy + 16)):
                        enemyy -= 0.01
                        enemyx += 0.01
            else:
                if not block.collidepoint(
                    (enemyx - 0.01, enemyy)
                ) and block.collidepoint((enemyx - 0.01, enemyy + 16)):
                    enemyx -= 0.01
                else:
                    if not block.collidepoint((enemyx + 0.01, enemyy + 16)):
                        enemyy -= 0.01
                        enemyx -= 0.01
        pig.draw.rect(screen, (200, 0, 0), (enemyx, enemyy, 20, 20))
        terrain_gen.camera_x += vx
        terrain_gen.camera_y += vy
        player.draw(screen, player_sprite)
        # player.draw_trail(screen)
        pig.display.flip()
        clock.tick(60)
