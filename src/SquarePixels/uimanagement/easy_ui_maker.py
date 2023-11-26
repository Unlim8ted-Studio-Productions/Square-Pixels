import pygame
import sys
import pyperclip  # Required for clipboard copy
import tkinter as tk
from tkinter import filedialog
from PIL import Image


# Initialize Pygame
pygame.init()
if __name__ == "__main__":
    from elements.button import Button
    from elements.input_feild import InputField
    from elements.TextElement import TextElement
    from elements.checkbox import CheckBox
    from elements.color import ColorPickerInputField
    from elements.Image import ImageElement
    from elements.numeric_input import NumericInputField
    from script import Script
    from UIpanel import UIPanel
    from elements.slider import Slider
else:
    from SquarePixels.uimanagement.elements.button import Button
    from SquarePixels.uimanagement.elements.input_feild import InputField
    from SquarePixels.uimanagement.elements.TextElement import TextElement
    from SquarePixels.uimanagement.elements.checkbox import CheckBox
    from SquarePixels.uimanagement.elements.color import ColorPickerInputField
    from SquarePixels.uimanagement.elements.Image import ImageElement
    from SquarePixels.uimanagement.elements.numeric_input import NumericInputField
    from SquarePixels.uimanagement.script import Script
    from SquarePixels.uimanagement.UIpanel import UIPanel
    from SquarePixels.uimanagement.elements.slider import Slider

    # from Nodes import


# Constants
BUTTON_COLOR = (50, 50, 50)
BUTTON_HOVER_COLOR = (100, 100, 100)
WHITE = (255, 255, 255)

# Set the screen size
infoObject: object = pygame.display.Info()
WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
screen_width, screen_height = infoObject.current_w, infoObject.current_h
screen: pygame.Surface = pygame.display.set_mode(
    (infoObject.current_w, infoObject.current_h)
)
pygame_icon = pygame.image.load(
    r"recources\program recources\Screenshot 2023-09-21 181742.png"
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
images = []
sliders = []


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
    """
    Updates the font size of a selected element based on scroll direction
    Args:
        selected_element: The element to update font size for
        scroll_direction: The direction of scrolling ('up' or 'down')
    Returns:
        None: Does not return anything
    - Check if selected element is a Button
    - If scroll direction is 'up', increase font size by 1 point
    - If scroll direction is 'down', decrease font size by 1 point
    - Set the new font size on the selected element"""
    if isinstance(selected_element, Button):
        selected_element.font_size += scroll_direction * 2


def create_button(text, x, y, width, height, command, additional_data=None):
    """
    Create a button widget
    Args:
        text: Button text
        x: x-coordinate of button
        y: y-coordinate of button
        width: Width of button
        height: Height of button
        command: Command to execute on click
        additional_data: Optional additional data to pass to command
    Returns:
        Button: Button widget object
    - Create a Button object with the given parameters
    - Return the Button object
    """
    butn = Button(text, x, y, width, height, command, additional_data)
    buttons.append(butn)
    return butn


def create_input_field(x, y, width, height, placeholder):
    """
    Creates an input field widget
    Args:
        x: X coordinate of input field
        y: Y coordinate of input field
        width: Width of input field
        height: Height of input field
        placeholder: Placeholder text for input field
    Returns:
        InputField: Input field widget object
    - Creates an InputField object with the provided x, y, width, height
    - Sets the placeholder text on the input field
    - Returns the InputField object
    """
    ifield = InputField(x, y, width, height, placeholder)
    input_fields.append(ifield)
    return ifield


def create_button_on_sidebar(text, y, create_function, extra=None):
    """
    Creates a button on the sidebar.
    Args:
        text: The text to display on the button.
        y: The y coordinate for the button.
        create_function: The function to call when button is clicked.
        extra: Optional additional data to pass to create_function.
    Returns:
        new_button: The created button object.
    - A new Button object is created with the given parameters
    - The button is added to the sidebar_buttons list
    - The button can now be clicked to call create_function, passing extra data
    """
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


def add_image(circle=None):
    """
    Add an image to the canvas
    Args:
        circle: The circle object to add the image to
    Returns:
        None: Does not return anything
    - Opens a file dialog to select an image file
    - Checks if a file was selected
    - If file selected, adds the image to the canvas"""
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )

    if file_path:
        # Load the selected image using PIL
        image = Image.open(file_path)

        # Create an ImageElement object and add it to your list of elements
        if circle:
            image_element = ImageElement(200, 400, image, "Circle")
        else:
            image_element = ImageElement(200, 400, image)
        images.append(image_element)


