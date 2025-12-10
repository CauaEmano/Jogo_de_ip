import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()

indio_surf = pygame.image.load('imagens/indio.png').convert_alpha()
indio_rect = indio_surf.get_rect(midbottom = (80, 300))
gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                gravity = -20


    keys = pygame.key.get_pressed()  
    if keys[pygame.K_LEFT]:
        indio_rect.x -= 2
    if keys[pygame.K_RIGHT]:
        indio_rect.x += 2
    
    gravity += 2
    indio_rect.y += gravity
    if indio_rect.y >= 300:
        indio_rect.y = 300


            

    screen.fill('Red')
    screen.blit(indio_surf,indio_rect)
    pygame.display.update()
    clock.tick(60)