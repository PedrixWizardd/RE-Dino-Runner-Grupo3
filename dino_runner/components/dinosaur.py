from pygame.sprite import Sprite
import pygame


from dino_runner.utils.constants import DEFAULT_TYPE, DUCKING, DUCKING_SHIELD, DUCKING_HAMMER, JUMPING, JUMPING_SHIELD, JUMPING_HAMMER, RUNNING, RUNNING_SHIELD, RUNNING_HAMMER, SHIELD_TYPE, BG_POS, HAMMER_TYPE

from dino_runner.utils.constants import NDUCKING, NDUCKING_HAMMER, NDUCKING_SHIELD, NRUNNING, NRUNNING_SHIELD, NRUNNING_HAMMER, NJUMPING, NJUMPING_HAMMER, NJUMPING_SHIELD

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER}

NDUCK_IMG = {DEFAULT_TYPE: NDUCKING, SHIELD_TYPE: NDUCKING_SHIELD, HAMMER_TYPE: NDUCKING_HAMMER}
NJUMP_IMG = {DEFAULT_TYPE: NJUMPING, SHIELD_TYPE: NJUMPING_SHIELD, HAMMER_TYPE: NJUMPING_HAMMER}
NRUN_IMG = {DEFAULT_TYPE: NRUNNING, SHIELD_TYPE: NRUNNING_SHIELD, HAMMER_TYPE: NRUNNING_HAMMER}

si = True
X_POS = 80
Y_POS = BG_POS - 70
Y_POS_DUCK = BG_POS -30
JUMP_VELOCITY = 8
class Dinosaur(Sprite):
    dino_dead = False
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.mode = False
        self.mode_clock = 0
        self.time_to_show = 0

        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.jump_velocity = JUMP_VELOCITY 
        self.has_power_up = False
        self.power_up_time_up = 0

    def update(self, user_input):
        self.mode_change()
        self.draw_power_up_activate()
        if self.dino_run:
            self.run()

        elif self.dino_jump:
            self.jump()

        elif self.dino_duck:
            self.ducking()


        #print(self.dino_run, self.dino_duck, self.dino_jump)

        if (user_input[pygame.K_UP] or user_input[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False 

        if self.step_index >= 10:
            self.step_index = 0
        

    def jump(self, ):
        if self.mode:
            self.image = NJUMP_IMG[self.type]
            self.dino_rect.y -= self.jump_velocity * 4
            self.jump_velocity -=0.8
        else:
            self.image = JUMP_IMG[self.type]
            self.dino_rect.y -= self.jump_velocity * 4
            self.jump_velocity -=0.8

        if  self.jump_velocity < -JUMP_VELOCITY:
            self.dino_jump = False
            self.dino_rect.y = Y_POS
            self.jump_velocity = JUMP_VELOCITY

    def run (self):
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        if self.mode:
            if self.step_index > 5:
                self.image = NRUN_IMG[self.type][1]
            else:
                self.image = NRUN_IMG[self.type][0]
            self.step_index +=1
        else:
            if self.step_index > 5:
                self.image = RUN_IMG[self.type][1]
            else:
                self.image = RUN_IMG[self.type][0]
            self.step_index +=1

    def ducking (self):
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        if self.mode:
            if self.step_index > 5:
                self.image = NDUCK_IMG[self.type][1]
            else:
                self.image = NDUCK_IMG[self.type][0]
            self.step_index +=1
        else: 
            if self.step_index > 5:
                self.image = DUCK_IMG[self.type][1]
            else:
                self.image = DUCK_IMG[self.type][0]
            self.step_index +=1



    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

    def on_pick_power_up (self, start_time, duration, type):
        self.has_power_up = True
        self.uout = False
        self.power_up_time_up = start_time + (duration * 1000)
        self.type = type
        self.uout = True



    def mode_change(self):
        self.mode_clock += 1
        if self.mode_clock > 700:
            self.mode = True
        else: 
            self.mode = False
        if self.mode_clock > 1100:
            self.mode_clock = 0

    def reset_mode(self):
        global si
        si = True
        self.mode_clock = 0
        self.mode = False
        
    def draw_power_up_activate (self):
        global si
        if self.has_power_up:
            if si:
                self.time_to_show = round ((self.power_up_time_up - pygame.time.get_ticks())) / 1000
            else:
                self.time_to_show = 0
            if self.time_to_show <= 0:
                self.has_power_up = False
                self.type = DEFAULT_TYPE

    

    def power_up_end():
        global si
        si = False


    def reactivate_power_up():
        global si
        si = True