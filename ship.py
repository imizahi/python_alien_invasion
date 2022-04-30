import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
	"""Class Ship for ship management"""
	def __init__(self,ai_game):
		super().__init__()
		"""initialize ship and start position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		#Move indicator
		self.moving_right = False
		self.moving_left = False

		#Download ship img and get rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#Make every new ship in the down and center screen
		self.rect.midbottom = self.screen_rect.midbottom

		#Save float value for ship position horizontal
		self.x = float(self.rect.x)
	def blitme(self):
		"""draw ship in the current designation"""
		self.screen.blit(self.image,self.rect)
		
	def update(self):
		"""update current ship position on the basis move indicator"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		#Update obj rect with self.x
		self.rect.x = self.x

	def center_ship(self):
		"""centre ship"""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)