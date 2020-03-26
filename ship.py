import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

       
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.centerx = self.screen_rect.centerx

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        #обновить селфецентр корабля, без прямоугольника
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed
        #обновить прямоугольник по селфцентру
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx