import pygame
from scripts.scene import Scene
from scripts.obj import Obj
from scripts.background import Background
from scripts.settings import *

class Game(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = Background(self.all_sprites)
        self.spaceship = SpaceShip("assets/nave/nave0.png", [600, 600], [self.all_sprites])
        
    def update(self):
        self.bg.update()
        return super().update()
    
class SpaceShip(Obj):
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.direction = pygame.math.Vector2()
        self.speed = 5
        
    def input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_w]:
            self.direction.y = -1
        elif key[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0
            
        if key[pygame.K_a]:
            self.direction.x = -1
        elif key[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0
            
    def limit(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > WIDTH - self.rect.width:
            self.rect.x = WIDTH - self.rect.width
            
        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > HEIGHT - self.rect.height:
            self.rect.y = HEIGHT - self.rect.height
            
    def move(self):
        self.rect.center += self.direction * self.speed
        
    def update(self):
        self.input()
        self.limit()
        self.move()
