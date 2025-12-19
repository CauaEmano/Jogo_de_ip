import pygame

def colisao(player, solidos, chao, parede):
    player.no_ar = True
    
    colisoes = [objeto for objeto in solidos if player.hitbox.colliderect(objeto.hitbox)]
    
    for objeto in colisoes:
        # Lógica para as laterais da parede
        if objeto == parede:
            if player.vel_x > 0: 
                player.rect.right = objeto.hitbox.left + 5
                player.hitbox.right = player.rect.right
            elif player.vel_x < 0: 
                player.rect.left = objeto.hitbox.right - 5
                player.hitbox.left = player.rect.left

        if player.vel_y >= 0:
            if player.hitbox.bottom <= objeto.hitbox.top + player.vel_y + 5:
                
                player.hitbox.bottom = objeto.hitbox.top
                
                player.rect.bottom = player.hitbox.bottom
                
                player.vel_y = 0
                player.no_ar = False

def colisao_subboss(player, subboss):
    
    colisoes = player.hitbox.colliderect(subboss.rect)
    if colisoes:
        if player.vel_x > 0: 
            player.rect.right = subboss.hitbox.left + 5
            player.hitbox.right = player.rect.right
        elif player.vel_x < 0: 
            player.rect.left = subboss.hitbox.right - 5
            player.hitbox.left = player.rect.left