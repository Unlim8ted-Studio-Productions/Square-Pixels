import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
NODE_RADIUS = 20
NODE_COLOR = (100, 100, 100)
LINE_COLOR = (255, 255, 255)
CONNECTION_COLOR = (255, 255, 0)
CONNECTION_WIDTH = 2
TEXT_COLOR = (0, 0, 255)  # Blue for node labels

# Node types and their labels
node_types = [
    {"label": "Remove Object", "action": "remove"},
    {"label": "Add Object", "action": "add"},
    {"label": "Reveal Object", "action": "reveal"},
    {"label": "Hide Object", "action": "hide"},
    {"label": "Move Object", "action": "move"},
    {"label": "Function", "action": "Script"},
    {"label": "If", "action": "if"},
    {"label": "is_clicked", "action": "clicked"},
]

# Create a Pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Node Editor")

# List to store nodes and connections
nodes = []
connections = []
start_node = {"type": "Start", "label": "Start", "position": (50, HEIGHT // 2)}
end_node = {"label": "End", "type": "End", "position": (WIDTH - 50, HEIGHT // 2)}
nodes.append(start_node)
nodes.append(end_node)


# Function to add a new node to the canvas
def add_node(node_type, position):
    nodes.append(
        {
            "type": node_type["label"],
            "position": position,
            "rect": pygame.Rect(20, 20, 20, 20),
        }
    )


# Function to create a connection between two nodes
def add_connection(start_node, end_node):
    connections.append((start_node, end_node))


# Main loop
running = True
selected_node = None
adding_node = None
dragging_node = None
mouse_dragging = False
connecting_node = None
# Additional variable to track line drawing
drawing_line = False
line_start = None
# Additional variables for node movement and direction drawing
node_moving = False
directions = {}  # Dictionary to store directions for each connection

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                pos = pygame.mouse.get_pos()
                if adding_node is not None:
                    add_node(adding_node, pos)
                    adding_node = None
                for node in nodes:
                    if node["rect"].collidepoint(pos):
                        selected_node = node
                        dragging_node = node
                for idx, node_type in enumerate(node_types):
                    node_rect = pygame.Rect(10, 10 + idx * 30, 200, 20)
                    if node_rect.collidepoint(pos):
                        adding_node = node_type

                # Check for starting a connection
                for node in nodes:
                    if node["rect"].collidepoint(pos):
                        connecting_node = node
                        drawing_line = True
                        line_start = connecting_node["position"]

            elif event.button == 2:  # Middle mouse button (scroll wheel)
                pos = pygame.mouse.get_pos()
                for node in nodes:
                    if node["rect"].collidepoint(pos):
                        selected_node = node
                        dragging_node = node
                        mouse_dragging = True
            if event.button == 3:  # Right mouse button
                pos = pygame.mouse.get_pos()
                for node in nodes:
                    if node["rect"].collidepoint(pos):
                        selected_node = node
                        node_moving = True
                        break

        # Check for completing a connection
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                if drawing_line:
                    pos = pygame.mouse.get_pos()
                    for node in nodes:
                        if node["rect"].collidepoint(pos) and node != connecting_node:
                            add_connection(connecting_node, node)
                    drawing_line = False
                connecting_node = None

            if event.button == 1:  # Left mouse button
                if dragging_node and selected_node:
                    selected_node = None
                    dragging_node = None

            elif event.button == 2:  # Middle mouse button (scroll wheel)
                selected_node = None
                dragging_node = None
                mouse_dragging = False

    screen.fill((0, 0, 0))

    # Draw connections
    for connection in connections:
        start_pos = connection[0]["position"]
        end_pos = connection[1]["position"]
        pygame.draw.line(screen, LINE_COLOR, start_pos, end_pos, CONNECTION_WIDTH)

    # Draw start and end nodes
    for node in [start_node, end_node]:
        node["rect"] = pygame.draw.circle(
            screen, NODE_COLOR, node["position"], NODE_RADIUS
        )
        pygame.draw.circle(screen, LINE_COLOR, node["position"], NODE_RADIUS, 2)

    # Draw node types and labels
    for idx, node_type in enumerate(node_types):
        node = node_type["label"]
        node_rect = pygame.Rect(10, 10 + idx * 30, 200, 20)
        pygame.draw.rect(screen, NODE_COLOR, node_rect)
        font = pygame.font.Font(None, 36)
        text = font.render(node, True, (255, 255, 255))
        screen.blit(text, (20, 20 + idx * 30))

    # Draw nodes and their names in blue
    for node in nodes:
        node["rect"] = pygame.draw.circle(
            screen, NODE_COLOR, node["position"], NODE_RADIUS
        )
        pygame.draw.circle(screen, LINE_COLOR, node["position"], NODE_RADIUS, 2)
        font = pygame.font.Font(None, 24)
        text = font.render(node["type"], True, TEXT_COLOR)
        text_rect = text.get_rect()
        text_rect.center = (node["position"][0], node["position"][1] - NODE_RADIUS - 10)
        screen.blit(text, text_rect)

    # Draw the line while drawing_line is True
    if drawing_line:
        pygame.draw.line(
            screen,
            CONNECTION_COLOR,
            line_start,
            pygame.mouse.get_pos(),
            CONNECTION_WIDTH,
        )

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
