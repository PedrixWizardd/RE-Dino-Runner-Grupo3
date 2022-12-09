from dino_runner.components.Power_Ups.power_up import PowerUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE

class Hammer(PowerUp):
    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)