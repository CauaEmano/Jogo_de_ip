import pygame

class Camera:
    def __init__(self, largura, altura):
        self.offset = pygame.Vector2()
        self.largura_tela = largura
        self.altura_tela = altura

    def update(self, alvo):
        # calcula quanto o mundo deve deslocar para o player estar no centro
        self.offset.x = alvo.rect.centerx - self.largura_tela // 2
        self.offset.y = alvo.rect.centery - self.altura_tela // 2

    def aplicar_rect(self, entidade):
        # retorna o retângulo da entidade ajustado pela câmera
        return entidade.rect.move(-self.offset)