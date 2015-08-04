import pygame, random, sys
from pygame.locals import *
from random import randint
from Ship import *
from Particle import *
from Logic import *
from EventHandler import *
from Menu import *

background_color = (51,51,51)

def clear():
  screen.fill(background_color)
  pygame.draw.rect(screen, (71,71,71), (0, 580,800, 20))
  return True

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

background = pygame.Surface((800, 600))
background.fill(background_color)

clock = pygame.time.Clock()

menu = Menu()

END_MUSIC_EVENT = pygame.USEREVENT + 0
pygame.mixer.music.set_endevent(END_MUSIC_EVENT)
sound = pygame.mixer.Sound("background.wav")
sound.play()

logic = Logic(pygame, screen)

ship = Ship(pygame, screen)
particle = Particle(pygame, screen,logic,0,0)

handler = EventHandler()

while clear():
  for event in pygame.event.get():
    if event.type == QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
      handler.handle(event, pygame, screen, ship)
    elif event.type == END_MUSIC_EVENT and event.code == 0:
      sound.play()
  logic.hit_ship()
  if logic.win_game():
    clear()
    menu.draw_winner(pygame,screen,logic.score)
  elif logic.is_game_over():
    clear()
    menu.draw_loser(pygame, screen,logic.score)
  elif menu.started:
    menu.draw_score_and_lives(pygame,screen,logic.score,logic.lives,logic.level)
    if handler.keys['space']:
      if not particle.is_visible():
        sound = pygame.mixer.Sound("laser.wav")
        sound.play()
        particle.start(ship)

    if handler.keys['right']:
      ship.move_right()
    if handler.keys['left']:
      ship.move_left()

    ship.redraw()

    if particle.is_visible():
      particle.render()

    logic.draw_enemies()

    if logic.win_level():
      logic.next_level()

  else:
    menu.draw(pygame, screen)
    if handler.keys['space']:
      menu.started = True
  if logic.is_game_over() or logic.win_game():
     if handler.keys['space']:
      menu.started = True
      logic.restart_game()
  time_passed = clock.tick(60)


  pygame.display.flip()
  pygame.time.wait(5)
