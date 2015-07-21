
def main():
        import pygame
        pygame.init()
	import random
	# Initialize the game engine
	BLACK = [0, 0, 0]
	WHITE = [255, 255, 255]
	RED = [255, 0, 0]
	GREEN = [0 , 255, 0]
	BLUE = [0, 0, 225]
	color_list = [RED, GREEN, BLUE]
	# Set the height and width of the screen
	SIZE = [400, 400]
	screen = pygame.display.set_mode(SIZE)
	pygame.display.set_caption("Flying Circus Animation")
	# Create an empty array
	ball_list = []
	# Loop 50 times and add a bouncy ball in a random x,y position with down direction and alternating colors
	for i in range(50):
		x = random.randrange(0, 400)
		y = random.randrange(0, 400)
		#picks a random color
		color = color_list[random.randint(0,2)]
		ball_list.append([x, y,color])
	clock = pygame.time.Clock()
	# Loop until the user clicks the close button.
	done = False
	while not done:
		for event in pygame.event.get(): # User did something
		        if event.type == pygame.QUIT: # If user clicked close
		                done = True # Flag that we are done so we exit this loop
		# Set the screen background
		screen.fill(WHITE)
		# Process each snow flake in the list
		for i in range(len(ball_list)):
		        # Draw the snow flake
		        color = ball_list[i][2]
		        xPos = ball_list[i][0]
		        yPos = ball_list[i][1]
		        pygame.draw.circle(screen, color, [xPos,yPos], 10)
		        # Move the snow flake some random number of pixels down
		        number_of_pixels_down=random.randint(0,5)
		        ball_list[i][1] += number_of_pixels_down
		        #Snowflake off screen           
		        if ball_list[i][1] > 400:
		                # Reset it just above the top
		                y = random.randrange(-50, -10)
		                ball_list[i][1] = y
		                # Give it a new x position
		                x = random.randrange(0, 400)
		                ball_list[i][0] = x
		# Go ahead and update the screen with what we've drawn.
		pygame.display.flip()
		clock.tick(20)

