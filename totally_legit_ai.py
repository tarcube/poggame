import pygame
from define import *

WIDTH,HEIGHT,WIN,WHITE,BLACK,YELLOW,RED,BORDER,HEALTH_FONT,POWER_FONT,WINNER_FONT,BULLET_HIT_SOUND,BULLET_FIRE_SOUND,BOUNCE_SOUND,ROUND_SOUND,SAGE_WALL,MUSIC,FPS,VEL,BULLET_VEL,MAX_BULLETS,YELLOW_HIT,RED_HIT,YELLOW_POINT,RED_POINT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT,YELLOW_SPACESHIP_IMAGE,YELLOW_SPACESHIP,RED_SPACESHIP_IMAGE,RED_SPACESHIP,SPACE,RED_ROCKET_IMAGE,RED_ROCKET,YELLOW_ROCKET_IMAGE,YELLOW_ROCKET,EXPLOSION_IMAGE,EXPLOSION = define()

bounce = True

def totally_legit_ai(keys_pressed,red,pygame,frame_iterator,balls):
    for ball in balls:
        if ball.y < red.y - HEIGHT//60 and red.y - VEL > HEIGHT//6:
            if frame_iterator % 30 <= 20:
                red.y -= VEL
            if frame_iterator % 30 > 20 and red.y + VEL + red.height < HEIGHT+SPACESHIP_HEIGHT//20:
                red.y += VEL//2
        if ball.y > red.y + HEIGHT//60 and red.y + VEL + red.height < HEIGHT+SPACESHIP_HEIGHT//20:
            if frame_iterator % 30 < 10 and red.y - VEL > HEIGHT//6:
                red.y -= VEL//2
            if frame_iterator % 30 >= 10:
                red.y += VEL
        global bounce
        if bounce:
            red.x -= VEL
        if not bounce:
            red.x += VEL
        if red.x <= WIDTH // 2 + SPACESHIP_WIDTH:
            bounce = False
        if red.x >= WIDTH - SPACESHIP_WIDTH:
            bounce = True