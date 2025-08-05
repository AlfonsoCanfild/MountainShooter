import pygame
from code.Entity import Entity


class Explosion(Entity):
    def __init__(self, position: tuple[int, int], frames: list[pygame.Surface]):
        self.name = 'Explosion'
        self.health = 1
        self.score = 0
        self.frames = frames
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 5  # Quanto menor, mais rápida a explosão
        self.total_frames = len(frames)
        self.finished = False  # Vai marcar se já acabou

        self.surf = self.frames[self.current_frame]
        self.rect = self.surf.get_rect(center=position)

    def move(self):
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.current_frame += 1

            if self.current_frame < self.total_frames:
                self.surf = self.frames[self.current_frame]
            else:
                self.finished = True  # Marca que acabou a explosão

