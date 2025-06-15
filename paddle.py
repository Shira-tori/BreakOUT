import pygame

class Paddle:
    def __init__(self, WIDTH: int, HEIGHT: int):
        self.speed_x = 0
        self.rect_width = 150
        self.rect_height = 10
        self.rect = pygame.Rect((WIDTH/2) - self.rect_width/2, 
                                HEIGHT-(self.rect_height + 50), 
                                self.rect_width, 
                                self.rect_height)

    def renderPaddle(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "white", self.rect)

    def movePaddle(self, speed: int):
        if(self.rect.x+self.rect_width + speed > 980):
            self.rect.x = 980 - self.rect_width
            return
        if(self.rect.x + speed < 300):
            self.rect.x = 300
            return
        self.rect.x += speed