import pygame

from bloco import Bloco

LARGURA = 400
ALTURA = 500
FPS = 30

BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Meu jogo")
#lista de personagens
listaSprites = pygame.sprite.Group()
bloco = Bloco(AZUL, 20, 20, 30, 0)
grama = Bloco(VERDE, LARGURA, 30, 0, ALTURA - 30 )
listaSprites.add(bloco)
listaSprites.add(grama)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_DOWN]:
                bloco.cair()
                bateu = pygame.sprite.collide_rect(bloco, grama)
                if bateu == True:
                    grama.image.fill(VERMELHO)

    tela.fill(PRETO)
    listaSprites.draw(tela)
    pygame.display.update()



















