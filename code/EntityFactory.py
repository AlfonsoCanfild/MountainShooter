import pygame

from code.Background import Background


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1BG':
                list_bg = []
                for layer in range(4):
                    img = pygame.image.load(f'./assets/Level1BG{layer}.png').convert_alpha()
                    image_width = img.get_width()
                    for i in range(2):  # duas cópias
                        x = i * image_width
                        list_bg.append(Background(f'Level1BG{layer}', (x, 0)))
                return list_bg
