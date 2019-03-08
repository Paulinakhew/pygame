import pygame
import random
import sys


pygame.init()

#declare width and height of screen
WIDTH = 800
HEIGHT = 600

#rgb colour codes
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND_COLOUR = (0, 0, 0)

#player variables
player_size = 50
player_pos = [WIDTH/2, HEIGHT-2*player_size]

#enemy variables
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH-enemy_size), 0]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

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
    if enemy_pos[1] >= 0 and enemy_pos[1] < HEIGHT:
        enemy_pos[1] += 10
    else:
        enemy_pos[0] = random.randint(0, WIDTH-enemy_size)
        enemy_pos[1] = 0
    pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    clock.tick(30)

    pygame.display.update()