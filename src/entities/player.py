import pygame
from src import *
from src.core.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        global gravidade, velocidade, inercia_x, pulo_duplo, pulo_duplo_timer
        global invencib_timer, invencib_duracao
        global tiro_cooldown, tiro_cooldown_max
        global tecla_pulo, tecla_tiro
        global frame_index, animation_speed

        # Variáveis globais (usadas apenas na classe)
        gravidade = 2
        velocidade = 10
        inercia_x = 1.5
        pulo_duplo = False
        pulo_duplo_timer = 0
        tecla_pulo = False
        invencib_timer = 0
        invencib_duracao = 60 # 1 segundo de invulnerabilidade (em 60 FPS)
        tiro_cooldown = 0
        tiro_cooldown_max = 40

        # Propriedades do player
        self.max_vida = 8
        self.vida = 8
        self.vel_x = 0
        self.vel_y = gravidade
        self.inventario = {'pedra': 10}
        # Estados
        self.no_ar = True
        self.flip = False
        self.atirando = False

        # --- Configuração da Animação ---
        frame_index = 0
        animation_speed = 0.4
        self.frames_andar = []
        self.frames_parado = []
        self.frames_atirando = []

        # (Carregamento de imagens mantido igual ao seu original)
        for i in range(35):
            img = pygame.image.load(f"assets/images/Indigena/indigena_correndo{i}.png").convert_alpha()
            img = pygame.transform.rotozoom(img, 0, 0.35)
            self.frames_andar.append(img)

        for i in range(36):
            img = pygame.image.load(f"assets/images/Indigena/indigena{i}.png").convert_alpha()
            img = pygame.transform.rotozoom(img, 0, 0.35)
            self.frames_parado.append(img)

        for i in range(16):
            img = pygame.image.load(f"assets/images/Indigena/indigena_atirando{i}.png").convert_alpha()
            img = pygame.transform.rotozoom(img, 0, 0.52)
            self.frames_atirando.append(img)
            
        self.image = self.frames_andar[frame_index]
        self.rect = self.image.get_rect(midbottom = (80, 500))
        self.mask = pygame.mask.from_surface(self.image)

        # Rect separado para hitbox
        self.hitbox = pygame.Rect(0, 0, 
                                 self.rect.width * 0.6,  # 60% da largura
                                 self.rect.height * 0.75) # 70% da altura
        self.hitbox.x = self.rect.x
        self.hitbox.bottom = self.rect.bottom

        #Carregando sons
        self.som_pulo = pygame.mixer.Sound('assets/audios/pulo.wav')
        self.som_pulo.set_volume(0.3)
        self.som_hit = pygame.mixer.Sound('assets/audios/Hit.wav')
        self.som_hit.set_volume(0.3)
        self.som_tiro = pygame.mixer.Sound('assets/audios/tiro.wav')
        self.som_tiro.set_volume(0.3)
        self.som_caminhar = pygame.mixer.Sound('assets/audios/caminhar.wav')
        self.som_caminhar.set_volume(0.3)
    
    def movimentacao(self):
        global gravidade, velocidade, inercia_x, pulo_duplo, pulo_duplo_timer, tecla_pulo, keys

        mov_esq = False
        mov_dir = False

        if not self.atirando:
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                mov_esq = True 
                self.som_caminhar.play()
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
                mov_dir = True
                self.som_caminhar.play()

        if mov_esq and not mov_dir:
            self.vel_x = -velocidade
            self.flip = True
        elif not mov_esq and mov_dir:
            self.vel_x = velocidade
            self.flip = False
        
        # Inércia do movimento
        if not self.no_ar: 
            inercia_x = 1.5
            pulo_duplo = False
        else: 
            inercia_x = 0.7

        if self.vel_x < 0:
            self.vel_x += inercia_x
            if self.vel_x > 0: self.vel_x = 0
        elif self.vel_x > 0:
            self.vel_x -= inercia_x
            if self.vel_x < 0: self.vel_x = 0


        if pulo_duplo: pulo_duplo_timer += 1
        else: pulo_duplo_timer = 0
        
        if not self.atirando:
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and not tecla_pulo and self.no_ar and pulo_duplo and pulo_duplo_timer >= 12:
                pulo_duplo = False
                self.vel_y = -20
                self.som_pulo.play()
            
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and not tecla_pulo and not self.no_ar:
                pulo_duplo = True if "pipa" in self.inventario else False
                self.vel_y = -25
                self.som_pulo.play()

        tecla_pulo = (keys[pygame.K_UP] or keys[pygame.K_w])

        if self.vel_y <= 25:
            self.vel_y += gravidade


        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def animar(self):
        global frame_index, animation_speed

        if self.atirando: # Animação atirando
            animation_speed = 0.4
            frame_index += animation_speed
            if frame_index >= len(self.frames_atirando):
                frame_index = 0
            frame_atual = self.frames_atirando[int(frame_index)]

        elif self.no_ar: # Visual quando está no ar
            frame_atual = self.frames_andar[5]



        elif self.vel_x != 0: # Animação andando
            animation_speed = 0.4
            frame_index += animation_speed
            if frame_index >= len(self.frames_andar):
                frame_index = 0
            frame_atual = self.frames_andar[int(frame_index)]

        else: # Animação em idle
            animation_speed = 0.4
            frame_index += animation_speed
            if frame_index >= len(self.frames_parado):
                frame_index = 0
            frame_atual = self.frames_parado[int(frame_index)]

        pos_chao_atual = self.rect.midbottom 

        # Efeito visual opcional de piscar ao receber dano BUG
        if invencib_timer > 0 and (pygame.time.get_ticks() // 100) % 2 == 0:
            # Não desenha a imagem (cria efeito de piscar)
            self.image = pygame.Surface((0,0))
        else:
            self.image = pygame.transform.flip(frame_atual, self.flip, False)
        
        self.rect = self.image.get_rect(midbottom = pos_chao_atual)
        self.mask = pygame.mask.from_surface(self.image)
    
    def shoot(self, bullet_group, objetos_solidos, coletaveis, Pedra):
        global balas, objetos, gp_coletáveis, pedra, tiro_cooldown, tiro_cooldown_max
        balas = bullet_group
        objetos = objetos_solidos
        gp_coletáveis = coletaveis
        pedra = Pedra
        
        municao_tipo = 'pedra'
        if tiro_cooldown == 0 and self.inventario.get(municao_tipo, 0) > 0:
            self.som_tiro.play()
            self.atirando = True

            tiro_cooldown = tiro_cooldown_max
            self.inventario[municao_tipo] -= 1 
        
    def update(self):
        global keys
        global invencib_timer, tiro_cooldown
        global balas, objetos, gp_coletáveis, pedra

        keys = pygame.key.get_pressed()

        if invencib_timer > 0:
            invencib_timer -= 1

        if tiro_cooldown > 0:
            tiro_cooldown -= 1
        else:
            self.atirando = False

        if self.atirando and tiro_cooldown == 30:
            direction = -1 if self.flip else 1
            spawn_x = self.rect.centerx + (20 * direction)

            new_bullet = Bullet(spawn_x, self.rect.centery, direction, objetos, gp_coletáveis, pedra)
            balas.add(new_bullet)

        self.movimentacao()
        self.animar()

        self.hitbox.midbottom = self.rect.midbottom


    def take_damage(self, amount=None, attacker_rect=None):
        global invencib_timer

        if invencib_timer <= 0:
            self.som_hit.play()
            self.vida -= 1 
            invencib_timer = 60
            
            if self.vida <= 0:
                self.die()
                
    def die(self):
        print("Player morreu!")
        self.kill()