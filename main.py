import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((740, 520))
pygame.display.set_caption("Mountain Shooter - by Alfonso")
clock = pygame.time.Clock()
running = True

while running:
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color
    screen.fill("black")

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()

