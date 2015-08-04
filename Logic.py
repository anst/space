import time
from random import randint

class Logic():
    pygame = None
    screen = None

    light_blue = (153, 204, 255)
    width = 35
    height = 15

    time_start = time.time()

    lives = 3
    game_over = False

    level = 1

    dy = 0
    d2y = 1

    levels = {
      1: [
          [1,0,1,1,1,1,0,1],
          [1,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,1],
          [1,1,0,0,0,0,1,1],
         ],
      2: [
          [1,1,1,1,1,1,1,1],
          [1,1,1,0,0,1,1,1],
          [1,0,0,1,1,0,0,1],
          [1,1,1,1,1,1,1,1],
         ],
      3: [
          [1,0,0,0,0,0,0,1],
          [1,1,0,0,0,0,1,1],
          [1,1,1,0,0,1,1,1],
          [1,1,1,1,1,1,1,1],
         ],
      4: [
          [1,1,1,1,1,1,1,1],
          [0,1,1,0,0,1,1,0],
          [1,1,1,0,0,1,1,1],
          [1,1,1,1,1,1,1,1],
         ],
      5: [
          [0,0,1,1,1,1,0,0],
          [1,1,1,1,1,1,1,1],
          [0,1,1,1,1,1,1,0],
          [0,0,0,1,1,0,0,0],
         ]
    }

    cached_levels = {
      1: [
          [1,0,1,1,1,1,0,1],
          [1,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,1],
          [1,1,0,0,0,0,1,1],
         ],
      2: [
          [1,1,1,1,1,1,1,1],
          [1,1,1,0,0,1,1,1],
          [1,0,0,1,1,0,0,1],
          [1,1,1,1,1,1,1,1],
         ],
      3: [
          [1,0,0,0,0,0,0,1],
          [1,1,0,0,0,0,1,1],
          [1,1,1,0,0,1,1,1],
          [1,1,1,1,1,1,1,1],
         ],
      4: [
          [1,1,1,1,1,1,1,1],
          [0,1,1,0,0,1,1,0],
          [1,1,1,0,0,1,1,1],
          [1,1,1,1,1,1,1,1],
         ],
      5: [
          [0,0,1,1,1,1,0,0],
          [1,1,1,1,1,1,1,1],
          [0,1,1,1,1,1,1,0],
          [0,0,0,1,1,0,0,0],
         ]
    }

    enemies = []

    score = 0

    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen

    def hit_enemy(self, x,y,particle):
        self.enemies.remove(particle)
        self.levels[self.level][x][y] = 0
        self.score+=50

    def hit_bonus(self):
        score+=randint(150,350) #random score between 150-350

    def hit_ship(self):
        if self.dy > 200:
            self.lives-=1
            self.dy = 0
            if self.lives <= 0:
                self.game_over = True
            else:
                self.reset_level()
            return True
        return False

    def win_level(self):
        return sum([sum(x) for x in self.levels[self.level]]) == 0

    def win_game(self):
        return self.level > 5

    def reset_level(self):
        self.d2y = self.level
        self.dy = 0
        if not self.win_game():
            self.levels[self.level] = self.cached_levels[self.level]

    def restart_game(self):
        self.d2y = 1
        self.dy = 0
        self.levels = self.cached_levels
        self.score = 0
        self.lives = 0
        self.level = 1


    def next_level(self):
        self.level+=1
        self.reset_level()

    def is_game_over(self):
        return self.game_over

    def draw_enemies(self):
        self.enemies = []
        if time.time()-self.time_start>.5:
            self.dy+=self.d2y
            self.time_start = time.time()
        for r in range(4):
            for c in range(8):
                if self.levels[self.level][r][c]:
                    a = self.pygame.draw.rect(self.screen, self.light_blue, (c*75+self.width+85, r*85+self.height+10+self.dy, self.width, self.height))
                    if not a in self.enemies:
                        self.enemies.append(a)
