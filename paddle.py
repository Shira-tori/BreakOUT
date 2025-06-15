import pygame

class Paddle:
    def __init__(self, WIDTH: int, HEIGHT: int):
        self.speed_x = 0
        self.rect_width = 200
        self.rect_height = 20
        self.rect = pygame.Rect((WIDTH/2) - self.rect_width/2, 
                                HEIGHT-self.rect_height, 
                                self.rect_width, 
                                self.rect_height)

    def renderPaddle(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "white", self.rect)

    def movePaddle(self, speed: int):
        self.rect.x += speed