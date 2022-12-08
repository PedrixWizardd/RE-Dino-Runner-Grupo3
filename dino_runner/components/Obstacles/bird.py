from dino_runner.components.Obstacles.obstacle import obstacle
from dino_runner.utils.constants import BG_POS, BIRD
import random
class Bird (obstacle):
    def __init__(self, images):
        self.type = random.randint(0, 2)
        super().__init__(images, self.type)
        self.rect.y = BG_POS -100
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        if self.index > 5:
            SCREEN.blit(self.images[1], self.rect)
        else:
             SCREEN.blit(self.images[0], self.rect)
        self.index += 1