import pygame
import paddle
import ball

class Breakout:
	def __init__(self):
		pygame.init()
		self.HEIGHT = 720
		self.WIDTH = 1280
		self.paddle = paddle.Paddle(self.WIDTH, self.HEIGHT)
		self.ball = ball.Ball(self.WIDTH, self.HEIGHT)
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True
		self.gameLoop()

	def gameLoop(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.screen.fill("black")
			self.paddle.renderPaddle(self.screen)
			self.ball.renderBall(self.screen)

			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				pass
			if keys[pygame.K_RIGHT]:
				pass

			pygame.display.flip()
			
			self.clock.tick(60)


def main():
	print("Hello World!")
	game = Breakout()
	pygame.quit()

if __name__ == '__main__':
	main()