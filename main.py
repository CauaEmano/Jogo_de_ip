import pygame
from sys import exit

from src.entities import *
from src.world import *
<<<<<<< HEAD
from src.Objects import *
=======
from src.core import *
>>>>>>> 795a87e8f2296ec22afb1102104143c911ca604e

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
plataforma1 = Plataforma(x=200, y=480, largura=120, altura=30)
plataforma2 = Plataforma(x=450, y=400, largura=150, altura=30)
objetos_solidos.add(chao, plataforma1, plataforma2)


# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    screen.fill('Black')
    objetos_solidos.draw(screen)

    player.draw(screen)
    player.update()

    colisao(player.sprite, objetos_solidos, chao)
    
    pygame.display.update()
    clock.tick(60)