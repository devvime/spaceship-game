import pygame
from scripts.scene import Scene
from scripts.obj import Obj
from scripts.text import Text
from scripts.background import Background
from scripts.settings import *

import random

class Game(Scene):

    def __init__(self):
        super().__init__()
        
        self.tick = 0
        self.pts = 0
        
        self.enemy_group = pygame.sprite.Group()
        self.power_up_group = pygame.sprite.Group()
        
        self.bg = Background(self.all_sprites)
        self.spaceship = SpaceShip("assets/nave/nave0.png", [600, 600], [self.all_sprites])    
        self.score_text = Text(font="assets/fonts/airstrike.ttf", size=25, text="Score: 0", color="white", pos=(30, 30))
        
        self.life1 = Obj("assets/hud/nave.png", [30, 60], [self.all_sprites])
        self.life2 = Obj("assets/hud/nave.png", [70, 60], [self.all_sprites])
        self.life3 = Obj("assets/hud/nave.png", [110, 60], [self.all_sprites])
        
        self.music = pygame.mixer.Sound("assets/sounds/bg.ogg")
        self.music.play(-1)
        
    def spaw_enemy(self):
        self.tick += 1
        
        if self.tick == 60:
            BigShip("assets/nave/enemy3_0.png", [random.randint(100, 1180), -250], [self.all_sprites, self.enemy_group])
        elif self.tick == 120:
            MediumShip("assets/nave/enemy2_0.png", [random.randint(100, 1180), -200], [self.all_sprites, self.enemy_group])
            MediumShip("assets/nave/enemy2_0.png", [random.randint(100, 1180), -200], [self.all_sprites, self.enemy_group])
        elif self.tick == 180:
            self.tick = 0
            SmallShip("assets/nave/enemy0.png", [random.randint(100, 1180), -100], [self.all_sprites, self.enemy_group])
            SmallShip("assets/nave/enemy0.png", [random.randint(100, 1180), -100], [self.all_sprites, self.enemy_group])
            SmallShip("assets/nave/enemy0.png", [random.randint(100, 1180), -100], [self.all_sprites, self.enemy_group])
            SmallShip("assets/nave/enemy0.png", [random.randint(100, 1180), -100], [self.all_sprites, self.enemy_group])
            PowerUp("assets/nave/powerup0.png", [random.randint(100, 1180), -100], [self.all_sprites, self.power_up_group])
            
    def collision(self):
        for shoot in self.spaceship.shoots_group:
            for enemy in self.enemy_group:
                if shoot.rect.colliderect(enemy.rect):
                    shoot.kill()
                    enemy.life -= 1
                    self.pts += 1
                    self.score_text.update(f"Score: {str(self.pts)}")
                    
                    sound = pygame.mixer.Sound("assets/sounds/block.ogg")
                    sound.play()
                    
                    if enemy.life <=0:
                        self.explosion(enemy)
                        sound = pygame.mixer.Sound("assets/sounds/damage.ogg")
                        sound.play()
                
                if self.spaceship.rect.colliderect(enemy.rect):
                    enemy.kill()
                    self.explosion(enemy)
                    self.spaceship.life -= 1
                    self.spaceship.level = 1
                    sound = pygame.mixer.Sound("assets/sounds/damage.ogg")
                    sound.play()
                
        for enemy in self.enemy_group:    
            if self.spaceship.rect.colliderect(enemy.rect):
                enemy.kill()
                self.explosion(enemy)
                self.spaceship.life -= 1
                sound = pygame.mixer.Sound("assets/sounds/damage.ogg")
                sound.play()
                
        for power in self.power_up_group:    
            if self.spaceship.rect.colliderect(power.rect):
                power.kill()
                self.spaceship.level += 1
                sound = pygame.mixer.Sound("assets/sounds/levelup.ogg")
                sound.play()
                    
    def hud(self):
        if self.spaceship.life == 2:
            self.life3.kill()
        elif self.spaceship.life == 1:
            self.life2.kill()
        elif self.spaceship.life == 0:
            self.life1.kill()
            
    def explosion(self, enemy):
        x = enemy.rect.x + enemy.image.get_width() / 2
        y = enemy.rect.y + enemy.image.get_height() / 2
        Explosion("assets/explosion/0.png", [x, y], [self.all_sprites])
                    
    def gameover(self):
        if self.spaceship.life <= 0:
            self.music.stop()
            self.active = False
        
    def update(self):
        self.bg.update()
        self.spaceship.shoots_group.draw(self.display)
        self.spaceship.shoots_group.update()
        self.spaw_enemy()
        self.collision()
        self.score_text.draw()
        self.hud()
        self.gameover()
        return super().update()
    
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
            
class Enemy(Obj):
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 1
        self.life = 1
        
    def move(self):
        self.rect.y += self.speed
        
        if self.rect.y >= HEIGHT + self.image.get_height():
            self.kill()
            
    def destroy(self):
        if self.life <= 0:
            self.kill()
    def update(self):
        self.destroy()
        self.move()
        
class SmallShip(Enemy):
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 6
        self.life = 1
        
    def update(self):
        self.anim(image="nave/enemy", speed=8, frames=3)
        return super().update()
    
class MediumShip(Enemy):
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 4
        self.life = 2
        
    def update(self):
        self.anim(image="nave/enemy2_", speed=8, frames=3)
        return super().update()
    
class BigShip(Enemy):
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 1
        self.life = 10
        
    def update(self):
        self.anim(image="nave/enemy3_", speed=8, frames=3)
        return super().update()

class PowerUp(Enemy):
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.speed = 2
        
    def update(self):
        self.anim(image="nave/powerup", speed=16, frames=3)
        return super().update()
    
class Explosion(Obj):
    
    def __init__(self, img, pos, *groups):
        super().__init__(img, pos, *groups)
        
        self.ticks = 0
        
    def update(self):
        self.anim(image="explosion/", speed=5, frames=5)
        
        self.ticks += 1
        if self.ticks >= 25:
            self.kill()
        return super().update()