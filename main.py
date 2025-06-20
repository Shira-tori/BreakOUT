import pygame
import paddle
import ball
import walls
import brick

class Breakout:
	def __init__(self):
		pygame.init()
		self.HEIGHT = 720
		self.WIDTH = 1280
		self.paddle_speed = 10
		self.ball_speed = 10
		self.paddle = paddle.Paddle(self.WIDTH, self.HEIGHT)
		self.ball = ball.Ball(self.WIDTH, self.HEIGHT, self.ball_speed)
		self.walls = walls.Walls()
		self.bricks: list[brick.Brick] = []
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.clock = pygame.time.Clock()
		self.running = True
		self.dt = 0
		self.initailizeBricks()
		self.gameLoop()

	def initailizeBricks(self):
		for i in range(6):
			brick_ = brick.Brick(380 + (i*80), 50, 80, 15)
			if(i != 0):
				brick_.rect.x += 10*i
			self.bricks.append(brick_)

	def renderBricks(self):
		for i in self.bricks:
			i.renderBrick(self.screen)

	def gameLoop(self):
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False

			self.screen.fill("black")
			self.paddle.renderPaddle(self.screen)
			self.ball.renderBall(self.screen)
			self.walls.renderWalls(self.screen)
			self.renderBricks()

			self.ball.moveBall(self.dt)
			self.ball.checkIfBounce(self.paddle, self.walls, self.bricks)

			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				self.paddle.movePaddle(self.paddle_speed * -1 * self.dt)
			if keys[pygame.K_RIGHT]:
				self.paddle.movePaddle(self.paddle_speed * self.dt)
			
			pygame.display.flip()
			
			self.dt = self.clock.tick(60) / 10



def main():
	game = Breakout()
	pygame.quit()

if __name__ == '__main__':
	main()