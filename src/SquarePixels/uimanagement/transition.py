from random import choice, randint, uniform
import sys
from SquarePixels.uimanagement.clouds import Cloud
import pygame

infoObject: object = pygame.display.Info()
# Initial position of the background
bg_x, bg_y = 0, 0

backround = pygame.transform.scale(
    pygame.image.load(r"Recources\ui\mainmen\background\cover.png"),
    (infoObject.current_w + 100, infoObject.current_h + 80),
)


def transition(screen):
    global bg_x, bg_y
    black_rectangles = []

    x, y = pygame.mouse.get_pos()

    # Calculate the offset for the panoramic effect
    offset_x = (infoObject.current_w / 2 - x) / 20
    offset_y = (infoObject.current_h / 2 - y) / 20

    # Apply smoothing to gradually move toward the target position
    smoothing_factor = 0.1
    bg_x += (offset_x - bg_x) * smoothing_factor
    bg_y += (offset_y - bg_y) * smoothing_factor
    clouds = []
    # Blit the background with the calculated offset
    screen.blit(backround, (round(-50 - bg_x), round(-50 - bg_y)))

    # Load cloud images
    cloud_images = [
        pygame.transform.scale(
            pygame.image.load(r"Recources\ui\mainmen\background\clouds1.png"),
            (infoObject.current_w / 4, infoObject.current_h / 4),
        ),
        pygame.transform.scale(
            pygame.image.load(r"Recources\ui\mainmen\background\clouds2.png"),
            (infoObject.current_w / 4, infoObject.current_h / 4),
        ),
    ]
    while len(clouds) <= 50:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        cloud_image = choice(cloud_images)
        cloud_x = randint(0, infoObject.current_w)
        cloud_y = randint(0, infoObject.current_h)
        cloud_speed = uniform(1, 20)  # Random speed between 1 and 4
        new_cloud = Cloud(cloud_x, cloud_y, cloud_image, cloud_speed)
        clouds.append(new_cloud)

        # Remove clouds that are off-screen
        for cloud in clouds:
            if cloud.image == cloud_images[1]:
                if cloud.x <= -300:
                    clouds.remove(cloud)
            else:
                if cloud.x <= -500:
                    clouds.remove(cloud)

        # Move and draw clouds
        for cloud in clouds:
            cloud.move()
            cloud.draw(screen)
        pygame.display.update()
        pygame.display.flip()
    ## Fill the screen with black rectangles
    # for x in range(infoObject.current_w // 250 + 50):
    #    for y in range(infoObject.current_h // 250 + 50):
    #        black_rect = pygame.Rect((x * 250, y * 250, 250, 250))
    #        black_rectangles.append(black_rect)
    # while len(black_rectangles) > 0:
    #    for event in pygame.event.get():
    #        if event.type == pygame.QUIT:
    #            pygame.quit()
    #            sys.exit()
    #    i = randint(0, len(black_rectangles) - 1)
    #    pygame.draw.rect(screen, (0,0,0), black_rectangles[i])
    #    black_rectangles.pop(i)
    #    pygame.display.update()
    #    pygame.display.flip()
