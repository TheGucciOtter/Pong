import pygame
import pong_objects
from pygame.math import Vector2
import random
import pong_util
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
right_goal = pong_objects.Goal(Vector2(1193,126),COLOR,7,450)
left_goal = pong_objects.Goal(Vector2(0,126),COLOR,7,450)

wall_sprites = pygame.sprite.Group()

wall_sprites.add(right_upper_wall)
wall_sprites.add(right_lower_wall)
wall_sprites.add(left_upper_wall)
wall_sprites.add(left_lower_wall)
wall_sprites.add(right_goal)
wall_sprites.add(left_goal)

wall_sprites.add(upper_wall)
wall_sprites.add(lower_wall)

ball = pong_objects.Ball(Vector2(590, 340), (255,255,255), 20, 20, 600)
all_sprites.add(ball)

ball_reset = True
game_start = False

power_up = pong_objects.Power_Up(Vector2(random.randint(340,850),random.randint(5,665)))
all_power_ups = pygame.sprite.Group()
all_power_ups.add(power_up)

player_1_p_up = False
player_2_p_up = False

p1_speed_value = 10
p2_speed_value = 10

p1_reverse_indicator = 'Not Active'
p2_reverse_indicator = 'Not Active'
p1_invisible_indicator = 'Not Active'
p2_invisible_indicator = 'Not Active'

p1_reverse_indicator_color = (255,0,0)
p2_reverse_indicator_color = (255,0,0)
p1_invisible_indicator_color = (255,0,0)
p2_invisible_indicator_color = (255,0,0)

POWER_UP_TIMER = pygame.USEREVENT+0
HIT_TIMER = pygame.USEREVENT+1
P1_POWER_UP_STOP_TIMER = pygame.USEREVENT+2
P2_POWER_UP_STOP_TIMER = pygame.USEREVENT+3
can_hit = True

pygame.font.init()
pointfond = pygame.font.SysFont('Arial', 80)
power_up_fond = pygame.font.SysFont('Arial', 20)

