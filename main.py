import pygame
from sys import exit
from src import *

# Variáveis e funções essenciais
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Jogo')
clock = pygame.time.Clock()

# NOVO: Variável de estado e Fonte para o menu
em_jogo = False 
fonte_menu = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 50)

# Objeto do player
player = pygame.sprite.GroupSingle()
player.add(Player())
subboss = pygame.sprite.GroupSingle()
boszinho = SubBoss(pos_x=500, pos_y=600)
subboss.add(boszinho)

bullet_group = pygame.sprite.Group()

# Objetos do mundo
objetos_solidos = pygame.sprite.Group()
objetos_solidos_pedra = pygame.sprite.Group()
chao = Chao()
parede = Parede(x=-50, y=-100, largura=50, altura=700)
plataformas = [Plataforma(x=200, y=480, largura=120, altura=30),
Plataforma(x=450, y=400, largura=150, altura=30),
Plataforma(x=1200, y=480, largura=120, altura=30),
Plataforma(x=1450, y=400, largura=150, altura=30),
Plataforma(x=2200, y=480, largura=120, altura=30),
Plataforma(x=2450, y=400, largura=150, altura=30),
Plataforma(x=3200, y=480, largura=120, altura=30),
Plataforma(x=3450, y=400, largura=150, altura=30)]
objetos_solidos.add(chao, parede, plataformas)
objetos_solidos_pedra.add(chao, parede)

#Coletáveis
coletaveis = pygame.sprite.Group()

#Inimigos
inimigos = pygame.sprite.Group()
tiros_inimigos = pygame.sprite.Group()

player, bullet_group, tiros_inimigos, inimigos, coletaveis = carregar_nivel(player, bullet_group, tiros_inimigos, inimigos, coletaveis)
interface = UI()

camera = Camera(1280, 720, 15000, 720)

fonte_game_over = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 30)
fonte_retry = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 20)

background = Background()
subboss_spawnado = False
# Loop principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            # --- NOVO: Iniciar o jogo ao apertar Espaço ou Enter ---
            if not em_jogo:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    em_jogo = True
            
            # Sua lógica original de tiro e restart
            elif event.key == pygame.K_SPACE and player.sprite:
                player.sprite.shoot(bullet_group, objetos_solidos_pedra, coletaveis, Pedra)
            
            if not player.sprite and event.key == pygame.K_r:
                player, bullet_group, tiros_inimigos, inimigos, coletaveis = carregar_nivel(player, bullet_group, tiros_inimigos, inimigos, coletaveis)
    
    # tela inicial
    if not em_jogo:
        screen.blit(background.image, (0,0)) 
        screen.blit(chao.image, (0,580))
        
        
        texto_titulo = fonte_menu.render("Helicônia", True, (240, 248, 255))
        texto_start = fonte_retry.render("Pressione ESPAÇO para Iniciar", True, "Yellow")
        
        screen.blit(texto_titulo, texto_titulo.get_rect(center=(640, 300)))
        screen.blit(texto_start, texto_start.get_rect(center=(640, 450)))
    
    # jogo
    else:
        p = player.sprite
        s = subboss.sprite

        if p:
            camera.update(p)
            p.update()
            
            colisao(p, objetos_solidos, chao, parede) 

            if pygame.sprite.spritecollide(p, inimigos, False, pygame.sprite.collide_mask):
                p.take_damage(1)

            colisoes_tiro_inimigo = pygame.sprite.spritecollide(p, tiros_inimigos, True, pygame.sprite.collide_mask)
            if colisoes_tiro_inimigo:
                p.take_damage(1)

            colidiu = [objeto for objeto in coletaveis if p.hitbox.colliderect(objeto.rect)]
            for item in colidiu:
                item.kill()
                p.inventario[item.tipo] = p.inventario.get(item.tipo, 0) + 1
                if item.tipo == "guarana" and player.sprite.vida < player.sprite.max_vida:
                    player.sprite.vida += 1

            batidas_inimigo = pygame.sprite.groupcollide(bullet_group, inimigos, True, False, pygame.sprite.collide_mask)
            if batidas_inimigo:
                for lista_inimigos in batidas_inimigo.values():
                    for inimigo in lista_inimigos:
                        inimigo.take_damage(1) 
                        
            colisao_subboss(p, subboss.sprite)

            player_rect = p.rect
        else:
            player_rect = pygame.Rect(0,0,0,0)

        # Atualizar grupos
        bullet_group.update()
        coletaveis.update()
        tiros_inimigos.update()
        for inimigo in inimigos:
            inimigo.update(objetos_solidos, player_rect)
        subboss.update(objetos_solidos, player_rect)

        # --- DESENHO DO MUNDO ---
        screen.blit(background.image, camera.aplicar_rect(background))
        for sprite in objetos_solidos:
            if sprite == chao:
                chao_rect = camera.aplicar_rect(sprite)
                chao_rect.y -= 20
                screen.blit(sprite.image, chao_rect)
            else:
                screen.blit(sprite.image, camera.aplicar_rect(sprite))
        for sprite in coletaveis:
            screen.blit(sprite.image, camera.aplicar_rect(sprite))
        for sprite in bullet_group:
            screen.blit(sprite.image, camera.aplicar_rect(sprite))
        for inimigo in inimigos:
            screen.blit(inimigo.image, camera.aplicar_rect(inimigo))
        
        sub_rect = camera.aplicar_rect(subboss.sprite)
        if subboss.sprite.atacando:
            sub_rect.x -= 50
            sub_rect.y -= 15
        screen.blit(subboss.sprite.image, sub_rect)

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