from random import randint

class Particle():
    x = 0
    y = 0

    width = 8
    height = 15

    tick = 10

    color = (randint(100,255),randint(100,255),randint(100,255))

    pygame = None
    screen = None

    visible = False

    def __init__(self, pygame, screen,logic, x, y):
        self.x = x
        self.y = y

        self.pygame = pygame
        self.screen = screen
        self.logic = logic

        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def collision(self):
        selected_particle = [s for s in self.logic.enemies if s.collidepoint((self.x, self.y))]
        if self.y < 0 or len(selected_particle)>0:
            self.visible = False
            if len(selected_particle):
                xx = selected_particle[0].x
                yy = selected_particle[0].y
                yy -= self.logic.dy
                xx-=120
                xx/=75
                yy-=10
                yy/=85
                sound = self.pygame.mixer.Sound("explosion.wav")
                sound.play()
                self.logic.hit_enemy(yy,xx,selected_particle[0])
            return True
        return False

    def start(self, ship):
        self.x = ship.x+(ship.width/2)
        self.y = ship.y-(ship.height/2)
        self.visible = True
        self.render()

    def render(self):
        self.y-=self.tick
        self.redraw()

    def is_visible(self):
        return self.visible and not self.collision()

    def redraw(self):
        if self.y%6==0:
            self.color = (randint(0,255),randint(0,255),randint(0,255))
        self.pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

