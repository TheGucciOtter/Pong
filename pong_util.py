import random
def new_angle1(phi,speed_x,ball_y,player_y):
    from_center = ball_y - player_y
    if speed_x < 0:
        if from_center < 0:
            phi = 180 - from_center
        else:
            phi = 180 + from_center
    if speed_x > 0:

        if ball_y > player_y:
            phi = 180 - phi - (230 / 180) * abs(from_center)
            if phi < 125.0:
                phi = 145.0 - random.randint(0,20)
        else:
            phi = 180 - phi + (230 / 180) * abs(from_center)
            if phi > 235.0:
                phi = 215.0 + random.randint(0,20)
    return phi

def new_angle2(phi,speed_x,ball_y,player_y):
    from_center = ball_y - player_y
    if speed_x > 0:
        if from_center > 0:
            phi = -abs(from_center)
        else:
            phi = from_center
    if speed_x < 0:

        if ball_y > player_y:
            phi = 180 - phi - (230 / 180) * abs(from_center)
            if phi > 55.0:
                phi = 55.0 - random.randint(0,20)
        else:
            phi = 180 - phi - (230 / 180) * abs(from_center)
            if phi < 305.0:
                phi = 305.0 + random.randint(0,20)
    return phi
