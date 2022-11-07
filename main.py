import pygame
from pygame import display
from pygame import event
from pygame.image import load
from pygame.locals import QUIT, KEYUP, K_SPACE
from pygame.sprite import Group, GroupSingle, groupcollide
from pygame.time import Clock
from pygame.transform import scale

from sprites.Enemy import Enemy
from sprites.Player import Player
from utils.constants import TAMANHO, TITLE, FUNDO_URL

pygame.init()
disparo = 0
superficie = display.set_mode((TAMANHO))  # variável que absorve a contrução do plano.
display.set_caption(TITLE)  # funcão que escreve o nome da janela.
fundo = scale(load(FUNDO_URL),
              TAMANHO)  # como a imagem é maior que o plano, usamos a função SCALE para transformar a imagem no TAMANHO do plano.


# class Chefao(Sprite):  # criamos o segundo sprint que irá compor o jogo.
#     def __init__(self):
#         super().__init__()
#
#         self.image = load('images/inimigo_2.png')
#         self.rect = self.image.get_rect(
#             center=(800, 300)  # retorna posição aleatoria.
#         )
#
#     def update(self):
#         self.rect.x -= 0.1


# Espaço do display
grupo_inimigo = Group()
grupo_chefao = Group()
players_group = Group()
player = Player(players_group)
grupo_geral = GroupSingle(player)

grupo_inimigo.add(Enemy())
# grupo_chefao.add(Chefao())

round = 0
morte = 0
clock = Clock()
count = 1

while True:
    clock.tick(120)
    if round % 120 == 0:
        grupo_inimigo.add(Enemy())

    superficie.blit(fundo, (
        0, 0))  # Faço o Bit Blit na imagem no ponto 0,0 do plano definimo, com isso consigo inserir a imagem no jogo.
    grupo_geral.draw(superficie)  # Desenhar o objeto no plano

    if (morte < 1):
        grupo_inimigo.draw(superficie)
        grupo_inimigo.update()
        disparo = 0
    else:
        grupo_chefao.draw(superficie)
        grupo_chefao.update()

    players_group.draw(superficie)

    grupo_geral.update()
    players_group.update()

    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYUP:
            if evento.key == K_SPACE:
                if count % 5 == 0:
                    player.atirarTorpedo()
                    count = 1
                else:
                    player.atirar()
                    count += 1


    if groupcollide(players_group, grupo_inimigo, True, True):
        morte += 1

    if disparo == 10:
        resposta = True
    else:
        resposta = False

    if groupcollide(players_group, grupo_chefao, True, resposta):
        disparo += 1

    round += 1
    display.update()  # a função update atualiza os frames.