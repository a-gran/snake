import pygame
from random import randrange

SCREEN_SIDE = 1000 # width and height of the screen
SIZE_ONE_CUBE = 50 # snake size

x, y = randrange(0, SCREEN_SIDE, SIZE_ONE_CUBE), randrange(0, SCREEN_SIDE, SIZE_ONE_CUBE) # snake's initial position
apple = randrange(0, SCREEN_SIDE, SIZE_ONE_CUBE), randrange(0, SCREEN_SIDE, SIZE_ONE_CUBE) # apple's initial position
dictionary_snake_move = {'W': True, 'S': True, 'A': True, 'D': True} # snake's movements
length = 1 # snake's length
score = 0 # game score
fps = 5 # fps and the speed of the snake, that will grow up with the score
snake = [(x, y)] # snake's position
dx, dy = 0, 0 # snake's move direction

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIDE, SCREEN_SIDE))
pygame.display.set_caption('Snake!')