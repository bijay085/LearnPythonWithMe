import pygame
import sys

# Initialize Pygame
pygame.init()

# Set Up Display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Moving Rectangle')

# Colors
blue = (0, 0, 255)
red = (255, 0, 0)

# Rectangle Position and Speed
x = 100
y = 100
speed_x = 2
speed_y = 2

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Move the rectangle
    x += speed_x
    y += speed_y
    
    # Bounce the rectangle off the edges
    if x < 0 or x > 800 - 50:
        speed_x = -speed_x
    if y < 0 or y > 600 - 50:
        speed_y = -speed_y
    
    # Fill the screen
    screen.fill(blue)
    
    # Draw the rectangle
    pygame.draw.rect(screen, red, (x, y, 50, 50))  # Red rectangle at (x, y) with size 50x50
    
    # Update the display
    pygame.display.flip()
    
    # Control the frame rate
    pygame.time.Clock().tick(60)  # 60 frames per second
