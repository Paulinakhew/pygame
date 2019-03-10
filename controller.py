import pygame
import random
import sys

import model as m
import view as v

pygame.init()

#declare width and height of screen
WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
#BACKGROUND_COLOUR = (11, 238, 207)
BACKGROUND_COLOUR = (0, 0, 0)

#player variables
player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

#enemy variables
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]
enemy_list = [enemy_pos]

SPEED = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

score = 0

clock = pygame.time.Clock()

myFont = pygame.font.SysFont("monospace", 35)


def collision_check(enemy_list, player_pos):
    for enemy_pos in enemy_list:
        if detect_collision(enemy_pos, player_pos):
            return True
    return False

def detect_collision(player_pos, enemy_pos):
    p_x = player_pos[0]
    p_y= player_pos[1]

    e_x = enemy_pos[0]
    e_y = enemy_pos[1]

    if (e_x >= p_x and e_x < (p_x + player_size)) or (p_x >= e_x and p_x < (e_x + enemy_size)):
        if (e_y >= p_y and e_y < (p_y + player_size)) or (p_y >= e_y and p_y < (e_y + enemy_size)):
            return True
    return False


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size

            player_pos = [x, y]
    
    screen.fill(BACKGROUND_COLOUR)
    
    enemy_list = m.drop_enemies(enemy_list, WIDTH, enemy_size)
    enemy_list, score, SPEED = m.update_enemy_positions(enemy_list, score, SPEED, HEIGHT)
    SPEED = m.set_level(score, SPEED)
    
    text = "Score: " + str(score)
    label = myFont.render(text, 1, YELLOW)
    screen.blit(label, (WIDTH-200, HEIGHT-40))

    if collision_check(enemy_list, player_pos):
        game_over = True
        #break
    
    v.draw_enemies(enemy_list, screen, enemy_pos, enemy_size, BLUE)

    v.draw_player(screen, RED, player_pos, player_size)

    clock.tick(30)

    v.update_screen()
