import pygame
import random

WIDTH = 960
HEIGHT = 720

def define():
    pygame.font.init()
    pygame.mixer.init()
    global WIDTH,HEIGHT
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    WHITE = (255,255,255)
    BLACK = (0,0,0)
    YELLOW = (255,255,0)
    RED = (255,40,40)
    BORDER = pygame.Rect(WIDTH//2-WIDTH//100,0,WIDTH//50,HEIGHT)
    STAT_FONT = pygame.font.SysFont('comicsans',WIDTH//16)
    FPS_FONT = pygame.font.SysFont('comicsans',WIDTH//32)
    WINNER_FONT = pygame.font.SysFont('comicsans',WIDTH//8)
    BULLET_HIT_SOUND = pygame.mixer.Sound('hit.mp3.ogg')
    BULLET_FIRE_SOUND = pygame.mixer.Sound('fire.mp3.ogg')
    BOUNCE_SOUND = pygame.mixer.Sound('bounce.mp3.ogg')
    ROUND_SOUND = pygame.mixer.Sound('round.mp3.ogg')
    SAGE_WALL = pygame.mixer.Sound('sage_wall.mp3.ogg')
    FPS = 120
    _rand_ = random.randint(1,3)
    if _rand_ == 1:
        SPEED = 48000
    if _rand_ == 2:
        SPEED = 42000
    if _rand_ == 3:
        SPEED = 36000
    VEL = (WIDTH*HEIGHT)//(SPEED*2)
    if SPEED == 48000:
        MUSIC = pygame.mixer.Sound('turtle.mp3.ogg')
    if SPEED == 42000:
        MUSIC = pygame.mixer.Sound('pacificrim.mp3.ogg')
    if SPEED == 36000:
        MUSIC = pygame.mixer.Sound('lastingpromise.mp3.ogg')
    BULLET_VEL = (WIDTH*HEIGHT)//(288000/4)
    MAX_BULLETS = 0
    YELLOW_HIT = pygame.USEREVENT + 1
    RED_HIT = pygame.USEREVENT + 2
    YELLOW_POINT = pygame.USEREVENT + 3
    RED_POINT = pygame.USEREVENT + 4
    SPACESHIP_WIDTH,SPACESHIP_HEIGHT = WIDTH//10,HEIGHT//10
    YELLOW_SPACESHIP_IMAGE = pygame.image.load('spaceship_yellow.png').convert_alpha()
    YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
    RED_SPACESHIP_IMAGE = pygame.image.load('spaceship_red.png').convert_alpha()
    RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT)),180)
    SPACE = pygame.transform.scale(pygame.image.load('space.png').convert(),(WIDTH,HEIGHT-HEIGHT//6))
    RED_ROCKET_IMAGE = pygame.image.load('RED_ROCKET.png').convert_alpha()
    RED_ROCKET = pygame.transform.scale(RED_ROCKET_IMAGE,(SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//4))
    YELLOW_ROCKET_IMAGE = pygame.image.load('YELLOW_ROCKET.png').convert_alpha()
    YELLOW_ROCKET = pygame.transform.scale(YELLOW_ROCKET_IMAGE,(SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//4))
    EXPLOSION_IMAGE = pygame.image.load('explosion.png').convert_alpha()
    EXPLOSION = pygame.transform.scale(EXPLOSION_IMAGE,(SPACESHIP_WIDTH,SPACESHIP_HEIGHT))
    return WIDTH,HEIGHT,WIN,WHITE,BLACK,YELLOW,RED,BORDER,STAT_FONT,FPS_FONT,WINNER_FONT,BULLET_HIT_SOUND,BULLET_FIRE_SOUND,BOUNCE_SOUND,ROUND_SOUND,SAGE_WALL,MUSIC,FPS,VEL,BULLET_VEL,MAX_BULLETS,YELLOW_HIT,RED_HIT,YELLOW_POINT,RED_POINT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT,YELLOW_SPACESHIP_IMAGE,YELLOW_SPACESHIP,RED_SPACESHIP_IMAGE,RED_SPACESHIP,SPACE,RED_ROCKET_IMAGE,RED_ROCKET,YELLOW_ROCKET_IMAGE,YELLOW_ROCKET,EXPLOSION_IMAGE,EXPLOSION