import pygame

def colisao(player, solidos, chao):
    # Inicialmente assume que está no ar, a colisão abaixo vai desmentir isso se houver contato
    player.no_ar = True
    
    colisoes = pygame.sprite.spritecollide(player, solidos, False)
    
    for objeto in colisoes:
        # 1. COLISÃO VERTICAL (CHÃO E TOPO DE PLATAFORMAS)
        # Checa se o player está caindo (vel_y >= 0) e se os pés dele estavam acima do objeto no frame anterior
        if player.vel_y >= 0 and player.rect.bottom <= objeto.rect.top + abs(player.vel_y) + 5:
            player.rect.bottom = objeto.rect.top
            player.no_ar = False
            player.vel_y = 0 # Para de aplicar gravidade
            
        # 2. COLISÃO HORIZONTAL (PAREDES)
        # Se não colidiu com o topo, checamos as laterais
        else:
            player.rect.right = objeto.rect.left
            player.rect.left = objeto.rect.right

