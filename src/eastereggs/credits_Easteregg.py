import pygame
import sys
import random
from collections import deque
from soundmanagement.music import play_music


# Function to generate a random maze using Recursive Backtracking algorithm
def generate_maze(WIDTH, CELL_SIZE, HEIGHT):
    maze = [
        ["#" for _ in range(WIDTH // CELL_SIZE)] for _ in range(HEIGHT // CELL_SIZE)
    ]
    visited = set()

    def can_visit(x, y):
        return (
            0 < x < WIDTH // CELL_SIZE - 1
            and 0 < y < HEIGHT // CELL_SIZE - 1
            and maze[y][x] == "#"
        )

    def carve_path(x, y):
        maze[y][x] = " "
        visited.add((x, y))

        directions = [(x + 2, y), (x - 2, y), (x, y + 2), (x, y - 2)]
        random.shuffle(directions)

        for nx, ny in directions:
            if (nx, ny) not in visited and can_visit(nx, ny):
                maze[(y + ny) // 2][(x + nx) // 2] = " "
                carve_path(nx, ny)

    start_x, start_y = (
        random.randint(1, WIDTH // (2 * CELL_SIZE)) * 2 - 1,
        random.randint(1, HEIGHT // (2 * CELL_SIZE)) * 2 - 1,
    )
    carve_path(start_x, start_y)

    return maze


# Breadth-First Search (BFS) Pathfinding
def bfs(maze, start, goal):
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()

        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if (
                0 <= neighbor[0] < len(maze[0])
                and 0 <= neighbor[1] < len(maze)
                and maze[neighbor[1]][neighbor[0]] != "#"
            ):
                queue.append((neighbor, path + [neighbor]))

    return None


def start():
    # Initialize Pygame
    pygame.init()
    infoObject: object = pygame.display.Info()
    screen: pygame.Surface = pygame.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    pygame_icon = pygame.image.load(
        r"terraria_styled_game\program recources\Screenshot 2023-09-21 181742.png"
    )
    pygame.display.set_icon(pygame_icon)

    # Constants
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    WHITE = (0, 0, 0)
    RED = (255, 0, 0)
    CELL_SIZE = 40

    # Create the screen

    # pygame.display.toggle_fullscreen()
    pygame.display.set_caption("Square Pixel")
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

    # Player
    player = pygame.Rect(40, 40, CELL_SIZE // 2, CELL_SIZE // 2)

    # Goal
    goal = pygame.Rect(680, 440, CELL_SIZE, CELL_SIZE)
    maze = generate_maze(WIDTH, CELL_SIZE, HEIGHT)

    # Game loop
    running = True
    won = False
    credits_font = pygame.font.Font(
        "terraria_styled_game\Fonts\PixelifySans-Regular.ttf", 50
    )
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                return None

        # Get the current mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Calculate the path from player to mouse using BFS algorithm
        start_pos = (player.centerx // CELL_SIZE, player.centery // CELL_SIZE)
        goal_pos = (mouse_x // CELL_SIZE, mouse_y // CELL_SIZE)
        path = bfs(maze, start_pos, goal_pos)

        if path:
            # Move player towards the next position in the path
            next_pos = path[1] if len(path) >= 2 else path[0]
            dx = (next_pos[0] * CELL_SIZE + CELL_SIZE / 2) - player.centerx
            dy = (next_pos[1] * CELL_SIZE + CELL_SIZE / 2) - player.centery
            length = max(1, (dx**2 + dy**2) ** 0.5)
            dx /= length
            dy /= length
            player.x += dx
            player.y += dy

        # Check if player reaches the goal
        if player.colliderect(goal):
            won = True

        # Clear the screen
        screen.fill(WHITE)

        # Draw maze, player, and goal
        if not won:
            for y, row in enumerate(maze):
                for x, cell in enumerate(row):
                    if cell == "#":
                        pygame.draw.rect(
                            screen,
                            RED,
                            (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
                        )

        pygame.draw.rect(screen, (200, 231, 193), player)
        pygame.draw.rect(screen, (123, 143, 233), goal)
        text_surface = credits_font.render(
            "press anything to escape", True, (100, 100, 100)
        )
        screen.blit(
            text_surface,
            (
                WIDTH // 4 - text_surface.get_width() // 2,
                HEIGHT - 50,
            ),
        )
        pygame.display.flip()

        # Scroll credits down the screen if the player won
        if won:
            play_music(r"terraria_styled_game\sounds\music\EndCredits.mp3")
            text_surface = credits_font.render(
                "press anything to skip", True, (100, 100, 100)
            )
            screen.blit(
                text_surface,
                (
                    WIDTH // 4 - text_surface.get_width() // 2,
                    HEIGHT - 50,
                ),
            )
            credits_y = HEIGHT
            credits_text = [
                "Congratulations! You won!",
                "Credits:",
                "Game developed by [Augustus R. Angelides]",
                "Block Artwork by [Sam Cook]",
                "Creature Artwork by [Finn]",
                "Music by [Finn]",
                "Sounds by [Augustus R. Angelides]",
                "Software Developers: [Teo, Augustus R. Angelides]",
                "Playtesters: [Augustus R. Angelides, Ada, Abe]",
                "Music from #Uppbeat (free for Creators!):",
                "https://uppbeat.io/t/michael-grubb/threshold",
                "License code: AVGIIL4ZOS36UYVZ ",
                "Music from #Uppbeat (free for Creators!):",
                "https://uppbeat.io/t/kevin-macleod/cyborg-ninja",
                "License code: CYD3DXMQBEOXDEAY",
            ]
            credits_font = pygame.font.Font(None, 36)

            while credits_y >= -len(credits_text) * 40 and won:
                screen.fill(WHITE)
                for i, text in enumerate(credits_text):
                    text_surface = credits_font.render(text, True, RED)
                    screen.blit(
                        text_surface,
                        (
                            WIDTH // 2 - text_surface.get_width() // 2,
                            credits_y + i * 40,
                        ),
                    )
                pygame.display.flip()
                credits_y -= 2
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        won = False
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        return None
                pygame.time.delay(50)
            if not credits_y >= -len(credits_text) * 40:
                return None

    # Quit Pygame
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    start()
