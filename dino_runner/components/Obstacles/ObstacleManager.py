
from dino_runner.components.Obstacles.smallcactus import Small_Cactus
from dino_runner.components.Obstacles.largecactus import Large_Cactus
from dino_runner.components.Obstacles.bird import Bird
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.Obstacles.shield import Shield
from dino_runner.utils.constants import SHIELD_TYPE, SMALL_CACTUS, LARGE_CACTUS, BIRD, NBIRD, NSMALL_CACTUS, NLARGE_CACTUS
import pygame
import random

class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.mode = False
        self.mode_clock = 0 
        self.player = Dinosaur()

    def update (self, game):
        self.mode_change()
        if self.mode:
            if len(self.obstacles) == 0:
                if random.randint(0, 2) == 0:
                    self.obstacles.append(Small_Cactus(NSMALL_CACTUS))
                elif random.randint(0, 2) == 1:
                    self.obstacles.append(Large_Cactus(NLARGE_CACTUS))
                elif random.randint(0, 2) == 2:
                    self.obstacles.append(Bird(NBIRD))
        else:
            if len(self.obstacles) == 0:
             if random.randint(0, 2) == 0:
                self.obstacles.append(Small_Cactus(SMALL_CACTUS))
             elif random.randint(0, 2) == 1:
                 self.obstacles.append(Large_Cactus(LARGE_CACTUS))
             elif random.randint(0, 2) == 2:
                 self.obstacles.append(Bird(BIRD))
        

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                if game.on_death():
                    self.obstacles.remove(obstacle)
                else:
                    break

    def reset_Obstacles(self):
        self.obstacles = []
        self.mode_clock = 0 



    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def mode_change(self):
        self.mode_clock += 1
        if self.mode_clock > 700:
            self.mode = True
        else: 
            self.mode = False
        if self.mode_clock > 1100:
            self.mode_clock = 0

