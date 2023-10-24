import pygame
import sys
import pyperclip  # Required for clipboard copy

# Initialize Pygame
pygame.init()
if __name__ == "__main__":
    from button import Button
    from input_feild import InputField
    from TextElement import TextElement
    from checkbox import CheckBox
    from color import ColorPickerInputField
else:
    from uimanagement.button import Button
    from uimanagement.input_feild import InputField
    from uimanagement.TextElement import TextElement
    from uimanagement.checkbox import CheckBox
    from uimanagement.color import ColorPickerInputField


# Constants
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)
WHITE = (255, 255, 255)


# Set the screen size
infoObject: object = pygame.display.Info()
screen_width, screen_height = infoObject.current_w, infoObject.current_h
screen: pygame.Surface = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h)
)
pygame_icon = pygame.image.load(
    r"terraria_styled_game\program recources\Screenshot 2023-09-21 181742.png"
)
pygame.display.set_icon(pygame_icon)  # pygame.display.toggle_fullscreen()
pygame.display.set_caption("Square Pixel")
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

buttons = []
input_fields = []
sidebar_buttons = []
text_elements = []
checkboxes = []
scripts = []


# Element that is currently being moved or scaled
selected_element = None
scaling = False
scale_start_x = 0
scale_start_y = 0
scale_start_width = 0
scale_start_height = 0

# UI panel properties
ui_panel_x = screen_width - 200
ui_panel_y = 0
ui_panel_width = 200
ui_panel_height = screen_height

# UI panel background color
UI_PANEL_COLOR = (200, 200, 200)

# Create a font for displaying instructions
instruction_font = pygame.font.Font(None, 13)
# Add instructions for updating the selected element
instruction_text = "Click and drag to move, right-click to resize element and scroll to change font size. "
instruction_text += "Edit properties in the UI panel, then press Enter to apply changes to the selected element. "
instruction_text += "To use color wheel hold mouse button down and then move it around the inner circle. "
instruction_text += "The bar on the right of the wheel controls brightness. "
instruction_text += (
    "Once you find the color you want then just click the element you want to recolor. "
)


# Function for updating font size when scrolling
def update_font_size(selected_element, scroll_direction):
    if isinstance(selected_element, Button):
        selected_element.font_size += scroll_direction * 2


def create_button(text, x, y, width, height, command, additional_data=None):
    return Button(text, x, y, width, height, command, additional_data)


def create_input_field(x, y, width, height, placeholder):
    return InputField(x, y, width, height, placeholder)


def create_button_on_sidebar(text, y, create_function, extra=None):
    button_width = 120
    button_height = 40
    button_x = 10
    new_button = Button(
        text,
        button_x,
        y,
        button_width,
        button_height,
        create_function,
        additional_data=extra,
    )
    sidebar_buttons.append(new_button)


# Function for creating a new button
def create_new_button():
    button = create_button("Button", 200, 200, 100, 50, None)
    buttons.append(button)


# Function for creating a new text element
def create_new_text_element():
    text_element = TextElement(200, 300, "Text", 24)
    text_elements.append(text_element)


def delete_selected_element():
    global selected_element

    if selected_element:
        if isinstance(selected_element, Button):
            buttons.remove(selected_element)
        elif isinstance(selected_element, InputField):
            input_fields.remove(selected_element)
        elif isinstance(selected_element, TextElement):
            text_elements.remove(selected_element)
        elif isinstance(selected_element, CheckBox):
            checkboxes.remove(selected_element)

        selected_element = None


def create_delete_button():
    delete_button = Button("Delete", 10, 280, 120, 40, delete_selected_element)
    sidebar_buttons.append(delete_button)


def export_ui_elements():
    global buttons, input_fields
    code = []

    # Create buttons
    for index, button in enumerate(buttons):
        code.append(
            f"button{index + 1} = Button('{button.text}',{button.x}, {button.y}, {button.width}, {button.height}, None)"
        )

    # Create input fields
    for index, input_field in enumerate(input_fields):
        code.append(
            f"input_field{index + 1} = InputField({input_field.x}, {input_field.y}, {input_field.width}, {input_field.height}, '{input_field.placeholder}')"
        )
    for index, text_element in enumerate(text_elements):
        code.append(
            f"TextElement{index + 1} = TextElement({text_element.x}, {text_element.y}, {text_element.width}, {text_element.height}, '{text_element.placeholder}')"
        )
    for index, checkbox in enumerate(checkboxes):
        code.append(
            f"CheckBox{index + 1} = CheckBox({checkbox.x}, {checkbox.y}, {checkbox.width}, {checkbox.height}, '{checkbox.placeholder}')"
        )
    result = "\n".join(code)
    pyperclip.copy(result)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0, 0, 0))
        # Display the generated code on the screen
        code_text = "\n".join(code) + "\n code copied to clipboard"
        font = pygame.font.Font(None, 18)
        code_surface = font.render(code_text, True, (255, 255, 255))
        screen.blit(code_surface, (10, 60))  # Adjust position as needed
        pygame.display.flip()