# Function for creating a new button
def create_new_button():
    """Creates a new button and adds it to the buttons list

    Args:
        None
    Returns:
        None: No value is returned

    - A new button object is created with the label "Button", positioned at (200,200) with dimensions of 100x50 pixels
    - The new button is appended to the global buttons list
    - No value is returned as the button is added directly to the buttons list"""
    button = create_button("Button", 200, 200, 100, 50, None)
    buttons.append(button)


# Function for creating a new text element
def create_new_text_element():
    """
    Creates and adds a new text element to the list
    Args:
        None
    Returns:
        None: No value is returned
    - Creates a new TextElement object with default values
    - Adds the new TextElement to the text_elements list
    - No value is returned, only side effect is adding to list"""
    text_element = TextElement(200, 300, "Text", 24)
    text_elements.append(text_element)


def delete_selected_element():
    """Deletes currently selected element
    Args:
        None
    Returns:
        None: Selected element is deleted from list
    - Check if a selected element exists
    - If it does, remove it from the global list storing all elements
    - Clear the selected element variable
    - Refresh the UI to remove the selected element"""
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
        elif isinstance(selected_element, Slider):
            sliders.remove(selected_element)
        elif isinstance(selected_element, Image):
            images.remove(selected_element)

        selected_element = None


def create_delete_button(y=280):
    """
    Create and add a delete button to the sidebar
    Args:
        y: Position of the button from the top of the sidebar in pixels
    Returns:
        None: No value is returned
    - Create a Button object with text "Delete", x position 10, y position from argument, width 120 and height 40
    - Assign the delete_selected_element function to the button's command
    - Append the button object to the sidebar_buttons list"""
    delete_button = Button("Delete", 10, y, 120, 40, delete_selected_element)
    sidebar_buttons.append(delete_button)


