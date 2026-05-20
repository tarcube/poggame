import asyncio
import pygame

pygame.init()
pygame.display.set_mode((960, 720))
clock = pygame.time.Clock()

async def main():
    import define
    WIDTH,HEIGHT,WIN,WHITE,BLACK,YELLOW,RED,BORDER,HEALTH_FONT,POWER_FONT,WINNER_FONT,BULLET_HIT_SOUND,BULLET_FIRE_SOUND,BOUNCE_SOUND,ROUND_SOUND,SAGE_WALL,MUSIC,FPS,VEL,BULLET_VEL,MAX_BULLETS,YELLOW_HIT,RED_HIT,YELLOW_POINT,RED_POINT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT,YELLOW_SPACESHIP_IMAGE,YELLOW_SPACESHIP,RED_SPACESHIP_IMAGE,RED_SPACESHIP,SPACE,RED_ROCKET_IMAGE,RED_ROCKET,YELLOW_ROCKET_IMAGE,YELLOW_ROCKET,EXPLOSION_IMAGE,EXPLOSION = define.define()
    yellow = pygame.Rect(WIDTH//2-WIDTH//2+SPACESHIP_WIDTH//4,HEIGHT//2+HEIGHT//12,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    red = pygame.Rect(WIDTH//2+WIDTH//2-SPACESHIP_WIDTH,HEIGHT//2+HEIGHT//12,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
    yellow_bullets = []
    red_bullets = []
    yellow_points = 0
    red_points = 0
    balls = []
    ball = pygame.Rect(WIDTH//2-SPACESHIP_WIDTH//6,HEIGHT//2+HEIGHT//12,SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//2)
    balls.append(ball)
    yellow_health = 20
    red_health = 20
    explosions = []
    dx = WIDTH/960
    dy = HEIGHT/720
    yellow_power = MAX_BULLETS
    red_power = MAX_BULLETS
    yellow_walls = []
    red_walls = []
    toggle = 'red'
    clock = pygame.time.Clock()
    run = True
    import draw_window
    import handle_bullets
    import yellow_handle_movement
    import totally_legit_ai
    MUSIC.play(-1)
    frame_iterator = 0
    ai_key_toggle = True
    while run:
        frame_iterator += 1
        clock.tick(FPS)
        fps2 = clock.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e and yellow_power >= 2:
                    yellow_power -= 2
                    bullet = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2.1,SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//4)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    explosion = pygame.Rect(yellow.x+yellow.width,yellow.y+yellow.height//2.1,SPACESHIP_WIDTH//3,SPACESHIP_HEIGHT//3)
                    explosions.append(explosion)
                if frame_iterator > 30 and ai_key_toggle and red_power >= 2:
                    red_power -= 2
                    bullet = pygame.Rect(red.x,red.y+red.height//2.1,SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//4)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                    explosion = pygame.Rect(red.x,red.y+red.height//2.1,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
                    explosions.append(explosion)
                    ai_key_toggle = False
                    frame_iterator = 0
                if event.key == pygame.K_q and yellow_power >= 2:
                    yellow_power -= 2
                    wall = pygame.Rect(yellow.x+yellow.width,yellow.y,SPACESHIP_WIDTH//8,SPACESHIP_HEIGHT*2)
                    yellow_walls.append(wall)
                    SAGE_WALL.play()
                if frame_iterator > 30 and not ai_key_toggle and red_power >= 2:
                    red_power -= 2
                    wall = pygame.Rect(red.x,red.y,SPACESHIP_WIDTH//8,SPACESHIP_HEIGHT*2)
                    red_walls.append(wall)
                    SAGE_WALL.play()
                    ai_key_toggle = True
                    frame_iterator = 0
            if event.type == YELLOW_HIT:
                yellow_health -= 4
                BULLET_HIT_SOUND.play()
                explosion = pygame.Rect(yellow.x,yellow.y,SPACESHIP_WIDTH//3,SPACESHIP_HEIGHT//3)
                explosions.append(explosion)
            if event.type == RED_HIT:
                red_health -= 4
                BULLET_HIT_SOUND.play()
                explosion = pygame.Rect(red.x,red.y,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
                explosions.append(explosion)
            if event.type == YELLOW_POINT:
                frame_iterator = 0
                ROUND_SOUND.play()
                yellow_points += 1
                yellow_power = 0
                red_power = 0
                yellow_health = 20
                red_health = 20
                yellow_bullets = []
                red_bullets = []
                yellow_walls = []
                red_walls = []
                balls = []
                ball = pygame.Rect(WIDTH//2-SPACESHIP_WIDTH//6,HEIGHT//2+HEIGHT//12,SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//2)
                balls.append(ball)
                yellow = pygame.Rect(WIDTH//2-WIDTH//2+SPACESHIP_WIDTH//4,HEIGHT//2+HEIGHT//12,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
                red = pygame.Rect(WIDTH//2+WIDTH//2-SPACESHIP_WIDTH,HEIGHT//2+HEIGHT//12,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
                draw_window.draw_window(yellow,red,yellow_bullets,red_bullets,yellow_health,red_health,balls,yellow_power,red_power,pygame,yellow_points,red_points,fps2,yellow_walls,red_walls,explosions)
                temp = handle_bullets.handle_bullets(yellow_bullets,red_bullets,yellow,red,balls,pygame,yellow_walls,red_walls,True)
                pygame.time.delay(1000)
                ROUND_SOUND.play()
            if event.type == RED_POINT:
                frame_iterator = 0
                ROUND_SOUND.play()
                red_points += 1
                yellow_power = 0
                red_power = 0
                yellow_health = 20
                red_health = 20
                yellow_bullets = []
                red_bullets = []
                yellow_walls = []
                red_walls = []
                balls = []
                ball = pygame.Rect(WIDTH//2-SPACESHIP_WIDTH//6,HEIGHT//2,SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//2)
                balls.append(ball)
                yellow = pygame.Rect(WIDTH//2-WIDTH//2+SPACESHIP_WIDTH//4,HEIGHT//2,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
                red = pygame.Rect(WIDTH//2+WIDTH//2-SPACESHIP_WIDTH,HEIGHT//2,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
                draw_window.draw_window(yellow,red,yellow_bullets,red_bullets,yellow_health,red_health,balls,yellow_power,red_power,pygame,yellow_points,red_points,fps2,yellow_walls,red_walls,explosions)
                temp = handle_bullets.handle_bullets(yellow_bullets,red_bullets,yellow,red,balls,pygame,yellow_walls,red_walls,True)
                pygame.time.delay(1000)
                ROUND_SOUND.play()
        winner_text = ''
        if red_health <= 0:
            pygame.event.post(pygame.event.Event(YELLOW_POINT))
        if yellow_health <= 0:
            pygame.event.post(pygame.event.Event(RED_POINT))
        if red_points >= 7:
            winner_text = 'Red Wins!'
        if yellow_points >= 7:
            winner_text = 'Yellow Wins!'
        if winner_text != '':
            MUSIC.stop()
            import draw_winner
            draw_winner.draw_winner(winner_text,pygame)
            import define
            WIDTH,HEIGHT,WIN,WHITE,BLACK,YELLOW,RED,BORDER,HEALTH_FONT,POWER_FONT,WINNER_FONT,BULLET_HIT_SOUND,BULLET_FIRE_SOUND,BOUNCE_SOUND,ROUND_SOUND,SAGE_WALL,MUSIC,FPS,VEL,BULLET_VEL,MAX_BULLETS,YELLOW_HIT,RED_HIT,YELLOW_POINT,RED_POINT,SPACESHIP_WIDTH,SPACESHIP_HEIGHT,YELLOW_SPACESHIP_IMAGE,YELLOW_SPACESHIP,RED_SPACESHIP_IMAGE,RED_SPACESHIP,SPACE,RED_ROCKET_IMAGE,RED_ROCKET,YELLOW_ROCKET_IMAGE,YELLOW_ROCKET,EXPLOSION_IMAGE,EXPLOSION = define.define()
            yellow = pygame.Rect(WIDTH//2-WIDTH//2+SPACESHIP_WIDTH//4,HEIGHT//2+HEIGHT//12,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
            red = pygame.Rect(WIDTH//2+WIDTH//2-SPACESHIP_WIDTH,HEIGHT//2+HEIGHT//12,SPACESHIP_WIDTH,SPACESHIP_HEIGHT)
            yellow_bullets = []
            red_bullets = []
            yellow_points = 0
            red_points = 0
            balls = []
            ball = pygame.Rect(WIDTH//2-SPACESHIP_WIDTH//6,HEIGHT//2+HEIGHT//12,SPACESHIP_WIDTH//2,SPACESHIP_HEIGHT//2)
            balls.append(ball)
            yellow_health = 20
            red_health = 20
            explosions = []
            dx = WIDTH/960
            dy = HEIGHT/720
            yellow_power = MAX_BULLETS
            red_power = MAX_BULLETS
            yellow_walls = []
            red_walls = []
            toggle = 'red'
            clock = pygame.time.Clock()
            run = True
            import draw_window
            import handle_bullets
            import yellow_handle_movement
            import totally_legit_ai
            MUSIC.play(-1)
            frame_iterator = 0
            ai_key_toggle = True
        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement.yellow_handle_movement(keys_pressed,yellow,pygame)
        totally_legit_ai.totally_legit_ai(keys_pressed,red,pygame,frame_iterator,balls)
        temp = handle_bullets.handle_bullets(yellow_bullets,red_bullets,yellow,red,balls,pygame,yellow_walls,red_walls,False)
        if yellow_power < 20:
            yellow_power += temp[0]
        if red_power < 20:
            red_power += temp[1]
        if frame_iterator > 240:
            frame_iterator = 0
        draw_window.draw_window(yellow,red,yellow_bullets,red_bullets,yellow_health,red_health,balls,yellow_power,red_power,pygame,yellow_points,red_points,fps2,yellow_walls,red_walls,explosions)
        await asyncio.sleep(0)

asyncio.run(main())