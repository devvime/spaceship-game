from scripts.obj import Obj

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