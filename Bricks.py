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
		# print(self.brick_list)



	def draw(self):		
		self.create_bricks()
	#--This draws on the bricks from the list, with each object being brick
		for brick in self.brick_list:
			pygame.draw.rect(self.game_display, self.brick_color, brick)


	

	# HERE YOU HAVE TO DRAW THE INITIAL BRICKS 
	# THE PROBLEM IS THAT THE BRICK OBJECT IS BEING REMOVED BUT NOT THE PICTURE
	# MAYBE SEPERATE AN INITIAL DRAW WITH BRICKS 
	# THEN AN UPDATE FUNCTION THAT CREATES THE BRICKS 
	# AND ACCOUNTS FOR THE CHANGE IN THE BRICK_LIST
	# MAYBE CREATE SEPEREATE METHODS HERE