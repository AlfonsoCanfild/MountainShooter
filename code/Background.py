from code.Const import WIN_WIDTH
from code.Entity import Entity


class Background(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, speed=1):
        self.rect.x -= speed
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH
