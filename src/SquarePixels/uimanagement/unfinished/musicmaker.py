import pygame
import time
import numpy as np

# Initialize Pygame
pygame.init()

# Set the screen dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 400

# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set the font
font = pygame.font.Font(None, 36)

# Set the sample rate and bit size
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()

# Define some constants
SAMPLE_RATE = 44100

# Define some notes and their corresponding frequencies
notes = {
    "C": 261.63,
    "D": 293.66,
    "E": 329.63,
    "F": 349.23,
    "G": 392.00,
    "A": 440.00,
    "B": 493.88,
}


# Function to generate a simple square wave for a given frequency and duration
def generate_square_wave(frequency, duration):
    num_samples = int(SAMPLE_RATE * duration)
    t = np.linspace(0, duration, num_samples, endpoint=False)

    # Create a mono wave
    mono_wave = 0.5 * (1 + np.sign(np.sin(2 * np.pi * frequency * t)))

    # Convert mono to stereo (duplicate the mono wave for both channels)
    stereo_wave = np.column_stack((mono_wave, mono_wave))

    return (stereo_wave * 32767).astype(np.int16)


# Function to play a note
def play_note(note, duration, tempo=120):
    frequency = notes[note]
    square_wave = generate_square_wave(frequency, duration * 60.0 / tempo)
    sound = pygame.sndarray.make_sound(square_wave)
    sound.play()
    time.sleep(duration * 60.0 / tempo)


# Function to draw the piano keys
def draw_piano(screen):
    screen.fill(BLACK)
    key_width = SCREEN_WIDTH // len(notes)

    for i, (note, frequency) in enumerate(notes.items()):
        key_rect = pygame.Rect(i * key_width, 0, key_width, SCREEN_HEIGHT)
        pygame.draw.rect(screen, WHITE, key_rect)
        pygame.draw.rect(screen, BLACK, key_rect, 1)

        # Display note labels
        text = font.render(note, True, BLACK)
        text_rect = text.get_rect(
            center=(i * key_width + key_width // 2, SCREEN_HEIGHT // 2)
        )
        screen.blit(text, text_rect)


# Function to draw the notes being played
def draw_notes(screen, melody, scroll_x):
    for i, (note, duration, start_time) in enumerate(melody):
        elapsed_time = time.time() - start_time
        time_to_play = max(duration - elapsed_time, 0)

        # Calculate the rectangle length based on note duration
        rect_length = int(time_to_play * 50)

        # Calculate the y-position based on pitch
        pitch_y = int((SCREEN_HEIGHT // len(notes)) * list(notes.keys()).index(note))

        # Draw the note rectangle
        pygame.draw.rect(screen, WHITE, (i * 50 - scroll_x, pitch_y, 40, rect_length))

        # Draw triangle marker
        pygame.draw.polygon(
            screen,
            WHITE,
            [
                (i * 50 - scroll_x + 20, pitch_y - 10),
                (i * 50 - scroll_x + 30, pitch_y),
                (i * 50 - scroll_x + 20, pitch_y + 10),
            ],
        )


# Function to add note on click
def add_note_on_click(x, melody, scroll_x):
    note_index = int(x // (SCREEN_WIDTH / len(notes)))
    note = list(notes.keys())[note_index]
    start_time = time.time()
    melody.append((note, note_duration, start_time))
    generate_and_play_sound(note, note_duration, start_time)
    return scroll_x


# Function to generate and play a sound
async def generate_and_play_sound(note, duration, start_time, tempo=120):
    frequency = notes[note]
    square_wave = generate_square_wave(frequency, duration * 60.0 / tempo)
    sound = pygame.sndarray.make_sound(square_wave)
    sound.play()


# Function to delete a note
def delete_note(x, melody, scroll_x):
    note_index = int((x + scroll_x) // (SCREEN_WIDTH / len(notes)))
    if 0 <= note_index < len(melody):
        del melody[note_index]
    return scroll_x


# Function to stop playing a note
def stop_all_notes():
    pygame.mixer.stop()


# Example song with one track (melody)
melody = []

# Current note duration
note_duration = 0.5

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

# Scroll position
scroll_x = 0

# Main loop
running = True
playing = False  # Flag to track whether notes are currently playing

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # Left click to add a note
                if not playing:
                    scroll_x = add_note_on_click(
                        pygame.mouse.get_pos()[0], melody, scroll_x
                    )
            elif event.button == 3:
                # Right click to delete a note
                if not playing:
                    scroll_x = delete_note(pygame.mouse.get_pos()[0], melody, scroll_x)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                # Left mouse button released, stop all notes
                stop_all_notes()
                playing = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            # Scroll right
            scroll_x += 50
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            # Scroll left
            scroll_x -= 50
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Space key to toggle play/pause
                if not melody:
                    print("Melody is empty. Add notes to play.")
                else:
                    if playing:
                        stop_all_notes()
                    else:
                        playing = True
                        for note, duration, start_time in melody:
                            generate_and_play_sound(note, duration, start_time)

    # Draw piano keys
    draw_piano(screen)

    # Draw all notes in the current pattern
    draw_notes(screen, melody, scroll_x)

    pygame.display.flip()

pygame.quit()
