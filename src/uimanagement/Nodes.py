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

# Constants for the inspector tab
INSPECTOR_WIDTH = 200
INSPECTOR_COLOR = (50, 50, 50)

# Create an Inspector rect
inspector_rect = pygame.Rect(WIDTH - INSPECTOR_WIDTH, 0, INSPECTOR_WIDTH, HEIGHT)

# Create a text input area
text_input_rect = pygame.Rect(
    WIDTH - INSPECTOR_WIDTH + 10, 50, INSPECTOR_WIDTH - 20, 100
)
text_input_text = ""
font = pygame.font.Font(None, 36)
text_input_active = False


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
    """
    Adds a connection between two nodes
    Args:
        start_node: The starting node of the connection 
        end_node: The ending node of the connection
    Returns: 
        None: Does not return anything
    - Appends a tuple containing the start and end nodes to the connections list
    - This records the connection between the two nodes passed as arguments
    - No value is returned as the connection is added by side effect of appending to the list
    - Only the connection between the two nodes is recorded, no checking is done on the nodes"""
    connections.append((start_node, end_node))


# Function to draw the inspector tab
def draw_inspector():
    """Draws the inspector rectangle on screen
    Args: 
        screen: The screen surface to draw on
    Returns:
        None: Does not return anything
    - Draws a rectangle on the screen surface using pygame's draw.rect method  
    - The rectangle is drawn with the color INSPECTOR_COLOR
    - The rectangle is drawn using the inspector_rect object which defines its position and size
    - No value is returned as the rectangle is drawn directly to the screen surface"""
    """Draws the inspector rectangle on screen
    Args:
        screen: The screen surface to draw on
    Returns: 
        None: Does not return anything
    - Draws a rectangle on the screen surface using pygame's draw.rect method
    - The rectangle is drawn with the color INSPECTOR_COLOR
    - The rectangle is drawn using the inspector_rect object which defines its position and size
    - No value is returned as the rectangle is drawn directly to the screen surface"""
    pygame.draw.rect(screen, INSPECTOR_COLOR, inspector_rect)


# Function to display details about the selected node in the inspector tab
def show_inspector(node):
    """
    Display inspector details of a node
    Args:
        node: The node to display inspector details for
    Returns: 
        None: Does not return anything
    - Check if the passed node is not None
    - If node is valid, display its inspector details
    - No return value as function just displays details"""
    if node is not None:
        # Create a text input box for details
        pygame.draw.rect(screen, (255, 255, 255), text_input_rect)
        pygame.draw.rect(screen, (0, 0, 0), text_input_rect, 2)

        # Display details about the selected node
        if "type" in node:
            details = "Node Type: " + node["type"]
            font = pygame.font.Font(None, 28)
            text = font.render(details, True, (0, 0, 0))
            text_rect = text.get_rect()
            text_rect.topleft = (text_input_rect.x + 10, text_input_rect.y + 10)
            screen.blit(text, text_rect)
        else:
            text_input_text = ""


# Main loop
running = True
selected_node = None
adding_node = None
dragging_node = None
mouse_dragging = False
connecting_node = None
drawing_line = False
line_start = None
node_moving = False
directions = {}

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if adding_node is not None:
                    add_node(adding_node, pos)
                    adding_node = None

                # Check if a node is clicked and make it the selected node
                for node in nodes:
                    if node["rect"].collidepoint(pos):
                        selected_node = node
                        dragging_node = node

                for idx, node_type in enumerate(node_types):
                    node_rect = pygame.Rect(10, 10 + idx * 30, 200, 20)
                    if node_rect.collidepoint(pos):
                        adding_node = node_type

                for node in nodes:
                    if node["rect"].collidepoint(pos):
                        connecting_node = node
                        drawing_line = True
                        line_start = connecting_node["position"]

            elif event.button == 2:
                pos = pygame.mouse.get_pos()
                for node in nodes:
                    if node["rect"].collidepoint(pos):
                        selected_node = node
                        dragging_node = node
                        mouse_dragging = True
                text_input_active = text_input_rect.collidepoint(pos)

            if event.button == 3:
                pos = pygame.mouse.get_pos()
                for node in nodes:
                    if node["rect"].collidepoint(pos):
                        selected_node = node
                        node_moving = True
                        break

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if drawing_line:
                    pos = pygame.mouse.get_pos()
                    for node in nodes:
                        if node["rect"].collidepoint(pos) and node != connecting_node:
                            add_connection(connecting_node, node)
                    drawing_line = False
                connecting_node = None

            if event.button == 1:
                if dragging_node and selected_node:
                    selected_node = None
                    dragging_node = None

            elif event.button == 2:
                selected_node = None
                dragging_node = None
                mouse_dragging = False

    screen.fill((0, 0, 0))

    for connection in connections:
        start_pos = connection[0]["position"]
        end_pos = connection[1]["position"]
        pygame.draw.line(screen, LINE_COLOR, start_pos, end_pos, CONNECTION_WIDTH)

    for node in [start_node, end_node]:
        node["rect"] = pygame.draw.circle(
            screen, NODE_COLOR, node["position"], NODE_RADIUS
        )
        if node == selected_node:
            pygame.draw.circle(screen, (0, 255, 0), node["position"], NODE_RADIUS)
        pygame.draw.circle(screen, LINE_COLOR, node["position"], NODE_RADIUS, 2)

    for idx, node_type in enumerate(node_types):
        node = node_type["label"]
        node_rect = pygame.Rect(10, 10 + idx * 30, 200, 20)
        pygame.draw.rect(screen, NODE_COLOR, node_rect)
        font = pygame.font.Font(None, 36)
        text = font.render(node, True, (255, 255, 255))
        screen.blit(text, (20, 20 + idx * 30))

    for node in nodes:
        node["rect"] = pygame.draw.circle(
            screen, NODE_COLOR, node["position"], NODE_RADIUS
        )
        if node == selected_node:
            pygame.draw.circle(screen, (0, 255, 0), node["position"], NODE_RADIUS)
        pygame.draw.circle(screen, LINE_COLOR, node["position"], NODE_RADIUS, 2)
        font = pygame.font.Font(None, 24)
        text = font.render(node["type"], True, TEXT_COLOR)
        text_rect = text.get_rect()
        text_rect.center = (node["position"][0], node["position"][1] - NODE_RADIUS - 10)
        screen.blit(text, text_rect)

    if drawing_line:
        pygame.draw.line(
            screen,
            CONNECTION_COLOR,
            line_start,
            pygame.mouse.get_pos(),
            CONNECTION_WIDTH,
        )

    # Draw the inspector tab
    draw_inspector()

    # Show options for the selected node in the inspector tab
    show_inspector(selected_node)

    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
