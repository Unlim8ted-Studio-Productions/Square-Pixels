import pygame
from pygame import RESIZABLE
import socket
import threading
import ipaddress
import client

SERVER_PORT = 12345
TIMEOUT = 1.0  # Timeout value for socket operations
SCAN_TIMEOUT = 2.0  # Timeout value for server scanning
SCAN_THREADS = 50  # Number of threads for concurrent scanning
pygame.init()
infoObject: object = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
BACKGROUND_COLOR = (255, 255, 255)
TEXT_COLOR = (0, 0, 0)
ip = ""
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), RESIZABLE)
pygame.display.set_caption("Server Finder")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 24)

running = True
servers = []
selected_server = None
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
    global running
    if running:
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
    global player_name, character_image, input_text, settings

    input_rect = pygame.Rect(10, 400, 200, 30)
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
                        client.main(ip, input_text)
                        player_name = input_text
                        # character_image = ...  # Save the selected character image
                        print("Player Name:", player_name)
                        print("Character Image:", character_image)
                        pygame.quit()
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

    pygame.quit()


if __name__ == "__main__":
    find_servers()
    main()
