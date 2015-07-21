import pygame
import basic_player as player
import basic_food as food

class Game_Window(object):
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((400,400),0,32)
		self.clock = pygame.time.Clock()
		self.player = player.Snake(400,400)
		self.Food = food.Food()

		self.font = pygame.font.SysFont('Comic Sans MS',40)

	def blit_grid(self):
		for x in range(40):
			pygame.draw.aaline(self.screen,(255,255,255),(x*10,0),(x*10,400))
		for y in range(40):
			pygame.draw.aaline(self.screen,(255,255,255),(0,y*10),(400,y*10))

	def game_over(self):
		running = True
		time = 0
		while running :
                        time += self.clock.tick()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				if event.type == pygame.KEYDOWN and time > 1500:
					running = False
			self.screen.fill((255,255,255))
			text = self.font.render('GAME OVER ',True,(255,0,0))
			self.screen.blit(text,(200-text.get_width()/2,200-text.get_height()))
			text_displaying_points = 'POINT : ' + str(self.player.point)
                        #TODO SCORE To implement the score, display something like "Points: " and concatenate that
                        # with the <<<string>>> version of the score. The score is the "point" attribute of the player object
                        text_displaying_points = "POINTS NOT IMPLEMENTED"
			rendered_text = self.font.render(text_displaying_points,True,(255,0,0))
			self.screen.blit(rendered_text,(200-rendered_text.get_width()/2,200+rendered_text.get_height()))
			
			pygame.display.update()
		self.player.is_dead = False
		self.clock.tick()
		self.player.restart()
		self.Food.restart()

	def run(self):
		while True :
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
			self.screen.fill((255,255,255))

			dt = self.clock.tick()
			self.player.update(dt,self.screen)
			self.Food.update(dt,self.screen,self.player)
			self.blit_grid()

			if self.player.is_dead :
				self.game_over()

			point = self.font.render(str(self.player.point),True,(0,0,0))
			self.screen.blit(point,(0,0))
			pygame.display.update()


if __name__ == '__main__':
	app = Game_Window()
	app.run()

