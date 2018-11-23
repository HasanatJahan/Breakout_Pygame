import pygame
from pygame.locals import *

from Config import Config 
from Paddle import Paddle

class Ball():
	def __init__(self, game_display):
		self.game_display = game_display
		
		self.ball_x= 300
		self.ball_y = 300
		self.ball_radius= Config['ball']['ball_radius']
		self.ball_diameter= Config['ball']['ball_diameter']
		self.paddle_width= Config['paddle']['paddle_width']

		self.max_x = Config['game']['display_width']- self.ball_diameter
		self.max_y = Config['game']['display_height'] - self.ball_diameter 

	def draw(self):
		self.ball= pygame.Rect(self.ball_x, Config['paddle']['paddle_width']- self.ball_diameter, self.ball_diameter, self.ball_diameter)
		pygame.draw.circle(self.game_display, Config['colors']['white'], [self.ball_x + self.ball_radius, self.ball_y + self.ball_radius] ,self.ball_radius)
	
	def ball_move(self, ball_vel):
		self.ball.left += ball_vel[0]
		self.ball.top += ball_vel[1] 

		#--Handles the movement- when it hits something it goes in the opposite direction
		if self.ball.left <=0:
			self.ball.left = 0
			ball_vel[0] == -ball_vel[0]
		elif self.ball.left >= self.max_x: 
			self.ball.left = max_x
			ball_vel[0] = -ball_vel[0]

		if self.ball.top < 0:
			self.ball.top = 0
			ball_vel[1] = -ball_vel[1]




