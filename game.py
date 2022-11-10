import pygame
from pygame.locals import*
from pieces import *
from pygame.sprite import *
from pygame.font import *
from pygame import *

pygame.init() # starts up pyGame

WIDTH, HEIGHT = 40, 60
SCALE = 10

screen = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()
clock.tick(24)
piece_sprite = pygame.sprite.GroupSingle()
back_sprite = pygame.sprite.GroupSingle()
name = Font(None, 16)

pygame.display.set_caption("Tetris")
pieces = Piece()
background = Background(SCALE, WIDTH, HEIGHT)
piece_sprite.add(pieces)
back_sprite.add(background)


def main():
    running = 1
    
    #pygame.display.flip()
    while running:
        e = event.wait() #pause until event occurs
        if e.type == QUIT:
            pygame.quit() #shuts down pyGame
            running = 0
            break

        screen.fill((255, 255, 255))
        back_sprite.draw(screen)
        back_sprite.update()
        piece_sprite.draw(screen)
        piece_sprite.update()
       
        pygame.display.update()
        #pygame.quit()
    

if __name__ == '__main__':  
    main()

