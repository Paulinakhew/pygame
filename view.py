import pygame

def draw_enemies(enemy_list, screen, enemy_pos, enemy_size, BLUE):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

def update_screen():
    pygame.display.update()

def draw_player(screen, RED, player_pos, player_size):
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

def set_fps(clock):
    clock.tick(30)