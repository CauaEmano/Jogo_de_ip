import pygame
from sys import exit
from src import *
import random

# Variáveis e funções essenciais
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Helicônia')
clock = pygame.time.Clock()

# ESTADOS DO JOGO E FONTES
em_jogo = False 
venceu = False
tempo_inicio = 0
tempo_final = ""

fonte_menu = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 50)
fonte_vitoria = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 30)
fonte_game_over = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 30)
fonte_retry = pygame.font.Font("assets/Fontes/WatercolorDemo.ttf", 20)
fonte_tempo = pygame.font.Font(None, 60)

# Objeto do player
player = pygame.sprite.GroupSingle()
player.add(Player())
bullet_group = pygame.sprite.Group()

# Objetos do mundo (Plataformas e Colisões)
objetos_solidos = pygame.sprite.Group()
objetos_solidos_pedra = pygame.sprite.Group()
chao = Chao()
parede = Parede(x=-50, y=-100, largura=50, altura=700)
paredef = Parede(x=15000, y=-100, largura=50, altura=700)
plataformas = [
Plataforma(x=1200, y=480, largura=120, altura=30),
Plataforma(x=1450, y=400, largura=150, altura=30),
Plataforma(x=2200, y=480, largura=120, altura=30),
Plataforma(x=2450, y=400, largura=150, altura=30),
Plataforma(x=3200, y=480, largura=120, altura=30),
Plataforma(x=3450, y=400, largura=150, altura=30),
Plataforma(x=4200, y=480, largura=120, altura=30),
Plataforma(x=4450, y=400, largura=150, altura=30),
Plataforma(x=5200, y=480, largura=120, altura=30),
Plataforma(x=5450, y=400, largura=150, altura=30),
Plataforma(x=6200, y=480, largura=120, altura=30),
Plataforma(x=6450, y=400, largura=150, altura=30),
Plataforma(x=7200, y=480, largura=120, altura=30),
Plataforma(x=8200, y=480, largura=120, altura=30),
Plataforma(x=8450, y=400, largura=150, altura=30),
Plataforma(x=8700, y=400, largura=120, altura=30),
Plataforma(x=9200, y=480, largura=150, altura=30),
Plataforma(x=10200, y=480, largura=120, altura=30),
Plataforma(x=10450, y=400, largura=150, altura=30),
Plataforma(x=10700, y=400, largura=120, altura=30),
Plataforma(x=10950, y=400, largura=150, altura=30),
Plataforma(x=12200, y=480, largura=120, altura=30),
Plataforma(x=12450, y=400, largura=150, altura=30),
Plataforma(x=12700, y=480, largura=120, altura=30),
Plataforma(x=13200, y=480, largura=120, altura=30),
Plataforma(x=13450, y=400, largura=150, altura=30),
Plataforma(x=13900, y=480, largura=120, altura=30),
Plataforma(x=14150, y=400, largura=150, altura=30),
Plataforma(x=14350, y=320, largura=150, altura=30),
Plataforma(x=14600, y=400, largura=120, altura=30),
Plataforma(x=14800, y=480, largura=120, altura=30),]
objetos_solidos.add(chao, parede, plataformas, paredef)
objetos_solidos_pedra.add(chao, parede, paredef)

# Coletáveis e Inimigos
coletaveis = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
tiros_inimigos = pygame.sprite.Group()
subboss = pygame.sprite.GroupSingle()

# Carregar nível e Câmera
player, bullet_group, tiros_inimigos, inimigos, coletaveis, subboss = carregar_nivel(player, bullet_group, tiros_inimigos, inimigos, coletaveis, subboss)
interface = UI()
camera = Camera(1280, 720, 15000, 720)
background = Background()

# Variáveis de Boss e Efeitos
subboss_spawnado = True # Definido como True para detectar vitória quando ele morrer
shake_timer = 0

