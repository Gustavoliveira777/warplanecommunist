import pygame
from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

from sprites.Shot import Shot
from sprites.Torpedo import Torpedo
from utils.constants import AIRPLANE_SIZE


class Player(Sprite):  # criamos o primeiro sprint que irá compor o jogo, o objeto principal.
    def __init__(self, tiro, torpedo): #construtor
        super().__init__()  # defino essa função será usada em outras classes como herança.

        self.image = scale(load('images/planes/AviaoComuna.png'),AIRPLANE_SIZE)  # carrego a imagem e em seguida tranfiro para uma variável.
        self.rect = self.image.get_rect(center = (75,250))  # uso a função get_rect na imagem, onde irá me permitir o movimento no plano.
        self.velocidade = 2
        self.tiro = tiro
        self.torpedo = torpedo
        self.ctTiro = 0
        self.ctTorpedos = 0
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
                Shot(*self.rect.center,False)
            )
            self.ctTiro += 1


    def atirarTorpedo(self):
        if len(self.torpedo) < 15:
            self.torpedo.add(
                Torpedo(*self.rect.center,False)
            )
