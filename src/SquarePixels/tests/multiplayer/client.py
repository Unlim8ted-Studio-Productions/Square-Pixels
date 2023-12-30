import ctypes
import random
import socket
import threading
import pygame
import typing
import pickle
import win32con
import win32gui

ipp = ""
import pygame
from pygame import RESIZABLE
import socket
import threading
import ipaddress

SERVER_PORT = 9999
TIMEOUT = 1.0  # Timeout value for socket operations
SCAN_TIMEOUT = 2.0  # Timeout value for server scanning
SCAN_THREADS = 50  # Number of threads for concurrent scanning
pygame.init()
infoObject: object = pygame.display.Info()
WIDTH, HEIGHT = 400, 400
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
ip = ""
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("chat client")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

running = True
servers = []
selected_server = None
usernamee = ""
input_text = "Name"
settings = True


def check_server(server_ip):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            result = sock.connect_ex((server_ip, SERVER_PORT))
            if result == 0 and server_ip not in servers:
                servers.append(server_ip)
    except:
        pass


def scan_servers(ip_range):
    network = ipaddress.ip_network(ip_range)
    for ip_address in network.hosts():
        server_ip = str(ip_address)
        threading.Thread(target=check_server, args=(server_ip,)).start()


def find_servers():
    global running, ipp
    if running and ipp == "":
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        network = ipaddress.ip_network(ip_address, strict=False)
        ip_range = f"{network.network_address}/{network.prefixlen}"

        print("Automatically selected IP range:", ip_range)
        print("Scanning for servers...")
        scan_servers(ip_range)

        threading.Timer(SCAN_TIMEOUT, find_servers).start()


def draw_text(text, x, y):
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)


def handle_server_click(selected_server):
    if selected_server is not None:
        # Perform actions based on the selected server
        print("Clicked on server:", selected_server)
        ip = selected_server
        # client.main(selected_server)
        handle_server_options(ip)


def handle_server_options(ip) -> None:
    global player_name, character_image, input_text, settings, usernamee

    input_rect = pygame.Rect(10, 40, 200, 30)
    character_rect = pygame.Rect(220, 400, 100, 100)
    input_active = True

    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if input_rect.collidepoint(event.pos):
                        input_active = True
                    else:
                        input_active = False
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_RETURN:
                        # Save the player name and character image
                        settings = False
                        global ipp
                        ipp = ip
                        player_name = input_text
                        usernamee = input_text
                        # character_image = ...  # Save the selected character image
                        print("Player Name:", player_name)
                        # print("Character Image:", character_image)
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

        screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(screen, (200, 200, 200), input_rect, 2)

        if input_active:
            pygame.draw.rect(screen, (200, 200, 200), input_rect, 0)

        input_surface = font.render(input_text, True, TEXT_COLOR)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.draw.rect(screen, (200, 200, 200), character_rect, 2)
        # Draw the selected character image in the character_rect

        pygame.display.flip()
        clock.tick(60)


def main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                quit()

        screen.fill(BACKGROUND_COLOR)
        draw_text("Found Servers:", 10, 10)
        global ipp
        if ipp != "":
            not running
        for i, server in enumerate(servers):
            text = f"Server {i+1}: {server}"
            text_surface = font.render(text, True, TEXT_COLOR)
            text_rect = text_surface.get_rect()
            text_rect.topleft = (10, 40 + i * 30)
            if text_rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (200, 200, 200), text_rect)
                if pygame.mouse.get_pressed()[0]:
                    selected_server = server
                    running = False
                    handle_server_click(selected_server)
            screen.blit(text_surface, text_rect)

        pygame.display.flip()
        clock.tick(60)


import pygame
import random


def draw_rain(screen, raindrops, wind):
    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
    threshold_distance = 100  # Threshold distance for mouse effect

    for drop in raindrops:
        dx = drop[0] - mouse_x  # Difference in x
        dy = drop[1] - mouse_y  # Difference in y
        distance = (dx**2 + dy**2) ** 0.5  # Calculate distance
        try:
            if distance < threshold_distance:
                # Move raindrop away from the mouse
                avoidance_strength = (
                    threshold_distance - distance
                ) / threshold_distance
                drop[0] += (dx / distance) * avoidance_strength * 2
                drop[1] += (dy / distance) * avoidance_strength * 2
        except:
            pass

        # Update raindrop position based on wind
        drop[0] += wind + random.uniform(-0.1, 0.1)
        drop[1] += 5  # Move down
        drop[2] -= 5  # Decrease opacity

        # Draw semi-transparent line for a blur effect
        pygame.draw.aaline(
            screen,
            (
                random.randint(0, 20),
                random.randint(0, 220),
                random.randint(220, 255),
                drop[2],
            ),
            (drop[0], drop[1]),
            (drop[0], drop[1] + 5),
        )

    # Remove raindrops that have moved out of the screen or faded completely
    raindrops[:] = [drop for drop in raindrops if drop[1] < 400 and drop[2] > 0]


