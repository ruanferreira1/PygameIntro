import pygame
from bloco import Bloco

VERMELHO = (255, 0, 0)
LARGURA = 500
ALTURA = 400
FPS = 30
contador = 0
sair = False

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
fonte = pygame.font.SysFont("monospace", 48)



while sair == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
        if event.type == pygame.MOUSEMOTION:
            contador += 1

    tela.fill((0, 0, 0))
    texto = fonte.render("Vezes: " + str(contador),
            True, (255, 0, 0))
    #texto, antialias, cor, fundo (opcional)
    tela.blit(texto, (0, 0))   #coordenadas
    pygame.display.update()


pygame.quit()
















