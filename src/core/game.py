import pygame, random

def colisao(player, solidos, parede):
    # inicialmente assume que está no ar
    player.no_ar = True
    
    colisoes = pygame.sprite.spritecollide(player, solidos, False)
    
    for objeto in colisoes:
        # Checa se o player está caindo (vel_y >= 0) e se os pés dele estavam acima do objeto no frame anterior
        if player.vel_y >= 0 and player.rect.bottom <= objeto.rect.top + abs(player.vel_y) + 5:
            player.rect.bottom = objeto.rect.top
            player.no_ar = False
            player.vel_y = 0 # Para de aplicar gravidade
            
        # Se não colidiu com o topo, checamos as laterais
        elif objeto == parede:
            if player.vel_x > 0:
                player.rect.right = objeto.rect.left
            if player.vel_x < 0:
                player.rect.left = objeto.rect.right

def gerar_itens(coletaveis, Item, quantidade, y=600):
    z = 0
    f = 15000//quantidade
    for i in range(quantidade):
        x = random.randint(z, z + f)
        item = Item(x, y)
        coletaveis.add(item)
        z += f

