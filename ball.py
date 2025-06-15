import pygame
import paddle
import walls
import random

class Ball:
    def __init__(self, WIDTH: int, HEIGHT: int, speed: int):
        random.seed()
        self.size = 10
        self.x = WIDTH / 2
        self.y = HEIGHT / 2 
        self.width_of_screen = WIDTH
        self.height_of_screen = HEIGHT
        self.speed_x = speed
        self.speed_y = speed
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def renderBall(self, screen: pygame.Surface):
        self.rect = pygame.draw.circle(screen, "white", (self.x, self.y), self.size)

    def moveBall(self, dt: float):
        self.x += self.speed_x * dt
        self.y += self.speed_y * dt
        if(self.x > self.width_of_screen-self.size):
            self.x = self.width_of_screen-self.size
        if(self.x < self.size):
            self.x = self.size
        if(self.y > self.height_of_screen-self.size):
            self.y = self.height_of_screen-self.size
        if(self.y < self.size):
            self.y = self.size

    def checkIfBounce(self, paddle: paddle.Paddle, walls: walls.Walls):
        if self.y >= self.height_of_screen-self.size or self.y <= self.size:
            self.speed_y = -self.speed_y
        if paddle.rect.colliderect(self.rect):
            self.y = paddle.rect.y - self.size
            self.speed_y = -self.speed_y
            self.speed_x = random.randrange(-500, 500, 100)
        if self.rect.colliderect(walls.left_wall_rect):
            self.x = 300 + (self.size * 2)
            self.speed_x = -self.speed_x
        if self.rect.colliderect(walls.right_wall_rect):
            self.x = 980 - self.size
            self.speed_x = -self.speed_x