#!/usr/bin/env python3
"""
    Sample game 
"""
import sys
import time

import pygame

#CONSTANTS
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FRAME_RATE = 20
BG_COLOR_LIGHT_BLUE = (200, 200, 255)
BG_COLOR_LIGHT_GREEN = (200, 255, 200)

def main():
    """
        Main game
    """
    character = pygame.image.load('images/sprite.png')
    game_time = 100
    while game_time:
        SCREEN.fill(BG_COLOR_LIGHT_BLUE)
        if game_time % 5:
            SCREEN.fill(BG_COLOR_LIGHT_GREEN)
        SCREEN.blit(character, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        SCREEN.blit(character, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                pass
        pygame.display.flip()
        CLOCK.tick(FRAME_RATE)
        game_time -= 1
    return

    
    
if __name__ == '__main__':
    pygame.init()
    SCREEN = pygame.display.set_mode(SCREEN_SIZE)
    CLOCK = pygame.time.Clock()
    exit_status = main()
    pygame.quit()
    sys.exit(exit_status)
