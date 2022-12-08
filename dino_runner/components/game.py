import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.Obstacles.obstacle import obstacle
from dino_runner.components.Obstacles.ObstacleManager import ObstacleManager
from dino_runner.components.Score import Score
from dino_runner.components.dead import Dead
import random

from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, BG_POS, FONT_STYLE, RUNNING, DINO_DEAD

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = BG_POS
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.death = Dead()
        self.score = Score()

    def execute(self):
        #Dead.resset_death_counter(self)
        self.executing = True

        while self.executing:
            if not self.playing:
                self.show_menu()
        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_Obstacles()
        self.score.reset_score(self)
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.score.update(self)
    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255)) #white
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if int(Dead.show_death_counter(self)) == 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text_component = font.render("Press Any key to play", True, (71, 75, 78))
            text_rect = text_component.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text_component, text_rect)
            self.screen.blit(RUNNING[0], (half_screen_width - 30, half_screen_height + 140))
            pygame.display.update()
            self.hleom()
        elif int(Dead.show_death_counter(self)) > 0:
            font = pygame.font.Font(FONT_STYLE, 30)
            text_component = font.render("You Died, press any key to try again", True, (71, 75, 78))
            text_rect = text_component.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text_component, text_rect)
            self.screen.blit(DINO_DEAD, (half_screen_width - 30, half_screen_height + 140))
            self.death.draw(self.screen)
            self.score.draw(self.screen)
            pygame.display.update()
            self.hleom()

    def hleom(self): #handle key events on menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

