import pygame
from pygame.locals import *

from Config import Config 
from Paddle import Paddle
from Bricks import Bricks
from Ball import Ball

pygame.init()

#--Display settings
pygame.display.set_caption(Config['game']['caption'])
game_display = pygame.display.set_mode((Config['game']['display_width'], Config['game']['display_height']))
clock = pygame.time.Clock()

#--Taking the different elements of the game
paddle= Paddle(game_display)
bricks= Bricks(game_display)
ball= Ball(game_display)

#--State constants
ball_in_paddle = 0  
playing = 1
won = 2
game_over = 3

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

#--Loop will run forever unless disrupted
while True:
	event_handler()
	game_display.fill(Config['colors']['black'])
	
	
	#HERE WE HANDLE THE STATES OF THE GAME WITH THE BALL
	# if state==ball_in_paddle:


	#--Deals with paddle
	paddle.draw()
	paddle.movement(x_change)

	#--Deals with bricks
	bricks.draw()

	#--Deals with the ball
	ball.draw()
	ball.ball_move()

	pygame.display.update()
	clock.tick(Config['game']['fps'])
