import pygame


#rgb colour codes
BLUE = (0, 0, 255)


def draw_enemies(enemy_list, screen, enemy_pos, enemy_size):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_screen():
    pygame.display.update()