import pygame

class Walls:
    def __init__(self):
        self.left_wall_rect = pygame.Rect(300, 10, 10, 700)
        self.right_wall_rect = pygame.Rect(980, 10, 10, 700)

    def renderWalls(self, screen: pygame.Surface):
        pygame.draw.rect(screen, "white", self.left_wall_rect)
        pygame.draw.rect(screen, "white", self.right_wall_rect)
