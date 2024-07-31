import pygame
import sys

# Initialize Pygame
pygame.init()

# This program is responsible for making a extra window 

# Set Up Display
screen = pygame.display.set_mode((800, 600))  # Window size 800x600, we can use variable a b c d anything but screeen is used so which increase readability !
pygame.display.set_caption('My First Pygame Window') #this is title of the window 

# Main Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Fill the screen with a color (RGB)
    screen.fill((0, 0, 255))  # Fill the screen with blue color
    
    # Update the display
    pygame.display.flip()
