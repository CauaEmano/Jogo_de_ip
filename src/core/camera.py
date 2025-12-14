import pygame

class Camera:
    def __init__(self, largura_tela, altura_tela, largura_mapa, altura_mapa):
        self.offset = pygame.Vector2()
        self.largura_tela = largura_tela
        self.altura_tela = altura_tela
        self.largura_mapa = largura_mapa
        self.altura_mapa = altura_mapa

    def update(self, alvo):
        # calcula a posição ideal (centralizado no player)
        x = alvo.rect.centerx - self.largura_tela // 2
        y = alvo.rect.centery - self.altura_tela // 2

        # restringe o movimento
        # não deixa o X ser menor que 0 nem maior que o limite do mapa
        x = max(0, min(x, self.largura_mapa - self.largura_tela))
        
        # não deixa o Y ser menor que 0 nem maior que o limite do mapa
        y = max(0, min(y, self.altura_mapa - self.altura_tela))

        self.offset.x = x
        self.offset.y = y

    def aplicar_rect(self, entidade):
        return entidade.rect.move(-self.offset)