# Function for creating a new input field
def create_new_input_field():
    input_field = create_input_field(300, 300, 200, 30, "Enter text")
    input_fields.append(input_field)


def create_new_checkbox():
    checkbox = CheckBox(380, 40, "Label")
    checkboxes.append(checkbox)


create_button_on_sidebar("New Button", 10, create_new_button)
create_button_on_sidebar("New Input", 60, create_new_input_field)
create_button_on_sidebar("New Text", 110, create_new_text_element)
create_button_on_sidebar("Checkbox", 170, create_new_checkbox)
create_button_on_sidebar("Save UI", 230, export_ui_elements, [buttons, input_fields])
create_delete_button()


# UI panel for editing properties
class UIPanel:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.bg_color = UI_PANEL_COLOR
        self.elements = []

    def draw(self, screen):
        pygame.draw.rect(
            screen, self.bg_color, (self.x, self.y, self.width, self.height)
        )

        for element in self.elements:
            element.draw(screen)


class Script:
    def __init__(self):
        self.nodes = []  # List of nodes
        self.connections = []  # List of connections between nodes


class Node:
    def __init__(self, node_type, x, y, node_id):
        self.type = node_type
        self.x = x
        self.y = y
        self.id = node_id
        self.logic = lambda: None  # Default logic for the node


# Text input field for customizing text
class TextInputField:
    def __init__(self, x, y, width, height, label, default_text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.default_text = default_text
        self.text = default_text
        self.active = False

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(self.label, True, (0, 0, 0))
        screen.blit(text, (self.x, self.y))
        pygame.draw.rect(
            screen, (255, 255, 255), (self.x, self.y + 30, self.width, self.height), 2
        )
        text = font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + 5, self.y + 35))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = (
                self.x < event.pos[0] < self.x + self.width
                and self.y + 30 < event.pos[1] < self.y + 30 + self.height
            )
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode


