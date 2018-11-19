import pygame
from pygame.locals import *

from Config import Config 
from Paddle import Paddle

class Ball:
	def __init__(self, game_display):
		self.game_display = game_display
		self.ball_x= int(Config['game']['display_width'] * 0.45)
		self.ball_y = int(Config['game']['display_height'] * 0.92)
		self.ball_radius= Config['ball']['ball_radius']

		#--this is the ball velocity vector apparently
		self.ball_vel = [5,-5]

	def draw(self):
		#we use rect here because circle expects integers
		pygame.draw.circle(self.game_display, Config['colors']['blue'], (int(self.ball_x), int(self.ball_y)) ,self.ball_radius)		

		#--NEED TO MAKE THE BALL APPEAR ON TOP OF THE PADDLE IN THE MIDDLE AND MOVE WITH THE PADDLE

	
	#For the movement of the ball we need the velocity vector
