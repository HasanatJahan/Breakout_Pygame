import pygame
from pygame.locals import *

from Config import Config 
from Paddle import Paddle

pygame.init()

#--Display settings
pygame.display.set_caption(Config['game']['caption'])
game_display = pygame.display.set_mode((Config['game']['display_width'], Config['game']['display_height']))
clock = pygame.time.Clock()
paddle= Paddle(game_display)

x_change = 0
pressed_left = False
pressed_right = False

def event_handler():
	global pressed_left
	global pressed_right
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
			#Trying to account for the keyup to make the board movement smoother
			if event.key == K_LEFT:
				pressed_left = False
				x_change = 0
			elif event.key == K_RIGHT:
				pressed_right = False 
				x_change = 0

	#--This changes the position
	if pressed_left:
		x_change = -5
	if pressed_right:
		x_change = 5

	#--This handles the paddle going beyond the screen

#--To prevent the paddle from escaping the screen
if(paddle.x> Config['game']['display_width']):
	event_handler()


#--Loop will run forever unless disrupted
while True:
	event_handler()
	game_display.fill(Config['colors']['black'])
	paddle.draw()
	paddle.movement(x_change)

	pygame.display.update()
	clock.tick(Config['game']['fps'])

#--HOW TO GET THE PADDLE FROM ESCAPING THE SCREEN WITHOUT SPRITE
#--GET THE BALL FOR THE GAME 
#--GENERATE THE RECTANGULAR BRICKS
