import pygame

class Obj(pygame.sprite.Sprite):

    def __init__(self,img, pos, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect(topleft=pos)
        
        self.tick = 0
        self.frame = 0
        
    def anim(self, image='', speed=8, frames=3):
        self.tick += 1
        if self.tick >= speed:
            self.tick = 0
            self.frame = (self.frame + 1) % frames
            self.image = pygame.image.load(f"assets/{image}{self.frame}.png")