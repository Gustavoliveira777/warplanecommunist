import pygame
from pygame import display, K_LSHIFT, K_LCTRL, K_RSHIFT, K_RCTRL
from pygame import event
from pygame.image import load
from pygame.locals import QUIT, KEYUP
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

# Grupos
fogo_player2 = Group()
fogo_player1 = Group()
torpedo_player1 = Group()
torpedo_player2 = Group()
player1 = Player(fogo_player1,torpedo_player1)
player2 = Enemy(fogo_player2,torpedo_player2)
grupo_player1 = GroupSingle(player1)
grupo_player2 = Group()
grupo_player2.add(player2)

round = 0
morte = 0
clock = Clock()
count = 1
# Controlo de pontuação e danos
pontosPlayer1 = 0
pontosPlayer2 = 0
balasPlayer1 = 10
balasPlayer2 = 10
torpedoPlayer1 = 3
torpedoPlayer2 = 3
mortesPlayer1 = 0
mortesPlayer2 = 0
danoPlayer2 = 0
danoPlayer1 = 0
clockstampMortem = 0
morteRecenteP1 = False
morteRecenteP2 = False
interactionsMark = 0


# Funções gerais
def placardBar():
    rect = pygame.Rect(0,0,800,20)
    pygame.draw.rect(superficie,(51,51,51),rect,0,0,0,0,0)
def placard_1():
    # img_municao = scale(load("images/bala.png"),(110/5,115/5))
    # rect_municao = img_municao.get_rect()
    # rect_municao.top = -2
    # rect_municao.left = 68
    #
    # img_torpedo = scale(load("images/planes/torpedo/torpedo.png"),(415/18,226/18))
    # rect_torpedo = img_torpedo.get_rect()
    # rect_torpedo.top = 4
    # rect_torpedo.left = 124
    font = pygame.font.SysFont("arial", 11, False, False)
    placard_fase1_1 = font.render('Dano: {:d} | Munição : {:d} | Míssel : {:d} | Pontos: {:.2f}'.format(danoPlayer1,balasPlayer1,torpedoPlayer1,pontosPlayer1),
                                  True, (255, 255, 255))
    placard_fase1_rect_1 = placard_fase1_1.get_rect()
    placard_fase1_rect_1.top = 3
    placard_fase1_rect_1.x = 10
    superficie.blit(placard_fase1_1, placard_fase1_rect_1)
    # superficie.blit(img_municao,rect_municao)
    # superficie.blit(img_torpedo,rect_torpedo)

def placard_2():
    font = pygame.font.SysFont("arial", 11, False, False)
    placard_fase1_2 = font.render('Dano: {:d} | Munição : {:d} | Míssel : {:d} | Pontos: {:.2f}'.format(danoPlayer2,balasPlayer2,torpedoPlayer2,pontosPlayer2),
                                  True, (255, 255, 255))
    placard_fase1_rect_2 = placard_fase1_2.get_rect()
    placard_fase1_rect_2.top = 3
    placard_fase1_rect_2.x = 555
    superficie.blit(placard_fase1_2, placard_fase1_rect_2)

def limpaJogo():
    grupo_player1.empty()
    grupo_player2.empty()
    fogo_player1.empty()
    fogo_player2.empty()


def interactions(type):  # Mensagens do jogo
    if type == 1:
        font = pygame.font.SysFont("arial", 30, True, False)
        placard_fase1 = font.render("O Comunismo Venceu!",
                                    True, (252, 7, 3))
        rect_txt = placard_fase1.get_rect(center=superficie.get_rect().center)
        rect = pygame.Rect(0, 0, rect_txt.width + 50, rect_txt.height + 50)
        rect.center = rect_txt.center
        pygame.draw.rect(superficie, (51, 51, 51), rect, 0, 7, 7, 7, 7)
        superficie.blit(placard_fase1, rect_txt)
    elif type == 2:
        font = pygame.font.SysFont("arial", 30, True, False)
        placard_fase1 = font.render("O Capitalismo venceu, Marx estava errado",
                                    True, (14, 11, 163))
        rect_txt = placard_fase1.get_rect(center=superficie.get_rect().center)
        rect = pygame.Rect(0, 0, rect_txt.width + 50, rect_txt.height + 50)
        rect.center = rect_txt.center
        pygame.draw.rect(superficie, (51, 51, 51), rect, 0, 7, 7, 7, 7)
        superficie.blit(placard_fase1, rect_txt)
    elif type == 3:
        font = pygame.font.SysFont("arial", 30, True, False)
        placard_fase1 = font.render("Eram dois japoneses lutando :|",
                                True, (242, 242, 10))
        rect_txt = placard_fase1.get_rect(center=superficie.get_rect().center)
        rect = pygame.Rect(0, 0, rect_txt.width + 50, rect_txt.height + 50)
        rect.center = rect_txt.center
        pygame.draw.rect(superficie, (51, 51, 51), rect, 0, 7, 7, 7, 7)
        superficie.blit(placard_fase1, rect_txt)
    else:
        pass


