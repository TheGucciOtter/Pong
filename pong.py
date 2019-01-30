import pygame
import pong_objects
from pygame.math import Vector2
import random
# Setup
pygame.init()
done = False
clock = pygame.time.Clock()

# Screen
size = [1200, 700]
screen = pygame.display.set_mode(size)
COLOR = (0,0,0)

player_1 = pong_objects.Player(Vector2(990, 310))
player_2 = pong_objects.Player(Vector2(200, 310))
all_sprites = pygame.sprite.Group()

all_sprites.add(player_1)
all_sprites.add(player_2)
player_1_speed = Vector2(0,0)
player_2_speed = Vector2(0,0)

player_1_points = 0
player_2_points = 0

upper_wall = pong_objects.Wall(Vector2(0,0))
lower_wall = pong_objects.Wall(Vector2(0,699))
right_upper_wall = pong_objects.Side_Wall(Vector2(1193,0))
right_lower_wall = pong_objects.Side_Wall(Vector2(1193,575))
left_upper_wall = pong_objects.Side_Wall(Vector2(0,0))
left_lower_wall = pong_objects.Side_Wall(Vector2(0,575))

wall_sprites = pygame.sprite.Group()

wall_sprites.add(right_upper_wall)
wall_sprites.add(right_lower_wall)
wall_sprites.add(left_upper_wall)
wall_sprites.add(left_lower_wall)

wall_sprites.add(upper_wall)
wall_sprites.add(lower_wall)

ball = pong_objects.Ball(Vector2(590, 340))
all_sprites.add(ball)

ball_reset = True
game_start = False

power_up = pong_objects.Power_Up(Vector2(random.randint(340,850),random.randint(5,695)))
all_power_ups = pygame.sprite.Group()
all_power_ups.add(power_up)

player_1_p_up = False
player_2_p_up = False

POWER_UP_TIMER = pygame.USEREVENT+0
HIT_TIMER = pygame.USEREVENT+1
can_hit = True

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 80)

