import pygame

class Ball:
    def __init__(self):
        self.rect = pygame.Rect(1280/2, 720/2, 20, 20)

    def renderBall(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", (1280/2, 720/2), 20)