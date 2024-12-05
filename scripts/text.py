import pygame as pg

class Text:
    
    def __init__(self, font=None, size=12, text="", color="black", pos=(0, 0)):
        
        self.display = pg.display.get_surface()
        self.font = pg.font.Font(font, size)
        self.text = self.font.render(text, True, color).convert_alpha()
        self.pos = pos
        self.alpha = 255
        self.alpha_speed = 5
        
    def draw(self):
        self.display.blit(self.text, self.pos)
        
    def draw_fade(self):
        if self.alpha > 0:
            self.alpha -= self.alpha_speed
        else:
            self.alpha = 255
        
        self.text.set_alpha(self.alpha)
        self.display.blit(self.text, self.pos)