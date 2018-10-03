import pygame
import random

#Definindo cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (255, 255, 0)

class Bloco(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura):
        super().__init__()    #chama o construtor da superclasse
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()    # pega coordenadas



# -- bloco principal
pygame.init()
largura = 600
altura = 400
tela = pygame.display.set_mode([largura, altura])
listaBlocos = pygame.sprite.Group()
listaSprites = pygame.sprite.Group()


x = 0
y = 0
for i in range (20):
        bloco = Bloco(VERDE, 40, 20)
        bloco.rect.x = random.randrange(largura)
        bloco.rect.y = random.randrange(altura)
        listaBlocos.add(bloco)

listaSprites.add(listaBlocos)
blocoVermelho = Bloco(VERMELHO, 40, 20)
blocoVermelho.rect.x = random.randrange(largura)
blocoVermelho.rect.y = random.randrange(altura)
listaSprites.add(blocoVermelho)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    tela.fill(PRETO)
    pos = pygame.mouse.get_pos()
    blocoVermelho.rect.x = pos[0]
    blocoVermelho.rect.y = pos[1]
    pygame.sprite.spritecollide(blocoVermelho, listaBlocos, True)
    listaSprites.draw(tela)
    pygame.display.update()
