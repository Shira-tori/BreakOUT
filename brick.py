import pygame

class Brick:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, self.width, self.height)
    
    def renderBrick(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "white", self.rect)