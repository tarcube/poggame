import pygame
from define import *

WIDTH,HEIGHT,WIN,WHITE,BLACK,YELLOW,RED,BORDER,HEALTH_FONT,POWER_FONT,WINNER_FONT,BULLET_HIT_SOUND,BULLET_FIRE_SOUND,BOUNCE_SOUND,ROUND_SOUND,SAGE_WALL,MUSIC,FPS,VEL,BULLET_VEL,MAX_BULLETS,YELLOW_HIT,RED_HIT,YELLOW_POINT,RED_POINT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT,YELLOW_SPACESHIP_IMAGE,YELLOW_SPACESHIP,RED_SPACESHIP_IMAGE,RED_SPACESHIP,SPACE,RED_ROCKET_IMAGE,RED_ROCKET,YELLOW_ROCKET_IMAGE,YELLOW_ROCKET,EXPLOSION_IMAGE,EXPLOSION = define()

dx = WIDTH/960
dy = HEIGHT/720
yellow_power = MAX_BULLETS
red_power = MAX_BULLETS
toggle = 'red'

def handle_bullets(yellow_bullets,red_bullets,yellow,red,balls,pygame,yellow_walls,red_walls,qte):
    global dx,dy,yellow_power,red_power,toggle
    if qte:
        dx = WIDTH/960
    if not qte:
        for bullet in yellow_bullets:
            bullet.x += BULLET_VEL
            if red.colliderect(bullet):
                pygame.event.post(pygame.event.Event(RED_HIT))
                yellow_bullets.remove(bullet)
            elif bullet.x > WIDTH:
                yellow_bullets.remove(bullet)
        for bullet in red_bullets:
            bullet.x -= BULLET_VEL
            if yellow.colliderect(bullet):
                pygame.event.post(pygame.event.Event(YELLOW_HIT))
                red_bullets.remove(bullet)
            elif bullet.x < 0:
                red_bullets.remove(bullet)
        for ball in balls:
            ball.x += VEL * dx // 4
            ball.y += VEL * dy // 4
            if ball.y < HEIGHT//6:
                BOUNCE_SOUND.play()
                dy = abs(dy)
            elif ball.y > HEIGHT-SPACESHIP_HEIGHT//3:
                BOUNCE_SOUND.play()
                dy = abs(dy) * -1
            for wall in yellow_walls:
                if wall.colliderect(ball):
                    BOUNCE_SOUND.play()
                    dx = abs(dx)
                    dx += (WIDTH/960 / 40)
                    ball.x += VEL
                    yellow_walls.remove(wall)
                    if toggle == 'yellow':
                        toggle = 'red'
                        return [2,0]
                for bullet in red_bullets:
                    if bullet.colliderect(wall):
                        yellow_walls.remove(wall)
                        red_bullets.remove(bullet)
            if yellow.colliderect(ball):
                BOUNCE_SOUND.play()
                dx = abs(dx)
                dx += (WIDTH/960 / 40)
                ball.x += VEL
                if toggle == 'yellow':
                    toggle = 'red'
                    return [2,0]
            elif ball.x < 0:
                balls.remove(ball)
                pygame.event.post(pygame.event.Event(RED_POINT))
                dx = WIDTH/960
                ball2 = pygame.Rect(WIDTH//2-SPACESHIP_WIDTH//6,HEIGHT//2,SPACESHIP_WIDTH//3,SPACESHIP_HEIGHT//3)
                balls.append(ball2)
            for wall in red_walls:
                if wall.colliderect(ball):
                    BOUNCE_SOUND.play()
                    dx = abs(dx) * -1
                    dx -= (WIDTH/960 / 40)
                    ball.x -= VEL
                    red_walls.remove(wall)
                    if toggle == 'red':
                        toggle = 'yellow'
                        return [0,2]
                for bullet in yellow_bullets:
                    if bullet.colliderect(wall):
                        red_walls.remove(wall)
                        yellow_bullets.remove(bullet)
            if red.colliderect(ball):
                BOUNCE_SOUND.play()
                dx = abs(dx) * -1
                dx -= (WIDTH/960 / 40)
                ball.x -= VEL
                if toggle == 'red':
                    toggle = 'yellow'
                    return [0,2]
            elif ball.x > WIDTH:
                balls.remove(ball)
                pygame.event.post(pygame.event.Event(YELLOW_POINT))
                dx = WIDTH/960 * -1
                ball2 = pygame.Rect(WIDTH//2-SPACESHIP_WIDTH//6,HEIGHT//2,SPACESHIP_WIDTH//3,SPACESHIP_HEIGHT//3)
                balls.append(ball2)
    return [0,0]