import pygame
import sys

pygame.init()

#declare width and height of screen
WIDTH = 800
HEIGHT = 600

RED = (255, 0, 0) #rgb colour code of player
player_pos = [400, 300] #list of coordinates of player's position
player_size = 50 #define the player's height and width

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]

            if event.key == pygame.K_LEFT:
                x -= 5
            elif event.key == pygame.K_RIGHT:
                x += 5

            player_pos = [x, y]
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()