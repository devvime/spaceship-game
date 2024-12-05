import pygame
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.text import Text
from scripts.settings import *
from scripts.background import Background

class Menu(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = Background(self.all_sprites)
        self.title = Text(font="assets/fonts/airstrike.ttf", size=50, text="SpaceShip 13K", color="white", pos=(450, 300))
        self.info = Text(font="assets/fonts/airstrike.ttf", size=21, text="Press start to Play", color="white", pos=(508, 513))
        
    def events(self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False

    def update(self):
        self.bg.update()
        self.title.draw()
        self.info.draw_fade()
        return super().update()