def draw_lightning(screen, lightning_pos, lightning_duration, frame_count):
    if frame_count < lightning_duration:
        # Draw lightning
        pygame.draw.line(screen, (255, 255, 255), lightning_pos[0], lightning_pos[1], 2)

        # Simulate flash by adding a transparent white surface
        flash_surface = pygame.Surface((400, 400), pygame.SRCALPHA)
        flash_surface.fill(
            (255, 255, 255, min(100, frame_count * 10))
        )  # Adjust the transparency level
        screen.blit(flash_surface, (0, 0))

    else:
        # Fading out the lightning effect
        fade_out = min(255, max(0, 255 - (frame_count - lightning_duration) * 5))
        pygame.draw.line(
            screen, (255, 255, 255, fade_out), lightning_pos[0], lightning_pos[1], 2
        )


def draw_clouds(screen, clouds):
    for cloud in clouds:
        pygame.draw.ellipse(screen, (255, 255, 255), cloud)


def draw_leaves(screen, leaves):
    for leaf in leaves:
        pygame.draw.ellipse(screen, (34, 139, 34), leaf)


def update_weatherstuff(weather, raindrops, lightning_pos, clouds, leaves, wind):
    if weather == "rain":
        for i in range(10):
            # Initialize raindrop with random position and full opacity
            raindrops.append(
                [
                    random.randint(0, 400),
                    random.randint(0, 400),
                    255,
                ]
            )
    elif weather == "thunderstorm":
        if random.randint(0, 100) < 5:  # Probability of lightning occurring
            lightning_pos[0] = (random.randint(0, 400), 0)
            lightning_pos[1] = (
                random.randint(0, 400),
                400,
            )
            frame_count = 0  # Reset frame count for lightning duration
        for i in range(10):
            # Initialize raindrop with random position and full opacity
            raindrops.append(
                [
                    random.randint(0, 400),
                    random.randint(0, 400),
                    255,
                ]
            )

    elif weather == "cloudy":
        for i in range(5):
            cloud_size = random.randint(50, 100)
            cloud = pygame.Rect(
                random.randint(0, 400),
                random.randint(0, 400),
                cloud_size,
                cloud_size,
            )
            clouds.append(cloud)
    elif weather == "windy":
        for i in range(5):
            leaf_size = random.randint(5, 20)
            leaf = pygame.Rect(
                random.randint(0, 400),
                random.randint(0, 400),
                leaf_size,
                leaf_size,
            )
            leaves.append(leaf)


def receive_weather(client_socket, chat_messages):
    global weather
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        # try:
        #    if isinstance(pickle.loads(data), []):
        #        data = pickle.loads(data)
        #        user = data[0]
        #        pos = data[1]
        #        pygame.draw.rect(screen, (255, 255, 255), (*pos, 20, 20))
        #        font = pygame.font.Font(None, 20)
        #        text = font.render(user, True, (255, 255, 255))
        #        text_rect = text.get_rect(*pos)
        #        screen.blit(text, text_rect)
        #        pygame.display.update()
        #
        # except:
        #    pass
        if data.decode().startswith("MSG:"):
            message = data.decode()[4:]
            chat_messages.append(message)
            # if (
            #    message == "rain"
            #    or weather == "thunderstorm"
            #    or weather == "cloudy"
            #    # or weather == "windy"
            # ):
            #    weather = message
            print(f"Received message: {message}")


