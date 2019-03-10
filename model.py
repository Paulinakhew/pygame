import random

def set_level(score, SPEED):
    if score < 20:
        SPEED = 5
    elif score < 40:
        SPEED = 8
    elif score < 60:
        SPEED = 12
    else:
        SPEED = 15
    
    #SPEED = score/5 + 5
    return SPEED

def drop_enemies(enemy_list, WIDTH, enemy_size):
    delay = random.random()
    if len(enemy_list) < 10 and delay < 0.09:
        x_pos = random.randint(0, WIDTH-enemy_size)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])
    return enemy_list

def update_enemy_positions(enemy_list, score, SPEED, HEIGHT):
    for idx, enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
            enemy_pos[1] += SPEED
        else:
            enemy_list.pop(idx)
            score += 1
    return enemy_list, score, SPEED


def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False