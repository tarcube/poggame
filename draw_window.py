import pygame
from define import *

WIDTH,HEIGHT,WIN,WHITE,BLACK,YELLOW,RED,BORDER,STAT_FONT,FPS_FONT,WINNER_FONT,BULLET_HIT_SOUND,BULLET_FIRE_SOUND,BOUNCE_SOUND,ROUND_SOUND,SAGE_WALL,MUSIC,FPS,VEL,BULLET_VEL,MAX_BULLETS,YELLOW_HIT,RED_HIT,YELLOW_POINT,RED_POINT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT,YELLOW_SPACESHIP_IMAGE,YELLOW_SPACESHIP,RED_SPACESHIP_IMAGE,RED_SPACESHIP,SPACE,RED_ROCKET_IMAGE,RED_ROCKET,YELLOW_ROCKET_IMAGE,YELLOW_ROCKET,EXPLOSION_IMAGE,EXPLOSION = define()
toggle = 1

def draw_window(yellow,red,yellow_bullets,red_bullets,yellow_health,red_health,balls,yellow_power,red_power,pygame,yellow_points,red_points,fps2,yellow_walls,red_walls,explosions):
    ball_image = pygame.image.load('ball.png').convert_alpha()
    ball_ball = pygame.transform.scale(ball_image,(SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//2))
    WIN.blit(SPACE,(0,HEIGHT//6))
    pygame.draw.rect(WIN,BLACK,BORDER)
    WIN.blit(YELLOW_SPACESHIP,(yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP,(red.x,red.y))
    pygame.draw.rect(WIN,BLACK,pygame.Rect(0,0,WIDTH,HEIGHT//6))
    fps_text = FPS_FONT.render('fps: '+str(round(fps2,1)),1,WHITE)
    yellow_health_text = STAT_FONT.render('HP',1,YELLOW)
    red_health_text = STAT_FONT.render('HP',1,RED)
    yellow_power_text = STAT_FONT.render('POW',1,YELLOW)
    red_power_text = STAT_FONT.render('POW',1,RED)
    yellow_points_text = WINNER_FONT.render(''+str(yellow_points),1,YELLOW)
    red_points_text = WINNER_FONT.render(''+str(red_points),1,RED)
    WIN.blit(fps_text,(WIDTH//2-fps_text.get_width()//2,HEIGHT//20))
    WIN.blit(yellow_health_text,(WIDTH//60,HEIGHT//60))
    WIN.blit(red_health_text,(WIDTH-red_health_text.get_width()-WIDTH//60,HEIGHT//60))
    WIN.blit(yellow_power_text,(WIDTH//60,HEIGHT//12))
    WIN.blit(red_power_text,(WIDTH-red_power_text.get_width()-WIDTH//60,HEIGHT//12))
    WIN.blit(yellow_points_text,(WIDTH//2-yellow_points_text.get_width()*2,HEIGHT//32))
    WIN.blit(red_points_text,(WIDTH//2+yellow_points_text.get_width(),HEIGHT//32))
    pygame.draw.rect(WIN,(127,127,127),pygame.Rect((WIDTH//96)*12,HEIGHT//72,(WIDTH//40)*10,HEIGHT//20))
    pygame.draw.rect(WIN,YELLOW,pygame.Rect((WIDTH//96)*12,HEIGHT//72,(WIDTH//40)*(yellow_health//2),HEIGHT//20))
    pygame.draw.rect(WIN,(127,127,127),pygame.Rect((WIDTH//96)*12,HEIGHT//12,(WIDTH//40)*10,HEIGHT//20))
    pygame.draw.rect(WIN,YELLOW,pygame.Rect((WIDTH//96)*12,HEIGHT//12,(WIDTH//40)*(yellow_power//2),HEIGHT//20))
    pygame.draw.rect(WIN,(127,127,127),pygame.Rect((WIDTH//2)+((WIDTH//96)*12),HEIGHT//72,(WIDTH//40)*10,HEIGHT//20))
    pygame.draw.rect(WIN,RED,pygame.Rect((WIDTH//2)+((WIDTH//96)*12),HEIGHT//72,(WIDTH//40)*(red_health//2),HEIGHT//20))
    pygame.draw.rect(WIN,(127,127,127),pygame.Rect((WIDTH//2)+((WIDTH//96)*12),HEIGHT//12,(WIDTH//40)*10,HEIGHT//20))
    pygame.draw.rect(WIN,RED,pygame.Rect((WIDTH//2)+((WIDTH//96)*12),HEIGHT//12,(WIDTH//40)*(red_power//2),HEIGHT//20))
    for bullet in yellow_bullets:
        WIN.blit(YELLOW_ROCKET,(bullet.x,bullet.y))
    for bullet in red_bullets:
        WIN.blit(RED_ROCKET,(bullet.x,bullet.y))
    for ball in balls:
        WIN.blit(ball_ball,(ball.x,ball.y))
    for wall in yellow_walls:
        pygame.draw.rect(WIN,YELLOW,wall)
    for wall in red_walls:
        pygame.draw.rect(WIN,RED,wall)
    for explosion in explosions:
        WIN.blit(EXPLOSION,(explosion.x,explosion.y))
        explosions.remove(explosion)
    global toggle
    if toggle == 1:
        FADE = pygame.transform.scale(pygame.image.load('fade.png').convert_alpha(),(WIDTH,HEIGHT-HEIGHT//6))
    else:
        FADE = pygame.transform.scale(pygame.image.load('trans.png').convert_alpha(),(WIDTH,HEIGHT-HEIGHT//6))
    WIN.blit(FADE,(0,HEIGHT//6))
    pygame.display.update()