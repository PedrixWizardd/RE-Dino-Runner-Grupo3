from dino_runner.components.Power_Ups.power_up import PowerUp
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE
from dino_runner.components.dinosaur import Dinosaur
class Shield(PowerUp):
    def __init__(self): 
        super().__init__(SHIELD, SHIELD_TYPE)
        self.duration = 60
