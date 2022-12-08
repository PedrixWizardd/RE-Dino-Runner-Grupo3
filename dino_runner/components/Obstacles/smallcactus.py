from dino_runner.components.Obstacles.obstacle import obstacle
from dino_runner.utils.constants import BG_POS
import random
class Small_Cactus (obstacle):
    def __init__(self, images):
        type = random.randint(0, 2)
        super().__init__(images, type)
        self.rect.y = BG_POS - 55
