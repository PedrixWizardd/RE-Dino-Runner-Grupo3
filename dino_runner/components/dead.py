
import pygame

from dino_runner.utils.constants import FONT_STYLE, SCREEN_HEIGHT, SCREEN_WIDTH


class Dead:
    def __init__(self):
        global dead
        dead = 0


    def update (self):
        global dead
        dead +=1


    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, 22)
        text_component = font.render(f"Number of deaths: {dead}", True, (71, 75, 78))
        text_rect = text_component.get_rect()
        text_rect.center = ((SCREEN_WIDTH //2) , (SCREEN_HEIGHT //2) -200)
        screen.blit(text_component,text_rect)

    #def resset_death_counter(self):
       # global dead
        #dead = 0

    def show_death_counter(self):
        global dead
        death_count = dead
        return death_count

 