import os
import time
from random import randint

import pygame
from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

from sprites.Shot import Shot
from sprites.Torpedo import Torpedo
from utils.constants import AIRPLANE_SIZE


class Enemy(Sprite):  # criamos o segundo sprint que irá compor o jogo.

    def __init__(self, tiro, torpedo): #construtor
        super().__init__()  # defino essa função será usada em outras classes como herança.

        self.image = scale(load('images/planes/AviaoEUA.png'), AIRPLANE_SIZE)
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(center = (725,250))  # uso a função get_rect na imagem, onde irá me permitir o movimento no plano.
        self.velocidade = 2
        self.tiro = tiro
        self.torpedo = torpedo
        self.ctTorpedos = 0
    def update(self):

        keys = pygame.key.get_pressed()  # recebe o movimento

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.velocidade
        if keys[pygame.K_UP]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN]:
            self.rect.y += self.velocidade

    def atirar(self):
        if len(self.tiro) < 15:
            self.tiro.add(
                Shot(*self.rect.center,True)
            )


    def atirarTorpedo(self):
        if len(self.torpedo) < 15:
            self.torpedo.add(
                Torpedo(*self.rect.center,True)
            )
