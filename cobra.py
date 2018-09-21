import pygame

class Cobra(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()    #chama o construtor da superclasse
        self.image = pygame.image.load("cobraAndando.jpg").convert_alpha()
        self.rect = self.image.get_rect()    # pega coordenadas
        self.rect.x = x
        self.rect.y = y

    def andar(self):
        self.rect.x += 2