# Numeric input field for customizing numeric properties
class NumericInputField:
    def __init__(self, x, y, width, height, label, default_value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.value = default_value
        self.active = False

    def draw(self, screen):
        font = pygame.font.Font(None, 36)
        text = font.render(self.label, True, (0, 0, 0))
        screen.blit(text, (self.x, self.y))
        pygame.draw.rect(
            screen, (255, 255, 255), (self.x, self.y + 30, self.width, self.height), 2
        )
        text = font.render(str(self.value), True, (0, 0, 0))
        screen.blit(text, (self.x + 5, self.y + 35))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.active = (
                self.x < event.pos[0] < self.x + self.width
                and self.y + 30 < event.pos[1] < self.y + 30 + self.height
            )
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.value = int(str(self.value)[:-1])
            elif event.key in [
                pygame.K_0,
                pygame.K_1,
                pygame.K_2,
                pygame.K_3,
                pygame.K_4,
                pygame.K_5,
                pygame.K_6,
                pygame.K_7,
                pygame.K_8,
                pygame.K_9,
            ]:
                self.value = int(str(self.value) + event.unicode)


# Create UI panel
ui_panel = UIPanel(ui_panel_x, ui_panel_y, ui_panel_width, ui_panel_height)

# Create input fields for customization
text_input_field = TextInputField(
    ui_panel_x + 10, 30, ui_panel_width - 20, 30, "Text:", ""
)
text_size_input_field = NumericInputField(
    ui_panel_x + 10, 100, ui_panel_width - 20, 30, "Text Size:", 0
)
width_input_field = NumericInputField(
    ui_panel_x + 10, 170, ui_panel_width - 20, 30, "Width:", 0
)
height_input_field = NumericInputField(
    ui_panel_x + 10, 250, ui_panel_width - 20, 30, "Height:", 0
)

font_name_input_field = TextInputField(
    ui_panel_x + 10, 330, ui_panel_width - 20, 30, "Font Name:", "Arial"
)
bold_checkbox = CheckBox(ui_panel_x + 10, 450, "Bold", False, color=(0, 0, 0))
italic_checkbox = CheckBox(ui_panel_x + 10, 500, "Italic", False, color=(0, 0, 0))
underline_checkbox = CheckBox(ui_panel_x + 10, 550, "Underline", False, color=(0, 0, 0))
# Create color picker input field for customizing color
color_picker_input_field = ColorPickerInputField(
    ui_panel_x + 10, 630, ui_panel_width - 20, 40, "Color:", (255, 0, 0)
)

ui_panel.elements = [
    text_input_field,
    text_size_input_field,
    width_input_field,
    height_input_field,
    font_name_input_field,
    bold_checkbox,
    italic_checkbox,
    underline_checkbox,
    color_picker_input_field,
]
for el in ui_panel.elements:
    el.size = 20


def handle_events():
    global selected_element, scaling, scale_start_x, scale_start_y, scale_start_width, scale_start_height
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if scaling:
                scaling = False
            for button in buttons:
                if (
                    button.x < event.pos[0] < button.x + button.width
                    and button.y < event.pos[1] < button.y + button.height
                ):
                    button.selected()
                    selected_element = button
            for input_field in input_fields:
                if (
                    input_field.x < event.pos[0] < input_field.x + input_field.width
                    and input_field.y
                    < event.pos[1]
                    < input_field.y + input_field.height
                ):
                    input_field.active = True
                    selected_element = input_field
            for text in text_elements:
                if text.x < event.pos[0] < text.x + (
                    text.width + text.size
                ) and text.y < event.pos[1] < text.y + (text.height + text.size):
                    text.active = True
                    selected_element = text
            for check in checkboxes:
                if check.x < event.pos[0] < check.x + (
                    check.width + check.size
                ) and check.y < event.pos[1] < check.y + (check.height + check.size):
                    check.active = True
                    selected_element = check
            for sidebar_button in sidebar_buttons:
                if (
                    sidebar_button.x
                    < event.pos[0]
                    < sidebar_button.x + sidebar_button.width
                    and sidebar_button.y
                    < event.pos[1]
                    < sidebar_button.y + sidebar_button.height
                ):
                    sidebar_button.command()
            if selected_element:
                if not (
                    selected_element.x
                    < event.pos[0]
                    < selected_element.x + selected_element.width
                    and selected_element.y
                    < event.pos[1]
                    < selected_element.y + selected_element.height
                ):
                    selected_element = None
        elif (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 3
            and selected_element
        ):
            scaling = True
            scale_start_x = event.pos[0]
            scale_start_y = event.pos[1]
            scale_start_width = selected_element.width
            scale_start_height = selected_element.height

        for input_field in input_fields:
            input_field.change_text(event)
        for button in buttons:
            button.change_text(event)
        for text_element in text_elements:
            text_element.change_text(event)
        for checkbox in checkboxes:
            checkbox.change_text(event)
            checkbox.handle_event(event)
        if selected_element:
            # Update UI panel with the selected element's properties
            text_input_field.text = selected_element.text
            text_size_input_field.value = selected_element.size
            width_input_field.value = selected_element.width
            height_input_field.value = selected_element.height
            font_name_input_field.text = selected_element.font_name
            bold_checkbox.checked = selected_element.bold
            italic_checkbox.checked = selected_element.italics
            underline_checkbox.checked = selected_element.underlined

            if scaling and event.type == pygame.MOUSEMOTION:
                selected_element.width = scale_start_width + (
                    event.pos[0] - scale_start_x
                )
                selected_element.height = scale_start_height - (
                    scale_start_y - event.pos[1]
                )
            elif event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # Left mouse button is held
                    selected_element.x += event.rel[0]
                    selected_element.y += event.rel[1]
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                selected_element.size += 1
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                selected_element.size -= 1
        for inspect in ui_panel.elements:
            if isinstance(inspect, ColorPickerInputField):
                inspect.handle_event(event)
            else:
                inspect.handle_event(event)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            # Update the selected element's properties with the UI panel values
            if selected_element:
                selected_element.text = text_input_field.text
                selected_element.size = text_size_input_field.value
                selected_element.width = width_input_field.value
                selected_element.height = height_input_field.value
                selected_element.font_name = font_name_input_field.text
                selected_element.bold = bold_checkbox.checked
                selected_element.italics = italic_checkbox.checked
                selected_element.underlined = underline_checkbox.checked
        # Update the selected element's color based on the color picker value
        if selected_element:
            selected_element.color = color_picker_input_field.color


def main():
    while True:
        handle_events()
        screen.fill((0, 0, 0))

        # Draw the sidebar buttons
        for sidebar_button in sidebar_buttons:
            sidebar_button.draw(screen)

        # Add text elements to the drawing loop
        for text_element in text_elements:
            text_element.draw(screen)
        # Draw the elements (buttons and input fields)
        for button in buttons:
            button.draw(screen)
        for input_field in input_fields:
            input_field.draw(screen)
        for checkbox in checkboxes:
            checkbox.draw(screen)
            # Blit instructions on the screen
        instruction_surface = instruction_font.render(
            instruction_text, True, (255, 255, 255)
        )
        screen.blit(instruction_surface, (10, screen_height - 30))
        # Draw the UI panel
        ui_panel.draw(screen)

        pygame.display.flip()


def start():
    for bu in sidebar_buttons:
        bu.size = 20
    main()


if __name__ == "__main__":
    start()
