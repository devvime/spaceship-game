from scripts.settings import *
from scripts.obj import Obj

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