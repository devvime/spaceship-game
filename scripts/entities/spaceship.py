import pygame

from scripts.settings import *
from scripts.obj import Obj

class SpaceShip(Obj):
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.direction = pygame.math.Vector2()
        self.speed = 10
        self.shoot_time = 0
        self.life = 3     
        self.level = 1   
        self.shoots_group = pygame.sprite.Group()
        
        
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
            
        if key[pygame.K_SPACE]:
            self.shoot_time += 1
            if self.shoot_time >= 5:
                self.shoot_time = 0
                
                sound = pygame.mixer.Sound("assets/sounds/shot.ogg")
                sound.play()
                
                if self.level == 1:
                    Shoot("assets/tiros/tiro1.png", [self.rect.x + 30, self.rect.y - 20], [self.shoots_group])
                elif self.level == 2:
                    Shoot("assets/tiros/tiro2.png", [self.rect.x + 30, self.rect.y - 20], [self.shoots_group])
                elif self.level == 3:
                    Shoot("assets/tiros/tiro3.png", [self.rect.x + 30, self.rect.y - 20], [self.shoots_group])
                elif self.level == 4:
                    Shoot("assets/tiros/tiro1.png", [self.rect.x, self.rect.y - 20], [self.shoots_group])
                    Shoot("assets/tiros/tiro1.png", [self.rect.x + 60, self.rect.y - 20], [self.shoots_group])
                elif self.level == 5:
                    Shoot("assets/tiros/tiro2.png", [self.rect.x, self.rect.y - 20], [self.shoots_group])
                    Shoot("assets/tiros/tiro2.png", [self.rect.x + 60, self.rect.y - 20], [self.shoots_group])
                elif self.level == 6:
                    Shoot("assets/tiros/tiro3.png", [self.rect.x, self.rect.y - 20], [self.shoots_group])
                    Shoot("assets/tiros/tiro3.png", [self.rect.x + 60, self.rect.y - 20], [self.shoots_group])
                else:
                    Shoot("assets/tiros/tiro2.png", [self.rect.x, self.rect.y - 20], [self.shoots_group])
                    Shoot("assets/tiros/tiro2.png", [self.rect.x + 20, self.rect.y - 20], [self.shoots_group])
                    Shoot("assets/tiros/tiro2.png", [self.rect.x + 40, self.rect.y - 20], [self.shoots_group])
                    Shoot("assets/tiros/tiro2.png", [self.rect.x + 60, self.rect.y - 20], [self.shoots_group])
            
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
        self.anim(image="nave/nave", speed=8, frames=3)
        
class Shoot(Obj):
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 10
        
    def update(self):
        self.rect.y -= self.speed
        
        if self.rect.y <= -100:
            self.kill()