def render_chat(
    chat_messages: typing.List[str],
    screen_height: int,
    screen: pygame.Surface,
    input_text: str = "",
    input_active: bool = False,
) -> str:
    # Render the chat messages
    font = pygame.font.Font(None, 20)
    input_font = pygame.font.Font(None, 24)
    input_rect = pygame.Rect(10, screen_height - 30, 300, 25)

    for i, message in enumerate(chat_messages):
        text = font.render(message, True, (255, 255, 255))
        if 10 + i * 20 >= screen_height - 30:
            save = chat_messages[i]
            i = 0
            chat_messages.clear()
            chat_messages.append(save)
            text_rect = text.get_rect(left=10, top=10 + i * 20)
            screen.blit(text, text_rect)
        else:
            text_rect = text.get_rect(left=10, top=10 + i * 20)
            screen.blit(text, text_rect)

    # Render the input box and text
    pygame.draw.rect(screen, (200, 200, 200), input_rect, 2)
    input_surface = input_font.render(input_text, True, (255, 255, 255))
    screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

    return input_text  # Return the updated input text


def client_program(ipp):
    global weather, raindrops, lightning_pos, clouds, leaves, wind, screen, lightning_pos, lightning_duration, frame_count, clouds, leaves, newwind, username
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((ipp, 9999))

    chat_messages = []

    receive_thread = threading.Thread(
        target=receive_weather,
        args=(
            client,
            chat_messages,
        ),
    )

    receive_thread.start()

    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    # Get the window ID
    hwnd = pygame.display.get_wm_info()["window"]

    # Set the window as always on top
    ctypes.windll.user32.SetWindowPos(hwnd, -1, 0, 0, 0, 0, 0x0001 | 0x0002 | 0x0040)
    pygame.display.set_caption("Chat Client")
    clock = pygame.time.Clock()
    client.send(f"MSG: {username} has connected to the server".encode())
    chat_messages.append(f"{username} has connected to the server")
    input_text = ""

    running = True
    # chat_messages.append(
    #    "type rain, thunderstorm, cloudy, or windy to change the weather"
    # )
    while running:
        hwnd = pygame.display.get_wm_info()["window"]
        win32gui.SetWindowPos(
            hwnd,
            win32con.HWND_TOPMOST,
            0,
            0,
            0,
            0,
            win32con.SWP_NOMOVE | win32con.SWP_NOSIZE,
        )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Send the current input_text as a chat message
                    client.send(f"MSG: {username} - {input_text}".encode())
                    chat_messages.append(f"{username} - {input_text}")
                    # if (
                    #    input_text == "rain"
                    #    or weather == "thunderstorm"
                    #    or weather == "cloudy"
                    #    # or weather == "windy"
                    # ):
                    #    weather = input_text
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    # Remove last character from input_text
                    input_text = input_text[:-1]
                else:
                    # Add pressed key to input_text
                    input_text += event.unicode

        # client.send(pickle.dumps(["username", [20, 20]]))

        screen.fill((30, 30, 30))
        input_text = render_chat(chat_messages, 400, screen, input_text)
        if random.randint(0, 100) < 5:  # Probability of wind direction change occurring
            newwind = random.randint(-3, 3)  # Introduce wind for raindrops
        if wind < newwind:
            wind += 0.01
        if wind > newwind:
            wind -= 0.01

        # Update and draw weather effects
        update_weatherstuff(weather, raindrops, lightning_pos, clouds, leaves, wind)
        draw_rain(screen, raindrops, wind)
        # draw_lightning(screen, lightning_pos, lightning_duration, frame_count)
        # draw_clouds(screen, clouds)
        # draw_leaves(screen, leaves)
        pygame.display.flip()
        clock.tick(60)
    client.send(f"MSG: {username} has left the server".encode())
    client.close()


def customip():
    global ipp, running, username
    ipp = input("type a custom ip")
    username = input("type a custom username")
    running = False


if __name__ == "__main__":
    inputc = threading.Thread(target=customip)
    inputc.start()
    find_servers()
    main()
    pygame.init()
    # umbrella_cursor = pygame.image.load("umbrella.png")
    # umbrella_cursor = pygame.transform.scale(
    #    umbrella_cursor, (32, 32)
    # )  # Scale it to the desired cursor size
    ipp = socket.gethostbyaddr(ipp)[0]
    ipp = ipp.split(".")[0]
    print(ipp)
    username = (
        usernamee
        + f"{random.randrange(0, 10, 1)}"
        + f"{random.randrange(0, 10, 1)}"
        + f"{random.randrange(0, 10, 1)}"
    )
    clock = pygame.time.Clock()
    frame_count = 0  # Count frames for lightning duration
    lightning_duration = 10  # Adjust the duration of the lightning effect
    raindrops = []
    lightning_pos = [(0, 0), (0, 0)]
    clouds = []
    leaves = []
    wind = 0
    newwind = 0
    weather = "thunderstorm"  # Initial weather
    client_program(ipp)
