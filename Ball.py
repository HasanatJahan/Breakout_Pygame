import pygame
from pygame.locals import *

from Config import Config 
from Paddle import Paddle

class Ball():
	def __init__(self, game_display):
		self.game_display = game_display

		self.ball_vel = [5,-5]
		
		self.ball_x= 90
		self.ball_y = 300
		self.ball_radius= Config['ball']['ball_radius']
		self.ball_diameter= Config['ball']['ball_diameter']
		self.paddle_width= Config['paddle']['paddle_width']

		self.max_x= Config['game']['display_width']- self.ball_diameter
		self.ball_x= 50
		self.ball_y=50

	def draw(self):
		self.ball= pygame.Rect(self.ball_x, Config['paddle']['paddle_width']- self.ball_diameter, self.ball_diameter, self.ball_diameter)
		pygame.draw.circle(self.game_display, Config['colors']['white'], [self.ball_x + self.ball_radius, self.ball_y + self.ball_radius] ,self.ball_radius)
	
	def ball_move(self):
		self.ball.left += self.ball_vel[0]
		self.ball.top += self.ball_vel[1] 

		#--Handles the movement- when it hits something it goes in the opposite direction
		if self.ball.left <=0:
			self.ball.left = 0
			self.ball_vel[0] == -self.ball_vel[0]
		elif self.ball.left >= self.max_x: 
			self.ball.left = max_x
			self.ball_vel[0] = -self.ball_vel[0]

		# GET MORE CLEAR ON WHAT'S .LEFT DOINF
		# NEXT DAY FINISH THE MOVE FUNCTION 
		# HANDLE EVENTS OF THE BALL THE MOTION



