import pygame



class Bicho(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.setaDireita = pygame.image.load("direita.png").convert_alpha()
        self.setaEsquerda = pygame.image.load("esquerda.png").convert_alpha()
        self.image = self.setaDireita
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def definirImagem(self):
        tecla = pygame.key.get_pressed()
        if tecla[pygame.K_RIGHT]:
            self.image = self.setaDireita
            self.rect.x += 2
        if tecla[pygame.K_LEFT]:
            self.image = self.setaEsquerda
            self.rect.x -= 2


# ----
PRETO = (0, 0, 0)
LARGURA = 500
ALTURA = 500
sair = False

pygame.init()
clock = pygame.time.Clock()
tela = pygame.display.set_mode((LARGURA, ALTURA))
seta = Bicho(250, 250 )
objetos = pygame.sprite.Group()
objetos.add(seta)

while sair == False:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = True

    seta.definirImagem()
    tela.fill(PRETO)
    objetos.draw(tela)
    pygame.display.update()


pygame.quit()