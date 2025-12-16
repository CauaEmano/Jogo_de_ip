import pygame
from sys import exit

from src import *

# Variáveis e funções essenciais
pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()

# Objeto do player
player = pygame.sprite.GroupSingle()
player.add(Player())

bullet_group = pygame.sprite.Group()

# Objetos do mundo
objetos_solidos = pygame.sprite.Group()
chao = Chao()
parede = Parede(x=-50, y=-100, largura=50, altura=700)
plataforma1 = Plataforma(x=200, y=480, largura=120, altura=30)
plataforma2 = Plataforma(x=450, y=400, largura=150, altura=30)
objetos_solidos.add(chao, parede, plataforma1, plataforma2)

coletaveis = pygame.sprite.Group()
gerar_itens(coletaveis, Guarana, 2)
gerar_itens(coletaveis, Pedra, 2)

inimigos = pygame.sprite.Group()
tiros_inimigos = pygame.sprite.Group()
onca_teste = Onca(pos_x=1200, pos_y=600, velocidade=5, vida=1)
tucano_teste = Tucano(pos_x=1000, pos_y=100, velocidade=3, vida=1, grupo_tiros=tiros_inimigos)
capivara_teste = Capivara(pos_x=1100, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
inimigos.add(onca_teste, tucano_teste, capivara_teste)

interface = UI()

camera = Camera(1280, 720, 15000, 720)

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.sprite.shoot(bullet_group, objetos_solidos, coletaveis, Pedra)
            
    screen.fill('Black')
    
    camera.update(player.sprite) # atualiza a posição da câmera

    bullet_group.update()
    coletaveis.update()
    player.update()

    colisao(player.sprite, objetos_solidos, parede)

    # Colisão do tiro do Player com Inimigos (Dano ao Inimigo)
    colisoes_pedra_inimigo = pygame.sprite.groupcollide(bullet_group, inimigos, True, False) 
    
    if colisoes_pedra_inimigo:
        for inimigos_atingidos in colisoes_pedra_inimigo.values():
            for inimigo in inimigos_atingidos:
                # Chama o método de dano que definimos na classe Inimigo
                inimigo.take_damage(1)

    # Se houver colisão, chama take_damage no player (inimigo não é removido: False)
    colisoes_contato = pygame.sprite.spritecollide(player.sprite, inimigos, False, pygame.sprite.collide_mask)
    if colisoes_contato:
        atacante = colisoes_contato[0]
        player.sprite.take_damage(10, atacante.rect)

    # Se houver colisão, chama take_damage e remove o tiro (True)
    colisoes_tiro_inimigo = pygame.sprite.spritecollide(player.sprite, tiros_inimigos, True, pygame.sprite.collide_mask)
    if colisoes_tiro_inimigo:
        tiro_atacante = colisoes_tiro_inimigo[0]
        player.sprite.take_damage(5, tiro_atacante.rect)

    
    
    colidiu = pygame.sprite.spritecollide(player.sprite, coletaveis, True, pygame.sprite.collide_mask)
    for item in colidiu: #Itera sobre os itens colididos
        if player.sprite.inventario.get(item.tipo, ''):
            player.sprite.inventario[item.tipo] += 1
        else:
            player.sprite.inventario[item.tipo] = 1

    # Desenha objetos sólidos
    for sprite in objetos_solidos:
        screen.blit(sprite.image, camera.aplicar_rect(sprite))

    # Desenha coletáveis
    for sprite in coletaveis:
        screen.blit(sprite.image, camera.aplicar_rect(sprite))

    # Desenha o player
    screen.blit(player.sprite.image, camera.aplicar_rect(player.sprite))

    player_rect = player.sprite.rect 

    for inimigo in inimigos:
        inimigo.update(objetos_solidos, player_rect) 
        
    tiros_inimigos.update() 

    for inimigo in inimigos:
        screen.blit(inimigo.image, camera.aplicar_rect(inimigo))
        
    for bala in tiros_inimigos:
        screen.blit(bala.image, camera.aplicar_rect(bala))

    for sprite in bullet_group:
        screen.blit(sprite.image, camera.aplicar_rect(sprite))

    interface.display(screen, player.sprite.inventario, player.sprite.vida, player.sprite.max_vida)

    pygame.display.update()
    clock.tick(60)