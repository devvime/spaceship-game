import pygame
import random

from scripts.scene import Scene
from scripts.obj import Obj
from scripts.settings import *
from scripts.text import Text

from scripts.entities.background import Background
from scripts.entities.spaceship import SpaceShip
from scripts.entities.enemys import SmallShip, MediumShip, BigShip, PowerUp
from scripts.entities.explosion import Explosion

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
