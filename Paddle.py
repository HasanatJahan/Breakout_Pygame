import pygame
from pygame.locals import *

from Config import Config

class Paddle:
	def __init__(self, game_display):
			self.x = (Config['game']['display_width'] * 0.45)
			self.y = (Config['game']['display_height'] * 0.92)
			self.game_display=game_display
			
			
	def draw(self):
		pygame.draw.rect(self.game_display, Config['colors']['red'], [self.x, self.y, 40, 25])
		
	def movement(self, x_change):
		self.x += x_change
