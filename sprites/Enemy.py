from random import randint

import pygame
from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

from sprites.Shot import Shot
from utils.constants import AIRPLANE_SIZE


class Enemy(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self, tiro):
        super().__init__()

        self.image = scale(load('images/planes/plane_1/plane_1_blue.png'),AIRPLANE_SIZE)
        self.image = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect(
            center=(800, randint(10, 500))  # retorna posição aleatoria.
        )
        self.tiro = tiro

    def update(self):
        self.rect.x -= 0.1

    def atirar(self):
        if len(self.tiro) < 15:
            self.tiro.add(
                Shot(*self.rect.center, True)
            )



