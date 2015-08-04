
import pygame, random, sys
from pygame.locals import *

class Menu():
    started = False

    def draw(self, pygame, screen):
        ff = pygame.font.SysFont("Helvetica", 56,1,0)
        screen.blit(ff.render("SPAAAAAAACE INVADERS", 1, (255,255,0)), (35, 100))
        ff = pygame.font.SysFont("Helvetica", 32,1,0)
        screen.blit(ff.render("by Andy Sturzu", 1, (0,255,135)), (300, 175))

        ff = pygame.font.SysFont("Helvetica", 32,0,0)
        screen.blit(ff.render("press space to start", 1, (130,122,135)), (275, 375))

    def draw_winner(self, pygame, screen, score=0):
        ff = pygame.font.SysFont("Helvetica", 108,1,0)
        screen.blit(ff.render("YOU DID IT!", 1, (0,255,135)), (105, 100))
        ff = pygame.font.SysFont("Helvetica", 32,1,0)
        screen.blit(ff.render("Score: "+str(score), 1, (130,122,135)), (340, 225))

        ff = pygame.font.SysFont("Helvetica", 32,0,0)
        screen.blit(ff.render("press space to restart", 1, (130,122,135)), (255, 375))

    def draw_loser(self, pygame, screen, score=0):
        ff = pygame.font.SysFont("Helvetica", 108,1,0)
        screen.blit(ff.render("YOU LOST IT!", 1, (255, 58, 58)), (55, 100))
        ff = pygame.font.SysFont("Helvetica", 32,1,0)
        screen.blit(ff.render("Score: "+str(score), 1, (130,122,135)), (350, 225))

        ff = pygame.font.SysFont("Helvetica", 32,0,0)
        screen.blit(ff.render("press space to restart", 1, (130,122,135)), (255, 375))

    def draw_score_and_lives(self, pygame, screen, score, lives,level):
        ff = pygame.font.SysFont("Helvetica", 16,1,0)
        screen.blit(ff.render("Score", 1, (255, 58, 58)), (10, 5))
        screen.blit(ff.render(str(score), 1, (255, 58, 58)), (25, 30))
        screen.blit(ff.render("Lives", 1, (255, 58, 58)), (735, 5))
        screen.blit(ff.render(str(lives), 1, (255, 58, 58)), (750, 30))
        ff = pygame.font.SysFont("Helvetica", 16,0,0)
        screen.blit(ff.render("Level "+str(level), 1, (230,230,230)), (375, 580))