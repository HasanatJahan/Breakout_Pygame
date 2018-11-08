import pygame
from pygame.locals import *


#initialize pygame 
pygame.init()
#initilization a success
i = pygame.init()
print(i)

#screen dimensions
display_width = 800
display_height = 600
#color definitions
black = (0,0,0)
white = (255,255,255)

#set the name
pygame.display.set_caption("Breakout!")
#sets the display for the game
game_display = pygame.display.set_mode((display_width, display_height))
#specific game clock- imposes time in the game
clock = pygame.time.Clock()

#generate the image
cloudImg = pygame.image.load("CuteCloud.png")

#define functions of the game
def cloud(x,y):
	game_display.blit(cloudImg,(x,y))

#referencing the object by the top left
x = (display_width * 0.45)
y = (display_height * 0.8)

#accounts for the change in position of the object
x_change = 0


#this detects the events
def event_handler():
	#gets every event on the screen
	for event in pygame.event.get():
		#print (event)
		#to exit the game
		if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
			#uninitializes all python modules
			pygame.quit()
			#this exits the program
			quit()

		#to move the cloud to the left and right
		if event.type== KEYDOWN:
			if event.key == K_LEFT:
				x_change = -5
			elif event.key== K_RIGHT:
				x_change = 5

		#if the key is up- the object should maintain its old position
		if event.type == KEYUP:
			if event.key == K_LEFT or event.key == K_RIGHT:
				x_change = 0 

	#change the position of the object* 
	#NEED TO FIGURE OUT WHERE THIS GOES
x += x_change


#loop will run forever unless disrupted
while True:
	event_handler()
	#game display- has to be before the game elements
	game_display.fill(white)
	#to show the object
	cloud(x,y)
	#updates the display
	pygame.display.update()
	#frames per second-how fast things move- increase for faster
	clock.tick(80)
