import pygame
from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

import Shot
from sprites.Torpedo import Torpedo
from utils.constants import AIRPLANE_SIZE


class Player(Sprite):  # criamos o primeiro sprint que irá compor o jogo, o objeto principal.
    def __init__(self, tiro): #construtor
        super().__init__()  # defino essa função será usada em outras classes como herança.

        self.image = scale(load('images/planes/plane_2/plane_2_yellow.png'),AIRPLANE_SIZE)  # carrego a imagem e em seguida tranfiro para uma variável.
        self.rect = self.image.get_rect()  # uso a função get_rect na imagem, onde irá me permitir o movimento no plano.
        self.velocidade = 2
        self.tiro = tiro

    def update(self):

        keys = pygame.key.get_pressed()  # recebe o movimento

        if keys[pygame.K_a]:
            self.rect.x -= self.velocidade
        if keys[pygame.K_d]:
            self.rect.x += self.velocidade
        if keys[pygame.K_w]:
            self.rect.y -= self.velocidade
        if keys[pygame.K_s]:
            self.rect.y += self.velocidade

    def atirar(self):
        if len(self.tiro) < 15:
            self.tiro.add(
                Shot(*self.rect.center)
            )

    def atirarTorpedo(self):
        if len(self.tiro) < 15:
            self.tiro.add(
                Torpedo(*self.rect.center)
            )
