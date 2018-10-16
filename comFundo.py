import pygame
from bloco import Bloco

VERMELHO = (255, 0, 0)
LARGURA = 900
ALTURA = 464
FPS = 30
sair = False

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Praia")
fundo = pygame.image.load("praia.jpg").convert_alpha()
bloco = Bloco(VERMELHO, 20, 20, 0, 0)
sprites = pygame.sprite.Group()
sprites.add(bloco)

tela.blit(fundo, (0,0))   # põe o objeto na tela na posição especificada

while sair == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        if event.type == pygame.KEYDOWN:
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_F1]:
                print("F1")


    tela.blit(fundo, (0,0))    # põe o objeto na tela na posição especificada
    sprites.draw(tela)         # desenha demais objetos
    pygame.display.update()


pygame.quit()
















