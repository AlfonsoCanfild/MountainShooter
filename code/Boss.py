import random

from code.Enemy import Enemy
from code.Const import WIN_WIDTH, WIN_HEIGHT


# Classe especial para movimentação do Boss
class Boss(Enemy):
    def __init__(self):
        # Posição inicial no canto direito e centralizado
        start_x = WIN_WIDTH - 120
        start_y = WIN_HEIGHT // 2 - 60
        super().__init__('Ship_EnemyBoss', (start_x, start_y))

        # Movimento vertical (cima, baixo)
        self.speed_y = 2
        self.direction_y = random.choice([-1, 1])

        # Movimento horizontal (avançar/recuar)
        self.original_x = self.rect.x
        self.advance_distance = 120
        self.advance_speed = 2
        self.advancing = False

    def move(self):
        # Movimento vertical
        self.rect.y += self.speed_y * self.direction_y
        if self.rect.top <= 0 or self.rect.bottom >= WIN_HEIGHT:
            self.direction_y *= -1

        # Movimento horizontal de avanço/recuo
        if not self.advancing and random.randint(0, 200) == 1:
            self.advancing = True
        if self.advancing:
            self.rect.x -= self.advance_speed
            if self.rect.x <= self.original_x - self.advance_distance:
                self.advancing = False
        else:
            if self.rect.x < self.original_x:
                self.rect.x += self.advance_speed
