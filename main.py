import pygame

print('Setup Start')
pygame.init()
window = pygame.display.set_mode(size=(800, 580))
print('Setup Start')

while True:
    # check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var = pygame.QUIT
            quit()

