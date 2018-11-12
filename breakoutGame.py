import pygame
from pygame.locals import *

from Config import Config 

pygame.init()

#--Display settings
pygame.display.set_caption(Config['game']['caption'])
game_display = pygame.display.set_mode((Config['game']['display_width'], Config['game']['display_height']))
clock = pygame.time.Clock()

# #--Paddle 
# def paddle(x, y):
# 	pygame.draw.rect(game_display, Config['colors']['red'], [x, y, 40, 25])

# #--Referencing the object by the top left
# x = (Config['game']['display_width'] * 0.45)
# y = (Config['game']['display_height'] * 0.92)
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
				pressed_left = True  
			elif event.key== K_RIGHT:
				pressed_right = True

		#If the key is up- the object should maintain its old position
		if event.type == KEYUP:
			if event.key == K_LEFT or event.key == K_RIGHT:
				x_change = 0 
			#Trying to account for the keyup to make the board movement smoother
			if event.key == K_LEFT:
				pressed_left = False
			elif event.key == K_RIGHT:
				pressed_right = False 

		movement()

#--This changes the position
if pressed_left:
	x_change = -5
if pressed_right:
	x_change = 5

#--Loop will run forever unless disrupted
while True:
	event_handler()
	game_display.fill(Config['colors']['white'])
	#--rectangle to contain screen size
	paddle(x, y)
	pygame.display.update()
	clock.tick(Config['game']['fps'])

	#CALL THE PADDLE CLASS HERE
	


#NOTES FOR NEXT DAY:
# HOW TO PREVENT THE BOARD FROM LEAVING THE SCREEN
# HOW TO GET THE BOARD TO MOVE SMOOTHLY

# MAKE THE DIFFERENT THINGS INTO DIFFERENT CLASSES
# CHANGE THE VARIABLES TO GET STUFF FROM CONFIG