pygame.mixer.music.load('assets/audios/floresta.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.1)

# --- LOOP PRINCIPAL ---
while True:
    shake_x = 0
    shake_y = 0
    if shake_timer > 0:
        shake_timer -= 1
        shake_x = random.randint(-8, 8) 
        shake_y = random.randint(-8, 8) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            # INICIAR JOGO
            if not em_jogo and not venceu:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    em_jogo = True
                    tempo_inicio = pygame.time.get_ticks() # Começa a contar
            
            # ATIRAR
            elif em_jogo and event.key == pygame.K_SPACE and player.sprite:
                player.sprite.shoot(bullet_group, objetos_solidos_pedra, coletaveis, Pedra)
            
            # REINICIAR (Morte ou Vitória)
            if (not player.sprite or venceu) and event.key == pygame.K_r:
                player, bullet_group, tiros_inimigos, inimigos, coletaveis, subboss = carregar_nivel(player, bullet_group, tiros_inimigos, inimigos, coletaveis, subboss)
                em_jogo = True
                venceu = False
                subboss_spawnado = True
                shake_timer = 0
                tempo_inicio = pygame.time.get_ticks() # Reseta o tempo

    # DESENHO E TELAS 

    # TELA DE VITÓRIA
    if venceu:
        screen.blit(background.image, (0,0)) 
        screen.blit(chao.image, (0,580))
        texto_v = fonte_vitoria.render("VOCÊ VENCEU!", True, "Gold")
        texto_t = fonte_tempo.render(f"Tempo: {tempo_final}", True, "White")
        texto_r = fonte_retry.render("Pressione R para jogar novamente", True, "Yellow")
        
        screen.blit(texto_v, texto_v.get_rect(center=(640, 250)))
        screen.blit(texto_t, texto_t.get_rect(center=(640, 380)))
        screen.blit(texto_r, texto_r.get_rect(center=(640, 520)))

    # TELA INICIAL
    elif not em_jogo:
        screen.blit(background.image, (0,0)) 
        screen.blit(chao.image, (0,580))
        texto_titulo = fonte_menu.render("Ecos de Aranãmi", True, (240, 248, 255))
        texto_start = fonte_retry.render("Pressione ESPAÇO para Iniciar", True, "Yellow")
        screen.blit(texto_titulo, texto_titulo.get_rect(center=(640, 300)))
        screen.blit(texto_start, texto_start.get_rect(center=(640, 450)))
    
    # JOGO ATIVO
    else:
        p = player.sprite
        if p:
            camera.update(p)
            p.update()
            colisao(p, objetos_solidos, chao, parede, paredef) 

            # Colisões Inimigo/Player
            if pygame.sprite.spritecollide(p, inimigos, False, pygame.sprite.collide_mask):
                p.take_damage(1)
            if pygame.sprite.spritecollide(p, tiros_inimigos, True, pygame.sprite.collide_mask):
                p.take_damage(1)

            # Itens e Tiro do Player
            colidiu = [objeto for objeto in coletaveis if p.hitbox.colliderect(objeto.rect)]
            for item in colidiu:
                item.kill()
                p.inventario[item.tipo] = p.inventario.get(item.tipo, 0) + 1
                if item.tipo == "guarana" and p.vida < p.max_vida:
                    p.vida += 1

            batidas_inimigo = pygame.sprite.groupcollide(bullet_group, inimigos, True, False, pygame.sprite.collide_mask)
            if batidas_inimigo:
                for lista in batidas_inimigo.values():
                    for inimigo in lista:
                        inimigo.take_damage(1) 
            
            # LÓGICA DO BOSS
            if subboss.sprite:
                colisao_subboss(p, subboss.sprite)
                # Efeito de quase morte
                if subboss.sprite.vida <= 5:
                    if not getattr(subboss.sprite, 'ja_gritou', False):
                        subboss.sprite.ja_gritou = True
                        if hasattr(subboss.sprite, 'som_grito') and subboss.sprite.som_grito:
                            subboss.sprite.som_grito.play()
                        shake_timer = 90
                    for plat in plataformas:
                        plat.caindo = True
                player_rect = p.rect
            else:
                # CONDIÇÃO DE VITÓRIA: Boss morreu e o grupo está vazio
                if subboss_spawnado:
                    venceu = True
                    em_jogo = False
                    subboss_spawnado = False
                    # Calcular tempo final
                    ms_total = pygame.time.get_ticks() - tempo_inicio
                    mins = (ms_total // 60000)
                    segs = (ms_total // 1000) % 60
                    tempo_final = (f"{mins:02d}:{segs:02d}")

            player_rect = p.rect
        else:
            player_rect = pygame.Rect(0,0,0,0)

        # Atualizar Grupos
        bullet_group.update()
        coletaveis.update()
        tiros_inimigos.update()
        for inimigo in inimigos:
            inimigo.update(objetos_solidos, player_rect)
        objetos_solidos.update()

        # --- RENDERIZAÇÃO DO MUNDO ---
        def aplicar_shake(rect):
            r = rect.copy()
            r.x += shake_x
            r.y += shake_y
            return r

        screen.blit(background.image, aplicar_shake(camera.aplicar_rect(background)))
        
        for sprite in objetos_solidos:
            if sprite == chao:
                chao_rect = camera.aplicar_rect(sprite)
                chao_rect.y -= 20
                screen.blit(sprite.image, aplicar_shake(chao_rect))
            else:
                screen.blit(sprite.image, aplicar_shake(camera.aplicar_rect(sprite)))

        for sprite in coletaveis: screen.blit(sprite.image, aplicar_shake(camera.aplicar_rect(sprite)))
        for sprite in bullet_group: screen.blit(sprite.image, aplicar_shake(camera.aplicar_rect(sprite)))
        
        for inimigo in inimigos:
            if inimigo != subboss.sprite:
                screen.blit(inimigo.image, aplicar_shake(camera.aplicar_rect(inimigo)))
        
        if subboss.sprite:
            sub_rect = camera.aplicar_rect(subboss.sprite)
            if subboss.sprite.atacando:
                if subboss.sprite.direction == -1:
                    sub_rect.x -= 50
                else:
                    sub_rect.x -= 10

                sub_rect.y -= 15
            screen.blit(subboss.sprite.image, aplicar_shake(sub_rect))
        
        for bala in tiros_inimigos: screen.blit(bala.image, aplicar_shake(camera.aplicar_rect(bala)))

        if p:
            screen.blit(p.image, aplicar_shake(camera.aplicar_rect(p)))
            interface.display(screen, p.inventario, p.vida, p.max_vida)
        else:
            # GAME OVER OVERLAY
            overlay = pygame.Surface((1280, 720))
            overlay.set_alpha(150)
            overlay.fill((30, 0, 0))
            screen.blit(overlay, (0,0))
            screen.blit(fonte_game_over.render("Você Morreu", True, (255, 50, 50)), (520, 320))
            screen.blit(fonte_retry.render("Aperte R para reiniciar", True, "White"), (530, 420))

    pygame.display.update()
    clock.tick(60)