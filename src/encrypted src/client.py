import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Bouncing Balls Animation")

# Define colors
WHITE = (255, 255, 255)


# Define Ball class
class Ball:
    def __init__(self, x, y, radius):
        self.radius = radius
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.x = x
        self.y = y
        self.dx = random.choice([-1, 1]) * random.randint(1, 3)
        self.dy = random.choice([-1, 1]) * random.randint(1, 3)

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Check for collisions with the screen edges
        if self.x - self.radius < 0 or self.x + self.radius > screen_width:
            self.dx *= -1
        if self.y - self.radius < 0 or self.y + self.radius > screen_height:
            self.dy *= -1

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def eat(self, other_ball):
        if self.radius > other_ball.radius:
            self.radius += int(other_ball.radius * 0.2)  # Increase radius
            other_ball.reset()  # Reset the smaller ball

    def reset(self):
        self.x = random.randint(self.radius, screen_width - self.radius)
        self.y = random.randint(self.radius, screen_height - self.radius)
        self.radius = random.randint(10, 30)
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.dx = random.choice([-1, 1]) * random.randint(1, 3)
        self.dy = random.choice([-1, 1]) * random.randint(1, 3)


# Create a list to store the balls
balls = []

# Create some initial balls
for _ in range(10):
    x = random.randint(30, screen_width - 30)
    y = random.randint(30, screen_height - 30)
    radius = random.randint(10, 30)
    ball = Ball(x, y, radius)
    balls.append(ball)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Update and draw the balls
    for ball in balls:
        ball.update()
        ball.draw()

    # Check for collisions between balls
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            dx = balls[i].x - balls[j].x
            dy = balls[i].y - balls[j].y
            distance = ((dx**2) + (dy**2)) ** 0.5

            if distance < balls[i].radius + balls[j].radius:
                if balls[i].radius > balls[j].radius:
                    balls[i].eat(balls[j])
                else:
                    balls[j].eat(balls[i])

    # Remove balls that are too big
    balls = [ball for ball in balls if ball.radius < 500]

    # Spawn new balls
    while len(balls) < 10:
        x = random.randint(30, screen_width - 30)
        y = random.randint(30, screen_height - 30)
        radius = random.randint(10, 30)
        ball = Ball(x, y, radius)
        balls.append(ball)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the program
pygame.quit()
