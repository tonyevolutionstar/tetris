import pygame 
from piece import Piece
from command import *
from scoreboard import ScoreBoard
from screen_play import Screen_play


from pygame.font import *
from pygame.sprite import *

pygame.init() # starts up pyGame

WIDTH, HEIGHT = 30, 40
SCALE = 10

screen = pygame.display.set_mode((SCALE * WIDTH, SCALE * HEIGHT))
clock = pygame.time.Clock()
score_label = Font(None, 20)
pygame.display.set_caption("Tetris")

screen_sprite = pygame.sprite.Group()
falling_piece_sprite = pygame.sprite.Group()
next_piece_sprite = pygame.sprite.Group()


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
    pygame.Surface.blit(screen, level_surface, (WIDTH * SCALE - 100, 50))
    pygame.Surface.blit(screen, level_score, (WIDTH * SCALE - 100, 65))
    pygame.Surface.blit(screen, lines_surface, (WIDTH * SCALE - 100, 90))
    pygame.Surface.blit(screen, lines_score, (WIDTH * SCALE - 100, 105))
    pygame.Surface.blit(screen, next_piece_label, (WIDTH * SCALE - 100, 200))
    return text_score

def generate_falling_piece():
    fall_piece = Piece(screen, SCALE, int((WIDTH-5)/2), 2)
    fall_piece.choose_piece()
    fall_piece.set_coord()
    fall_piece.coord[fall_piece.piece] = sorted(fall_piece.coord[fall_piece.piece], key = lambda x: x[0], reverse=False)

    return fall_piece 

def generate_next_piece():
    next_p = Piece(screen, SCALE, WIDTH - 8, (HEIGHT/2) + 5)
    next_p.choose_piece()
    next_p.set_coord()
    next_p.coord[next_p.piece] = sorted(next_p.coord[next_p.piece], key = lambda x: x[0], reverse=False)

    return next_p

def validate_space(free_pos, falling_piece, ori):
    # verify if falling piece is free space when reaches bottom
    # falling piece is a list of the coordinates of the piece
    # grid already was free pos with white color
    x_dir, y_dir = ori

    if free_pos is None:
        free_pos = []

    for pos in falling_piece:
        x,y = pos
        new_p = (x+x_dir, y+y_dir )
       
        if new_p not in free_pos:
            return False
    
    return True

def validate_rotate(free_pos, piece, falling_piece):
    new_l = []
    if piece != "R":
        center = falling_piece[3] # middle
        x_c, y_c = center  

        for pos in falling_piece:
            x,y = pos
            new_x = y - y_c
            new_y = x - x_c
            x = x_c - new_x
            y = y_c + new_y

            new_p = (x, y)
            new_l.append(new_p)
            if new_p not in free_pos:
                if new_p[1] > 1:
                    return False, new_l
    else:
        return False, new_l
    return True, new_l

def validate_rotate_l(free_pos, piece, falling_piece):
    new_l = []
    if piece != "R":
        center = falling_piece[3] # middle
        x_c, y_c = center  
  
        for pos in falling_piece:
            x,y = pos
            new_x = y - y_c
            new_y = x - x_c
            x = x_c + new_x
            y = y_c - new_y

            new_p = (x, y)
            new_l.append(new_p)
            if new_p not in free_pos:
                if new_p[1] > 1:
                    return False, new_l
    else:
        return False, new_l
    return True, new_l


def set_grid(grid, fall_piece, color):
    for val_pos in fall_piece:   
        grid[val_pos] = color
        
    return grid

def main():
    x_left = 80
    x_right = 180 
    y_top = 20
    y_bottom = 220 

    run = 1
    orientation_piece = (0, 1)
    state = "soft"
    count = 1
    fall_speed = 0.29
    fall_time = 0
    level_time = 0
     # trigger to change piece

    screen_play = Screen_play(screen, x_left, x_right, y_top, y_bottom, SCALE)
    screen_sprite.add(screen_play)
   
    score = ScoreBoard()

    #pieces
    fall_piece = generate_falling_piece()
    falling_piece_sprite.add(fall_piece)
    next_piece = generate_next_piece()
    next_piece_sprite.add(next_piece)
    hold_piece = Piece(screen, SCALE, 2, 5)
    
    #dimensions grid 10x20

    screen_play.create_grid()
    change_piece = False
  

    while run:
        #print(screen_play.grid)

        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

    
        if level_time/1000 > 4:
            level_time = 0
            if fall_speed > 0.15:
                fall_speed -= 0.005

        if fall_time/1000 >= fall_speed:
            fall_time = 0
            free_pos = []
            for val in screen_play.grid:
                if screen_play.grid[val] == "white":
                    free_pos.append(val)
            orientation_piece = (0, 1)
            if validate_space(free_pos, fall_piece.coord[fall_piece.piece], orientation_piece):
                fall_piece.set_pos(orientation_piece) 
                score.score += 1
            else:
                change_piece = True
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #shuts down pyGame
                run = 0
            elif event.type == pygame.KEYDOWN:
                i = InputHandler()    
                orientation_piece, state, count = i.handleInput(event, orientation_piece, state, count)               
                
                if event.key == pygame.K_LEFT:
                    orientation_piece = (-1, 0)
                    if validate_space(free_pos,fall_piece.coord[fall_piece.piece], orientation_piece):
                        fall_piece.set_pos(orientation_piece)  
                elif event.key == pygame.K_RIGHT:
                    orientation_piece = (1, 0)
                    if validate_space(free_pos,fall_piece.coord[fall_piece.piece], orientation_piece):
                        fall_piece.set_pos(orientation_piece) 
                elif event.key == pygame.K_DOWN:
                    state = "soft"
                    orientation_piece = (0, 1)
                    if validate_space(free_pos,fall_piece.coord[fall_piece.piece], orientation_piece):
                        fall_piece.set_pos(orientation_piece) 
                        score.score += 1

                if event.key == pygame.K_z:# rotate left
                    val_rot, pos = validate_rotate_l(free_pos, fall_piece.piece, fall_piece.coord[fall_piece.piece])
                    if val_rot:
                        fall_piece.coord[fall_piece.piece] = pos
                elif event.key == pygame.K_UP: # rotate right
                    val_rot, pos = validate_rotate(free_pos, fall_piece.piece, fall_piece.coord[fall_piece.piece])
                    if val_rot:
                        fall_piece.coord[fall_piece.piece] = pos

        #screen_play.grid = set_grid(screen_play.grid, fall_piece.coord[fall_piece.piece], fall_piece.color_piece[fall_piece.piece])

        if change_piece:
            screen_play.set_grid(fall_piece.coord[fall_piece.piece], fall_piece.color_piece[fall_piece.piece])
            fall_piece.piece = next_piece.piece
            fall_piece.set_coord()
            next_piece = generate_next_piece()
            change_piece = False

            #change_piece = False


        screen.fill("white")   
        labels(score, WIDTH)
        screen_play.fill()
        fall_piece.fill()
        next_piece.fill()
        screen_play.draw_grid()
     
        falling_piece_sprite.update()
        next_piece_sprite.update()
        screen_sprite.update()
        #pygame.display.flip()
        pygame.display.update()


if __name__ == '__main__':  
    main()
