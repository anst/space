class Ship():
    x = 0
    y = 0

    width = 50
    height = 25

    tick = 5

    color = (96,140,0)

    pygame = None
    screen = None

    def __init__(self, pygame, screen):
        self.x = 400-self.width/2
        self.y = 550-self.height/2

        self.pygame = pygame
        self.screen = screen

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move_left(self):
        self.x-=self.tick
        self.x%=800
        self.redraw()

    def move_right(self):
        self.x+=self.tick
        self.x%=800
        self.redraw()

    def redraw(self):
        self.pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

