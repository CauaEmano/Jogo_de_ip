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
gerar_itens(coletaveis, Pipa, 1, 450)

inimigos = pygame.sprite.Group()
tiros_inimigos = pygame.sprite.Group()
onca_teste = Onca(pos_x=1200, pos_y=600, velocidade=10, vida=1)
tucano_teste = Tucano(pos_x=1000, pos_y=100, velocidade=3, vida=1, grupo_tiros=tiros_inimigos)
capivara_teste = Capivara(pos_x=1100, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
inimigos.add(onca_teste, tucano_teste, capivara_teste)

interface = UI()

camera = Camera(1280, 720, 15000, 720)

def reiniciar_jogo():
    # Reset do Player
    player.add(Player())
    
    # Limpa grupos
    bullet_group.empty()
    tiros_inimigos.empty()
    inimigos.empty()
    coletaveis.empty()
    
    # Recria os inimigos e itens
    onca_teste = Onca(pos_x=1200, pos_y=600, velocidade=5, vida=1)
    tucano_teste = Tucano(pos_x=1000, pos_y=100, velocidade=3, vida=1, grupo_tiros=tiros_inimigos)
    capivara_teste = Capivara(pos_x=1100, pos_y=600, vida=1, grupo_tiros=tiros_inimigos)
    inimigos.add(onca_teste, tucano_teste, capivara_teste)
    
    gerar_itens(coletaveis, Guarana, 2)
    gerar_itens(coletaveis, Pedra, 2)

fonte_game_over = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 30)
fonte_retry = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 20)

background = pygame.image.load('assets/images/cenario.png').convert()
background = pygame.transform.scale(background, (1280, 850))

# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player.sprite:
                player.sprite.shoot(bullet_group, objetos_solidos, coletaveis, Pedra)
            
            if not player.sprite and event.key == pygame.K_r:
                reiniciar_jogo()
            
    screen.blit(background, (0,0))
    
    p = player.sprite

    if p:
        camera.update(p)
        p.update()
        
        colisao(p, objetos_solidos, parede) 

        if pygame.sprite.spritecollide(p, inimigos, False, pygame.sprite.collide_mask):
            p.take_damage(1)

        # 2. Player toma dano (Tiros dos inimigos)
        colisoes_tiro_inimigo = pygame.sprite.spritecollide(p, tiros_inimigos, True, pygame.sprite.collide_mask)
        if colisoes_tiro_inimigo:
            p.take_damage(1)

        # 3. Player pega itens
        colidiu = pygame.sprite.spritecollide(p, coletaveis, True, pygame.sprite.collide_mask)
        for item in colidiu:
            p.inventario[item.tipo] = p.inventario.get(item.tipo, 0) + 1
            if item.tipo == "guarana" and player.sprite.vida < player.sprite.max_vida:
                player.sprite.vida += 1

        batidas_inimigo = pygame.sprite.groupcollide(bullet_group, inimigos, True, False, pygame.sprite.collide_mask)
        if batidas_inimigo:
            for lista_inimigos in batidas_inimigo.values():
                for inimigo in lista_inimigos:
                    inimigo.take_damage(1) 

        player_rect = p.rect
    else:
        player_rect = pygame.Rect(0,0,0,0)

    # Atualizar grupos
    bullet_group.update()
    coletaveis.update()
    tiros_inimigos.update()
    for inimigo in inimigos:
        inimigo.update(objetos_solidos, player_rect)

    # --- DESENHO DO MUNDO ---
    for sprite in objetos_solidos:
        screen.blit(sprite.image, camera.aplicar_rect(sprite))
    for sprite in coletaveis:
        screen.blit(sprite.image, camera.aplicar_rect(sprite))
    for sprite in bullet_group:
        screen.blit(sprite.image, camera.aplicar_rect(sprite))
    for inimigo in inimigos:
        screen.blit(inimigo.image, camera.aplicar_rect(inimigo))
    for bala in tiros_inimigos:
        screen.blit(bala.image, camera.aplicar_rect(bala))

    # Interface e Game Over
    if p:
        screen.blit(p.image, camera.aplicar_rect(p))
        interface.display(screen, p.inventario, p.vida, p.max_vida)
    else:
        overlay = pygame.Surface((1280, 720))
        overlay.set_alpha(150)
        overlay.fill((30, 0, 0))
        screen.blit(overlay, (0,0))

        texto_morte = fonte_game_over.render("Voce Morreu", True, (255, 50, 50))
        screen.blit(texto_morte, texto_morte.get_rect(center=(640, 320)))

        texto_r = fonte_retry.render("Aperte R para reiniciar", True, "White")
        screen.blit(texto_r, texto_r.get_rect(center=(640, 420)))

        interface.display(screen, {}, 0, 12)

    pygame.display.update()
    clock.tick(60)