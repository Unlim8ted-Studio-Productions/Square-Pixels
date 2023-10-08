import pygame as pig


def draw_death_screen(screen, width, height):
    clock: object = pig.time.Clock()
    death_text = pig.font.Font(
        "terraria_styled_game\Fonts\PixelifySans-Regular.ttf", 50
    )
    d_text = death_text.render("You Died", True, (255, 255, 255))
    death_text_rect = d_text.get_rect(center=(width // 2, height // 3))
    # Define buttons
    respawn_button = pig.Rect(width // 4, height // 2, 200, 50)
    menu_button = pig.Rect(3 * width // 4, height // 2, 200, 50)
    while True:
        for event in pig.event.get():
            if event.type == pig.QUIT:
                pig.quit()
                quit()
        screen.fill((0, 0, 0))
        screen.blit(d_text, death_text_rect)
        # Check if the mouse is hovering over the buttons
        if respawn_button.collidepoint(pig.mouse.get_pos()):
            pig.draw.rect(screen, (150, 150, 150), respawn_button)
            respawn_text = death_text.render("Respawn", True, (0, 0, 0))
            respawn_text_rect = respawn_text.get_rect(center=respawn_button.center)
            screen.blit(respawn_text, respawn_text_rect)
        else:
            pig.draw.rect(screen, (255, 255, 255), respawn_button)
            respawn_text = death_text.render("Respawn", True, (0, 0, 0))
            respawn_text_rect = respawn_text.get_rect(center=respawn_button.center)
            screen.blit(respawn_text, respawn_text_rect)

        if menu_button.collidepoint(pig.mouse.get_pos()):
            pig.draw.rect(screen, (150, 150, 150), menu_button)
            menu_text = death_text.render("Main Menu", True, (0, 0, 0))
            menu_text_rect = menu_text.get_rect(center=menu_button.center)
            screen.blit(menu_text, menu_text_rect)
        else:
            pig.draw.rect(screen, (255, 255, 255), menu_button)
            menu_text = death_text.render("Main Menu", True, (0, 0, 0))
            menu_text_rect = menu_text.get_rect(center=menu_button.center)
            screen.blit(menu_text, menu_text_rect)
        pig.display.flip()
        clock.tick(60)
