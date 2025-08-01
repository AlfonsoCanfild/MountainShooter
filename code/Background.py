from code.Const import WIN_WIDTH
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, speed=1):
        super().__init__(name, position)
        self.speed = speed
        self.image_width = self.surf.get_width()

    def move(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.rect.left = 0  # reposiciona à direita