def export_ui_elements():
    """
    Exports UI elements to Python code
    Args:
        None: No arguments
    Returns:
        None: Does not return anything
    Processes Logic:
        - Loops through button, input_field, checkbox, image lists and generates Python code to recreate each element
        - Copies generated code to clipboard
        - Displays message that code was copied
    """
    global buttons, input_fields, checkboxes, images, sliders, text_elements
    code = [
        "if __name__ == '__main__':",
        "    from SquarePixels.uimanagement.elements.button import Button",
        "    from SquarePixels.uimanagement.elements.input_feild import InputField",
        "    from SquarePixels.uimanagement.elements.TextElement import TextElement",
        "    from SquarePixels.uimanagement.elements.checkbox import CheckBox",
        "    from SquarePixels.uimanagement.elements.color import ColorPickerInputField",
        "    from SquarePixels.uimanagement.elements.Image import ImageElement",
        "    from SquarePixels.uimanagement.elements.slider import Slider",
    ]

    # Create buttons  screen_width/{screen_width/x}
    for index, button in enumerate(buttons):
        code.append(
            f"button{index + 1} = Button('{button.text}', WIDTH / {WIDTH / button.x}, HEIGHT / {HEIGHT / button.y}, WIDTH / {WIDTH / button.width}, HEIGHT / {HEIGHT / button.height}, None)"
        )

    # Create input fields
    for index, input_field in enumerate(input_fields):
        code.append(
            f"input_field{index + 1} = InputField(WIDTH / {WIDTH / input_field.x}, HEIGHT / {HEIGHT / input_field.y}, WIDTH / {WIDTH / input_field.width}, HEIGHT / {HEIGHT / input_field.height}, '{input_field.placeholder}')"
        )
    for index, text_element in enumerate(text_elements):
        code.append(
            f"TextElement{index + 1} = TextElement(WIDTH / {WIDTH / text_element.x}, HEIGHT / {HEIGHT / text_element.y}, WIDTH / {WIDTH / text_element.width}, HEIGHT / {HEIGHT / text_element.height}')"
        )
    for index, checkbox in enumerate(checkboxes):
        code.append(
            f"CheckBox{index + 1} = CheckBox(WIDTH / {WIDTH / checkbox.x}, HEIGHT / {HEIGHT / checkbox.y}, WIDTH / {WIDTH / checkbox.width}, HEIGHT / {HEIGHT / checkbox.height}')"
        )

    for index, image in enumerate(images):
        code.append(
            f"Image{index + 1} = ImageElement(WIDTH / {WIDTH / image.x}, HEIGHT / {HEIGHT / image.y}, WIDTH / {WIDTH / image.width}, HEIGHT / {HEIGHT / image.height})"
        )
    for index, slider in enumerate(sliders):
        code.append(
            f"SliderElement{index + 1} = Slider(WIDTH / {WIDTH / slider.x}, HEIGHT / {HEIGHT / slider.y}, WIDTH / {WIDTH / slider.width}, HEIGHT / {HEIGHT / slider.height}, {slider.min_value}, {slider.max_value}, {slider.default_value}, {slider.command}, {slider.additional_data}, {slider.color}, {slider.colortwo}, {slider.text}, {slider.text_position_below}, {slider.size})"
        )
    code.append("code copied to clipboard")
    result = "\n".join(code)
    pyperclip.copy(result)
    screen.fill((0, 0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Display the generated code on the screen
        font = pygame.font.Font(None, 15)
        for index, t in enumerate(code):
            if index == len(code) - 1:
                index += 5
                font = pygame.font.Font(None, 25)
            code_surface = font.render(t, True, (255, 255, 255))
            screen.blit(
                code_surface, (10, 60 + (15 * index))
            )  # Adjust position as needed
            pygame.display.flip()


def create_input_field(x, y, width, height, placeholder):
    """
    Creates an input field widget
    Args:
        x: X coordinate of input field
        y: Y coordinate of input field
        width: Width of input field
        height: Height of input field
        placeholder: Placeholder text for input field
    Returns:
        InputField: Input field widget object
    - Creates an InputField object with the provided x, y, width, height
    - Sets the placeholder text on the input field
    - Returns the InputField object
    """
    return InputField(x, y, width, height, placeholder)


def create_button_on_sidebar(text, y, create_function, extra=None):
    """
    Creates a button on the sidebar.
    Args:
        text: The text to display on the button.
        y: The y coordinate for the button.
        create_function: The function to call when button is clicked.
        extra: Optional additional data to pass to create_function.
    Returns:
        new_button: The created button object.
    - A new Button object is created with the given parameters
    - The button is added to the sidebar_buttons list
    - The button can now be clicked to call create_function, passing extra data
    """
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


def add_image(circle=None):
    """
    Add an image to the canvas
    Args:
        circle: The circle object to add the image to
    Returns:
        None: Does not return anything
    - Opens a file dialog to select an image file
    - Checks if a file was selected
    - If file selected, adds the image to the canvas"""
    root = tk.Tk()
    root.withdraw()  # Hide the main tkinter window

    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )

    if file_path:
        # Load the selected image using PIL
        image = Image.open(file_path)

        # Create an ImageElement object and add it to your list of elements
        if circle:
            image_element = ImageElement(200, 400, image, "Circle")
        else:
            image_element = ImageElement(200, 400, image)
        images.append(image_element)


# Function for creating a new button
def create_new_button():
    """Creates a new button and adds it to the buttons list

    Args:
        None
    Returns:
        None: No value is returned

    - A new button object is created with the label "Button", positioned at (200,200) with dimensions of 100x50 pixels
    - The new button is appended to the global buttons list
    - No value is returned as the button is added directly to the buttons list"""
    button = create_button("Button", 200, 200, 100, 50, None)
    buttons.append(button)


# Function for creating a new text element
def create_new_text_element():
    """
    Creates and adds a new text element to the list
    Args:
        None
    Returns:
        None: No value is returned
    - Creates a new TextElement object with default values
    - Adds the new TextElement to the text_elements list
    - No value is returned, only side effect is adding to list"""
    text_element = TextElement(200, 300, "Text", 24)
    text_elements.append(text_element)


def delete_selected_element():
    """Deletes currently selected element
    Args:
        None
    Returns:
        None: Selected element is deleted from list
    - Check if a selected element exists
    - If it does, remove it from the global list storing all elements
    - Clear the selected element variable
    - Refresh the UI to remove the selected element"""
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


def create_delete_button(y=280):
    """
    Create and add a delete button to the sidebar
    Args:
        y: Position of the button from the top of the sidebar in pixels
    Returns:
        None: No value is returned
    - Create a Button object with text "Delete", x position 10, y position from argument, width 120 and height 40
    - Assign the delete_selected_element function to the button's command
    - Append the button object to the sidebar_buttons list"""
    delete_button = Button("Delete", 10, y, 120, 40, delete_selected_element)
    sidebar_buttons.append(delete_button)


# Function for creating a new input field
def create_new_input_field():
    """
    Creates and adds a new input field to the list of input fields
    Args:
        None: No arguments are passed to this function
    Returns:
        None: This function does not return anything
    - Creates a new input field object using the create_input_field function and default parameters
    - Appends the newly created input field object to the list of existing input fields
    - This allows adding multiple input fields dynamically to the UI"""
    input_field = create_input_field(300, 300, 200, 30, "Enter text")
    input_fields.append(input_field)


def create_new_checkbox():
    """Creates a new checkbox object and appends it to the checkboxes list

    Args:
        None
    Returns:
        None: No value is returned
    - A CheckBox object is instantiated with coordinates (380, 40) and label "Label"
    - The new CheckBox object is appended to the checkboxes list
    - This allows the checkbox to be drawn and interacted with through the checkboxes list
    """
    checkbox = CheckBox(380, 40, "Label")
    checkboxes.append(checkbox)


def add_slider():
    """
    Add an image to the canvas
    Args:
        circle: The circle object to add the image to
    Returns:
        None: Does not return anything
    - Opens a file dialog to select an image file
    - Checks if a file was selected
    - If file selected, adds the image to the canvas"""

    # Create an slider object and add it to your list of elements
    slider_element = Slider(200, 400, 100, 10, 0, 100, 50)
    sliders.append(slider_element)


create_button_on_sidebar("New Button", 10, create_new_button)
create_button_on_sidebar("New Input", 60, create_new_input_field)
create_button_on_sidebar("New Text", 110, create_new_text_element)
create_button_on_sidebar("Checkbox", 170, create_new_checkbox)
create_button_on_sidebar("Add Image", 230, add_image)
create_button_on_sidebar("Add Circle Image", 290, add_image, [True])  # circle
create_button_on_sidebar("Add Slider", 350, add_slider)  # circle
create_button_on_sidebar("Save UI", 410, export_ui_elements)
create_delete_button(470)


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
        """
        Initialize a graph object
        Args:
            None: No arguments required
        Returns:
            None: Does not return anything
        - Initialize an empty list to store nodes
        - Initialize an empty list to store connections between nodes"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.default_text = default_text
        self.text = default_text
        self.active = False

    def draw(self, screen):
        """Draws a rectangle on the screen.
        Args:
            screen: The screen surface to draw on.
        Returns:
            None: Does not return anything.
        - Draws a filled rectangle on the screen surface using the object's position, size and background color attributes.
        - Loops through the object's elements list and draws each element."""
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
            for slider in sliders:
                if (
                    slider.x < event.pos[0] < slider.x + slider.width
                    and slider.y < event.pos[1] < slider.y + slider.height
                ):
                    slider.active = True
                    selected_element = slider
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
            for image in images:
                if (
                    image.x < event.pos[0] < image.x + image.width
                    and image.y < event.pos[1] < image.y + image.height
                ):
                    image.active = True
                    selected_element = image
            for sidebar_button in sidebar_buttons:
                if (
                    sidebar_button.x
                    < event.pos[0]
                    < sidebar_button.x + sidebar_button.width
                    and sidebar_button.y
                    < event.pos[1]
                    < sidebar_button.y + sidebar_button.height
                ):
                    if sidebar_button.additional_data:
                        sidebar_button.command(*sidebar_button.additional_data)
                    else:
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
        for slider in sliders:
            slider.change_text(event)
            slider.handle_event(event)
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
        for image in images:
            image.draw(screen)
        for slider in sliders:
            slider.draw(screen)
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
