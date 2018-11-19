import pygame
from pygame.locals import *

from Config import Config

class Bricks:
	def __init__(self, game_display):
		self.game_display = game_display
		self.brick_width = Config['bricks']['brick_width']
		self.brick_height = Config['bricks']['brick_height']
		self.brick_color = Config['colors']['brick_red']
		#self.brick_x = Config['game']['game_display'] * 0.92

	#--This adds on rectangle objects to a list of bricks
	def draw(self):
		self.bricks_y=35
		self.brick_list=[]
		for i in range(7):
			self.bricks_x=35
			for j in range(8):
				# self.brick_list.append(pygame.draw.rect(self.game_display, Config['colors']['brick_red'] ,[self.bricks_x, self.bricks_y, self.brick_width, self.brick_height]))
				self.brick_list.append(pygame.Rect(self.bricks_x, self.bricks_y, self.brick_width, self.brick_height))
				self.bricks_x += self.brick_width+10
			self.bricks_y+=self.brick_height + 5

	#--This draws on the bricks from the list, with each object being brick
		for brick in self.brick_list:
			pygame.draw.rect(self.game_display, self.brick_color, brick)
		