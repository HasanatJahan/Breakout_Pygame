import pygame
from pygame.locals import *
 
pygame.init()

#--Screen dimensions
display_width = 800
display_height = 600

#--Object dimensions
img_width = 40
img_height = 40

#--Color definitions
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

#--Display settings
pygame.display.set_caption("Breakout!")
game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

#---------------------------------------------------------------------
#--------------------------------------------------REFERENCE FOR LATER
#--Generate the image
#cloudImg = pygame.image.load("CuteCloud.png")
#Trying to scale the image to screen size
#cloudImg = pygame.transform.scale(cloudImg, (img_width, img_height))

#--Define functions of the game
#def cloud(x,y):
#	game_display.blit(cloudImg,(x,y))

#----------------------------------------------------------------------

#--Draw a rectangle 
def paddle(x, y):
	pygame.draw.rect(game_display, red, [x, y, 40, 25])

#--Referencing the object by the top left
x = (display_width * 0.45)
y = (display_height * 0.92)
x_change = 0

#--Function that handles the movement
def movement():
	global x
	global x_change
	print(x)
	x += x_change


pressed_left = False
pressed_right = False

def event_handler():
	global x
	global x_change
	#--Gets every event on the screen
	for event in pygame.event.get():
		#print (event)
		if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			quit()

		#To move the paddle to the left and right
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				x_change = -5  
			elif event.key== K_RIGHT:
				x_change = 5

		#If the key is up- the object should maintain its old position
		if event.type == KEYUP:
			if event.key == K_LEFT or event.key == K_RIGHT:
				x_change = 0 
			#Trying to account for the keyup to keep moving
			if event.key == K_LEFT:
				x_change = -5
			elif event.key == K_RIGHT:
				x_change = 5

		movement()


#Loop will run forever unless disrupted
while True:
	event_handler()
	game_display.fill(white)
	#show the object
#	cloud(x,y)
	paddle(x, y)
	pygame.display.update()
	clock.tick(80)
