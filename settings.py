class Settings():
	"""Class settings"""

	def __init__(self):
		"""initialize game setting"""
		#Screen settings
		self.screen_width = 1000
		self.screen_height = 600
		self.bg_color = (0,191,255)
		#self.ship_speed = 1.5
		self.ship_limit = 3

		#Bullet settings
		#self.bullet_speed = 1.5
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allowed = 10

		#alien settings
		#self.alien_speed = 1.0
		self.fleet_drop_speed = 10

		#fleet_direction means 1 to right -1 to left
		#self.fleet_direction = 1

		#speed up game
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""initialize settings"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)