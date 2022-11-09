import pygame
import random
from pygame.locals import*
from pieces import Piece
from pygame.sprite import *
from pygame.font import *
from pygame import *

pygame.init() # starts up pyGame

WIDTH, HEIGHT = 80, 80
SCALE = 10

screen = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()
clock.tick(24)
all_sprites = pygame.sprite.GroupSingle()
name = Font(None, 16)

pygame.display.set_caption("Tetris")
pieces = Piece()
all_sprites.add(pieces)

def main():
    running = 1
    
    #for i in pieces.images:
        #print(i)
    #    display.blit(pieces.images[i], (50,20))
    #pygame.display.flip()
    while running:
        e = event.wait() #pause until event occurs
        if e.type == QUIT:
            pygame.quit() #shuts down pyGame
            running = 0
            break
        screen.fill((255, 255, 255))

        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.update()
    #    running = 0
   
    #display.update()
    #pygame.quit() 
    

if __name__ == '__main__':  
    main()