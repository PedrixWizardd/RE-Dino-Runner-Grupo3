from pygame.sprite import Sprite 
import pygame
from dino_runner.utils.constants import RUNNING, JUMPING
X_POS = 80
Y_POS = 310
JUM_VEL = 8
class dinosaur(Sprite):


    def __init__(self):
        self.image = RUNNING [0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.slep_index = 0

        self.dino_run = True
        self.dino_jump = False
        self.jump_velocity = JUM_VEL

    def update():
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()

        if user_input[pygame.K_UP] and not self.dino_jump:
            dino_jump = True
            self.dino_run = False
        
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True

        if self.slep_index > 10:
            self.slep_index = 0
        
    def draw():
        screen.blit(self.image, (self.dino_rect.y, self.dino_rect.x))
    
    def run(self): 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        if self.slep_index > 5:
            self.image = RUNNING [1]
        else:
            self.image = RUNNING [0]
        self.step_index +=1
    
    def jump(self):
        self.image = JUMPING
        self.dino_rect.y = JUM_VEL * 4
        self.jump_velocity -= 0.8

        if self.jump_velocity < -JUM_VEL:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_velocity = JUM_VEL

