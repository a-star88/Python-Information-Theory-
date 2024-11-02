import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("HSB to RGB Animation")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Function to convert HSB to RGB
def hsb_to_rgb(hue, saturation, brightness):
    h = hue / 360.0
    s = saturation / 100.0
    v = brightness / 100.0
    i = int(h * 6)
    f = h * 6 - i
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)
    i = i % 6
    if i == 0:
        r, g, b = v, t, p
    elif i == 1:
        r, g, b = q, v, p
    elif i == 2:
        r, g, b = p, v, t
    elif i == 3:
        r, g, b = p, q, v
    elif i == 4:
        r, g, b = t, p, v
    elif i == 5:
        r, g, b = v, p, q
    return int(r * 255), int(g * 255), int(b * 255)

# User input for saturation and brightness
user_saturation = int(input("Enter a saturation value from 0 to 100: "))
user_brightness = int(input("Enter a brightness value from 0 to 100: "))

# Main loop
running = True
clock = pygame.time.Clock()
hue = 0
hue_direction = 1
plane_y_position = 100  # Starting position for the moving plane

while running:
    screen.fill(black)

    # Animate hue from 0 to 360 and back
    hue += hue_direction
    if hue >= 360 or hue <= 0:
        hue_direction *= -1

    # Calculate RGB values
    r, g, b = hsb_to_rgb(hue, user_saturation, user_brightness)

    # Draw the moving plane (changing hue)
    pygame.draw.rect(screen, hsb_to_rgb(hue, user_saturation, user_brightness), (100, plane_y_position, 600, 20))

    # Update plane's vertical position based on hue
    plane_y_position = 100 + hue

    # Draw the static planes
    pygame.draw.rect(screen, hsb_to_rgb(180, user_saturation, user_brightness), (100, 200, 200, 200))
    pygame.draw.rect(screen, hsb_to_rgb(270, user_saturation, user_brightness), (500, 200, 200, 200))

    # Draw the RGB pixel indicator
    pygame.draw.rect(screen, (r, 0, 0), (100, 500, 100, 50))
    pygame.draw.rect(screen, (0, g, 0), (250, 500, 100, 50))
    pygame.draw.rect(screen, (0, 0, b), (400, 500, 100, 50))

    # Draw the RGB text
    font = pygame.font.Font(None, 36)
    rgb_text = font.render(f"R: {r} G: {g} B: {b}", True, white)
    screen.blit(rgb_text, (550, 520))

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

    # Control the speed of the animation
    clock.tick(30)

# Quit Pygame
pygame.quit()
