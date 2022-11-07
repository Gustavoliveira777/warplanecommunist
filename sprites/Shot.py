from pygame.image import load
from pygame.sprite import Sprite
from pygame.transform import scale

from utils.constants import TAMANHO, SHOT_SIZE


class Shot(Sprite):  # criamos o segundo sprint que irá compor o jogo.
    def __init__(self, x, y):
        super().__init__()

        self.image = scale(load('images/planes/torpedo/fire_ball_1.png'),SHOT_SIZE)
        self.rect = self.image.get_rect(
            center=(x, y)
        )

    def update(self):
        self.rect.x += 1
        if self.rect.x > TAMANHO[0]:
            self.kill()