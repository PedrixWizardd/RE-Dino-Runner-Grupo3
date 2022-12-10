import pygame
import os

# Global Constants
TITLE = "Dino Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
FONT_STYLE = "freesansbold.ttf"

# Assets Constants
BG_POS = 380

ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

DINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDead.png"))
DINO_START = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoStart.png"))

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Shield.png")),
]

RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2Hammer.png")),
]

JUMPING = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJump.png"))
JUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Shield.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2Hammer.png")),
]

SMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/SmallCactus3.png")),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

DEFAULT_TYPE = "default" 
SHIELD_TYPE = "shield"
HAMMER_TYPE = "hammer"





NDINO_DEAD = pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoDead.png"))
NDINO_START = pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoStart.png"))

NRUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoRun1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoRun2.png")),
]

NRUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoRun2Shield.png")),
]

NRUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoRun1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoRun2Hammer1.png")),
]

NJUMPING = pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoJump.png"))
NJUMPING_SHIELD = pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoJumpShield.png"))
NJUMPING_HAMMER = pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoJumpHammer.png"))

NDUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoDuck1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoDuck2.png")),
]

NDUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoDuck2Shield.png")),
]

NDUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NDino/DinoDuck2Hammer.png")),
]

NSMALL_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "NCactus/SmallCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NCactus/SmallCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NCactus/SmallCactus3.png")),
]
NLARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "NCactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NCactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NCactus/LargeCactus3.png")),
]

NBIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "NBird/Bird1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "NBird/Bird2.png")),
]

# NCLOUD = pygame.image.load(os.path.join(IMG_DIR, 'NOther/Cloud.png'))
# NSHIELD = pygame.image.load(os.path.join(IMG_DIR, 'NOther/shield.png'))
# NHAMMER = pygame.image.load(os.path.join(IMG_DIR, 'NOther/hammer.png'))

NBG = pygame.image.load(os.path.join(IMG_DIR, 'NOther/Track.png'))

NHEART = pygame.image.load(os.path.join(IMG_DIR, 'NOther/SmallHeart.png'))