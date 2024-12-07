import pygame
from scripts.scene import Scene
from scripts.background import Background
from scripts.text import Text


class GameOver(Scene):

    def __init__(self):
        super().__init__()
        
        self.bg = Background(self.all_sprites)
        self.title = Text(font="assets/fonts/airstrike.ttf", size=50, text="GAMEOVER", color="white", pos=(501, 350))
        
    def events(self, event):
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.active = False

    def update(self):
        self.bg.update()
        self.title.draw_fade()
        return super().update()