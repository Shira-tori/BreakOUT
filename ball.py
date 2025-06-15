import pygame

class Ball:
    def __init__(self, WIDTH: int, HEIGHT: int, speed: int):
        self.size = 15
        self.x = WIDTH / 2
        self.y = HEIGHT / 2 
        self.width_of_screen = WIDTH
        self.height_of_screen = HEIGHT
        self.speed_x = speed
        self.speed_y = speed
        self.rect = pygame.Rect(self.x/2, self.x/2, self.size, self.size)

    def renderBall(self, screen: pygame.Surface):
        self.rect = pygame.draw.circle(screen, "white", (self.x, self.y), self.size)

    def moveBall(self, dt: float):
        self.x += self.speed_x * dt
        self.y += self.speed_y * dt
        if(self.x > self.width_of_screen-15):
            self.x = self.width_of_screen-15
        if(self.x < 15):
            self.x = 15
        if(self.y > self.height_of_screen-15):
            self.y = self.height_of_screen-15
        if(self.y < 15):
            self.y = 15

    def checkIfBounce(self):
        if self.x >= self.width_of_screen-15 or self.x <= 15:
            self.speed_x = -self.speed_x
        if self.y >= self.height_of_screen-15 or self.y <= 15:
            self.speed_y = -self.speed_y