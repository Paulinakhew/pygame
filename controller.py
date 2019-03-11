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
BACKGROUND_COLOUR = (0, 0, 0) #black

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

    if m.collision_check(enemy_list, player_pos, player_size, enemy_size):
        game_over = True
        #break
    
    v.draw_enemies(enemy_list, screen, enemy_pos, enemy_size, BLUE)

    v.draw_player(screen, RED, player_pos, player_size)

    v.set_fps(clock)

    v.update_screen()