the_way = 11

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_SPACE:
                game_start = True
            elif event.key == pygame.K_w and game_start:
                player_2_speed.y -= 10
            elif event.key == pygame.K_s and game_start:
                player_2_speed.y += 10
            elif event.key == pygame.K_UP and game_start:
                player_1_speed.y -= 10
            elif event.key == pygame.K_DOWN and game_start:
                player_1_speed.y += 10

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_2_speed.y = 0
            elif event.key == pygame.K_s:
                player_2_speed.y = 0
            elif event.key == pygame.K_UP:
                player_1_speed.y = 0
            elif event.key == pygame.K_DOWN:
                player_1_speed.y = 0

        elif event.type == POWER_UP_TIMER:
            power_up = pong_objects.Power_Up(Vector2(random.randint(340,850),random.randint(5,695)))
            all_power_ups.add(power_up)
            pygame.time.set_timer(POWER_UP_TIMER, 0)
        elif event.type == HIT_TIMER:
            can_hit = True
            pygame.time.set_timer(HIT_TIMER, 0)


    player_1.speed = player_1_speed
    player_2.speed = player_2_speed

    if game_start and ball_reset:
        ball_speed = Vector2(the_way,0)
        ball.speed = ball_speed
        ball_reset = False
        random_ball_speed_y = random.randint(-10,10)
        ball_speed.y = random_ball_speed_y

    screen.fill((COLOR))
    pygame.draw.line(screen, (255,255,255), (600,0),(600,700), 10)

    all_sprites.update()
    all_sprites.draw(screen)
    wall_sprites.update()
    wall_sprites.draw(screen)
    all_power_ups.update()
    all_power_ups.draw(screen)

    if player_1.position.y >= 620:
        player_1.position.y = 620
    elif player_1.position.y <= 0:
        player_1.position.y = 0
    if player_2.position.y >= 620:
        player_2.position.y = 620
    elif player_2.position.y <= 0:
        player_2.position.y = 0

    if can_hit:
        if pygame.sprite.collide_rect(ball, player_1):
            pygame.time.set_timer(HIT_TIMER, 350)
            can_hit = False
            from_center = abs(ball.rect.y - player_1.rect.centery)
            (r,phi) = ball.speed.as_polar()
            if ball.speed.x < 0:
                if from_center < 0:
                    phi = 180 - from_center
                else:
                    phi = 180 + from_center
            if ball.speed.x > 0:
                ball.speed.x = -abs(ball.speed.x)
                if ball.rect.y > player_1.rect.centery:
                    phi = 180 + phi - (230 / 180) * abs(from_center)
                    print (phi)
                    if phi < 125.0:
                        print('working')
                        phi = 125.0
                else:
                    phi = 180 + phi + (230 / 180) * abs(from_center)
                    print (phi)
                    if phi > 235.0:
                        print('working')
                        phi = -125.0
            ball.speed.from_polar((r,phi))

            COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
            player_1_p_up = True
            player_2_p_up = False

    if can_hit:
        if pygame.sprite.collide_rect(ball, player_2):
                pygame.time.set_timer(HIT_TIMER, 350)
                can_hit = False
                if ball.rect.y > player_2.rect.centery:
                    ball.speed.x = - ball.speed.x
                    (r,phi) = ball.speed.as_polar()
                    ball.speed.from_polar((r,phi + 230 * (ball.rect.y - player_2.rect.centery) / 120))
                else:
                    ball_speed.from_polar((r,180-phi + 130 * (ball.rect.y - player_2.rect.centery) / 120))
                    COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
                    player_2_p_up = True
                    player_1_p_up = False

    if ball.position.x >= 1190:
        game_start = False
        ball.position = (590, 340)
        ball_speed.x = 0
        ball_speed.y = 0
        ball_reset = True
        player_1.position = Vector2(990, 310)
        player_2.position = Vector2(200, 310)
        player_2_points += 1
        the_way = 11

    elif ball.position.x <= -10:
        game_start = False
        ball.position = (590, 340)
        ball_speed.x = 0
        ball_speed.y = 0
        ball_reset = True
        player_1.position = Vector2(990, 310)
        player_2.position = Vector2(200, 310)
        player_1_points += 1
        the_way = -11

    if pygame.sprite.collide_rect(ball, upper_wall):
        (r,phi) = ball_speed.as_polar()
        ball_speed.from_polar((r, -phi))
        COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    elif pygame.sprite.collide_rect(ball, lower_wall):
        (r,phi) = ball_speed.as_polar()
        ball_speed.from_polar((r, -phi))
        COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    elif pygame.sprite.collide_rect(ball, right_lower_wall):
        COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        ball_speed.x = -11

    elif pygame.sprite.collide_rect(ball, right_upper_wall):
        COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        ball_speed.x = -11

    elif pygame.sprite.collide_rect(ball, left_lower_wall):
        COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        ball_speed.x = 11

    elif pygame.sprite.collide_rect(ball, left_upper_wall):
        COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        ball_speed.x = 11

    elif pygame.sprite.collide_rect(ball, power_up) and player_1_p_up:
        random_power_up = random.randint(1,2)
        power_up.kill()
        pygame.time.set_timer(POWER_UP_TIMER, random.randint(3,10) * 1000)
    elif pygame.sprite.collide_rect(ball, power_up) and player_2_p_up:
        random_power_up = random.randint(1,2)
        power_up.kill()
        pygame.time.set_timer(POWER_UP_TIMER, random.randint(3,10) * 1000)


    (r,phi) = ball.speed.as_polar()
    angle = myfont.render(str((phi)), False, (255, 255, 255))
    player_1_points_text = myfont.render(str(player_1_points), False, (255, 255, 255))
    player_2_points_text = myfont.render(str(player_2_points), False, (255, 255, 255))
    screen.blit(player_1_points_text, (620,20))
    screen.blit(player_2_points_text, (20,20))
    screen.blit(angle, (430,200))
    #Update screen
    pygame.display.flip()
    clock.tick(60)
# Close the window and quit.
pygame.quit()
