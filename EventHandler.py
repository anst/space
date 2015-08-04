import pygame, random, sys
from pygame.locals import *

class EventHandler():
    keys = {'left':False, 'right':False, 'space':False}

    def __init__(self):
        pass

    def handle(self, event, pygame, screen, ship):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.keys['left'] = True
            elif event.key == pygame.K_RIGHT:
                self.keys['right'] = True
            elif event.key == pygame.K_SPACE:
                self.keys['space'] = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.keys['left'] = False
            elif event.key == pygame.K_RIGHT:
                self.keys['right'] = False
            elif event.key == pygame.K_SPACE:
                self.keys['space'] = False





