import pygame
from pygame.locals import *

from Config import Config

class Paddle:
	def __init__(self, game_display):
			self.x = int(Config['game']['display_width'] * 0.45)
			self.y = int(Config['game']['display_height'] * 0.92)
			self.game_display=game_display
			self.paddle_width = Config['paddle']['paddle_width']
			self.paddle_height = Config['paddle']['paddle_height']
	
			
	def draw(self):
		pygame.draw.rect(self.game_display, Config['colors']['red'], [self.x, self.y, self.paddle_width, self.paddle_height ])
		
	def movement(self, x_change):
		self.x += x_change
		#--This sets the boundary so the paddle does not leave the screen
		if self.x>Config['game']['display_width']-self.paddle_width or self.x<0:
			self.x -= x_change