import pygame

def colisao(player, solidos, chao, parede):
    player.no_ar = True
    
    colisoes = [objeto for objeto in solidos if player.hitbox.colliderect(objeto.rect)]
    # colisoes = pygame.sprite.spritecollide(player, solidos, False)

    
    for objeto in colisoes:
        # Se o objeto é uma parede, tratar as laterais primeiro
        if objeto == parede:
            if player.vel_x > 0:
                player.rect.right = objeto.rect.left + 5
            if player.vel_x < 0:
                player.rect.left = objeto.rect.right - 5
                
        if player.hitbox.bottom > objeto.rect.top and player.hitbox.top < objeto.rect.top:
             
            # Se a colisão não foi com a lateral da 'parede' E o player estava caindo ou parado:
            if player.vel_y >= 0 and objeto == chao:
                player.rect.bottom = objeto.rect.top
                player.no_ar = False
                player.vel_y = 0

            # Colisão com as plataformas flutuantes (tem tolerância de 5 pixels)
            elif player.vel_y >= 0 and player.rect.bottom - player.vel_y <= objeto.rect.top + 5:
                player.rect.bottom = objeto.rect.top
                player.no_ar = False
                player.vel_y = 0