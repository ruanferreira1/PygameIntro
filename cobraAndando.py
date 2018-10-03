import pygame
from cobra import Cobra

LARGURA = 800
ALTURA = 500
FPS = 200
terminou = False
# define colors
BRANCO = (255, 255, 255)
# initialize pygame and create window
pygame.init()
pygame.font.init()
fonte = pygame.font.SysFont('Calibri', 30)
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Cobrinha")
clock = pygame.time.Clock()  # controle do tempo para atualização da tela

# grupo de personagens
listaSprites = pygame.sprite.Group()
cobra = Cobra(-235, 100)
listaSprites.add(cobra)

while terminou == False:
    # mantem o jogo rodando na velocidade correta
    clock.tick(FPS)   # frequência de atualização

    # processa input (eventos)
    for event in pygame.event.get():
        # verifica fechamento da janela
        if event.type == pygame.QUIT:
            terminou = True

    cobra.andar()

    if cobra.rect.x > 800:
        cobra.rect.x = -235

    # atualiza tela
    tela.fill(BRANCO)
    listaSprites.draw(tela)
    pygame.display.update()

pygame.quit()