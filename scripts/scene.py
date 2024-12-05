import pygame
from scripts.obj import Obj
from scripts.settings import *

class Scene:

    def __init__(self):
        
        self.display = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.active = True
        self.fade = Fade()

    def events(self, event):
        pass

    def draw(self):
        self.all_sprites.draw(self.display)

    def update(self):
        self.fade.draw()
        self.all_sprites.update()
        
        
class Fade:
    
    def __init__(self, speed=10):
        
        self.display = pygame.display.get_surface()
        self.surface = pygame.Surface((WIDTH, HEIGHT)).convert_alpha()
        self.surface.fill("black")
        self.alpha = 255
        self.speed = speed
        
    def draw(self):
        
        if self.alpha > 0:
            self.alpha -= self.speed
            
        self.surface.set_alpha(self.alpha)
        self.display.blit(self.surface, [0, 0])

