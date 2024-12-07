import pygame, sys

from scripts.settings import *

from scripts.scenes.menu import Menu
from scripts.scenes.game import Game
from scripts.scenes.gameover import GameOver

class StartGame:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        pygame.display.set_caption("SpaceShip 13K")
        
        self.display = pygame.display.set_mode([WIDTH,HEIGHT])
        self.scene = "menu"
        self.current_scene = Menu()
        self.fps = pygame.time.Clock()
    
    def run(self):
        
        while True:

            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "game"
                self.current_scene = Game()
            elif self.scene == "game" and self.current_scene.active == False:
                self.scene = "gameover"
                self.current_scene = GameOver()
            elif self.scene == "gameover" and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.current_scene.events(event)
            
            self.fps.tick(60)
            self.display.fill("black")
            self.current_scene.draw()
            self.current_scene.update()
            pygame.display.flip()