while True:
    clock.tick(120)

    superficie.blit(fundo, (
        0, 0))  # Faço o Bit Blit na imagem no ponto 0,0 do plano definimo, com isso consigo inserir a imagem no jogo.
    # Controlo de mensagens, interações e placard
    placardBar()
    interactions(interactionsMark)
    placard_1()
    placard_2()
    # Controlo de respawn e recarga
    if round % 200 == 0:
        if mortesPlayer2 < 3 and morteRecenteP2:
            morteRecenteP2 = False
            grupo_player2.add(player2)
        if mortesPlayer1 < 3 and morteRecenteP1:
            morteRecenteP1 = False
            grupo_player1.add(player1)
    if round % 350 == 0:
        if balasPlayer1 == 0:
            balasPlayer1 = 5
        if balasPlayer2 == 0:
            balasPlayer2 = 5

    grupo_player1.draw(superficie)  # Desenhar o objeto no plano
    grupo_player2.draw(superficie)
    fogo_player1.draw(superficie)
    fogo_player2.draw(superficie)
    torpedo_player1.draw(superficie)
    torpedo_player2.draw(superficie)

    grupo_player1.update()  # Desenhar o objeto no plano
    grupo_player2.update()
    fogo_player1.update()
    fogo_player2.update()
    torpedo_player1.update()
    torpedo_player2.update()
    # Controlo de eventos
    for evento in event.get():  # Events
        if evento.type == QUIT:
            pygame.quit()

        if evento.type == KEYUP:
            if evento.key == K_LSHIFT:
                if balasPlayer1 > 0:
                    balasPlayer1 -= 1
                    player1.atirar()
            if evento.key == K_LCTRL:
                if torpedoPlayer1 > 0:
                    torpedoPlayer1 -= 1
                    player1.atirarTorpedo()
            if evento.key == K_RSHIFT:
                if balasPlayer2 > 0:
                    balasPlayer2 -= 1
                    player2.atirar()
            if evento.key == K_RCTRL:
                if torpedoPlayer2 > 0:
                    torpedoPlayer2 -= 1
                    player2.atirarTorpedo()
    # Controlo de mortes
    if groupcollide(fogo_player1, grupo_player2, True, False): #Morte na bala do Player 2
        danoPlayer2 += 1
        pontosPlayer1 += 0.10
        print(f'Dano P2: {danoPlayer2}\nPontos P1{pontosPlayer1}')
        if danoPlayer2 >= 10:
            player2.kill()
            danoPlayer2 = 0
            mortesPlayer2 += 1
            pontosPlayer1 += 5
            morteRecenteP2 = True
    if groupcollide(torpedo_player1, grupo_player2, True, False): #Morte por missel do Player 2
        danoPlayer2 += 3
        pontosPlayer1 += 0.5
        print(f'Dano P2: {danoPlayer2}\nPontos P1{pontosPlayer1}')
        if danoPlayer2 >= 10:
            player2.kill()
            danoPlayer2 = 0
            mortesPlayer2 += 1
            pontosPlayer1 += 5
            morteRecenteP2 = True

    if groupcollide(torpedo_player2, grupo_player1, True, False): #Morte na bala do Player 1
        danoPlayer1 += 3
        pontosPlayer2 += 0.5
        if danoPlayer1 >= 10:
            player1.kill()
            danoPlayer1 = 0
            mortesPlayer1 += 1
            pontosPlayer2 += 5
            morteRecenteP1 = True
    if groupcollide(fogo_player2, grupo_player1, True, False): #Morte por torpedo do Player 1
        danoPlayer1 += 1
        pontosPlayer2 += 0.1
        if danoPlayer1 >= 10:
            player1.kill()
            danoPlayer1 = 0
            mortesPlayer1 += 1
            pontosPlayer2 += 5
            morteRecenteP1 = True

    if groupcollide(grupo_player1,grupo_player2,True,True):
        morteRecenteP1 = False
        morteRecenteP2 = False
        limpaJogo()
        interactionsMark = 3

    groupcollide(fogo_player1,fogo_player2,True,True)
    groupcollide(torpedo_player1,torpedo_player2,True,True)

    # Controlo de pontos
    if pontosPlayer1 >= 15:
        morteRecenteP1 = False
        morteRecenteP2 = False
        limpaJogo()
        interactionsMark = 1
    elif pontosPlayer2 >= 15:
        morteRecenteP1 = False
        morteRecenteP2 = False
        limpaJogo()
        interactionsMark = 2

    round += 1
    # print(f'Round:{round}')
    display.update()  # a função update atualiza os frames.
