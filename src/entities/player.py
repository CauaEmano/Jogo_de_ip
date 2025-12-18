import pygame
from src import *
from src.core.bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # Mantendo as globais conforme seu código original
        global gravidade, velocidade, inercia_x, pulo_duplo, pulo_duplo_timer
        global invencib_timer, invencib_duracao
        global tiro_cooldown, tiro_cooldown_max
        global tecla_pulo, tecla_tiro
        global frame_index, animation_speed

        # Variáveis de física e timers
        gravidade = 2
        velocidade = 10
        inercia_x = 1.5
        pulo_duplo = False
        pulo_duplo_timer = 0
        tecla_pulo = False
        invencib_timer = 0
        invencib_duracao = 60 
        tiro_cooldown = 0
        tiro_cooldown_max = 40

        # Propriedades do player
        self.max_vida = 8
        self.vida = 8
        self.vel_x = 0
        self.vel_y = gravidade
        self.inventario = {'pedra': 10}
        self.no_ar = True
        self.flip = False
        self.atirando = False

        # --- Configuração da Animação ---
        frame_index = 0
        animation_speed = 0.4
        self.frames_andar = []
        self.frames_parado = []
        self.frames_atirando = []

        # Carregamento de imagens
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

        # Hitbox (Este é o retângulo que a função colisao deve usar)
        self.hitbox = pygame.Rect(0, 0, self.rect.width * 0.6, self.rect.height * 0.75)
        self.hitbox.midbottom = self.rect.midbottom

        # Sons
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
                # Sugestão: adicione um timer para o som não tocar todo frame
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]: 
                mov_dir = True

        if mov_esq and not mov_dir:
            self.vel_x = -velocidade
            self.flip = True
        elif not mov_esq and mov_dir:
            self.vel_x = velocidade
            self.flip = False
        
        # Inércia
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
        global frame_index, animation_speed, invencib_timer

        # 1. Seleciona o frame correto
        if self.atirando:
            animation_speed = 0.4
            frame_index += animation_speed
            if frame_index >= len(self.frames_atirando): frame_index = 0
            frame_atual = self.frames_atirando[int(frame_index)]
        elif self.no_ar:
            frame_atual = self.frames_andar[5]
        elif self.vel_x != 0:
            animation_speed = 0.4
            frame_index += animation_speed
            if frame_index >= len(self.frames_andar): frame_index = 0
            frame_atual = self.frames_andar[int(frame_index)]
        else:
            animation_speed = 0.4
            frame_index += animation_speed
            if frame_index >= len(self.frames_parado): frame_index = 0
            frame_atual = self.frames_parado[int(frame_index)]

        pos_chao_atual = self.rect.midbottom 

        # 2. Aplica o flip
        self.image = pygame.transform.flip(frame_atual, self.flip, False)

        # 3. CORREÇÃO DO PISCAR (Alpha em vez de Surface 0,0)
        if invencib_timer > 0:
            # Alterna entre invisível (0) e visível (255) baseado no tempo
            alpha = 0 if (pygame.time.get_ticks() // 100) % 2 == 0 else 255
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255) # Garante que volte ao normal
        
        # 4. Atualiza Rect e Mask sem perder as dimensões
        self.rect = self.image.get_rect(midbottom = pos_chao_atual)
        self.mask = pygame.mask.from_surface(self.image)
    
    def shoot(self, bullet_group, objetos_solidos_pedra, coletaveis, Pedra):
        global balas, objetos, gp_coletáveis, pedra, tiro_cooldown, tiro_cooldown_max
        balas = bullet_group
        objetos = objetos_solidos_pedra
        gp_coletáveis = coletaveis
        pedra = Pedra
        
        municao_tipo = 'pedra'
        if tiro_cooldown == 0 and self.inventario.get(municao_tipo, 0) > 0:
            self.som_tiro.play()
            self.atirando = True
            tiro_cooldown = tiro_cooldown_max
            self.inventario[municao_tipo] -= 1 
        
    def update(self):
        global keys, invencib_timer, tiro_cooldown
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
            spawn_x = self.hitbox.centerx + (20 * direction)

            new_bullet = Bullet(spawn_x, self.hitbox.centery - 25, direction, objetos, gp_coletáveis, pedra)
            balas.add(new_bullet)

        self.movimentacao()
        self.animar()

        # O hitbox sempre segue o pé da imagem, não importa o tamanho do rect
        self.hitbox.midbottom = self.rect.midbottom

    def take_damage(self, amount=None, attacker_rect=None):
        global invencib_timer
        if invencib_timer <= 0:
            self.som_hit.play()
            self.vida -= 1 
            invencib_timer = 60 # 1 segundo de paz
            if self.vida <= 0:
                self.die()
                
    def die(self):
        self.kill()