the_way = 10

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
                player_2_speed.y -= p2_speed_value
            elif event.key == pygame.K_s and game_start:
                player_2_speed.y += p2_speed_value
            elif event.key == pygame.K_UP and game_start:
                player_1_speed.y -= p1_speed_value
            elif event.key == pygame.K_DOWN and game_start:
                player_1_speed.y += p1_speed_value


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
        elif event.type == P1_POWER_UP_STOP_TIMER:
            pygame.time.set_timer(P1_POWER_UP_STOP_TIMER, 0)
            p2_speed_value = 10
            p1_reverse_indicator = 'Not Active'
            p1_reverse_indicator_color = (255,0,0)
        elif event.type == P2_POWER_UP_STOP_TIMER:
            pygame.time.set_timer(P2_POWER_UP_STOP_TIMER, 0)
            p1_speed_value = 10
            p2_reverse_indicator = 'Not Active'
            p2_reverse_indicator_color = (255,0,0)

    player_1.speed = player_1_speed
    player_2.speed = player_2_speed

    if game_start and ball_reset:
        ball_speed = Vector2(the_way,0)
        ball.speed = ball_speed
        ball_reset = False
        random_ball_speed_y = random.randint(-5,5)
        ball_speed.y = random_ball_speed_y
        ball.owner = pong_objects.NEUTRAL
        p1_invisible_indicator = 'Not Active'
        p2_invisible_indicator = 'Not Active'
        p1_invisible_indicator_color = (255,0,0)
        p2_invisible_indicator_color = (255,0,0)

    screen.fill((0,0,0))
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
            (r,phi) = ball.speed.as_polar()
            phi = pong_util.new_angle1(phi,ball.speed.x,ball.rect.y,player_1.rect.centery)
            player_1_p_up = True
            player_2_p_up = False
            ball.speed.from_polar((r,phi))

    if can_hit:
        if pygame.sprite.collide_rect(ball, player_2):
            pygame.time.set_timer(HIT_TIMER, 350)
            can_hit = False
            (r,phi) = ball.speed.as_polar()
            phi = pong_util.new_angle2(phi,ball.speed.x,ball.rect.y,player_2.rect.centery)
            ball.speed.from_polar((r,phi))
            player_2_p_up = True
            player_1_p_up = False

    if pygame.sprite.collide_rect(ball, upper_wall):
        (r,phi) = ball_speed.as_polar()
        ball_speed.from_polar((r, -phi))

    elif pygame.sprite.collide_rect(ball, lower_wall):
        (r,phi) = ball_speed.as_polar()
        ball_speed.from_polar((r, -phi))

    elif pygame.sprite.collide_rect(ball, right_lower_wall):
        ball_speed.x = -10

    elif pygame.sprite.collide_rect(ball, right_upper_wall):
        ball_speed.x = -10

    elif pygame.sprite.collide_rect(ball, left_lower_wall):
        ball_speed.x = 10

    elif pygame.sprite.collide_rect(ball, left_upper_wall):
        ball_speed.x = 10

    elif pygame.sprite.collide_rect(ball, right_goal):
        game_start = False
        ball.position = (590, 340)
        ball_speed.x = 0
        ball_speed.y = 0
        ball_reset = True
        player_1.position = Vector2(990, 310)
        player_2.position = Vector2(200, 310)
        player_2_points += 1
        the_way = 10
        ball.owner = pong_objects.NEUTRAL

    elif pygame.sprite.collide_rect(ball, left_goal):
        game_start = False
        ball.position = (590, 340)
        ball_speed.x = 0
        ball_speed.y = 0
        ball_reset = True
        player_1.position = Vector2(990, 310)
        player_2.position = Vector2(200, 310)
        player_1_points += 1
        the_way = -10
        ball.owner = pong_objects.NEUTRAL

    elif pygame.sprite.collide_rect(ball, power_up):
        power_up.rect = (-100,-100, 30, 30)
        power_up.kill()
        random_power_up = random.randint(1,2)
        pygame.time.set_timer(POWER_UP_TIMER, random.randint(3,15) * 1000)
        if random_power_up == 1:
            if player_1_p_up:
                ball.owner = pong_objects.PLAYER1
                p1_invisible_indicator = 'Active'
                p1_invisible_indicator_color = (127,255,0)
            elif player_2_p_up:
                ball.owner = pong_objects.PLAYER2
                p2_invisible_indicator = 'Active'
                p2_invisible_indicator_color = (127,255,0)
        if random_power_up == 2:
            if player_1_p_up:
                pygame.time.set_timer(P1_POWER_UP_STOP_TIMER, 10000)
                p2_speed_value = -10
                p1_reverse_indicator = 'Active'
                p1_reverse_indicator_color = (127,255,0)
            elif player_2_p_up:
                pygame.time.set_timer(P2_POWER_UP_STOP_TIMER, 10000)
                p1_speed_value = -10
                p2_reverse_indicator = 'Active'
                p2_reverse_indicator_color = (127,255,0)

    (r,phi) = ball.speed.as_polar()

#    angle = pointfond.render(str((phi)), False, (255, 255, 255))

    player_1_reverse_text = power_up_fond.render(str('Enemy Reverse Control: '), False, (255,255,255))
    player_2_reverse_text = power_up_fond.render(str('Enemy Reverse Control: '), False, (255,255,255))

    player_1_invisible_text = power_up_fond.render(str('Enemy Invisible Ball Control: '), False, (255,255,255))
    player_2_invisible_text = power_up_fond.render(str('Enemy Invisible Ball Control: '), False, (255,255,255))

    player_1_points_text = pointfond.render(str(player_1_points), False, (255, 255, 255))
    player_2_points_text = pointfond.render(str(player_2_points), False, (255, 255, 255))

    p1_reverse_active_text = power_up_fond.render((p1_reverse_indicator), False, (p1_reverse_indicator_color))
    p2_reverse_active_text = power_up_fond.render((p2_reverse_indicator), False, (p2_reverse_indicator_color))
    p1_invisible_active_text = power_up_fond.render((p1_invisible_indicator), False, (p1_invisible_indicator_color))
    p2_invisible_active_text = power_up_fond.render((p2_invisible_indicator), False, (p2_invisible_indicator_color))

    screen.blit(player_1_points_text, (620,20))
    screen.blit(player_2_points_text, (20,20))

    screen.blit(player_1_reverse_text, (620,620))
    screen.blit(player_2_reverse_text, (20,620))

    screen.blit(player_1_invisible_text, (620,645))
    screen.blit(player_2_invisible_text, (20,645))

    screen.blit(p1_reverse_active_text, (875,620))
    screen.blit(p2_reverse_active_text, (275,620))
    screen.blit(p1_invisible_active_text, (875,645))
    screen.blit(p2_invisible_active_text, (275,645))
    #screen.blit(angle, (430,200))
    #Update screen
    pygame.display.flip()
    clock.tick(60)
# Close the window and quit.
pygame.quit()
