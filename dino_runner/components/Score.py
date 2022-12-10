import pygame

from dino_runner.utils.constants import FONT_STYLE


class Score:
    def __init__(self):
        self.score = 0
        self.mode = False
        self.mode_clock = 0

    def update (self, game):
        self.mode_change()
        self.score +=1
        if self.score % 100 == 0:
            if game.game_speed <= 50:
                game.game_speed += 1
        

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        if self.mode:
            text_component = font.render(f"Points: {self.score}", True, (255, 255, 255))
            text_rect = text_component.get_rect()
            text_rect.center = (1000, 50)
            screen.blit(text_component,text_rect)
        else:
            text_component = font.render(f"Points: {self.score}", True, (71, 75, 78))
            text_rect = text_component.get_rect()
            text_rect.center = (1000, 50)
            screen.blit(text_component,text_rect)


    def reset(self):
        self.score=0
        self.mode_clock = 0
        self.mode = False

    def mode_change(self):
        self.mode_clock += 1
        if self.mode_clock > 700:
            self.mode = True
        else: 
            self.mode = False
        if self.mode_clock > 1100:
            self.mode_clock = 0

        