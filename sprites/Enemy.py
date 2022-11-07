from random import randint

import pygame
from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

from utils.constants import AIRPLANE_SIZE


class Enemy(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self):
        super().__init__()

        self.image = scale(load('images/planes/plane_1/plane_1_blue.png'),AIRPLANE_SIZE)
        self.image = pygame.transform.flip(self.image,True,False)
        self.rect = self.image.get_rect(
            center=(800, randint(10, 500))  # retorna posição aleatoria.
        )

    def update(self):
        self.rect.x -= 0.1
