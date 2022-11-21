import pygame
from pygame.locals import*
from pieces import *
from pygame.sprite import *
from pygame.font import *
from pygame import *
from command import InputHandler
from scoreboard import ScoreBoard
from screen_play import Screen_play

pygame.init() # starts up pyGame

WIDTH, HEIGHT = 50, 60
SCALE = 10

screen = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()
clock.tick(24)
piece_sprite = pygame.sprite.Group()
screen_sprite = pygame.sprite.Group()
score_label = Font(None, 20)

pygame.display.set_caption("Tetris")

def labels(score, WIDTH):
    score_surface = score_label.render("Score", True, (0,0,0))
    level_surface = score_label.render("Level", True, (0,0,0))
    lines_surface = score_label.render("Lines", True, (0,0,0))
    hold_surface = score_label.render("Hold", True, (0,0,0))
    text_score = score_label.render(str(score.score), True, (132, 202, 255))
    level_score = score_label.render(str(score.level), True, (132, 202, 255))
    lines_score = score_label.render(str(score.lines), True, (132, 202, 255))
    next_piece_label = score_label.render("Next", True,(0,0,0))
    pygame.Surface.blit(screen, hold_surface, (10, 10))
    pygame.Surface.blit(screen, score_surface, (WIDTH * SCALE - 100, 10))
    pygame.Surface.blit(screen, text_score, (WIDTH * SCALE - 100, 25))
    pygame.Surface.blit(screen, level_surface, (WIDTH * SCALE - 100, 40))
    pygame.Surface.blit(screen, level_score, (WIDTH * SCALE - 100, 55))
    pygame.Surface.blit(screen, lines_surface, (WIDTH * SCALE - 100, 70))
    pygame.Surface.blit(screen, lines_score, (WIDTH * SCALE - 100, 85))
    pygame.Surface.blit(screen, next_piece_label, (WIDTH * SCALE - 100, 200))


def check_wall(piece_choosed, x, y):
    wall = 0
    if piece_choosed == "piece_1":
        if 8 <= x <= 35 and 0 <= y <= 59:
            wall = 0
        else:
            wall = 1
    else:
        if 8 <= x <= 34 and 0 <= y <= 59:
            wall = 0
        else:
            wall = 1
    return wall 
    

def main():
    pieces = Piece(screen, SCALE, WIDTH - 10, HEIGHT)
    piece_sprite.add(pieces)
    screen_play = Screen_play(screen, 70, 5, 30, 60, SCALE)
    piece_sprite.add(screen_play)
    score = ScoreBoard()
    image_ori = (0, -1)
    state = "soft"
    running = 1
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit() #shuts down pyGame
                running = 0
            elif event.type == pygame.KEYDOWN:
                min_tuple = min(pieces.pieces_dict[pieces.actual_piece], key=lambda tup: tup[1])
                wall = check_wall(pieces.actual_piece, min_tuple[0], min_tuple[1])
                
                i = InputHandler()
                image_ori, state = i.handleInput(event, image_ori, state, wall)
                print(wall)
                pieces.change_dir(image_ori)
                
        screen.fill((255, 255, 255))

        pieces.fill_piece()
        screen_play.draw_screen()

        labels(score, WIDTH)
        
        piece_sprite.update()
        screen_sprite.update()
     
        #pygame.display.update()
        pygame.display.flip()
        #pygame.quit()
    

if __name__ == '__main__':  
    main()

