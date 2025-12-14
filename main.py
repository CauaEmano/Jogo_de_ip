import pygame
from sys import exit

from src import *

# Variáveis e funções essenciais
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()

# Objeto do player
player = pygame.sprite.GroupSingle()
player.add(Player())

# Objetos do mundo
objetos_solidos = pygame.sprite.Group()
chao = Chao()
parede = Parede(x=-50, y=-100, largura=50, altura=700)
plataforma1 = Plataforma(x=200, y=480, largura=120, altura=30)
plataforma2 = Plataforma(x=450, y=400, largura=150, altura=30)
objetos_solidos.add(chao, parede, plataforma1, plataforma2)

coletaveis = pygame.sprite.Group()
guarana = Guarana(500, 550)
coletaveis.add(guarana)

camera = Camera(1280, 720)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.fill('Black')
    
    camera.update(player.sprite) # atualiza a posição da câmera
    coletaveis.update()
    player.update()
    colisao(player.sprite, objetos_solidos, parede)
    colidiu = pygame.sprite.spritecollide(player.sprite, coletaveis, True, pygame.sprite.collide_mask)

    
    # Desenha objetos sólidos
    for sprite in objetos_solidos:
        screen.blit(sprite.image, camera.aplicar_rect(sprite))

    # Desenha coletáveis
    for sprite in coletaveis:
        screen.blit(sprite.image, camera.aplicar_rect(sprite))

    # Desenha o player
    screen.blit(player.sprite.image, camera.aplicar_rect(player.sprite))

    pygame.display.update()
    clock.tick(60)