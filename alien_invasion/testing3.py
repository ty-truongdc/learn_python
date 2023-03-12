import pygame

# Initialize Pygame
pygame.init()

# Load an image into a Pygame surface
image = pygame.image.load('images/alien.bmp')

# Get the rectangular area of the surface
rect = image.get_rect()

# Set the screen size and title
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Pygame Example")

# Center the rectangle on the screen
rect.center = screen.get_rect().center

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((255, 255, 255))
    
    # Blit the surface onto the screen
    screen.blit(image, rect)
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
