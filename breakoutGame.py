import pygame
from pygame.locals import *
 
pygame.init()
#i = pygame.init()
#print(i)

#Screen dimensions
display_width = 800
display_height = 600

#Object dimensions
img_width = 40
img_height = 40

#Color definitions
black = (0,0,0)
white = (255,255,255)

#Display settings
pygame.display.set_caption("Breakout!")
game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

#Generate the image
cloudImg = pygame.image.load("CuteCloud.png")
#Trying to scale the image to screen size
cloudImg = pygame.transform.scale(cloudImg, (img_width, img_height))

#--Define functions of the game
def cloud(x,y):
	game_display.blit(cloudImg,(x,y))

#--Referencing the object by the top left
x = (display_width * 0.45)
y = (display_height * 0.8)
#--Accounts for the change in position of the object
x_change = 0

#--Function that handles the movement
def movement():
	global x
	global x_change
	print(x)
	x += x_change

#This detects the events
def event_handler():
	# To deal with global variables to deal with scoping issues
	global x
	global x_change
	#Gets every event on the screen
	for event in pygame.event.get():
		#print (event)
		if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
			#Uninitializes all python modules
			pygame.quit()
			quit()

		#To move the cloud to the left and right
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				x_change = -5
			elif event.key== K_RIGHT:
				x_change = 5

		#If the key is up- the object should maintain its old position
		if event.type == KEYUP:
			if event.key == K_LEFT or event.key == K_RIGHT:
				x_change = 0 

		#Change the position of the object
		movement()


#Loop will run forever unless disrupted
while True:
	event_handler()
	game_display.fill(white)
	#show the object
	cloud(x,y)
	pygame.display.update()
	clock.tick(80)
