import pygame

class Bloco(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura, x, y):
        super().__init__()
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def cair(self):
        self.rect.y += 20

    def mover(self, x, y):
        self.rect.x = x
        self.rect.y = y


