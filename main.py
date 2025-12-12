import pygame
from src.entities.player import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle()
player.add(Player())


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            

    screen.fill('Black')
    player.draw(screen)
    player.update()

    pygame.display.update()
    clock.tick(60)