from commands import Command, InputHandler
from observer import Subject
import pygame 
import logging
import os

if os.path.exists("logger.log"):
    os.remove("logger.log")
logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.DEBUG)

from piece import Piece
from screen_play import Screen_play

from pygame.font import *
from pygame.sprite import *
from collections import defaultdict


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


def labels(score, score_lines, lost, WIDTH, action):
    score_surface = score_label.render("Score", True, (0,0,0))
    lines_surface = score_label.render("Lines", True, (0,0,0))
    text_score = score_label.render(str(score), True, (132, 202, 255))
    lines_score = score_label.render(str(score_lines), True, (132, 202, 255))
    next_piece_label = score_label.render("Next", True,(0,0,0))
    lost_surface = score_label.render(lost, True, "Red")
    action_surface = score_label.render(action, True, "Green")
    pygame.Surface.blit(screen, score_surface, (WIDTH * SCALE - 100, 20))
    pygame.Surface.blit(screen, text_score, (WIDTH * SCALE - 100, 35))
    pygame.Surface.blit(screen, lines_surface, (WIDTH * SCALE - 100, 60))
    pygame.Surface.blit(screen, lines_score, (WIDTH * SCALE - 100, 75))
    pygame.Surface.blit(screen, next_piece_label, (WIDTH * SCALE - 100, 150))
    pygame.Surface.blit(screen, lost_surface, (WIDTH * SCALE - 200, 250))
    pygame.Surface.blit(screen, action_surface, (WIDTH * SCALE - 200, 250))
    return text_score


def generate_falling_piece():
    fall_piece = Piece(screen, SCALE, int((WIDTH-5)/2), 2)
    fall_piece.choose_piece()
    fall_piece.set_coord()
    fall_piece.coord[fall_piece.piece] = sorted(fall_piece.coord[fall_piece.piece], key = lambda x: x[0], reverse=False)
    logging.info("Generate new fall piece - " + fall_piece.piece)
    return fall_piece 

def generate_next_piece():
    next_p = Piece(screen, SCALE, WIDTH - 8, (HEIGHT/3)+ 5)
    next_p.choose_piece()
    next_p.set_coord()
    next_p.coord[next_p.piece] = sorted(next_p.coord[next_p.piece], key = lambda x: x[0], reverse=False)
    logging.info("Generate next piece - " + next_p.piece)
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
        center = falling_piece[2] # middle
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
        center = falling_piece[2] # middle
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


def check_lost(grid, top, bottom):
    top = int(top/10)
    bottom = int(bottom/10)
    compare_l = [x for x in range(top, bottom, 1)] 
    compare_l.sort()

    y_pos = set()

    for x, y in grid:
        if grid[(x,y)] != "white":
            y_pos.add(y)
    
    if sorted(y_pos) == compare_l:
        return True

    return False


def clear_rows(x_left, x_right, grid, new_g):
    # i need to create a dictionary to store all positions thats not white with y as key
    # then i need to check if all lines are occupied
    x_left = int(x_left/10)
    x_right = int(x_right/10)
  
    # add to a dictionary the values that are not white
    verify_val = defaultdict(list)
    for val in grid:
        x, y = val
        if (x,y) in grid:
            if grid[(x,y)] != "white":
                verify_val[y].append(x)

    # list of rows
    compare_l = [x for x in range(x_left, x_right, 1)] 
    compare_l.sort()
    lines = 0
   
    change = False
    for y in verify_val:
        verify_val[y].sort()
        #compare if rows are full 
        if verify_val[y] == compare_l: # it was the rows, full
            lines += 1
            change = True
    
    if change:
        new_g = grid # copy all positions
        #loop backwars to get previous positions
        for x, y in sorted(new_g,reverse=True):
            if y-1 > 1:
                new_g[(x, y)] = grid[(x,y-1)]
               
        
        return lines, new_g
    return 0, grid


def handle_score(lines, score):
    if lines != 0:
        lines_dict = {1: "Single", 2: "Double", 3: "Triple", 4: "Tetris"}
        score_dict = {1: 100, 2: 300, 3: 500, 4: 800}
        return score+score_dict[lines], lines_dict[lines]
    else:
        return score, ""

def set_free_pos(grid):
    logging.info("Creating a list with free positions of white cells")
    free_pos = []
    for val in grid:
        if grid[val] == "white":
            free_pos.append(val)
    return free_pos


