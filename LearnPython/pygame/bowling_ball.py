"""
Bowling ball animation example
Summer HSSP
Introduction to Programming Python
"""
import pygame
# Initialize the game engine
pygame.init()
#Create the colors you'll need
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
# Setting the size of the screen 
SIZE = [400, 400]
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Falling Bowling Ball")
#Create clock object
clock = pygame.time.Clock()
#Set initial position. Here, the x_position is in the middle, the y_position is at the top
x_position = 200
y_position = 0
# Main Game Loop
done = False
while not done:
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: # Someone clicked the exit X
			done = True # Indicates to exit the loop
	# Set the screen background
	screen.fill(WHITE)
	
	# Draw the bowling ball
	pygame.draw.circle(screen, BLACK, [x_position,y_position], 25)
	# Moves the bowling ball 6 pixels down
	y_position+=6
	#Logic to deal with when the bowling ball is off the screen 		
	if y_position> 400:
		# Reset the ball just above the top of the screen
		y_position = -10
	# Update the screen with the new drawing
	pygame.display.flip()
        #Moves the clock forward
	clock.tick(20)
pygame.quit()
