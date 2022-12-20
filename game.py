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
next_p_sprite = pygame.sprite.Group()
hold_sprite = pygame.sprite.Group()
pieces_g_sprite = pygame.sprite.Group()
screen_sprite = pygame.sprite.Group()
score_label = Font(None, 20)
flag_next_piece = False
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
    return text_score



def generate_piece():
    piece = Piece(screen, SCALE, (WIDTH-10)/2, 1)
    piece.actual_piece = piece.choice_pieces()
    piece.color = piece.set_color_piece()
    return piece

def next_piece():
    next_p = Piece(screen, SCALE, WIDTH - 8, (HEIGHT/2) - 5)
    next_p.actual_piece = next_p.choice_pieces()
    next_p.color = next_p.set_color_piece()
    return next_p


def calculateLevelAndFallFreq(score):
    # from https://inventwithpython.com/pygame/chapter7.html line 356 - 361
    level = int(score / 10) + 1
    fallFreq = 0.27 - (level * 0.02)
    return level, fallFreq  


def main():
    
    count = 1
    piece = generate_piece()
    next_p = next_piece()
    next_p_sprite.add(next_p)
    piece_sprite.add(piece)
    hold_p = Piece(screen, SCALE, 2, 5)
    screen_play = Screen_play(screen, 70, 5, 30, 60, SCALE)
    piece_sprite.add(screen_play)
    
    score = ScoreBoard()
    fall_time = 0
    level_time = 0


    image_ori = (0, -1)
    state = "soft"
    running = 1
    wall_l = {"piece_1": pygame.Rect(70, 0, 10, 580), 
              "piece_l": pygame.Rect(80, 0, 10, 580),
              "piece_j": pygame.Rect(70, 0, 10, 580),
              "piece_r": pygame.Rect(80, 0, 10, 580),
              "piece_s": pygame.Rect(90, 0, 10, 580),
              "piece_t": pygame.Rect(80, 0, 10, 580),
              "piece_z": pygame.Rect(70, 0, 10, 580) }

    wall_r = {"piece_1": pygame.Rect(360, 0, 10, 580), 
              "piece_l": pygame.Rect(360, 0, 10, 580),
              "piece_j": pygame.Rect(350, 0, 10, 580),
              "piece_r": pygame.Rect(360, 0, 10, 580),
              "piece_s": pygame.Rect(360, 0, 10, 580),
              "piece_t": pygame.Rect(350, 0, 10, 580),
              "piece_z": pygame.Rect(340, 0, 10, 580)}

  

    while running:
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #shuts down pyGame
                running = 0
            elif event.type == pygame.KEYDOWN:
                i = InputHandler()
                image_ori, state, count, score.score = i.handleInput(event, image_ori, state, count, score.score)

                if count % 2 != 0:
                    state ="soft"

                if event.key == pygame.K_z:# rotate left
                    piece.rotate()
                elif event.key == pygame.K_UP: # rotate right
                    piece.rotate()

                print(piece.rect) 
                x_p, y_p, w_p, h_p = piece.rect
                
                wall_b = {"piece_1": pygame.Rect(x_p, 590, w_p, h_p), 
                    "piece_l": pygame.Rect(x_p, 590,  w_p, h_p),
                    "piece_j": pygame.Rect(x_p, 590,  w_p, h_p),
                    "piece_r": pygame.Rect(x_p, 590,  w_p, h_p),
                    "piece_s": pygame.Rect(x_p, 590,  w_p, h_p),
                    "piece_t": pygame.Rect(x_p, 590, w_p, h_p),
                    "piece_z": pygame.Rect(x_p, 590,  w_p, h_p)
                }


                if pygame.Rect.colliderect(piece.rect, wall_l[piece.actual_piece]):
                    image_ori = (0, 0)
                    if event.key == pygame.K_RIGHT:
                        image_ori = (1, 0)
             
                elif pygame.Rect.colliderect(piece.rect, wall_r[piece.actual_piece]):
                    image_ori = (0, 0)    
                    if event.key == pygame.K_LEFT:
                        image_ori = (-1, 0)
                   
                elif pygame.Rect.colliderect(piece.rect, wall_b[piece.actual_piece]):
                    print("collide on buttom")
                     
                    if event.key == pygame.K_LEFT:
                        if pygame.Rect.colliderect(piece.rect, wall_l[piece.actual_piece]):
                            image_ori = (0, 0)
                        if event.key == pygame.K_RIGHT:
                            image_ori = (1, 0)
                    
                    elif event.key == pygame.K_RIGHT:
                       if pygame.Rect.colliderect(piece.rect, wall_r[piece.actual_piece]):
                        image_ori = (0, 0)    
                        if event.key == pygame.K_LEFT:
                            image_ori = (-1, 0)
                   
                    elif event.key == pygame.K_DOWN:
                        image_ori = (0, 0)  
                        score.score += 1

                piece.change_dir(image_ori)
               
        print(score.score)
        screen.fill((255, 255, 255))
        piece.fill_piece()
        next_p.fill_piece()
        screen_play.draw_screen()

        labels(score, WIDTH)

        piece_sprite.update()
        next_p_sprite.update()
        screen_sprite.update()
        

        if hold_p.actual_piece != "":
            hold_p.fill_piece()
            hold_p.change_dir((0,0))
            hold_sprite.add(hold_p)
            hold_sprite.update()
    

        if state == "hold":
            if hold_p.actual_piece == "":
                # a peça atual vai ser a hold, e a proxima vai passar À atual
                hold_p.actual_piece = piece.actual_piece
                hold_p.color = piece.color

                piece.actual_piece = next_p.actual_piece
                piece.color = next_p.color
                piece.fill_piece()
                next_p = next_piece()
                next_p.fill_piece()
            # vou remover a peça do hold e mete la como atual    
            if count % 2 == 1 and hold_p.actual_piece != "":
                piece.actual_piece = hold_p.actual_piece
                piece.color = hold_p.color
                hold_p.actual_piece = piece.actual_piece
                hold_p.color = piece.color
               
            if count % 2 == 0:
                hold_p.fill_piece()
                piece.fill_piece()
                hold_sprite.add(hold_p)
                hold_sprite.update()

        #pygame.display.update()
        pygame.display.flip()
      

if __name__ == '__main__':  
    main()