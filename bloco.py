import pygame

class Bloco(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura, x, y):
        super().__init__()
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def mover(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def cair(self):
        self.rect.y += 20

class Circulo(pygame.sprite.Sprite):
    def __init__(self, x, y):  # posição x,y
        super().__init__()
        self.image = pygame.Surface([40, 40])  # área que conterá o círculo
        self.image.fill((0,0,0))   #cor de fundo
        # Surface, cor, posição dentro da área, raio #
        self.rect = pygame.draw.circle(self.image, (255,0,0), (20,20), 20)
        self.rect.x = x
        self.rect.y = y