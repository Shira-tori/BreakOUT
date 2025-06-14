import pygame

class Breakout:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1280, 720))
		self.clock = pygame.time.Clock()
		self.running = True
		self.gameLoop()

	def gameLoop(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.screen.fill("white")

			pygame.display.flip()

			self.clock.tick(60)


def main():
	print("Hello World!")
	game = Breakout()
	pygame.quit()

if __name__ == '__main__':
	main()