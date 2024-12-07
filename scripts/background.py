import pygame as bg
from scripts.obj import Obj
from scripts.settings import *

class Background:

    def __init__(self, group):
        self.bg = Obj("assets/menu/bg.png", [0, 0], group)
        self.bg2 = Obj("assets/menu/bg.png", [0, -HEIGHT], group)
        
    def update(self):
        self.bg.rect.y += 5
        self.bg2.rect.y += 5
        
        if self.bg.rect.y >= HEIGHT:
            self.bg.rect.y = 0
        elif self.bg2.rect.y >= 0:
            self.bg2.rect.y = -HEIGHT + 5