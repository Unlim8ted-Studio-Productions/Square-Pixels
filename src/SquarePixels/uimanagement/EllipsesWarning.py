import pygame
import sys
from SquarePixels.uimanagement.elements.button import Button

# Initialize Pygame
pygame.init()

# Set up display
infoObject: object = pygame.display.Info()
width, height = infoObject.current_w, infoObject.current_h


# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

runningg = True

# Initialize font
font = pygame.font.Font(
    None, int(min(width, height) * 0.03)
)  # Scale the font size based on screen size


# Function to draw a warning box
def draw_warning_box(screen):
    pygame.draw.rect(
        screen, white, (width * 0.05, height * 0.05, width * 0.9, height * 0.9)
    )
    pygame.draw.rect(
        screen,
        red,
        (width * 0.05, height * 0.05, width * 0.9, height * 0.9),
        int(min(width, height) * 0.01),
    )


# Function to draw text on the screen
def draw_text(screen, text, x, y, font_size_factor=1, color=black):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def continue_game():
    global runningg
    runningg = False

def warning(screen):
    # Create an instance of the Button class
    agree_button = Button(
        "Continue",
        width * 0.4,
        height * 0.8,
        width * 0.2,
        height * 0.1,
        command=continue_game,
    )
    # Main game loop
    while runningg:
        for event in pygame.event.get():
            agree_button.handle_event(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        # Update font size based on screen size
        font_size = int(min(width, height) * 0.03)
        font = pygame.font.Font(None, font_size)
        # Calculate button dimensions based on the screen size
        button_x = int(width * 0.4)
        button_y = int(height * 0.8)
        button_width = int(width * 0.2)
        button_height = int(height * 0.06)
    
        # Update the Button instance with the calculated dimensions
        agree_button.x = button_x
        agree_button.y = button_y
        agree_button.width = button_width
        agree_button.height = button_height
        agree_button.size = font_size
    
        # Clear the screen
        screen.fill(black)
    
        # Draw warning box
        draw_warning_box(screen)
    
        # Draw text
        draw_text(screen, "Photosensitive Seizure Warning", width * 0.1, height * 0.07)
        draw_text(
            screen,
            "A very small percentage of people may experience a seizure when exposed to certain visual images,",
            width * 0.07,
            height * 0.12,
        )
        draw_text(
            screen,
            "including flashing lights or patterns that may appear within square pixels. Even people who have",
            width * 0.07,
            height * 0.15,
        )
        draw_text(
            screen,
            "no history of seizures or epilepsy may have an undiagnosed condition that can cause these “photosensitive",
            width * 0.07,
            height * 0.18,
        )
        draw_text(
            screen,
            "epileptic seizures” while viewing images within square pixels.",
            width * 0.07,
            height * 0.21,
        )
        draw_text(
            screen,
            "Immediately stop viewing and consult a doctor if you experience any symptoms. These seizures may",
            width * 0.07,
            height * 0.26,
        )
        draw_text(
            screen,
            "have a variety of symptoms, including lightheadedness, altered vision, eye or face twitching, jerking or",
            width * 0.07,
            height * 0.29,
        )
        draw_text(
            screen,
            "shaking of arms or legs, disorientation, confusion, or momentary loss of awareness. Seizures may also",
            width * 0.07,
            height * 0.32,
        )
        draw_text(
            screen,
            "cause loss of consciousness or convulsions that can lead to injury from falling down or striking nearby objects.",
            width * 0.07,
            height * 0.35,
        )
        draw_text(
            screen,
            "Parents should watch for or ask their children about the above symptoms. Children and teenagers are more likely",
            width * 0.07,
            height * 0.40,
        )
        draw_text(
            screen, "than adults to experience these seizures.", width * 0.07, height * 0.43
        )
        draw_text(
            screen,
            "You may reduce the risk of photosensitive epileptic seizures by taking the following precautions:",
            width * 0.07,
            height * 0.48,
        )
        draw_text(screen, "- View in a well-lit room.", width * 0.09, height * 0.51)
        draw_text(
            screen,
            "- Do not view if you are drowsy or fatigued.",
            width * 0.09,
            height * 0.54,
        )
        draw_text(
            screen,
            "If you or any of your relatives have a history of seizures or epilepsy, consult a doctor before playing square pixels.",
            width * 0.07,
            height * 0.59,
        )
    
        agree_button.draw(screen)
        # Update the display
        pygame.display.flip()
    
        # Control the frames per second
        pygame.time.Clock().tick(30)
    