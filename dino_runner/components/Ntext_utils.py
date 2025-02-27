import pygame

from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = 'freesansbold.ttf'
white_color = (255, 255, 255)


def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 22)

    text = font.render('Points: ' + str(points), True, white_color)
    text_rect = text.get_rect()
    text_rect.center = (1000, 50)
    return text, text_rect


def get_centered_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 30)
    text = font.render(message, True, white_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect