import pygame
from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

from utils.constants import TAMANHO, SHOT_SIZE


class Shot(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self, x, y, enemy):
        super().__init__()
        self.enemy = enemy
        self.image = scale(load('images/bala.png'), SHOT_SIZE)
        if self.enemy:
            self.image = pygame.transform.flip(self.image, True, False)

        self.rect = self.image.get_rect(
            center=(x, y)
        )

    def update(self):
        if self.enemy:
            self.rect.x -= 1
            if self.rect.x > TAMANHO[0]:
                self.kill()
        else:
            self.rect.x += 1
            if self.rect.x > TAMANHO[0]:
                self.kill()