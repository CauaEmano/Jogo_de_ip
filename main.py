import pygame
from sys import exit

from src.entities import *
from src.world import *

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

# Verificação de colisão
def colisao(player, solidos):
    if pygame.sprite.spritecollide(player, solidos, False) != chao:
        player.no_ar = True
        
    for objeto in pygame.sprite.spritecollide(player, solidos, False):
        # Mantém o jogador no chão
        if objeto == chao and player.rect.bottom >= objeto.rect.top:
            player.rect.bottom = objeto.rect.top
            player.no_ar = False
        
        # Mantém o jogador acima da plataforma flutuante
        elif player.vel_y >= 0 and player.rect.bottom - player.vel_y <= objeto.rect.top + 5:
            player.rect.bottom = objeto.rect.top
            player.no_ar = False

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

    colisao(player.sprite, objetos_solidos)
    
    pygame.display.update()
    clock.tick(60)