import pygame

class Soldier:
	"""Class Soldier for soldaten management"""
	def __init__(self,ai_game):
		"""initialize soldate and start position"""
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#Download soldier img and get rect
		self.image = pygame.image.load('images/tank.bmp')
		self.rect = self.image.get_rect()

		#Make every new ship in the down and center screen
		self.rect.center = self.screen_rect.center
		
	def blitme(self):
		"""draw ship in the current designation"""
		self.screen.blit(self.image,self.rect)
		