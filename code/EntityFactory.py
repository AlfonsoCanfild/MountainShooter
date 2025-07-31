from code.Background import Background
from code.Const import WIN_WIDTH

class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level2BG':
                list_bg = []
                for i in range(2):
                    x_offset = i * WIN_WIDTH * 2  # Espaço correto entre os pares
                    list_bg.append(Background(f'Level1BG{i}', (x_offset, 0)))
                    list_bg.append(Background(f'Level1BG{i}', (x_offset + WIN_WIDTH, 0)))
                return list_bg
