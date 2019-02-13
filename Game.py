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
paddle_obj= Paddle(game_display)
brick_obj= Bricks(game_display)
ball_obj= Ball(game_display)

#--Change variables 
x_change = 0
pressed_left = False
pressed_right = False

game_brick_list= []


def event_handler():
	global pressed_left
	global pressed_right
	global x_change
	global game_brick_list

	#--Gets every event on the screen
	for event in pygame.event.get():
		#print(event)
		if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			quit()

		#To move the paddle to the left and right
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				pressed_left = True  
			elif event.key== K_RIGHT:
				pressed_right = True

			#--If you press the spacebar then the game state changes
			# if event.key == K_SPACE:
			# 	ball_vel = [5,-5]
			# 	ball.ball_move(ball_vel)

		#If the key is up- the object should maintain its old position
		if event.type == KEYUP:
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

#----------------------------------------------------------------
	for brick in brick_obj.brick_list:
		if ball_obj.ball.colliderect(brick):
			#this appends to the created bricklist- which is then turned black in the brick_obj.update_bricks() function
			game_brick_list.append(brick)
			#check to see if game_brick_list is appended
			print(game_brick_list)
	 		# this is removing a brick object- it has no color attribute
			brick_obj.brick_list.remove(brick)
			#print(len(brick_obj.brick_list))
			# brick_obj.update_bricks(brick_obj.brick_list)
#-------------------------------------------------------------------


#--Loop will run forever unless disrupted
while True:
	event_handler()
	game_display.fill(Config['colors']['black'])
	
	#--Deals with paddle
	paddle_obj.draw()
	paddle_obj.movement(x_change)

#---------------------------------------------------------------------	
	#--Deals with bricks
	brick_obj.create_bricks()
	brick_obj.update_bricks(game_brick_list)
#------------------------------------------------------------------------

	#--Deals with the ball
	ball_obj.draw()

	#--Updating the display with the ball
	pygame.display.update()
	clock.tick(Config['game']['fps'])
