import pygame, random
from bloco import Bloco
import random

#Definindo cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
PRATA = (192,192,192)

# -- criação da tela
pygame.init()
fonte = pygame.font.SysFont("comicsansms", 30)
LARGURA = 600
ALTURA = 400
pontos = 0
tela = pygame.display.set_mode([LARGURA, ALTURA])
pygame.display.set_caption("Come Blocos")
mouse = pygame.mouse     # encurta o nome
mouse.set_visible(False) # esconde o ponteiro
amarelos = pygame.sprite.Group()       # blocos amarelos
todosObjetos = pygame.sprite.Group()   # todos blocos

for i in range (20):
    x = random.randrange(LARGURA)
    y = random.randrange(ALTURA)
    bloco = Bloco(AMARELO, 40, 20, x, y)
    amarelos.add(bloco)

todosObjetos.add(amarelos)
x = random.randrange(LARGURA)
y = random.randrange(ALTURA)
blocoVermelho = Bloco(VERMELHO, 40, 20, x, y)
todosObjetos.add(blocoVermelho)


while True:
    filaEventos = pygame.event.get()
    # percorre a fila de eventos
    for evento in filaEventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if evento.type == pygame.KEYDOWN:
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_F1]:
                print("F1")
            if tecla[pygame.K_ESCAPE]:
                pygame.quit()
                exit()

        if evento.type == pygame.MOUSEMOTION:
            pos = mouse.get_pos()
            blocoVermelho.mover(pos[0], pos[1])
            lista = []
            lista = pygame.sprite.spritecollide(blocoVermelho, amarelos, True)
            pontos += len(lista)
            # texto, antialias, cor, fundo (opcional)
            texto = fonte.render("Pontos: " + str(pontos), True, (BRANCO))


    tela.fill(PRETO)
    todosObjetos.draw(tela)
    tela.blit(texto, (0, 0))  # texto + coordenadas

    pygame.display.update()
