import pygame, random

def colisao(player, solidos, parede):
    player.no_ar = True
    
    colisoes = pygame.sprite.spritecollide(player, solidos, False)
    
    for objeto in colisoes:
        # Se o objeto é uma parede, tratar as laterais primeiro
        if objeto == parede:
            if player.vel_x > 0:
                player.rect.right = objeto.rect.left
            if player.vel_x < 0:
                player.rect.left = objeto.rect.right
                
        if player.rect.bottom > objeto.rect.top and player.rect.top < objeto.rect.top:
             
            # Se a colisão não foi com a lateral da 'parede' E o player estava caindo ou parado:
            if player.vel_y >= 0:
                player.rect.bottom = objeto.rect.top
                player.no_ar = False
                player.vel_y = 0 
                

def gerar_itens(coletaveis, Item, quantidade, y=600):
    z = 0
    f = 15000//quantidade
    for i in range(quantidade):
        x = random.randint(z, z + f)
        item = Item(x, y)
        coletaveis.add(item)
        z += f

