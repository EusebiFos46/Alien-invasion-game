import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Cargar la imagen del alien y configurar el rectangulo
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()

        # Iniciar cada nuevo alien cerca de la parte superior derecha de la pantalla
        self.rect.right = self.screen_rect.right - 10
        self.rect.top = 10

        #Guardar la posicion exacta del alien
        self.x = float(self.rect.x)
        
