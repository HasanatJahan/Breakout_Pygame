import pygame
from pygame.locals import *

from Config import Config

class Bricks:
	def __init__(self, game_display):
		self.game_display = game_display
		self.brick_width = Config['bricks']['brick_width']
		self.brick_height = Config['bricks']['brick_height']
		self.brick_color = Config['colors']['brick_red']
		self.brick_list = []
		self.bricks_y = 35
		self.bricks_x = 35

	#--This adds on rectangle objects to a list of bricks
	def create_bricks(self):
		self.brick_list.clear()
		self.bricks_y = 35
		for i in range(7):
			self.bricks_x = 35
			for j in range(8):
				#this appends the brick objects 
				self.brick_list.append(pygame.Rect(self.bricks_x, self.bricks_y, self.brick_width, self.brick_height))
				self.bricks_x += self.brick_width + 10
			self.bricks_y += self.brick_height + 5
		
		#this draws on the bricks for every brick in brick_list
		for brick in self.brick_list:
			pygame.draw.rect(self.game_display, self.brick_color, brick)			


	def update_bricks(self, game_brick_list):
		# this turns any bricks in the the game_brick_list to black
		for brick in game_brick_list:
			pygame.draw.rect(self.game_display, Config['colors']['black'], brick)