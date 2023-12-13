# Server code with chat functionality

import random
import socket
import threading
import pygame
import typing
import pickle


def handle_client(client_socket):
    global weather, chat_messages, screen
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        if data.decode() == "exit":
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
        #        for sock in client_sockets:
        #            if sock != client_socket:
        #                try:
        #                    sock.send(pickle.dumps(data))
        #                except socket.error as e:
        #                    # print(f"Error sending message to {sock}: {e}")
        #                    client_sockets.remove(sock)
        #
        # except:
        #    pass
        elif data.decode().startswith("MSG:"):
            message = data.decode()[4:]
            print(f"Received message: {message}")
            chat_messages.append(message)
            # if (
            #    message == "rain"
            #    or weather == "thunderstorm"
            #    or weather == "cloudy"
            #    or weather == "windy"
            # ):
            #    weather = message
            for sock in client_sockets:
                if sock != client_socket:
                    try:
                        sock.send(f"MSG:{message}".encode())
                    except socket.error as e:
                        # print(f"Error sending message to {sock}: {e}")
                        client_sockets.remove(sock)
        else:
            weather = data.decode()
            print(f"Updated weather: {weather}")
    client_socket.close()


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


def draw_rain(screen, raindrops, wind):
    for drop in raindrops:
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


def server_receive():
    global weather, chat_messages
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))
    server.listen(5)
    print("Server started, waiting for clients...")

    while True:
        client, addr = server.accept()
        print("Connected to", addr)
        client_sockets.append(client)
        for message in chat_messages:
            client.send(f"MSG:{message}".encode())
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()


def update_weather():
    global weather
    while True:
        weather = input("Enter new weather or 'exit' to quit chat: ")
        if weather.lower() == "exit":
            break
        for sock in client_sockets:
            try:
                sock.send(f"MSG:Weather updated to {weather}".encode())
            except socket.error as e:
                print(f"Error sending message to {sock}: {e}")
                client_sockets.remove(sock)


if __name__ == "__main__":
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
    client_sockets = []
    pygame.init()
    change_weather_thread = threading.Thread(target=update_weather)
    receive_thread = threading.Thread(target=server_receive)

    change_weather_thread.start()
    receive_thread.start()
    chat_messages = []
    # Define a dictionary to store usernames and corresponding client sockets
    client_usernames = {}
    input_text = ""
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Chat Server")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Send the current input_text as a chat message
                    for sock in client_sockets:
                        sock.send(f"MSG:server - {input_text}".encode())
                    chat_messages.append(input_text)
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    # Remove last character from input_text
                    input_text = input_text[:-1]
                else:
                    # Add pressed key to input_text
                    input_text += event.unicode

        screen.fill((30, 30, 30))
        input_text = render_chat(chat_messages, 400, screen, input_text)
        # if random.randint(0, 100) < 5:  # Probability of wind direction change occurring
        #    newwind = random.randint(-3, 3)  # Introduce wind for raindrops
        # if wind < newwind:
        #    wind += 0.01
        # if wind > newwind:
        #    wind -= 0.01

        # Update and draw weather effects
        # update_weatherstuff(weather, raindrops, lightning_pos, clouds, leaves, wind)
        # draw_rain(screen, raindrops, wind)
        # draw_lightning(screen, lightning_pos, lightning_duration, frame_count)
        # draw_clouds(screen, clouds)
        # draw_leaves(screen, leaves)
        # clock.tick(60)
        pygame.display.flip()
