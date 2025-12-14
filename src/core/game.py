import pygame

def colisao(player, solidos, chao):
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

