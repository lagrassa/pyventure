import pygame

class Snake_part(object):
	def __init__(self,pos,color = (0,255,0)):
		self.middle_x = pos[0]
		self.middle_y = pos[1]
		self.x = self.middle_x * 10
		self.y = self.middle_y * 10
		self.color = color

	def blit(self,screen):
		rect = pygame.Rect(self.x,self.y,10,10)
		pygame.draw.rect(screen,self.color,rect)

class Snake(object) :
	def __init__(self,width,height):
		self.x = 38
		self.y = 0

		self.length = 5

		self.tail = []
		self.time_tick = 40
		self.speed = 20
		self.time = 0
		self.last_key = None
		self.delta_x = -1
		self.delta_y = 0

		self.head_color = (0,0,255)
		self.head = Snake_part((self.x,self.y),self.head_color)
		self.point = 0
		self.is_dead = False

	def restart(self):
		self.x = 38
		self.y = 0
		self.is_dead = False
		self.length = 5
		self.tail = []
		self.speed = 1
		self.time = 0
		self.delta_x = -1
		self.delta_y = 0

	def update(self,dt,screen):
		self.update_position(dt)
		self.blit(screen)
                #TODO GAMEOVER
                #Run a check to see if the snake is dead

	def check_dead(self):
                
                #TODO GAMEOVER
                # Loop through every <segment> in self.tail (hint, use a for loop)
                # Check if the snake is crossing itself by seeing if the segment's location 
                #is the same as the snake's location, (which is the head). 
                #***********The segment's location is middle_x and middle_y 

                #TODO GAMEOVER
                #Check if the x position or y position are outside the screen, which ranges from 0 to 40
                # So if the x position is 52 and the y position is 20, the snake is dead
                # Then set the attribute is_dead to True.
                self.dead = False

                #TODO LENGTH create the method, increase_length(self, value, point), that takes the value of the food,
                # and the point value, then increments the snake's length by the value, and increments
                # the points by the number of points scored
                #increase the attribute self.point by 1 to increase the score

	def update_position(self,dt):
		self.time += dt
		key_pressed = pygame.key.get_pressed()
		if key_pressed[pygame.K_UP] and self.delta_y != +1 :
			self.delta_x = 0 
			self.delta_y = -1
		elif key_pressed[pygame.K_DOWN] and self.delta_y != -1 :
			self.delta_x = 0
			self.delta_y = +1
                #TODO MOVE Implement left and right movement
		elif key_pressed[pygame.K_LEFT] and self.delta_x != +1:
                        print "can't move left...."
		elif key_pressed[pygame.K_RIGHT] and self.delta_x != -1:
                        print "can't move right..."
		if self.time >= self.time_tick :
			self.tail.insert(0,Snake_part((self.x,self.y)))
			self.x += self.delta_x
			self.y += self.delta_y
			self.head.x,self.head.y = self.x*10,self.y*10
			if len(self.tail) > self.length :
				self.tail.pop(len(self.tail) -1)
			self.time = 0

	def blit(self,screen):
		for t in self.tail :
			t.blit(screen)
		self.head.blit(screen)

