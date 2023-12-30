# Server code with chat functionality

import ctypes
import random
import socket
import threading
import pygame
import typing
import pickle
import win32con
import win32gui


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


def server_receive():
    global weather, chat_messages, client_sockets
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Server started, waiting for clients...")

    while True:
        client, addr = server.accept()
        print("Connected to", addr)
        client_sockets.append(client)
        for message in chat_messages:
            client.send(f"MSG:{message}".encode())
            pygame.time.delay(100)

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
                sock.send(f"MSG: Weather updated to {weather}".encode())
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
    # change_weather_thread = threading.Thread(target=update_weather)
    receive_thread = threading.Thread(target=server_receive)

    # change_weather_thread.start()
    receive_thread.start()
    chat_messages = []
    # Define a dictionary to store usernames and corresponding client sockets
    client_usernames = {}
    input_text = ""
    screen = pygame.display.set_mode((400, 400))

    pygame.display.set_caption("Chat Server")
    running = True
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
                    for sock in client_sockets:
                        sock.send(f"MSG: server - {input_text}".encode())
                    chat_messages.append(f"server - {input_text}")
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
