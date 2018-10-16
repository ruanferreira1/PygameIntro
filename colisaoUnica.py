from bloco import Bloco
import pygame

BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
LARGURA = 500
ALTURA = 500
FPS = 200
sair = False

pygame.init()
clock = pygame.time.Clock()
contador = 0
fonte = pygame.font.SysFont("monospace", 30)
texto = fonte.render("Vezes: " + str(contador),True, (255, 0, 0))
tela = pygame.display.set_mode((LARGURA, ALTURA))
parede = Bloco(VERMELHO, 20, 300, 150, 30)
objetos = pygame.sprite.Group()
paredes = pygame.sprite.Group()
paredes.add(parede)
objetos.add(paredes)

tijolo = Bloco(AZUL, 20, 20, 0, 100)
objetos.add(tijolo)


while sair == False:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True
    tijolo.andarDireita()
    if (tijolo.rect.x + 20) == parede.rect.x:
        contador += 1
        texto = fonte.render("Vezes: " + str(contador),True, (255, 0, 0))
    if tijolo.rect.x > LARGURA:
        tijolo.rect.x = -20

    tela.fill(BRANCO)    # põe o objeto na tela na posição especificada
    objetos.draw(tela)         # desenha demais objetos
    tela.blit(texto, (0, 0))  # coordenadas
    pygame.display.update()


pygame.quit()
