def main():
    # observer pattern
    obs = Subject()
    obs.add_observer(obs)

    score = 0
    score_lines = 0
    lost = ""
    x_left = 80
    x_right = 180 
    y_top = 20
    y_bottom = 220 

    run = 1
    orientation_piece = (0, 1)
    fall_speed = 0.29
    fall_time = 0
    level_time = 0

    screen_play = Screen_play(screen, x_left, x_right, y_top, y_bottom, SCALE)
    screen_sprite.add(screen_play)
        
    #pieces
    fall_piece = generate_falling_piece()
    falling_piece_sprite.add(fall_piece) 
    next_piece = generate_next_piece()
    next_piece_sprite.add(next_piece)
    
    #dimensions grid 10x20
    screen_play.create_grid()
    create_grid = screen_play.create_grid()
    change_piece = False
    free_pos = set_free_pos(screen_play.grid)
    action = "" # info about clear rows

    while run:
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 4:
            level_time = 0
            if fall_speed > 0.15:
                fall_speed -= 0.005

        if fall_time/1000 >= fall_speed:
            fall_time = 0
            free_pos = set_free_pos(screen_play.grid) 
           
            orientation_piece = (0, 1)
            logging.info("Dropping piece")
          
            lines, screen_play.grid = clear_rows(x_left, x_right, screen_play.grid, create_grid)
            score_lines += lines
            if validate_space(free_pos, fall_piece.coord[fall_piece.piece], orientation_piece):
                fall_piece.set_pos(orientation_piece) 
                obs.notify(fall_piece, "Moved one square down")
                obs.notify("score", "Updated to " + str(score))
                score += 1
                score, action = handle_score(lines, score)
                if action != "":
                    logging.info("Action " + action)
                    logging.info("Score updated to " + str(score))
                    obs.notify("score", "Updated to " + str(score))
            else:
                change_piece = True
                logging.info("Changing piece")

            if check_lost(screen_play.grid, y_top, y_bottom):
                lost = 'Game Over!'
                logging.error(lost)
                run = 0        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() #shuts down pyGame
                logging.info("Exit Application")
                run = 0
            elif event.type == pygame.KEYDOWN:
                input_h = InputHandler()
                
                if event.key == pygame.K_DOWN:
                    logging.info("Down key pressed")
                    orientation_piece = (0, 1)
                    if validate_space(free_pos,fall_piece.coord[fall_piece.piece], orientation_piece):
                        input_h.handleInput(event.key, fall_piece, orientation_piece)
                        obs.notify(fall_piece, "Moved one square down faster")
                        logging.info("Down movement is possible") 
                        score += 1
                        logging.info("Score updated to " + str(score))
                        obs.notify("score", "Updated to " + str(score))
                    else:
                        logging.error("Invalid space")
                   
                elif event.key == pygame.K_LEFT:
                    logging.info("Left key pressed")
                    orientation_piece = (-1, 0)
                    if validate_space(free_pos,fall_piece.coord[fall_piece.piece], orientation_piece):
                        input_h.handleInput(event.key, fall_piece, orientation_piece)
                        logging.info("Left movement is possible")
                        obs.notify(fall_piece, "Moved one square left")
                    else:
                        logging.error("Invalid space")
                elif event.key == pygame.K_RIGHT:
                    logging.info("Right key pressed")
                    orientation_piece = (1, 0)
                    if validate_space(free_pos,fall_piece.coord[fall_piece.piece], orientation_piece):
                        input_h.handleInput(event.key, fall_piece, orientation_piece)
                        logging.info("Right movement is possible")
                        obs.notify(fall_piece, "Moved one square right")
                    else:
                        logging.error("Invalid space")
                        
                elif event.key == pygame.K_z:# rotate left
                    logging.info("Z key pressed")
                    val_rot, pos = validate_rotate_l(free_pos, fall_piece.piece, fall_piece.coord[fall_piece.piece])
                    if val_rot:
                        logging.info("Rotation to left is possible")
                        input_h.handleInput(event.key, fall_piece, pos)
                        obs.notify(fall_piece, "Rotated to left")
                    else:
                        logging.error("Invalid space")
                elif event.key == pygame.K_UP: # rotate right
                    val_rot, pos = validate_rotate(free_pos, fall_piece.piece, fall_piece.coord[fall_piece.piece])
                    logging.info("Up key pressed")
                    if val_rot:
                        logging.info("Rotation to right is possible")
                        obs.notify(fall_piece, "Rotated to right")
                        input_h.handleInput(event.key, fall_piece, pos)
                    else:
                        logging.error("Invalid space")
                else:
                    #ignore other keys pressed
                    orientation_piece = (0,0)
                    logging.error("Invalid Key pressed. Valid ones up, left, down, up, z")


        if change_piece:
            screen_play.set_grid(fall_piece.coord[fall_piece.piece], fall_piece.color_piece[fall_piece.piece])
            obs.notify(fall_piece, "Changed")
            obs.notify(screen_play, "updated grid")
            fall_piece.piece = next_piece.piece
            fall_piece.set_coord()
            next_piece = generate_next_piece()
            change_piece = False     

        screen.fill("white")  
        labels(score, score_lines, lost, WIDTH, action)

        screen_play.fill()
        fall_piece.fill()
        next_piece.fill()
        screen_play.draw_grid()
        falling_piece_sprite.update()
        next_piece_sprite.update()
        screen_sprite.update()
        pygame.display.update()
        if run == 0:
            logging.info("Exit Application")
            obs.notify("tetris", " is over")
            pygame.time.delay(1000)


if __name__ == '__main__':  
    main()
